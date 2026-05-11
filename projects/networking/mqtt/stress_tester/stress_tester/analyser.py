from mqtt import MQTT
from sys import argv
from ast import literal_eval
from time import sleep, time
from collections import defaultdict
from worker_thread import Worker
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pandas as pd
from stats import compute_statistics


class Analyser(MQTT):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threadpool = QThreadPool()
        self.final_count = 0
        self.verboseAnalyser = kwargs.get("verboseAnalyser", False)
        self.verbosePublisher = kwargs.get("verbosePublisher", False)
        self.results_dict = {
            "test_time": [],
            "qos": [],
            "analyserQos": [],
            "instancecount": [],
            "delay": [],
            "messages_received": [],
            "received_rate": [],
            "loss_rate": [],
            "out_of_order_rate": [],
            "median_inter_message_gap": [],
            "mean_inter_message_gap": [],
            "variance_inter_message_gap": [],
            "$SYS/broker/clients/connected": [],
            "$SYS/broker/load/publish/dropped/1min": [],
            "$SYS/broker/load/messages/sent/1min": [],
            "$SYS/broker/load/messages/received/1min": [],
            "$SYS/broker/messages/inflight": [],
        }

    def main(self):
        """
        This method performs the functionality of the Analyser as per
        the assignment specification.
        """
        # Define the transmission characteristics
        instancecount = [num for _ in range(12) for num in range(1, 6, 1)]
        qos = [num for _ in range(4) for num in range(3) for _ in range(5)]
        delay = [num for num in [4, 2, 1, 0] for _ in range(15)]
        duration = 60  # Number of seconds to listen for publishers.

        # For each transmission characteristic
        for analyserQos in range(3):
            for idx, _ in enumerate(instancecount):
                # Connect to the Broker
                self.connect()
                # Record test timestamp
                self.test_time = time()
                # Subscribe using the current qos
                self.unsubscribe_all()
                self.subscribe("counter/#", qos=analyserQos)
                # We use QoS 1 for $SYS measurements because we want to ensure
                # we get the most up-to-date $SYS metrics for each test configuration
                self.subscribe("$SYS/broker/clients/connected", qos=1)
                self.subscribe("$SYS/broker/load/publish/dropped/1min", qos=1)
                self.subscribe("$SYS/broker/load/messages/sent/1min", qos=1)
                self.subscribe("$SYS/broker/load/messages/received/1min", qos=1)
                self.subscribe("$SYS/broker/messages/inflight", qos=1)

                # Create the publishers
                self.publishers = [
                    Worker(
                        id=f"pub-{i}",
                        host=self.host,
                        port=self.port,
                        verbose=self.verbosePublisher,
                    )
                    for i in range(1, 6)
                ]
                for publisher in self.publishers:
                    # Connect signals (threadsafe queue)
                    publisher.signals.finished.connect(self.getFinalCount)
                    # Start the publishers
                    self.threadpool.start(publisher.run)

                # Give the publishers time to start
                sleep(5)

                # Provide instructions to the publishers
                if self.verboseAnalyser:
                    print(
                        f"\n\nSending instructions:\n\tqos = {qos[idx]}\n\tinstancecount = {instancecount[idx]}\n\tdelay = {delay[idx]}"
                    )
                self.publish(topic="request/qos", payload=f"{qos[idx]}", qos=2)
                self.publish(
                    topic="request/instancecount",
                    payload=f"{instancecount[idx]}",
                    qos=2,
                )
                self.publish(topic="request/delay", payload=f"{delay[idx]}", qos=2)

                # Listen to the publishers
                msgs = self.listen(duration, mode="seconds")

                # Reset the final message count, then kill the publishers
                # which triggers updating of the final count
                self.final_count = 0
                for publisher in self.publishers[: instancecount[idx]]:
                    publisher.kill()

                # Give the publishers time to emit their finished signals
                # (finished signals are the threadsafe queue that passes
                # the final count)
                sleep(5)
                if self.verboseAnalyser:
                    print(f"Total final count = {self.final_count}")

                # Construct dict of {topics:msgs}
                filtered = [tuple(msg.split("\t")) for msg in msgs]
                filtered_dict = defaultdict(list)
                for topic, message, timestamp in filtered:
                    filtered_dict[topic].append(
                        (message.strip("b'"), timestamp.strip("b'"))
                    )
                filtered_dict = dict(filtered_dict)
                # Define the publisher topics
                topics = [
                    f"counter/pub-{id+1}/{qos[idx]}/{delay[idx]}"
                    for id in range(instancecount[idx])
                ]
                # Compute statistics
                compute_statistics(
                    data=filtered_dict,
                    topics=topics,
                    analyser=self,
                    duration=duration,
                    analyserQos=analyserQos,
                    qos=qos[idx],
                    instancecount=instancecount[idx],
                    delay=delay[idx],
                )

                # Give the broker time to recover
                self.disconnect()
                print("Cooldown period...")
                if delay[idx] == 0:
                    sleep(30)
                else:
                    sleep(10)

        # Save the analysis required by the assignment
        results_df = pd.DataFrame(self.results_dict)
        results_df.to_excel("summary.xlsx", index=False)

    def getFinalCount(self, queue: int):
        """
        Threadsafe queue utilised to get final count
        of each publisher. This is necessary for computing
        the loss rate.

        :param queue: _description_
        :type queue: int
        """
        if self.verboseAnalyser:
            print(f"\tReceived final count: {queue}")
        self.final_count += queue


if __name__ == "__main__":
    id = str(argv[1]) if len(argv) >= 2 else "analyser"
    host = str(argv[2]) if len(argv) >= 3 else "192.168.20.39" 
    port = int(argv[3]) if len(argv) >= 4 else 1883
    verboseAnalyser = literal_eval(argv[4]) if len(argv) >= 5 else True
    verbosePublisher = literal_eval(argv[5]) if len(argv) >= 6 else False
    analyser = Analyser(
        id=id,
        host=host,
        port=port,
        verboseAnalyser=verboseAnalyser,
        verbosePublisher=verbosePublisher,
    )
    analyser.main()

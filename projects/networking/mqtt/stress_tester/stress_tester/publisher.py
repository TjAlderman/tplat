from mqtt import MQTT
from time import time


class Publisher(MQTT):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = 1 # Initialise state (1=alive, 0=dead)
        self.count = 1 # Initialise counter

    def loop(self):
        # Get the instructions
        self.subscribe(
            topic="request/+", qos=2
        )  # Use QOS 2 because our instruction loop relies on each instruction being received exactly once
        msgs = self.listen(3)
        for msg in msgs:
            if "qos" in msg:
                qos = int(msg.split("\t")[1].strip("b'"))
            elif "delay" in msg:
                delay = int(msg.split("\t")[1].strip("b'"))
            elif "instancecount" in msg:
                instancecount = int(msg.split("\t")[1].strip("b'"))

        # Unsubscribe just to clean-up print-outs for verbose mode
        self.unsubscribe(topic="request/+", qos=2)

        # Once we have obtained the three relevant pieces of information,
        # decide whether we are required to publish at the specified QOS
        # and delay
        if int(self.id.split("-")[-1]) <= instancecount:
            if self.verbose:
                print(f"\t\t{self.id} publishing...")
            # Connect to host, start network loop, and initialise count
            self.connect()
            self.client.loop_start()
            self.count = 1
            # While alive, keep publishing
            while self.state:
                self.pure_publish(
                    topic=f"counter/{self.id}/{qos}/{delay}",
                    payload=str(self.count),
                    qos=qos,
                )
                # A more accurate sleep method than using time.sleep()
                t1 = time()
                while (time() - t1) < (delay / 1000):
                    pass
                self.count += 1
            self.client.loop_stop()
            self.disconnect()

        if self.verbose:
            print(f"\t\t{self.id} finished!")

    def toggleState(self):
        """
        Method for the master to toggle state from
        spawning thread.
        """
        if self.verbose:
            print(f"\t\t\t{self.id} toggled")
        self.state = 0
from paho.mqtt.client import Client
import paho.mqtt.client as mqtt
from time import time
from typing import *


# This code is adapted from https://pypi.org/project/paho-mqtt/
# See source for detailed explanation of functionality.


class MQTT:
    def __init__(
        self,
        id: str,
        host: str = "localhost",
        port: int = 1883,
        verbose: bool = False,
        *args,
        **kwargs,
    ):
        """
        Generic MQTT class capable of virtually all MQTT functionality.

        :param id: Client ID.
        :type id: int
        :param host: Host address, defaults to "localhost"
        :type host: str, optional
        :param port: Host port, defaults to 1883
        :type port: int, optional
        :param verbose: Enable printouts, defaults to False
        :type verbose: bool, optional
        """
        # args
        self.id = id
        self.host = host
        self.port = port
        self.verbose = verbose

        # __post_init__
        self.client = Client(mqtt.CallbackAPIVersion.VERSION2, client_id=self.id)
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_unsubscribe = self.on_unsubscribe
        self.client.on_message = self.on_message
        self.connected = False
        self.topics = []
        self.old_msgs = []
        self.msgs = []

    def connect(self):
        self.client.connect(host=self.host, port=self.port)
        self.connected = True

    def reconnect(self):
        self.client.reconnect()

    def subscribe(self, topic: str, qos: int):
        """
        We do something a little odd here.
        Subscribe must be called from on_connect,
        so we add the requested topic to an attribute
        and then call connect() again to force
        the subscription to be processed

        :param topic: Topic to subscribe to.
        :type topic: str
        :param qos: QoS of subscription.
        :type qos: int
        """
        self.topics.append((topic, qos))
        if self.connected:
            self.reconnect()
        else:
            self.connect()
        if self.verbose:
            print(f'Client successfully subscribed to topic: "{topic}"')

    def unsubscribe(self, topic, qos):
        self.topics.remove((topic, qos))
        self.client.unsubscribe(topic=topic)
        if self.verbose:
            print(f'Client successfully unsubscribed from topic "{topic}"')

    def unsubscribe_all(self):
        for topic in self.topics:
            self.client.unsubscribe(topic=topic[0])
        self.topics = []
        if self.verbose:
            print(f"Client successfully unsubscribed from all topics")

    def listen(self, process: Union[int, float], mode: str = "messages"):
        if self.verbose:
            print("Client is listening for instructions...")
        self.client.user_data_set([])
        # Start network loop
        self.client.loop_start()
        # Listen for process number of messages
        if mode == "messages":
            assert isinstance(process, int)
            while True:
                if len(self.msgs) == int(process):
                    break
        # Listen for process number of seconds
        elif mode == "seconds":
            t1 = time()
            while (time() - t1) < process:
                pass
        # Stop network loop
        self.client.loop_stop()
        # Wipe the messages container and
        # return the received messages
        received = self.msgs
        self.msgs = []
        return received

    def publish(self, topic: str, payload: str, qos: int = 0, retain: bool = False):
        self.client.on_publish = self.on_publish
        self.unacked_publish = set()
        self.client.user_data_set(self.unacked_publish)
        if self.connected:
            self.client.reconnect()
        else:
            self.connect()
        self.client.loop_start()
        msg_info = self.client.publish(
            topic=topic, payload=payload, qos=qos, retain=retain
        )
        self.unacked_publish.add(msg_info.mid)
        msg_info.wait_for_publish()
        self.client.loop_stop()
        self.client.on_publish = None

    def pure_publish(
        self, topic: str, payload: str, qos: int = 0, retain: bool = False
    ):
        msg_info = self.client.publish(
            topic=topic, payload=payload, qos=qos, retain=retain
        )

    def disconnect(self):
        self.client.disconnect()

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(
        self,
        client,
        userdata,
        flags,
        reason_code,
        properties,
    ):
        if reason_code.is_failure:
            if self.verbose:
                print(
                    f"Client failed to connect: {reason_code}. loop_forever() will retry connection"
                )
            pass
        else:
            if self.verbose:
                print(f"Client connected with result code {reason_code}")
            # we should always subscribe from on_connect callback to be sure
            # our subscribed is persisted across reconnections.
            topics = self.topics
            for topic in topics:
                self.client.subscribe(topic=topic[0], qos=topic[1])

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        self.msgs.append(
            msg.topic + "\t" + str(msg.payload) + "\t" + str(msg.timestamp)
        )
        if self.verbose:
            print(msg.topic + "\t" + str(msg.payload) + "\t" + str(msg.timestamp))

    def on_publish(self, client, userdata, mid, reason_code, properties):
        # reason_code and properties will only be present in MQTTv5. It's always unset in MQTTv3
        try:
            userdata.remove(mid)
        except KeyError:
            if self.verbose:
                print(
                    "on_publish() is called with a mid not present in unacked_publish"
                )
                print("This is due to an unavoidable race-condition:")
                print("* publish() return the mid of the message sent.")
                print(
                    "* mid from publish() is added to unacked_publish by the main thread"
                )
                print("* on_publish() is called by the loop_start thread")
                print(
                    "While unlikely (because on_publish() will be called after a network round-trip),"
                )
                print(" this is a race-condition that COULD happen")
                print("")
                print(
                    "The best solution to avoid race-condition is using the msg_info from publish()"
                )
                print(
                    "We could also try using a list of acknowledged mid rather than removing from pending list,"
                )
                print("but remember that mid could be re-used !")

    def on_subscribe(self, client, userdata, mid, reason_code_list, properties):
        # Since we subscribed only for a single channel, reason_code_list contains
        # a single entry
        if self.verbose:
            if reason_code_list[0].is_failure:
                print(f"Broker rejected client subscription: {reason_code_list[0]}")
            else:
                print(
                    f"Broker client granted the following QoS: {reason_code_list[0].value}"
                )

    def on_unsubscribe(self, client, userdata, mid, reason_code_list, properties):
        # Be careful, the reason_code_list is only present in MQTTv5.
        # In MQTTv3 it will always be empty
        if self.verbose:
            if len(reason_code_list) == 0 or not reason_code_list[0].is_failure:
                print(
                    "unsubscribe succeeded (if SUBACK is received in MQTTv3 it success)"
                )
            else:
                print(f"Broker replied with failure: {reason_code_list[0]}")

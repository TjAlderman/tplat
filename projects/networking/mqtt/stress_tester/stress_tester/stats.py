import numpy as np
import matplotlib.pyplot as plt
from typing import *
import pandas as pd
import os


def compute_statistics(
    data: dict,
    topics: list,
    analyser,  # No type-hint to avoid cyclic import
    duration: Union[int, float],
    qos: int,
    analyserQos: int,
    instancecount: int,
    delay: int,
):
    """
    Compute statistics as per the assignment specification.

    :param data: Dictionary of message data.
    :type data: dict
    :param topics: Current topic.
    :type topics: list
    :param analyser: Reference to analyser.
    :type analyser: Analyser
    :param qos: QoS of current test configuration.
    :type qos: int
    :param analyserQos: Analyser QoS of current test configuration.
    :type analyserQos: int
    :param instancecount: Instancecount of current test configuration.
    :type instancecount: int
    :param delay: Delay of current test configuration.
    :type delay: int
    """
    # Total messages sent by publishers
    messages_received = sum([len(data[topic]) for topic in topics])

    # i. The total average rate of messages you actually receive from all publishers across the period [messages/second].
    # (how many messages did you see, versus how many should you have seen).
    received_rate = messages_received / duration

    # ii. The rate of message loss you see [percentage].
    loss_rate = (1 - messages_received / analyser.final_count) * 100

    # iii. The rate of any out-of-order messages you see [percentage]
    out_of_order_count = 0
    for topic in topics:
        forward_diff = np.diff(np.array([int(item[0]) for item in data[topic]]))
        out_of_order_count += np.sum(forward_diff != 1)
    out_of_order_rate = out_of_order_count / messages_received * 100

    # iv. The median inter-message-gap you see, compared to the requested delay [milliseconds].
    # Only measure for actually consecutive counter-value messages, ignore the gap if
    # you miss any messages in between.
    cons_inter_message_gaps = []
    for topic in topics:
        forward_diff = np.diff(np.array([int(item[0]) for item in data[topic]]))
        timestamps = np.array([float(item[1]) for item in data[topic]])
        cons_inter_message_gap = np.diff(timestamps)[forward_diff == 1]
        cons_inter_message_gaps += cons_inter_message_gap.tolist()
        # Plot message stats for this particular publisher
        generate_plots(
            data=data, topic=topic, qos=qos, analyserQos=analyserQos, instancecount=instancecount, delay=delay
        )

    median_inter_message_gap = np.median(np.array(cons_inter_message_gaps))
    # We also collect statistics on distribution of inter-message-gaps
    variance_inter_message_gap = np.var(np.array(cons_inter_message_gap))
    mean_inter_message_gap = np.mean(np.array(cons_inter_message_gap))

    # Print statistics
    if analyser.verboseAnalyser:
        print(
            f"Messages received = {messages_received}\nReceived rate (messages/second) = {received_rate}\nLoss rate (%) = {loss_rate}\nOut-of-order rate (%) = {out_of_order_rate}\nMedian inter-message-gap (milliseconds) = {median_inter_message_gap*1000}\nMean inter-message-gap (milliseconds) = {mean_inter_message_gap*1000}"
        )

    # b. While measuring the above also
    # i. Subscribe to and record the $SYS/# measurements, and identify what, if anything, on the
    # broker do any loss/misordered-rates correlate with. (Look at measurements under e.g.
    # ‘load’, ‘heap’, ‘active clients’, ‘messages’; anything that seems relevant. See e.g.
    # https://mosquitto.org/man/mosquitto-8.html for ideas. Be aware of the timing of the $SYS
    # measurements, to reflect when you actually put the broker under load)
    sys_connected_clients = data.get(
        "$SYS/broker/clients/connected", [(np.nan, np.nan, np.nan)]
    )  # The number of clients currently connected
    sys_publish_dropped = data.get(
        "$SYS/broker/load/publish/dropped/1min", [(np.nan, np.nan, np.nan)]
    )  # The moving average of the number of publish messages dropped by the broker over different time intervals. This shows the rate at which durable clients that are disconnected are losing messages. The final "+" of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of messages dropped in 1 minute, averaged over 1, 5 or 15 minutes.
    sys_messages_sent = data.get(
        "$SYS/broker/load/messages/sent/1min", [(np.nan, np.nan, np.nan)]
    )  # The moving average of the number of all types of MQTT messages sent by the broker over different time intervals. The final "+" of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of messages send in 1 minute, averaged over 1, 5 or 15 minutes.
    sys_messages_received = data.get(
        "$SYS/broker/load/messages/received/1min",
        [(np.nan, np.nan, np.nan)],
    )  # The moving average of the number of all types of MQTT messages received by the broker over different time intervals. The final "+" of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of messages received in 1 minute, averaged over 1, 5 or 15 minutes.
    sys_messages_inflight = data.get(
        "$SYS/broker/messages/inflight", [(np.nan, np.nan, np.nan)]
    )  # The number of messages with QoS>0 that are awaiting acknowledgments.

    # Update the results dictionary
    analyser.results_dict["test_time"].append(analyser.test_time)
    analyser.results_dict["qos"].append(qos)
    analyser.results_dict["analyserQos"].append(analyserQos)
    analyser.results_dict["instancecount"].append(instancecount)
    analyser.results_dict["delay"].append(delay)
    analyser.results_dict["messages_received"].append(messages_received)
    analyser.results_dict["received_rate"].append(received_rate)
    analyser.results_dict["loss_rate"].append(loss_rate)
    analyser.results_dict["out_of_order_rate"].append(out_of_order_rate)
    analyser.results_dict["median_inter_message_gap"].append(
        median_inter_message_gap * 1000
    )  # convert to milliseconds
    analyser.results_dict["mean_inter_message_gap"].append(
        mean_inter_message_gap * 1000
    )  # convert to milliseconds
    analyser.results_dict["variance_inter_message_gap"].append(
        variance_inter_message_gap
    )  # convert to milliseconds
    analyser.results_dict["$SYS/broker/clients/connected"].append(
        float(sys_connected_clients[-1][0])
    )
    analyser.results_dict["$SYS/broker/load/publish/dropped/1min"].append(
        float(sys_publish_dropped[-1][0])
    )
    analyser.results_dict["$SYS/broker/load/messages/sent/1min"].append(
        float(sys_messages_sent[-1][0])
    )
    analyser.results_dict["$SYS/broker/load/messages/received/1min"].append(
        float(sys_messages_received[-1][0])
    )
    analyser.results_dict["$SYS/broker/messages/inflight"].append(
        float(sys_messages_inflight[-1][0])
    )

    # Save the message logs for future analysis
    if not os.path.exists("data"): os.mkdir("data")
    result_df = pd.DataFrame(
        dict([(key, pd.Series(value)) for key, value in data.items()])
    )
    result_df.to_excel(f"data/{analyserQos}_{qos}_{instancecount}_{delay}.xlsx", index=False)


def generate_plots(data: dict, topic: str, qos: int, analyserQos: int, instancecount: int, delay: int):
    """
    For a given publisher, generate plots of message 
    delivery pattern, message gaps, and message gaps 
    distribution.
    """
    if not os.path.exists('figures'): os.mkdir("figures")
    forward_diff = np.diff(np.array([int(item[0]) for item in data[topic]]))
    timestamps = np.array([float(item[1]) for item in data[topic]])
    timestamps -= timestamps[0]

    plt.figure(figsize=(10, 10), dpi=300)
    plt.scatter(
        timestamps,
        np.array([int(item[0]) for item in data[topic]]),
        marker="x",
        color="black",
    )
    plt.xlabel("Time (s)")
    plt.ylabel("Payload versus Time")
    plt.title("Message Delivery")
    plt.savefig(f"figures/{topic.split('/')[1]}_{analyserQos}_{qos}_{instancecount}_{delay}_delivery.png")

    plt.figure(figsize=(10, 10), dpi=300)
    plt.scatter(
        timestamps[1:][forward_diff == 1],
        np.diff(timestamps)[forward_diff == 1] * 1000,
        marker=".",
        color="black",
    )
    plt.xlabel("Time (s)")
    plt.ylabel("Message gaps (ms)")
    plt.title("Message Gaps versus Time")
    plt.savefig(f"figures/{topic.split('/')[1]}_{analyserQos}_{qos}_{instancecount}_{delay}_gaps.png")

    # Plot the message gap distribution
    y_hist, y_bin_edges = np.histogram(
        np.diff(timestamps)[forward_diff == 1] * 1000, bins=1000
    )
    plt.figure(figsize=(10, 10), dpi=300)
    plt.bar(
        y_bin_edges[:-1],
        y_hist,
        width=np.diff(y_bin_edges),
        edgecolor="black",
        align="edge",
    )
    plt.xlabel("Message gap (ms)")
    plt.ylabel("Counts")
    plt.yscale("log")
    plt.title("Histogram of Message Gaps")
    plt.savefig(
        f"figures/{topic.split('/')[1]}_{analyserQos}_{qos}_{instancecount}_{delay}_gaps_distribution.png"
    )

    plt.close('all')

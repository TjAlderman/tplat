# MQTT Stress Tester

This code is intended to serve as a platform for stress-testing of an MQTT Broker. The code is broken into three classes:

* The ``MQTT`` class, located in ``mqtt.py``,
* the ``Analyser`` class, located in ``analyser.py``,
* and the ``Publisher`` class, located in ``publisher.py``.

The ``MQTT`` class is a generic class that encompasses all the basic functionality a user may desire from a MQTT client or publisher. The ``Analyser`` and ``Publisher`` inherit from the ``MQTT`` class, and extend the class with the functionality defined within the assignment specification.

Lastly, a ``stats.py`` file is included that contains two functions that are used by the ``Analyser`` to derive several statistics from the collected data, and the ``analysis.ipynb`` notebook was used to process these collected statistics and generate plots. These two files are much 'messier' than the aforementioned classes, and were intentionally isolated as they are hyperspecific to the deliverables of this project. In general, a user seeking to use/adapt this code will likely want to write their own statistics functions that record and save data specific to their needs.

> **Note:**

> Please note that the ``analysis.ipynb`` file is not submitted for marking. It is only submitted to prove that the report plots were generated from my own testing results.

If your goal is to stress-test an existing broker, you should be able to directly apply this code to your broker (amending the ``stats.py`` code as necessary). If your goal is something else, the ``MQTT`` class should serve as a valuable foundation upon which you can append your desired functionality.

## Userguide

Stress testing is initated by executing the ``analyser.py`` file. This file can be run from the command line as a script as follows:

```py
python analyser.py client_id host_address host_port verbose_analyser verbose_publisher 

id = str(argv[1]) if len(argv) >= 2 else "analyser"
host = str(argv[2]) if len(argv) >= 3 else "192.168.20.39" 
port = int(argv[3]) if len(argv) >= 4 else 1883
verboseAnalyser = literal_eval(argv[4]) if len(argv) >= 5 else True
verbosePublisher = literal_eval(argv[5]) if len(argv) >= 6 else False
```

With input arguments replaced with the appropriate values. verbose_analyser and verbose_publisher should be bool values that are used to enable/disable console printouts. Please note that setting verbose_publisher to True will add significant latency to the program and is not recommended unless debugging.

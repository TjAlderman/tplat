# LAN

The Local Area Network (LAN) seeks to get an application's message from here to there, as fast/efficiently as possible. The LAN is [generally] defined in hardware (i.e., a physical medium connecting clients). LANs have:

* No guaranteed delivery
* No built-in-error-detection/correction
* No specialised features (e.g., bulk transfers, realtime, security, etc.)
* Yes to "performance"

## Circuits, Cells, and Frames

**Circuits:** a fixed pipe, just for you, tied to both endpoints.
**Cells:** send a specific number of bits, when it's your turn, to the other end (i.e., Time Division Multiplexing).
**Frames:** send a collection of bits as and when you want (arbitrary length, targeted messages).

### Frames

Destination address
Source address
Specify start and stop
Agree how long a frame could be
Agree how to access the network fairly

```wave
{ 
  "signal": [ {"name": "CLK", "wave": "p.....|..."},
            {"name":"DAT", "wave":"x.345x|=.x", "data":["A","B","C","D"]},
            {"name": "REQ", "wave": "0.1..0|1.0"},
            {},
            {"name": "ACK", "wave": "1.....|01."}
]}
```

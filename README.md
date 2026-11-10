# TSAVcanlib
CANBUS Library


# canlib
CAN bus library for the TS FSAE.

## Install
pip install git+https://github.com/ORG/canlib.git@v0.1.0

Checking installation: 
python -c "import canlib; print(canlib.__version__)"

Upgrade to new versions:
pip install --upgrade git+https://github.com/ORG/canlib.git@v0.1.1


## Bring up the interface
sudo ip link set can0 up type can bitrate 500000

## API
| Method | Description |
| :--- | :---: |
| **CANBus(channel="can0", interface="socketcan")** | Opens the bus on creation. | 
| **send_message(can_id, data)** | Standard frame, 11-bit ID (0x000-0x7FF), up to 8 data bytes. |
| **send_extended_message(can_id, data)** | Extended frame, 29-bit ID, up to 8 data bytes. |
| **receive_message(timeout=1.0)** | Returns a can.Message, or None if nothing arrived in time. |
| **open() ** | Opens the bus (does nothing if already open). |
| **shutdown()**| Releases the bus. Safe to call more than once. |


## Usage
```python
## Usage

```python
from canlib import CANBus

bus = CANBus("can0")          # opens the bus
try:
    bus.send_message(0x123, [0x01, 0x02, 0x03])                # 11-bit ID
    bus.send_extended_message(0x1ABCDE, [0x01, 0x02, 0x03])    # 29-bit ID
    bus.receive_message(1.0)                                    # prints the frame
finally:
    bus.shutdown()            # always close the bus
```

## Safe shutdown (Ctrl+C)

Ctrl+C during `send_message`, `send_extended_message` or `receive_message`
prints "Interrupt", closes the bus, and re-raises the interrupt.

Ctrl+C anywhere else (e.g. during a `time.sleep`) does NOT close the bus.
Always wrap your code in `try/finally` and call `bus.shutdown()`.

Closing the bus does not stop a motor. Control code should send a
safe/zero command in its own `finally` block.


## Development
pip install -e ".[dev]"


## Layout 
canlib/
├── pyproject.toml
├── README.md
├── src/canlib/
│   ├── __init__.py      # public API and __version__
│   └── library.py       # CANBus class
└── examples/
    └── hardware_check.py

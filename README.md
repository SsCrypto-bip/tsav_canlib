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

## Usage
```python
from canlib import CanBus
with CanBus(interface="socketcan", channel="can0") as bus:
    bus.send(arbitration_id=0x123, data=[1, 2, 3])
```

Or alternatively (manually close the bus)
```python
bus = CANBus("can0")
try:
    ...
finally:
    bus.shutdown()
```

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

from canlib import CANBus

with CANBus("can0") as bus:
    for _ in range(30):
        msg = bus.receive_message(timeout=1.0)
        if msg:
            print(msg)

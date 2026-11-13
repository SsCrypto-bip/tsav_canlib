from canlib import CANBus
canbus = CANBus()

canbus.receive_message(timeout=10.0)

        

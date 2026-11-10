# Configurable CANBus base class 
#Final check + Make sure theres proper shut down
import can


class CANBus:
    '''Base class for CAN bus communication'''
    def __init__(self, channel='can0'):
        '''Initialize CAN bus connection
        ARG: channel name (default 'can0')
        
        e.g. can = CANBus()
        '''
        
        self.channel = channel
        self.bus = None
        self.open()

    def open(self):
        '''Open CAN bus connection
        e.g. can.open()'''
        
        if self.bus is not None:
            return

        try:
            self.bus = can.interface.Bus(
                channel=self.channel,
                interface='socketcan'
            )
            print(f"CAN opened {self.channel}")
        except can.CanError:
            print(f"Failed to open CAN {self.channel}")
            raise
        
    def send_message(self, can_id: int, data: list):
        '''Send CAN message:
        ARG: CAN ID 11-bits
        ARG: 8 bytes data listed
        
        e.g. send_message(0x123, [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])
        '''
        msg = can.Message(
            arbitration_id=can_id,
            data=data,
            is_extended_id=False
        )

        try:
            self.bus.send(msg)
            print(f"Sent ID={hex(can_id)} DATA={data}")

        except can.CanError:
            print("Failed to send CAN message")
        except KeyboardInterrupt:
            print("Interrupt")
            self.shutdown()
            raise

    
    #Add new extended message class       
    def send_extended_message(self, can_id: int, data: list):
        '''Send Extended CAN message:
        ARG: CAN ID 29-bits
        ARG: 8 bytes data listed
        
        e.g. send_extended_message(0x1ABCDE, [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])
        '''
        msg = can.Message(
                    arbitration_id=can_id,
                    data=data,
                    is_extended_id=True
                )
        
        try:
            self.bus.send(msg)
            print(f"Sent ID={hex(can_id)} DATA={data}")

        except can.CanError:
            print("Failed to send extended message")
        except KeyboardInterrupt:
            print("Interrupt")
            self.shutdown()
            raise
#
    def receive_message(self, timeout: float):
        '''Receive CAN message with timeout
        ARG: timeout in seconds
        
        e.g. receive_message(1.0)
        '''
        try:
            msg = self.bus.recv(timeout)
            print(
                f"ID={hex(msg.arbitration_id)} "
                f"DATA={list(msg.data)}"
            )
        except KeyboardInterrupt:
                print("Interrupt")
                self.shutdown()
                raise
        return msg
    
    def shutdown(self):
        '''Shutdown CAN bus connection
        e.g. self.shutdown()
        '''
        
        if self.bus is not None:
            self.bus.shutdown()
        print("CANbus shutdown")
        self.bus = None

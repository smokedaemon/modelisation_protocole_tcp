from enum import Enum


class PacketType(Enum):
    DATA = 'DATA'
    ACK = 'ACK'  # <--- CRUCIAL: Permet la création d'accusés de réception


class Packet:
    def __init__(self, sn, size, type=PacketType.DATA):
        self.size = size
        self.type = type
        self.serial_number = sn

    def __repr__(self):
        return f'Packet({self.type} SN={self.serial_number}, {self.size} bytes)'

[INFO ] @@0.000000, Host(A) sends Packet(PacketType.DATA SN=1, 10 bytes)
[INFO ] @@0.000000, Host(A) sends Packet(PacketType.DATA SN=2, 10 bytes)
[INFO ] @@0.000000, Host(A) sends Packet(PacketType.DATA SN=3, 10 bytes)
[INFO ] @@0.000000, Host(A) sends Packet(PacketType.DATA SN=4, 10 bytes)
[INFO ] @@0.000085, Router(R) received Packet(PacketType.DATA SN=1, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.000165, Router(R) received Packet(PacketType.DATA SN=2, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.000245, Router(R) received Packet(PacketType.DATA SN=3, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.000250, Host(B) received Packet(PacketType.DATA SN=1, 10 bytes), sending ACK
[INFO ] @@0.000271, Router(R) received Packet(PacketType.ACK SN=1, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.000284, Host(A) received ACK for SN=1
[INFO ] @@0.000284, Host(A) Frigo status: 3 packets pending [2, 3, 4]
[INFO ] @@0.000284, Host(A) Window space available, taking SN=5 from buffer
[INFO ] @@0.000284, Host(A) sends Packet(PacketType.DATA SN=5, 10 bytes)
[INFO ] @@0.000325, Router(R) received Packet(PacketType.DATA SN=4, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.000405, Router(R) received Packet(PacketType.DATA SN=5, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.000410, Host(B) received Packet(PacketType.DATA SN=2, 10 bytes), sending ACK
[INFO ] @@0.000431, Router(R) received Packet(PacketType.ACK SN=2, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.000444, Host(A) received ACK for SN=2
[INFO ] @@0.000444, Host(A) Frigo status: 3 packets pending [3, 4, 5]
[INFO ] @@0.000444, Host(A) Window space available, taking SN=6 from buffer
[INFO ] @@0.000444, Host(A) sends Packet(PacketType.DATA SN=6, 10 bytes)
[INFO ] @@0.000529, Router(R) received Packet(PacketType.DATA SN=6, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.000570, Host(B) received Packet(PacketType.DATA SN=3, 10 bytes), sending ACK
[INFO ] @@0.000591, Router(R) received Packet(PacketType.ACK SN=3, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.000604, Host(A) received ACK for SN=3
[INFO ] @@0.000604, Host(A) Frigo status: 3 packets pending [4, 5, 6]
[INFO ] @@0.000604, Host(A) Window space available, taking SN=7 from buffer
[INFO ] @@0.000604, Host(A) sends Packet(PacketType.DATA SN=7, 10 bytes)
[INFO ] @@0.000689, Router(R) received Packet(PacketType.DATA SN=7, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.000730, Host(B) received Packet(PacketType.DATA SN=4, 10 bytes), sending ACK
[INFO ] @@0.000751, Router(R) received Packet(PacketType.ACK SN=4, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.000764, Host(A) received ACK for SN=4
[INFO ] @@0.000764, Host(A) Frigo status: 3 packets pending [5, 6, 7]
[INFO ] @@0.000764, Host(A) Window space available, taking SN=8 from buffer
[INFO ] @@0.000764, Host(A) sends Packet(PacketType.DATA SN=8, 10 bytes)
[INFO ] @@0.000849, Router(R) received Packet(PacketType.DATA SN=8, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.000890, Host(B) received Packet(PacketType.DATA SN=5, 10 bytes), sending ACK
[INFO ] @@0.000911, Router(R) received Packet(PacketType.ACK SN=5, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.000924, Host(A) received ACK for SN=5
[INFO ] @@0.000924, Host(A) Frigo status: 3 packets pending [6, 7, 8]
[INFO ] @@0.000924, Host(A) Window space available, taking SN=9 from buffer
[INFO ] @@0.000924, Host(A) sends Packet(PacketType.DATA SN=9, 10 bytes)
[INFO ] @@0.001009, Router(R) received Packet(PacketType.DATA SN=9, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.001050, Host(B) received Packet(PacketType.DATA SN=6, 10 bytes), sending ACK
[INFO ] @@0.001071, Router(R) received Packet(PacketType.ACK SN=6, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.001071, NIC(R:eth0) packet Packet(PacketType.ACK SN=6, 1 bytes) lost on link Link(L1)
[INFO ] @@0.001210, Host(B) received Packet(PacketType.DATA SN=7, 10 bytes), sending ACK
[INFO ] @@0.001231, Router(R) received Packet(PacketType.ACK SN=7, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.001244, Host(A) received ACK for SN=7
[INFO ] @@0.001244, Host(A) Frigo status: 2 packets pending [8, 9]
[INFO ] @@0.001244, Host(A) Window space available, taking SN=10 from buffer
[INFO ] @@0.001244, Host(A) sends Packet(PacketType.DATA SN=10, 10 bytes)
[INFO ] @@0.001329, Router(R) received Packet(PacketType.DATA SN=10, 10 bytes) on NIC(R:eth0), forwarded on NIC(R:eth1)
[INFO ] @@0.001370, Host(B) received Packet(PacketType.DATA SN=8, 10 bytes), sending ACK
[INFO ] @@0.001391, Router(R) received Packet(PacketType.ACK SN=8, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.001404, Host(A) received ACK for SN=8
[INFO ] @@0.001404, Host(A) Frigo status: 2 packets pending [9, 10]
[INFO ] @@0.001530, Host(B) received Packet(PacketType.DATA SN=9, 10 bytes), sending ACK
[INFO ] @@0.001551, Router(R) received Packet(PacketType.ACK SN=9, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.001564, Host(A) received ACK for SN=9
[INFO ] @@0.001564, Host(A) Frigo status: 1 packets pending [10]
[INFO ] @@0.001690, Host(B) received Packet(PacketType.DATA SN=10, 10 bytes), sending ACK
[INFO ] @@0.001711, Router(R) received Packet(PacketType.ACK SN=10, 1 bytes) on NIC(R:eth1), forwarded on NIC(R:eth0)
[INFO ] @@0.001724, Host(A) received ACK for SN=10
[INFO ] @@0.001724, Host(A) Frigo status: 0 packets pending []

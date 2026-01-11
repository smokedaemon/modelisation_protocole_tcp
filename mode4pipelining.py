import random
import logging
from simulator.Simulator import Simulator
from Packet import Packet
from NIC import NIC
from Host import Host, ReliabilityMode
from Router import Router
from Link import Link

# Utilisation du seed imposé pour la reproductibilité [cite: 77]
random.seed(2147483611)

logging.basicConfig(format='[%(levelname)-5s] @%(message)s')
for logger in ['NIC', 'Routers', 'Hosts', 'simulator']:
    logging.getLogger(logger).setLevel(logging.INFO)

sim = Simulator()
sim.reset()

# Topologie standard [cite: 12, 16, 17]
L1 = Link("L1", distance=1000, speed=2e8, lost_prob=0.01)
L2 = Link("L2", distance=1000, speed=2e8, lost_prob=0.01)

# Configuration identique au mode précédent mais avec retransmission [cite: 103]
hostA = Host(sim, 'A', mode=ReliabilityMode.PIPELINING_FIXED_WINDOW)
nicA = NIC(sim, 'eth0', 1e6)
hostA._window_size = 4
hostA.add_nic(nicA)
nicA.attach(L1)

# Routeur avec file d'attente de 20 [cite: 25, 26]
router = Router(sim, 'R')
nicR1 = NIC(sim, 'eth0', 1e6)
nicR2 = NIC(sim, 'eth1', 5e5, queue_size=20)
router.add_nic(nicR1)
router.add_nic(nicR2)
nicR1.attach(L1)
nicR2.attach(L2)

hostB = Host(sim, 'B', mode=ReliabilityMode.PIPELINING_FIXED_WINDOW)
nicB = NIC(sim, 'eth0', 5e5)
hostB.add_nic(nicB)
nicB.attach(L2)

pkts = [Packet(sn=i, size=10) for i in range(1, 11)]
hostA.send(pkts)
sim.run()
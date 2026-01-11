import random
import logging
from simulator.Simulator import Simulator
from Packet import Packet
from NIC import NIC
from Host import Host, ReliabilityMode
from Router import Router
from Link import Link

random.seed(42) # Graine pour la reproductibilité

logging.basicConfig(format='[%(levelname)-5s] @%(message)s')
logging.getLogger('Hosts').setLevel(logging.INFO)
logging.getLogger('NIC').setLevel(logging.INFO)

sim = Simulator()
sim.reset()

# Topologie goulot d'étranglement (Section 3 du PDF)
L1 = Link("L1", distance=1000, speed=2e8, lost_prob=0) # Pas de perte pour voir l'effet file d'attente
L2 = Link("L2", distance=1000, speed=2e8, lost_prob=0)

hostA = Host(sim, 'A', mode=ReliabilityMode.PIPELINING_DYNAMIC_WINDOW)
nicA = NIC(sim, 'eth0', 5e6) # 5 Mbps
hostA.add_nic(nicA)
nicA.attach(L1)

router = Router(sim, 'R')
nicR1 = NIC(sim, 'eth0', 5e6)
nicR2 = NIC(sim, 'eth1', 5e5, queue_size=10) # File de 10 seulement !
router.add_nic(nicR1)
router.add_nic(nicR2)
nicR1.attach(L1)
nicR2.attach(L2)

hostB = Host(sim, 'B', mode=ReliabilityMode.PIPELINING_DYNAMIC_WINDOW)
nicB = NIC(sim, 'eth0', 5e5)
hostB.add_nic(nicB)
nicB.attach(L2)

# Envoi de 50 paquets
pkts = [Packet(sn=i, size=10) for i in range(1, 51)]
hostA.send(pkts)
sim.run()
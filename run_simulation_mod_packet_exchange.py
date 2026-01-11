import random
import logging
from simulator.Simulator import Simulator
from Packet import Packet
from NIC import NIC
from Host import Host, ReliabilityMode
from Router import Router
from Link import Link


def run_simulation(mode, lost_prob_l1, lost_prob_l2, num_packets=10, seed=2147483611, queue_size=20, r1=1e6, r2=5e5):
    """
    Exécute une simulation paramétrable basée sur les topologies des fichiers fournis.
    """
    # 1. Configuration de la graine pour la reproductibilité [cite: 75, 77]
    random.seed(seed)

    # 2. Reset du simulateur
    sim = Simulator()
    sim.reset()

    # 3. Configuration des liens avec les lost_prob paramétrés [cite: 27, 28]
    c = 3e8
    L1 = Link("L1", distance=1000, speed=2 / 3 * c, lost_prob=lost_prob_l1)
    L2 = Link("L2", distance=1000, speed=2 / 3 * c, lost_prob=lost_prob_l2)

    # 4. Configuration des Hôtes [cite: 20, 36]
    hostA = Host(sim, 'A', mode=mode)
    nicA = NIC(sim, 'eth0', r1)
    hostA.add_nic(nicA)
    nicA.attach(L1)

    hostB = Host(sim, 'B', mode=mode)
    nicB = NIC(sim, 'eth0', r2)
    hostB.add_nic(nicB)
    nicB.attach(L2)

    # 5. Configuration du Routeur [cite: 16, 25]
    router = Router(sim, 'R')
    nicR1 = NIC(sim, 'eth0', r1)
    nicR2 = NIC(sim, 'eth1', r2, queue_size=queue_size)
    router.add_nic(nicR1)
    router.add_nic(nicR2)
    nicR1.attach(L1)
    nicR2.attach(L2)

    # 6. Génération et envoi du trafic [cite: 33, 34]
    pkts = [Packet(sn=i, size=10) for i in range(1, num_packets + 1)]

    print(f"\n>>> DÉMARRAGE : Mode {mode.name} | LostProb L1: {lost_prob_l1} | L2: {lost_prob_l2}")
    hostA.send(pkts)
    sim.run()
    print(f">>> FIN DU SCÉNARIO {mode.name}\n" + "=" * 50)


if __name__ == "__main__":
    # Configuration globale des logs [cite: 79, 82]
    logging.basicConfig(format='[%(levelname)-5s] @%(message)s', level=logging.INFO)

    # --- EXEMPLES D'APPELS PARAMÉTRABLES ---

    # 1. Simulation sans fiabilité (Mode 1) avec 5% de perte [cite: 38]
    run_simulation(ReliabilityMode.NO_RELIABILITY, lost_prob_l1=0.05, lost_prob_l2=0.05)

    # 2. Simulation Stop-and-Wait (Mode 2) sans perte [cite: 43, 126]
    run_simulation(ReliabilityMode.ACKNOWLEDGES, lost_prob_l1=0.0, lost_prob_l2=0.0)

    # 3. Simulation Retransmission (Mode 3) avec forte perte (15%) [cite: 48, 103]
    run_simulation(ReliabilityMode.ACKNOWLEDGES_WITH_RETRANSMISSION, lost_prob_l1=0.15, lost_prob_l2=0.02)

    # 4. Simulation Fenêtre Dynamique (Mode 5) - Topologie Goulot d'étranglement [cite: 61, 113]
    run_simulation(
        mode=ReliabilityMode.PIPELINING_DYNAMIC_WINDOW,
        lost_prob_l1=0.0,
        lost_prob_l2=0.0,
        num_packets=50,
        queue_size=10,
        r1=5e6,  # 5 Mbps [cite: 114]
        r2=5e5  # 500 kbps [cite: 115]
    )
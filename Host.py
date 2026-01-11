from Packet import PacketType, Packet
from simulator.SimulatedEntity import SimulatedEntity
from enum import Enum
from simulator.Event import Event


class ReliabilityMode(Enum):
    NO_RELIABILITY = 0
    ACKNOWLEDGES = 1
    ACKNOWLEDGES_WITH_RETRANSMISSION = 2
    PIPELINING_FIXED_WINDOW = 3
    PIPELINING_DYNAMIC_WINDOW = 4


class Host(SimulatedEntity):

    def __init__(self, sim, name, mode=ReliabilityMode.NO_RELIABILITY):
        super().__init__(sim, logger_name='Hosts')
        self._name = name
        self._nic = None
        self._mode = mode

        # Structures de données pour la fiabilité
        self._unacked_packets = []  # Le "Frigo" (paquets envoyés en attente d'ACK)
        self._buffer = []  # La file d'attente (paquets pas encore envoyés)
        self._window_size = 1  # Taille de la fenêtre (évolutive en mode 5)
        self._timer_pending = False  # État du timer
        self._timeout_duration = 0.5  # Délai avant retransmission

    def add_nic(self, nic):
        self._nic = nic
        nic.set_host(self)

    def _start_timer(self):
        """Déclenche le timer UNIQUEMENT si le mode le permet (Pas en mode 2)"""
        if self._mode == ReliabilityMode.ACKNOWLEDGES:
            # En mode 2, on ne lance jamais de timer (pas de retransmission)
            return

        if not self._timer_pending:
            self._timer_pending = True
            self.debug(f"Timer armed for {self._timeout_duration}s")
            self._sim.add_event(Event(None, lambda _: self._on_timeout()), self._timeout_duration)

    def _stop_timer(self):
        if self._timer_pending:
            self.debug("Timer stopped")
            self._timer_pending = False

    def _on_timeout(self):
        """Gestion du dépassement de temps (Timeout)"""


        if self._unacked_packets:
            # On relance l'envoi du paquet le plus ancien (le premier du frigo)
            oldest_pkt = self._unacked_packets[0]
            self.info(f'Timer expired for packet number {oldest_pkt.serial_number} !!')
            self.info(f'Retransmitting {oldest_pkt}')
            self._nic.send(oldest_pkt)

            # En mode dynamique, une perte fait retomber la fenêtre à 1
            if self._mode == ReliabilityMode.PIPELINING_DYNAMIC_WINDOW:
                self._window_size = 1
                self.info(f'Window size reset to {self._window_size}')

            # On réarme le timer pour la nouvelle tentative
            self._timer_pending = False
            self._start_timer()

    def receive(self, nic, pkt):
        if pkt.type == PacketType.DATA:
            self.info(f'received {pkt}, sending ACK')
            ack = Packet(sn=pkt.serial_number, size=1, type=PacketType.ACK)
            self._nic.send(ack)

        elif pkt.type == PacketType.ACK:
            self.info(f'received ACK for SN={pkt.serial_number}')

            # On arrête le timer car un paquet a été acquitté
            self._stop_timer()

            # Mise à jour du "Frigo" : on retire le paquet acquitté et les précédents (cumulatif)
            self._unacked_packets = [p for p in self._unacked_packets if p.serial_number > pkt.serial_number]

            # LOG DU FRIGO (Mise en avant pour le rapport)
            frigo_sns = [p.serial_number for p in self._unacked_packets]
            self.info(f'Frigo status: {len(self._unacked_packets)} packets pending {frigo_sns}')

            # Gestion de la fenêtre dynamique (Section 2.2 / Mode 5)
            if self._mode == ReliabilityMode.PIPELINING_DYNAMIC_WINDOW:
                self._window_size += 1
                self.info(f'Window size increased to {self._window_size}')

            # RELANCE DE L'ENVOI : On pioche dans le buffer si de la place s'est libérée
            while self._buffer and len(self._unacked_packets) < self._window_size:
                next_pkt = self._buffer.pop(0)
                self.info(f'Window space available, taking SN={next_pkt.serial_number} from buffer')
                self._transmit_packet(next_pkt)

    def send(self, pkts):
        """Point d'entrée pour l'envoi d'une liste de paquets"""
        if self._mode == ReliabilityMode.NO_RELIABILITY:
            for pkt in pkts:
                self._nic.send(pkt)
        else:
            for pkt in pkts:
                # Si la fenêtre n'est pas pleine, on transmet
                if len(self._unacked_packets) < self._window_size:
                    self._transmit_packet(pkt)
                else:
                    # Sinon, on stocke dans le buffer (le frigo est plein)
                    self._buffer.append(pkt)

    def _transmit_packet(self, pkt):
        """Logique d'envoi physique et armement du timer"""
        self.info(f'sends {pkt}')
        self._nic.send(pkt)

        # On ajoute au frigo AVANT de lancer le timer
        if pkt not in self._unacked_packets:
            self._unacked_packets.append(pkt)

        self._start_timer()

    def __repr__(self):
        return f'Host({self._name})'
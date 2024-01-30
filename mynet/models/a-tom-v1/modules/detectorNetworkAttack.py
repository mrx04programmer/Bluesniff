from impacket.ImpactDecoder import EthDecoder
from impacket.ImpactPacket import IP, TCP
from scapy.all import sniff
from colors import *
from platform import platform as pl

global iface
iface = 'Ethernet'
port = 22

def analizar_paquete(packet):
    decoder = EthDecoder()
    eth_packet = decoder.decode(packet)

    if IP in eth_packet:
        ip_packet = eth_packet.get_protocol(IP)
        if TCP in ip_packet:
            tcp_packet = ip_packet.get_protocol(TCP)
            src_ip = ip_packet.get_ip_src()
            src_port = tcp_packet.get_th_sport()
            dst_ip = ip_packet.get_ip_dst()
            dst_port = tcp_packet.get_th_dport()
            
            if dst_port < 1024:
                print(f"Escaneo de puertos sospechoso detectado desde {src_ip}:{src_port} hacia {dst_ip}:{dst_port}")


            if dst_port == 22 and tcp_packet.get_SYN() == 1 and tcp_packet.get_ACK() == 0:
                print(f"Intento de conexión SSH sospechoso desde {src_ip}:{src_port} hacia {dst_ip}:{dst_port}")


def main():
    print(f"{G}DETECTION {W}Iniciando deteccion de paquetes sospechosos en la red")
    print(f"{O}LISTEN {W}Análizando trafico en vivo...\n")
    print(f"{W}OUTPUT {W}Cierra la terminal para terminal el proceso o termina el PID\n")
    if "indow" in pl:
        sniff(iface=iface, prn=analizar_paquete, filter='ip')
    else:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        s.bind((iface, 0))

        while True:
            packet = s.recv(65535)
            analizar_paquete(packet, port)

if __name__ == '__main__':
    main()

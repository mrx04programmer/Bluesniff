import sys
from scapy.all import *
from colors import *

mitm_status = []

def detectar_ataque_mitm(tiempo_limite):

    print(f"{G}INFO {W}Detectando ataques MITM ... ")
    conf.sniff_promisc = True
    
    paquetes = sniff(filter="arp", timeout=tiempo_limite)

    direcciones_ip = set()
    direcciones_mac = set()

    for paquete in paquetes:
        if paquete[ARP].op == 2:
            direccion_ip = paquete[ARP].psrc
            direccion_mac = paquete[ARP].hwsrc

            if direccion_ip in direcciones_ip:
                print(f"¡Posible ataque MitM detectado! Dirección IP duplicada: {direccion_ip}")
                mitm_status.append(direccion_ip)
            if direccion_mac in direcciones_mac:
                print(f"¡Posible ataque MitM detectado! Dirección MAC duplicada: {direccion_mac}")
                mitm_status.append(direccion_mac)
            direcciones_ip.add(direccion_ip)
            direcciones_mac.add(direccion_mac)
    
            

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python anti-mitm.py <tiempo de espera>")
        sys.exit(1)
    tiempo_limite = int(sys.argv[1])
    detectar_ataque_mitm(tiempo_limite)
    if len(mitm_status) == 0:
        print(f"{G}OK {W}Todo parece estar bien respecto a reglas ARP")

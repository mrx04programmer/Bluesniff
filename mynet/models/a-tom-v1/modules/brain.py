from modules.data import Data as data
import os,sys, platform,ipaddress, socket, uuid
import numpy as np
class BrainNetwork:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    lugarReal = np.array(['Bogotá','Colombia'])
    context = []
    natural = []
    hacking = []
    for d in data.contextHacking:
        hacking.append(d)
    for dn in data.contextNatural:
        natural.append(dn)
class BrainLocal:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    hostname = socket.gethostname()
    ipLocal = socket.gethostbyname(hostname)
    macLocal = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])
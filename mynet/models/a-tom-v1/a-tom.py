## Colors
# Author: Mrx04programmer
# Github : https://github.com/mrx04programmer
from modules.brain import *
from difflib import SequenceMatcher
W = '\033[37m' # Default
R = '\033[1;31m'  # red
G = '\033[1;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[1;34m'  # blue
P = '\033[1;35m'  # purple
C = '\033[1;36m'  # cyan
sh = os.system
context = ['natural-0', 'hacking-0','saludos-0','despidos-0']
contextosNaturales = []
contextosHacking = []
contextosMachine = []
contextosSaludos = []
contextosDespidos = []

def clear():
    if 'indow' in platform.platform():
        sh('cls')
    else:
        sh('clear')

def banner():
    print(f"""{O}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣴⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⠿⠛⠋⠉⠁⠀⠀⠀⠈⠙⠻⢷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣾⡿⠋⠁⠀⣠⣶⣿⡿⢿⣷⣦⡀⠀⠀⠀⠙⠿⣦⣀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⡿⠋⠀⠀⢀⣼⣿⣿⣿⣶⣿⣾⣽⣿⡆⠀⠀⠀⠀⢻⣿⣷⣶⣄⠀
⠀⣴⣿⣿⠋⠀⠀⠀⠀⠸⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⠀⠀⠀⠐⡄⡌⢻⣿⣿⡷
⢸⣿⣿⠃⢂⡋⠄⠀⠀⠀⢿⣿⣿⣿⣿⣿⣯⣿⣿⠏⠀⠀⠀⠀⢦⣷⣿⠿⠛⠁
⠀⠙⠿⢾⣤⡈⠙⠂⢤⢀⠀⠙⠿⢿⣿⣿⡿⠟⠁⠀⣀⣀⣤⣶⠟⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠿⣾⣠⣆⣅⣀⣠⣄⣤⣴⣶⣾⣽⢿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠙⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀{G}A-TOM{W}
-------------------------------------------> {BrainLocal.ipLocal}""")
def thinker(ainput):
    respAtom = f"{G}[A-TOM] --> {W}"
    for d in data.contextNatural:
        porcentaje = data.Think(ainput, d)
        porcentajeInt = int(porcentaje)
        if porcentajeInt >= 60:    
            contextosNaturales.append(f'natural:{d}')
    for d in data.contextHacking:
        porcentaje = data.Think(ainput, d)
        porcentajeInt = int(porcentaje)
        if porcentajeInt >= 60:    
            contextosHacking.append(f'hacking:{d}')
    for d in data.contextSaludos:
        porcentaje = data.Think(ainput, d)
        porcentajeInt = int(porcentaje)
        if porcentajeInt >= 60:    
            contextosSaludos.append(f'saludo:{d}')
    for d in data.contextDespidos:
        porcentaje = data.Think(ainput, d)
        porcentajeInt = int(porcentaje)
        if porcentajeInt >= 60:    
            contextosDespidos.append(f'despido:{d}')
    context[0] = f'natural-{len(contextosNaturales)}'
    context[1] = f'hacking-{len(contextosHacking)}'
    context[2] = f'saludos-{len(contextosSaludos)}'
    context[3] = f'despidos-{len(contextosDespidos)}'
    print(context)

def main():
    clear()
    banner()
    while True:
        ainput = str(input(f"{C}[A-TOM] <-- {W}"))
        thinker(ainput)
        
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"{R}ERR {W}Error casuado por: {O}{e}")
        
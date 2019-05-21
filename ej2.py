import math
import numpy as np
from enum import Enum
import matplotlib

pos = 0
vel = 0
ac = 0
dt = 0.2
t = 0
M = 5
m = 4
Mt = M + m

# definición de reglas
REGLAS = [['PF', 'PF', 'PF', 'Z', 'Z'],
          ['PF', 'PP', 'PP', 'Z', 'NP'],
          ['PF', 'PP', 'Z', 'NP', 'NF'],
          ['PP', 'Z', 'NP', 'NP', 'NF'],
          ['Z', 'Z', 'NF', 'NF', 'NF']]


# definicion de umbrales conjutos borrosos
uNF = -20
uNP = -10
uPP = 10
uPF = 20

while t <= 27:
    # Asignacion de los conjuntos borrosos
    # posicion
    if pos <= uNF:
        Pnf = 1
        pos1 = [0, Pnf]
        pos2 = [0, Pnf]
    if pos > uNF and pos <= uNP:
        Pnp = abs((pos - uNF) / (uNF - uNP))
        Pnf = 1 - Pnp
        if Pnp >= Pnf:
            pos1 = [1, Pnp]
            pos2 = [0, Pnf]
        else:
            pos1 = [0, Pnf]
            pos2 = [1, Pnp]
    if pos > uNP and pos <= 0:
        Pze = abs((pos - uNP) / uNP - 0)
        Pnp = 1 - Pze
        if Pze >= Pnp:
            pos1 = [2, Pze]
            pos2 = [1, Pnp]
        else:
            pos1 = [1, Pnp]
            pos2 = [2, Pze]
    if pos > 0 and pos <= uPP:
        Ppp = abs(pos / uPP)
        Pze = 1 - Ppp
        if Ppp >= Pze:
            pos1 = [3, Ppp]
            pos2 = [2, Pze]
        else:
            pos1 = [2, Pze]
            pos2 = [3, Ppp]
    if pos > uPP and pos <= uPF:
        Ppf = abs((pos - uPP) / (uPF - uPP))
        Ppp = 1 - Ppf
        if Ppf >= Ppp:
            pos1 = [4, Ppf]
            pos2 = [3, Ppp]
        else:
            pos1 = [3, Ppp]
            pos2 = [4, Ppf]
    if pos >= uPF:
        Ppf = 1
        pos1 = [4, Ppf]
        pos2 = [4, Ppf]
    # velocidad
    if vel <= uNF:
        Vnf = 1
        vel1 = [0, Vnf]
        vel2 = [0, Vnf]
    if vel > uNF and vel <= uNP:
        Vnp = abs((vel - uNF) / (uNF - uNP))
        Vnf = 1 - Vnp
        if Vnp >= Vnf:
            vel1 = [1, Vnp]
            vel2 = [0, Vnf]
        else:
            vel1 = [0, Vnf]
            vel2 = [1, Vnp]
    if vel > uNP and vel <= 0:
        Vze = abs((vel - uNP) / uNP - 0)
        Vnp = 1 - Vze
        if Vze >= Vnp:
            vel1 = [2, Vze]
            vel2 = [1, Vnp]
        else:
            vel1 = [1, Vnp]
            vel2 = [2, Vze]
    if vel > 0 and vel <= uPP:
        Vpp = abs(vel / uPP)
        Vze = 1 - Vpp
        if Vpp >= Vze:
            vel1 = [3, Vpp]
            vel2 = [2, Vze]
        else:
            vel1 = [2, Vze]
            vel2 = [3, Vpp]
    if vel > uPP and vel <= uPF:
        Vpf = abs((vel - uPP) / (uPF - uPP))
        Vpp = 1 - Vpf
        if Vpf >= Vpp:
            vel1 = [4, Vpf]
            vel2 = [3, Vpp]
        else:
            vel1 = [3, Vpp]
            vel2 = [4, Vpf]
    if vel >= uPF:
        Vpf = 1
        vel1 = [4, Vpf]
        vel2 = [4, Vpf]

    # Cálculo de salida borrosa
    F1 = REGLAS[pos1[0], vel1[0]]
    F2 = REGLAS[pos2[0], vel2[0]]

    peso1 = min(pos1[1], vel1[1])
    peso2 = min(pos2[1], vel2[1])

    # Desborrosificación por media de centros (weighted average)
    Fsal = (F1 * peso1 + F2 * peso2) / (peso1 + peso2)

    num = g * sin(pos) + cos(pos) * (- F - m * l * vel ** 2 * sin(pos)) / Mt
    den = l * (4 / 3 - m * (cos(pos)) ** 2 / Mt)
    new_ac = num / den
    new_vel = vel + ac * dt
    new_pos = pos + vel * dt + ac * dt ** 2 / 2

    ac = new_ac
    vel = new_vel
    pos = new_pos
    t = t + dt

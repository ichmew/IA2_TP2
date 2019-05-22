import numpy as np
import math
from enum import Enum
from matplotlib import pyplot

pos = math.pi / 3
vel = 0
ac = 0
dt = 0.001
Fsal = 0
t = 0
l = 0.5
M = 2
m = 0.2
Mt = M + m
g = 9.8

plot_fuerza = []
plot_posicion = []
plot_velocidad = []
plot_aceleracion = []
plot_tiempo = []
plot_fuerza.append(Fsal)
plot_posicion.append(pos)
plot_velocidad.append(vel)
plot_aceleracion.append(ac)
plot_tiempo.append(t)

# definición de reglas (0,0) = pos:NF, vel:NF
REGLAS = [['PF', 'PF', 'PF', 'Z', 'Z'],
          ['PF', 'PP', 'PP', 'Z', 'NP'],
          ['PF', 'PP', 'Z', 'NP', 'NF'],
          ['PP', 'Z', 'NP', 'NP', 'NF'],
          ['Z', 'Z', 'NF', 'NF', 'NF']]

Valores_Fuerza = {
    'NF': -5,
    'NP': -2,
    'Z': 0,
    'PP': 2,
    'PF': 5
}

# definicion de umbrales conjutos borrosos
uNF = - math.pi / 4
uNP = - math.pi / 12
uPP = math.pi / 12
uPF = math.pi / 4

mNF = - math.pi / 12
mNP = - math.pi / 36
mPP = math.pi / 36
mPF = math.pi / 12

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
    if vel <= mNF:
        Vnf = 1
        vel1 = [0, Vnf]
        vel2 = [0, Vnf]
    if vel > mNF and vel <= mNP:
        Vnp = abs((vel - mNF) / (mNF - mNP))
        Vnf = 1 - Vnp
        if Vnp >= Vnf:
            vel1 = [1, Vnp]
            vel2 = [0, Vnf]
        else:
            vel1 = [0, Vnf]
            vel2 = [1, Vnp]
    if vel > mNP and vel <= 0:
        Vze = abs((vel - mNP) / mNP - 0)
        Vnp = 1 - Vze
        if Vze >= Vnp:
            vel1 = [2, Vze]
            vel2 = [1, Vnp]
        else:
            vel1 = [1, Vnp]
            vel2 = [2, Vze]
    if vel > 0 and vel <= mPP:
        Vpp = abs(vel / mPP)
        Vze = 1 - Vpp
        if Vpp >= Vze:
            vel1 = [3, Vpp]
            vel2 = [2, Vze]
        else:
            vel1 = [2, Vze]
            vel2 = [3, Vpp]
    if vel > mPP and vel <= mPF:
        Vpf = abs((vel - mPP) / (mPF - mPP))
        Vpp = 1 - Vpf
        if Vpf >= Vpp:
            vel1 = [4, Vpf]
            vel2 = [3, Vpp]
        else:
            vel1 = [3, Vpp]
            vel2 = [4, Vpf]
    if vel >= mPF:
        Vpf = 1
        vel1 = [4, Vpf]
        vel2 = [4, Vpf]

    # Cálculo de salida borrosa
    F1 = REGLAS[pos1[0]][vel1[0]]
    F2 = REGLAS[pos2[0]][vel2[0]]

    print(pos1[0], vel1[0], F1, pos2[0], vel2[0], F2)
    F1 = Valores_Fuerza.get(F1)
    F2 = Valores_Fuerza.get(F2)

    peso1 = min(pos1[1], vel1[1])
    peso2 = min(pos2[1], vel2[1])

    # Desborrosificación por media de centros (weighted average)
    Fsal = (F1 * peso1 + F2 * peso2) / (peso1 + peso2)
    # Fsal = 0
    seno = math.sin(pos)
    coseno = math.cos(pos)
    num = g * seno + coseno * (- Fsal - m * l * math.pow(vel, 2) * seno) / Mt
    den = l * (4 / 3 - m * math.pow(coseno, 2) / Mt)
    new_ac = num / den
    new_vel = vel + ac * dt
    new_pos = pos + vel * dt + ac * math.pow(dt, 2) / 2

    ac = new_ac
    vel = new_vel
    pos = new_pos
    t = t + dt

    plot_fuerza.append(Fsal)
    plot_posicion.append(pos)
    plot_velocidad.append(vel)
    plot_aceleracion.append(ac)
    plot_tiempo.append(t)


pyplot.figure(1)
pyplot.plot(plot_tiempo, plot_posicion)
pyplot.ylabel('Posicion')
pyplot.xlabel('Tiempo')

pyplot.figure(2)
pyplot.plot(plot_tiempo, plot_velocidad)
pyplot.ylabel('Velocidad')
pyplot.xlabel('Tiempo')


pyplot.figure(3)
pyplot.plot(plot_tiempo, plot_aceleracion)
pyplot.ylabel('Aceleracion')
pyplot.xlabel('Tiempo')

pyplot.figure(4)
pyplot.plot(plot_tiempo, plot_fuerza)
pyplot.ylabel('Fuerza')
pyplot.xlabel('Tiempo')

pyplot.show()

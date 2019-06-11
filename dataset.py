import pandas as pd
import numpy as np

def genera_data():

    datos = pd.read_csv('titanic_train.csv', header=0, na_filter=False)

    datosfiltrados=[datos['Sex'],datos['Age'],datos['Pclass'],datos['Embarked'],datos['Survived']]
    datostranspuestos = np.transpose(datosfiltrados)

    datostranspuestosfiltrados = np.array([v for v in datostranspuestos if v[1] != ''])

    datostranspuestosfiltradoscasteados = np.zeros([len(datostranspuestosfiltrados), len(datostranspuestosfiltrados[0])])

    for i in range(0, len(datostranspuestosfiltrados)):
        for j in range(0, len(datostranspuestosfiltrados[0])):
            if datostranspuestosfiltrados[i][j] == 'male':
                datostranspuestosfiltradoscasteados[i][j] = float(0)
            elif datostranspuestosfiltrados[i][j] == 'female':
                datostranspuestosfiltradoscasteados[i][j] = float(1)
            elif datostranspuestosfiltrados[i][j] == 'S':
                datostranspuestosfiltradoscasteados[i][j] = float(1)
            elif datostranspuestosfiltrados[i][j] == 'C':
                datostranspuestosfiltradoscasteados[i][j] = float(2)
            elif datostranspuestosfiltrados[i][j] == 'Q':
                datostranspuestosfiltradoscasteados[i][j] = float(3)
            elif datostranspuestosfiltrados[i][j] == '0' or datostranspuestosfiltrados[i][j] == 0:
                datostranspuestosfiltradoscasteados[i][j] = float(0)
            elif datostranspuestosfiltrados[i][j] == '1' or datostranspuestosfiltrados[i][j] == 1:
                datostranspuestosfiltradoscasteados[i][j] = float(1)
            elif datostranspuestosfiltrados[i][j] == '2' or datostranspuestosfiltrados[i][j] == 2:
                datostranspuestosfiltradoscasteados[i][j] = float(2)
            elif datostranspuestosfiltrados[i][j] == '3' or datostranspuestosfiltrados[i][j] == 3:
                datostranspuestosfiltradoscasteados[i][j] = float(3)
        datostranspuestosfiltradoscasteados[i][1] = float(datostranspuestosfiltrados[i][1])

    df = pd.DataFrame(datostranspuestosfiltradoscasteados)
    df.to_csv('datos_filtrados_train.csv')

    ejemplos = np.zeros([len(datostranspuestosfiltrados), len(datostranspuestosfiltrados[0])-1])
    t = np.zeros(len(datostranspuestosfiltrados))

    for i in range(0, len(datostranspuestosfiltradoscasteados)):
        t[i] = datostranspuestosfiltradoscasteados[i][4]
        for j in range(0, len(datostranspuestosfiltradoscasteados[0])-1):
            ejemplos[i][j] = datostranspuestosfiltradoscasteados[i][j]     

    return t, ejemplos


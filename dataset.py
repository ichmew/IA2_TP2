import pandas as pd
import numpy as np

numfilas=890
datos = pd.read_csv('titanic_train.csv', header=0, na_filter=False)

datosfiltrados=[datos['Survived'],datos['Pclass'],datos['Sex'],datos['Age'],datos['Embarked']]
datostranspuestos = np.transpose(datosfiltrados)

datostranspuestosfiltrados = np.array([v for v in datostranspuestos if v[3] != ''])

print(datostranspuestosfiltrados)

df = pd.DataFrame(datostranspuestosfiltrados)
df.to_csv('datos_filtrados.csv')


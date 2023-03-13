import pandas as pd

df = pd.DataFrame()
nombres = ['Ana', 'Bruno', 'César', 'Diego', 'Erika']
edades = [28, 33, 34, 23, 28]
estatura = [172, 169, 177, 179, 169]
beca = [True, False, False, True, True]
calificacion = [8, 7, 8, 10, 7]

df['Nombre'] = nombres
df['Edad'] = edades
df['Estatura'] = estatura
df['¿Beca?'] = beca
df['Calificación'] = calificacion

print(df)

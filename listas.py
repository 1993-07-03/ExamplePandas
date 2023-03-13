import pandas as pd

nombre_columnas = ['Nombre', 'Edad', 'Estatura', '¿Beca?', 'Calificación']
lista_ana = ['Ana', 28, 1.72, True, 8]
lista_bruno = ['Bruno', 33, 1.69, False, 7]
lista_cesar = ['Cesar', 34, 1.77, False, 8]
lista_diego = ['Diego', 23, 1.79, True, 10]
lista_erika = ['Erika', 25, 1.69, True, 7]

df = pd.DataFrame([lista_ana, lista_bruno, lista_cesar, lista_diego, lista_erika],
    columns= nombre_columnas
)
print(df)

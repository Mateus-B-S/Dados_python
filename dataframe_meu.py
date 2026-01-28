import pandas as pd
import numpy as np


df_salarios = pd.DataFrame({ 
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel', 'mateus'], 
    'salario': [5000, np.nan, 5500, np.nan, 80000]
})

#tratamento de valores nulos
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median().round(2))
#cria uma coluna chamado "salario_media" e preenche os valores nulos com a média arredondada para 2 casas decimais

print("\nDataFrame com valores nulos tratados: \n" )
print(df_salarios)

df_temperaturas = pd.DataFrame({
    'dias': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [30.7, np.nan, np.nan, 19.0, 25.5]
})

print("\nDataFrame de temperaturas original: \n")
print(df_temperaturas)
df_temperaturas['temperatura_ffill'] = df_temperaturas['temperatura'].ffill() #fill forward
df_temperaturas['temperatura_bfill'] = df_temperaturas['temperatura'].bfill() #fill backward 
print("\nDataFrame de temperaturas com valores nulos tratados: \n")
print(df_temperaturas)

df_cidades = pd.DataFrame({
    'nomes': ["julia", "marcos", "ana", "carlos", "beatriz"],
    'cidades': ["são paulo", np.nan, "rio de janeiro", np.nan, "belo horizonte"]
})

print("\nDataFrame de cidades original: \n")
print(df_cidades)
df_cidades['cidades_preenchidas'] =  df_cidades['cidades'].fillna("não registrado")
print("\nDataFrame de cidades com valores nulos tratados: \n")
print(df_cidades)
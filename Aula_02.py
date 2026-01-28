import pandas as pd

from nomes import novos_nomes



dataFrame = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")


dataFrame.rename(columns=novos_nomes, inplace=True)

# lê e conta quais campos possuem valores nulos
print("Valores nulos por coluna: \n")
print(dataFrame.isnull().sum(), "\n")

#descobre-se que a coluna "ano" possui valores nulos

print(dataFrame['ano'].unique()) #aparece "NaN"

#filtro

print("Linhas com valores nulos na coluna 'ano': \n")
#Pega Toda a tabela, vê quais são os nulos e mostra as linhas com valores nulos
print(dataFrame[dataFrame.isnull().any(axis=1)]) 

#excluir linhas com valores nulos na coluna "ano"


print("\nDataFrame sem linhas com valores nulos na coluna 'ano': \n")
dataFrame_limpo = dataFrame.dropna(subset=['ano'])
dataFrame_limpo = dataFrame_limpo.assign(ano=dataFrame_limpo['ano'].astype("Int64")) #converte a coluna "ano" para inteiro

print(dataFrame_limpo.isnull().sum()) #verifica se ainda há valores nulos

import pandas as pd

from nomes import novos_nomes, senioridade, contrato, tamanho_empresa

dataFrame = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print("Tabela de salários:  \n")



dataFrame.rename(columns=novos_nomes, inplace=True)

dataFrame["senioridade"] = dataFrame["senioridade"].replace(senioridade)


dataFrame['contrato'] = dataFrame['contrato'].replace(contrato)



dataFrame['tamanho_empresa'] = dataFrame['tamanho_empresa'].replace(tamanho_empresa)


print(dataFrame.head(), "\n")

dataFrame = dataFrame.rename(columns=novos_nomes)

print(" informações: \n") 

dataFrame.info()

print("\n")

print("Descrição: \n")

print(dataFrame.describe(), "\n")

print("Análise de cada coluna: \n")

print(dataFrame.describe(include='str'), "\n")

print("linhas: ", dataFrame.shape[0], "\ncolunas: ", dataFrame.shape[1])

# Contagem de valores únicos na coluna 'senioridade'

print("\nContagem de valores únicos na coluna 'senioridade': \n")
print(dataFrame["senioridade"].value_counts())
print("\n")

# Tipo de contrato

print("Tipo do contrato: \n")
print(dataFrame["contrato"].value_counts())
print("\n")
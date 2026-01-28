import pandas as pd

dataFrame = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print("Tabela de salários:  \n")


novos_nomes = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

dataFrame.rename(columns=novos_nomes, inplace=True)
# modificando alguns valores
senioridade = {
    'SE': 'senior',
    'MI': 'pleno',
    'EN': 'junior',
    'EX': 'executivo'
}

dataFrame["senioridade"] = dataFrame["senioridade"].replace(senioridade)

contrato = {
    'FT': 'integral',
    'PT': 'parcial',
    'CT': 'contrato',
    'FL': 'freelancer'
}

dataFrame['contrato'] = dataFrame['contrato'].replace(contrato)

tamanho_empresa = {
    'L': 'grande',
    'S': 'pequena',
    'M':	'media'
}

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
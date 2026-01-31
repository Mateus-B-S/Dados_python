"""
  Criar um gráfico dinâmico que filtra o dataframe por país
  e, disso, pegar o salário médio de um cientista de dados (Data Scientist)
"""

import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from nomes import novos_nomes, moedas

dataFrame = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
dataFrame.rename(columns=novos_nomes, inplace=True)
dataFrame['moeda'] = dataFrame['moeda'].map(moedas)
dataFrame_limpo = dataFrame.dropna(subset=['ano'])
dataFrame_limpo = dataFrame_limpo.assign(ano=dataFrame_limpo['ano'].astype("Int64"))

ordem_moedas = dataFrame_limpo.groupby('moeda')['usd'].mean().sort_values(ascending=True).index
print(dataFrame['moeda'].unique()) #verifica as moedas presentes no dataframe
cientista_dados = dataFrame_limpo[dataFrame_limpo['cargo'] == 'Data Scientist']



    
# Agrupa por país e calcula a média salarial anual, mas deve apenas mostrar os países que tem cientistas de dados
data_scient_por_pais = cientista_dados.groupby('moeda')['usd'].mean().sort_values(ascending=True).index

plt.figure(figsize=(20,4))
sns.barplot(data= cientista_dados, x='moeda', y='usd', order=data_scient_por_pais, hue='moeda', palette='plasma', legend=False)
plt.title('Salário Médio Anual de Data Scientist por País')
plt.xlabel('País')
plt.ylabel('Salário Médio Anual (USD)')
plt.show()

fig = px.bar(cientista_dados,
             x='moeda',
             y='usd',
             title='Salário Médio Anual de Data Scientist por País',
             labels={'moeda': 'País', 'usd': 'Salário Médio Anual (USD)'},
             category_orders={'moeda':data_scient_por_pais}
)
fig.show()


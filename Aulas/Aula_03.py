import pandas as pd
from Ferraments_e_extras.nomes import novos_nomes, senioridade, indice_remoto
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"

dataFrame = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

dataFrame.rename(columns=novos_nomes, inplace=True)
dataFrame['senioridade'] = dataFrame['senioridade'].map(senioridade)
dataFrame['indice_remoto'] = dataFrame['indice_remoto'].map(indice_remoto)


df_limpo = dataFrame.dropna(subset=['ano'])
df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype("Int64"))

ordem_salarios = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index

#df_limpo['senioridade'].value_counts().plot(kind='barh', title='Distribuição de Senioridade')
#plt.show()



# Gráfico de barras do salário médio anual por senioridade
plt.figure(figsize=(8,4))
sns.barplot(data= df_limpo, x='senioridade', y='usd', order=ordem_salarios, hue='senioridade', palette='plasma', legend=False)
plt.title('Salário Médio Anual por Senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário Médio Anual (USD)')
plt.show()


# Histograma da distribuição dos salários em USD
plt.figure(figsize=(8,4))
sns.histplot(data=df_limpo, x='usd', bins = 50, kde=True, weights=None, palette='rocket', hue='senioridade', legend=True) #gráfico com o tamanho de 8 por 4, com 50 barras e com a linha de densidade
plt.title('Distribuição dos Salários em USD')
plt.ylabel('Frequência')
plt.xlabel('Salário (USD)')
plt.show()

# Gráfico de boxplot do salário por senioridade
ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']
plt.figure(figsize=(8,5))
sns.boxplot(data=df_limpo, x=df_limpo['senioridade'], y=df_limpo['usd'], order=ordem_senioridade, palette='Set2', hue='senioridade', legend=False)
plt.xlabel('Salário (USD)')
plt.title('Boxplot do Salário por Senioridade')
plt.show()



# Gráfico interativo de barras do salário médio anual por senioridade usando Plotly

media_salarios = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).reset_index()
fig = px.bar(media_salarios,
             x='senioridade',
             y='usd',
             title='Salário Médio Anual por Senioridade',
             labels={'senioridade':'Senioridade', 'usd':'Salário Médio Anual (USD)'},
)
fig.show()

remoto_contagem = df_limpo['indice_remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
fig2 = px.pie(remoto_contagem,
              names='tipo_trabalho',
              values='quantidade',
              title='Proporção dos Tipos de Trabalho',
              labels={'tipo_trabalho':'Tipo de Trabalho', 'quantidade':'Quantidade'}    
)
fig2.update_traces(textposition='inside', textinfo='percent+label')
fig2.show()
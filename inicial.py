#!/usr/bin/env python
# coding: utf-8

# # Python Insights - Analisando Dados com Python
# 
# ### Case - Cancelamento de Clientes
# 
# Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.
# 
# Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.
# 
# Base de dados e arquivos: https://drive.google.com/drive/folders/1uDesZePdkhiraJmiyeZ-w5tfc8XsNYFZ?usp=drive_link

# ### Importar a base de dados

# In[54]:


import pandas as pd


# ### Visualizar a base de dados

# In[55]:


df_cancelamentos = pd.read_csv('cancelamentos.csv')

display(df_cancelamentos)


# ### Tratamento de erros ( Resolver as cagadas da base de dados)

# #### Possiveis Problemas
#     - dados int em tipo float
#     - valores ausentes
#     - Colunas desnecessárias, como a customerID, não fazem sentido para a análise do motivo do cancelamento do cliente, pois não agregam valor à compreensão do problema. Manter essas colunas só torna a análise ou a planilha mais pesada e confusa, prejudicando o desempenho e a clareza do trabalho. Portanto, colunas ou linhas que não contribuem para a análise devem ser removidas para otimizar o processo.

# In[56]:


#identificamos que temos valores vazios em algumas colunas e com o DROPNA estamos exluindo todas essas linhas
print(df_cancelamentos.info())
df_cancelamentos = df_cancelamentos.dropna()
print(df_cancelamentos.info())


# In[57]:


#Excluindo colunas desnecessárias.
df_cancelamentos = df_cancelamentos.drop('CustomerID', axis=1)
print(df_cancelamentos.info())


# ### Análise inicial dos dados (entender como estão os cancelamentos)

# In[58]:


df_cancelamentos['duracao_contrato'].value_counts(normalize=True).map("{:.2%}".format)
df_cancelamentos['cancelou'].value_counts(normalize=True).map("{:.2%}".format)


# In[59]:


display(df_cancelamentos.groupby('duracao_contrato').mean(numeric_only=True)) 
#foi identificado que a média de contratos mensais cancelados é de 100% ou seja temos algum problema nos contratos mensais
display(df_cancelamentos.groupby('assinatura').mean(numeric_only=True))
display(df_cancelamentos.groupby('sexo').mean(numeric_only=True))
#nos tipos de assinaturas e sexo não foi identificado nenhuma disparidade de problemas


# In[60]:


df_cancelamentos_tratada = df_cancelamentos[df_cancelamentos['duracao_contrato']!='Monthly']
#vamos ver o cancelamento sem os clientes do mensal
df_cancelamentos_tratada['duracao_contrato'].value_counts(normalize=True).map("{:.2%}".format)
df_cancelamentos_tratada['cancelou'].value_counts(normalize=True).map("{:.2%}".format)


# ### Análise profuda da base de dados (encotrando a causa dos cancelamentos)

# In[61]:


import plotly.express as px

for coluna in df_cancelamentos_tratada.columns:
    grafico =  px.histogram(df_cancelamentos_tratada, x=coluna, color='cancelou', text_auto=True)
    grafico.show()


# In[62]:


#pessoas do plano mensal também cancelam
#ligações de call center a partir de 5 cancelam
df_cancelamentos_tratada = df_cancelamentos_tratada[df_cancelamentos_tratada['ligacoes_callcenter']<5]
#dias de atraso, a partir de 21 cancelam
df_cancelamentos_tratada = df_cancelamentos_tratada[df_cancelamentos_tratada['dias_atraso']<=20]
#total gasto até 492 cancelam
df_cancelamentos_tratada = df_cancelamentos_tratada[df_cancelamentos_tratada['total_gasto']>=493]
#pessoas acima de 51 anos de idade cancelam
df_cancelamentos_tratada = df_cancelamentos_tratada[df_cancelamentos_tratada['idade']<=50]


#vamos ver o cancelamento sem os clientes do mensal
display(df_cancelamentos_tratada['cancelou'].value_counts(normalize=True).map("{:.2%}".format))


# In[63]:


for coluna in df_cancelamentos_tratada.columns:
    grafico =  px.histogram(df_cancelamentos_tratada, x=coluna, color='cancelou', text_auto=True)
    grafico.show()


# In[ ]:





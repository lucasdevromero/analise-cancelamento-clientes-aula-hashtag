# Análise de Cancelamento de Clientes

Este projeto tem como objetivo analisar a base de dados de uma empresa com mais de 800 mil clientes para identificar os principais motivos que levam ao cancelamento de serviços. A partir da análise, buscamos extrair insights que possam embasar a criação de ações estratégicas para reduzir a taxa de churn (cancelamento).

O script `inicial.py` realiza o tratamento, a análise exploratória e a visualização dos dados para encontrar os padrões de comportamento dos clientes que cancelaram o serviço.

## 📁 Estrutura do Projeto

  - `inicial.py`: Script principal em Python que contém todo o processo de análise.
  - `cancelamentos.csv`: Base de dados com as informações dos clientes (não incluído neste repositório).

## 🎯 Objetivo

A empresa notou que a maior parte de sua base de clientes é composta por usuários inativos (que já cancelaram). O objetivo desta análise é responder às seguintes perguntas:

1.  Quais são os principais motivos que levam um cliente a cancelar?
2.  Qual o perfil dos clientes que cancelam?
3.  Quais ações podem ser tomadas para reduzir a taxa de cancelamento?

## 🛠️ Tecnologias e Bibliotecas Utilizadas

O projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas:

  - **Pandas:** Para manipulação e análise de dados.
  - **Plotly Express:** Para criação de visualizações de dados interativas.

### Pré-requisitos

Para executar o script, você precisará ter o Python e as bibliotecas listadas acima instaladas. Você pode instalá-las usando o pip:

```bash
pip install pandas plotly
```

## 📈 Etapas da Análise

O script segue um fluxo estruturado para garantir que os dados sejam corretamente processados e que os insights sejam confiáveis.

### 1\. Carga e Visualização dos Dados

  - A análise começa com a importação da base de dados `cancelamentos.csv` para um DataFrame do Pandas.

### 2\. Tratamento e Limpeza dos Dados

  - **Remoção de Valores Ausentes:** Linhas com dados faltantes foram removidas utilizando o método `.dropna()` para garantir a integridade da análise.
  - **Exclusão de Colunas Desnecessárias:** A coluna `CustomerID` foi removida, pois não agrega valor à análise dos motivos de cancelamento, servindo apenas como um identificador único.

### 3\. Análise Inicial

  - Foi realizada uma análise exploratória para entender a distribuição dos dados.
  - **Principal Descoberta Inicial:** Identificou-se que **100% dos clientes com contrato do tipo `Monthly` (Mensal) cancelaram o serviço**. Este foi o primeiro grande indicador de um problema crítico.

### 4\. Análise Aprofundada e Visualização

  - Para aprofundar a investigação, os clientes de contrato mensal foram temporariamente removidos da análise principal para que outros padrões pudessem ser observados.
  - Foram gerados histogramas para cada variável da base de dados, utilizando a biblioteca Plotly. Os gráficos foram coloridos pela variável `cancelou`, permitindo uma comparação visual clara entre o perfil dos clientes que cancelaram e dos que permaneceram.

## 📊 Principais Insights e Conclusões

A análise visual dos dados revelou os seguintes perfis de clientes com alta probabilidade de cancelamento:

1.  **Duração do Contrato:** Clientes com **contrato mensal** têm uma taxa de cancelamento altíssima.
2.  **Ligações para o Call Center:** Clientes que realizam **5 ou mais ligações** para o call center tendem a cancelar. Isso sugere insatisfação com o serviço ou problemas recorrentes não resolvidos.
3.  **Atraso no Pagamento:** Um atraso de **21 dias ou mais** no pagamento é um forte indicador de um futuro cancelamento.
4.  **Idade:** Clientes com **mais de 51 anos** apresentam uma taxa de cancelamento superior à dos mais jovens.
5.  **Total Gasto:** Clientes com um **gasto total acumulado abaixo de R$ 500** são mais propensos a cancelar, indicando baixo engajamento ou pouco valor percebido no serviço.

Ao filtrar a base de dados para remover os clientes que se encaixam nesses perfis de risco, a taxa de cancelamento na base remanescente caiu para menos de **8%**, validando que esses são os principais fatores que impulsionam o churn.

## 🚀 Recomendações

Com base nos insights gerados, as seguintes ações estratégicas são recomendadas:

  - **Incentivar Contratos de Longo Prazo:** Oferecer descontos ou benefícios para clientes que migrarem do plano mensal para o anual ou trimestral.
  - **Melhorar o Atendimento ao Cliente:** Investigar os motivos das ligações recorrentes ao call center e otimizar os processos para resolver os problemas dos clientes de forma mais eficiente, preferencialmente no primeiro contato.
  - **Ações Proativas para Pagamentos em Atraso:** Criar um sistema de régua de cobrança mais eficaz e oferecer opções de negociação para clientes com mais de 20 dias de atraso.
  - **Engajamento de Novos Clientes:** Desenvolver estratégias de *onboarding* para novos clientes, garantindo que eles extraiam o máximo de valor do serviço nos primeiros meses para aumentar o "total gasto" e diminuir a chance de cancelamento.
  - **Campanhas de Retenção Segmentadas:** Criar campanhas de marketing e relacionamento direcionadas ao público com mais de 50 anos para entender suas necessidades específicas e aumentar sua satisfação.

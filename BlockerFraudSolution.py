# MODELO DE NEGÓCIO
# receber 25% do valor de cada transação detectada verdadeiramente como fraude.
# receber 5% do valor de cada transação detectada como fraude, porém a transação é verdadeiramente legítima.
# devolver 100% do valor para cada transação detectada como legítima, porém a transação é verdadeiramente uma fraude.


# RESPONSER AS PERGUNTAS:
# Qual a Precisão e Acurácia do modelo?
# Qual a Confiabilidade do modelo em classificar as transações como legítimas ou fraudulentas?
# Qual o Faturamento Esperado pela Empresa se classificarmos 100% das transações com o modelo?
# Qual o Prejuízo Esperado pela Empresa em caso de falha do modelo?
# Qual o Lucro Esperado pela Blocker Fraud Company ao utilizar o modelo?

import pandas as pd

data = pd.read_csv("Data/PS_20174392719_1491204439457_log.csv")

# print(data.shape)     =       (6362620, 11)
print(data.dtypes)

# print(data['type'].unique())   =    ['PAYMENT' 'TRANSFER' 'CASH_OUT' 'DEBIT' 'CASH_IN']

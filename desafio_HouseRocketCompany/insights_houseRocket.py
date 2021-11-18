#carregue o conjunto de dados \kc_house_data.csv 
#local do arquivo: "H:\PYTHON\Python do ZERO ao DS\BD\kc_house_data.csv"

import numpy as np
import pandas as pd
from pandas.io.parsers import read_csv
from datetime import date

diretorio = open('D\kc_house_data.csv','rb')
dataset = pd.read_csv(diretorio)

#reponder as perguntas feitas pelo CEO sobre o seu negócio

print(' 1. Quantas casa estão dísponíveis para compra?' )
#selecionar apenas os valores da coluna id
#para retornar a quantidade de itens disponíveis no BD

totalCasas=len(dataset['id'].unique())
print('R: O total de casas disponíveis é de: {}'.format(totalCasas))


print('2. Quantos atributos as casas possuem? ')
# As colunas de id e data não são atributos das casas

atributos = len(dataset.drop(['id', 'date'], axis=1).columns)
print('R: O total de tributos que as casas possuem são: {}'. format(atributos))


print('3. Quais os atributos das casas? ')
#desconsiderar as colunas id, e data e listas da demais
print(dataset.drop(['id', 'date'], axis=1).columns)


print('4. Qual a casa mais cara? ')
#listar casa com maior valor na coluna price
#
casaMaiscara = dataset[['id', 'price']].sort_values('price', ascending=False).reset_index(drop=True).loc[0,'id']
print('R: A casa mais cara é:  {} '. format(casaMaiscara))

print('5. Qual a casa com maior número de quartos? ')
#listar casas com maior número de quartos na coluna bedrooms

casaMaisquartos = dataset[['id', 'bedrooms']].sort_values('bedrooms', ascending=False).reset_index(drop=True).loc[0,'id']
print('R: A casa com maior número de quartos é:  {} '. format(casaMaisquartos))

print('6. Qual a soma total de quartos de todas as casas? ')
#somar a quandidade de quartos do conjunto de dados

print(dataset['bedrooms'].sum())


print('7. Quantas casas possuem 2 banheiros? ')
#selecionar as casas com 2 banheiros, filtrar os valores e lista-las

casas=len(dataset.loc[dataset['bathrooms'] == 2, ['id', 'bathrooms']])
print('Quantidade de casas com 2 banheiros é: {}'. format(casas))

print('8. Qual a média dos preços da casas do conjunto de dados? ')
print(dataset['price'].mean())

print('9. Qual o preço médio das casas com 2 banheiros?' )
print(np.round(dataset.loc[dataset['bathrooms'] == 2, 'price'].mean(),2))

print('10. Qual o preço mínimo entre as casas com 3 quartos? ')
print(np.round(dataset.loc[dataset['bedrooms'] == 3, 'price'].min(),2))

print('11. Quantas casas possuem mais de 300 metros quadrados na sala de estar? ')
dataset['m2'] = dataset['sqrft_living'] * 0.093
len(dataset.loc[dataset['m2'] > 300, id])

print('12. Quantas casas tem mais de 2 andares? ')


print('13. Quantas casas tem vista para o mar? ')


print('14. Das casas com vista para o mar, quantas tem 3 quartos? ')


print('15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?')

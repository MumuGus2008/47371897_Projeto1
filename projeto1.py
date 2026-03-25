import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')

# ENTRADA
capital = float(input('Capital inicial: '))
aporte = float(input('Aporte mensal: '))
meses = int(input('Prazo : '))
cdi_anual = float(input('CDI anual (%): '))
per_cdb = float(input('Percentual CDI - CDB (%): '))
perc_lci = float(input('Percentual CDI - LCI (%): '))
taxa_fii = float(input('Rentabilidade FII (%): '))

# CONVERSÃO CDI
cdi_mensal = math.pow((1 + cdi_anual/100), 1/12) - 1

# TOTAL INVESTIDO
total_investido = capital + (aporte * meses)

# CDB
taxa_cdb = cdi_mensal * (per_cdb/100)
montante_cdb = (capital * math.pow((1 + taxa_cdb), meses)) + (aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

# LCI
taxa_lci = cdi_mensal * (perc_lci/100)
montante_lci = (capital * math.pow((1 + taxa_lci), meses)) + (aporte * meses)

# POUPANÇA
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1 + taxa_poupanca), meses)) + (aporte * meses)

# FII
investimento = float(input('Valor investido no FII (R$): '))
taxa_anual = float(input('Taxa anual (%): '))
tempo = int(input('Tempo do investimento (anos): '))

montante_fii = investimento * (1 + taxa_anual/100) ** tempo

print(f'Após {tempo} anos, seu montante é : {locale.currency(montante_fii, grouping=True)}')

# SIMULAÇÕES FII
resultados = []

for i in range(5):
    montante_fii_final = investimento * (1 + taxa_fii/100) ** tempo
    variacao = random.uniform(-0.03, 0.03)
    valor_final = montante_fii_final * (1 + variacao)
    resultados.append(valor_final)

# CALCULOS 
media = statistics.mean(resultados)
mediana = statistics.median(resultados)
desvio = statistics.stdev(resultados)

# RESULTADOS
print('Simulações FII:')
for i, valor in enumerate(resultados, 1):
    print(f'Simulação {i}: {locale.currency(valor, grouping=True)}')

print('Estatísticas:')
print(f'Média: {locale.currency(media, grouping=True)}')
print(f'Mediana: {locale.currency(mediana, grouping=True)}')
print(f'Desvio: {locale.currency(desvio, grouping=True)}')

# COMPARAÇÃO 
print('Comparação de investimentos:')
print(f'CDB líquido: {locale.currency(montante_cdb_liquido, grouping=True)}')
print(f'LCI: {locale.currency(montante_lci, grouping=True)}')
print(f'Poupança: {locale.currency(montante_poupanca, grouping=True)}')

# DATA
data_atual = input('Digite a data atual (d/m/y): ')
meses_resgate = int(input('Meses até o resgate: '))

data_inicial = datetime.datetime.strptime(data_atual, '%d/%m/%y')
data_final = data_inicial + datetime.timedelta(days=meses_resgate * 30)

print(f'Data de resgate: {data_final.strftime("%d/%m/%y")}')
print(f'Dia da semana: {data_final.strftime("%A")}')
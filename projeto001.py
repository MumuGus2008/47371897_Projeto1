from os import system 
from datetime import datetime, timedelta

def formata_valor(valor):
    return f'R$ {valor:_.2f}'.replace('_','.').replace('.' , ',')

system ('cls')
try:
    tipo = (input('Tipo de investimento (LCI ou CDB) :'))
    capital = float(input('Capital inicial:'))
    taxa = float (input('Taxa de juros mensal:'))
    prazo = int (input('Quantidade de meses:'))
    montante = capital * (1 + taxa / 100) ** prazo
    hoje = datetime.now()
    vencimento = hoje + timedelta(days = prazo*30)
    aplicacao = hoje + timedelta(days = prazo+0)
except ValueError:
        print('Entrada invalida !')
else:
    print('\nResumo do Investimento')
    print('\n')
    print (f'Tipo de invesstimento:{tipo}')
    print(f'Capital Inicial: {formata_valor(capital)}')
    print(f'Taxa de Juros: {taxa:.2f}% ao mês')
    print(f'Número de meses: {prazo}')
    print(f'Montante final: {formata_valor(montante)}')
    print('\n --------DATAS--------')
    print('\n')
    print(f'Data de Aplicação:{aplicacao.strftime('%d/%m/%y')}')
    print(f'Data de vencimento:{vencimento.strftime('%d/%m/%y')}')
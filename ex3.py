#EX 3

import json

with open('dados.json', 'r') as file:
    faturamentoDiario = json.load(file)

faturamentoValido = [dia['valor'] for dia in faturamentoDiario if dia['valor'] > 0]

menorFaturamento = min(faturamentoValido)
maiorFaturamento = max(faturamentoValido)

mediaMensal = sum(faturamentoValido) / len(faturamentoValido)

diasAcima = len([dia for dia in faturamentoValido if dia > mediaMensal])

print(f"Menor valor de faturamento: {menorFaturamento}")
print(f"Maior valor de faturamento: {maiorFaturamento}")
print(f"Número de dias com faturamento acima da média: {diasAcima}")

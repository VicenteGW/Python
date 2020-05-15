print('=' * 46)
print('{:^46}'.format('ALUGUEL DO VICENTÃO'))
print('=' * 46)

d = float(input('Quantos dias você alugou o carro? '))
g = float(input('Quantos Km você rodou? '))

dd = d * 60
gg = g * 0.15
t = dd + gg

print('O valor total do serviço é R${:.2f}'.format(t))

# É importante modularizar o código para minimizar o número de erros!

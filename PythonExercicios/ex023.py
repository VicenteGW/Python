print('=' * 46)
print('{:^46}'.format('ANÁLISE STR 2 DO VICENTÃO'))
print('=' * 46)
n = int(input('Digite um N° de até 4 dig: '))
nq = f'{n:04}'
line = '\n'
print(
    f'{line}',
    f'unidade: {nq[3]}{line}',
    f'dezena: {nq[2]}{line}',
    f'centena: {nq[1]}{line}',
    f'milhar: {nq[0]}{line}'
)
# SÓ TA ACEITANDO N DE ATÉ 4 DIGITOS, VEJA ex023alt.py


print('=' * 46)
print('{:^46}'.format('NOMEZÃO DO VICENTÃO'))
print('=' * 46)
n = str(input('Digite seu nome: '))
l = n.lower()
print(
    'Este nome possui Santo?',
    'santo' in l
)

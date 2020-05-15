import random
print('=' * 46)
print('{:^46}'.format('ROLETÃO DO VICENTÃO'))
print('=' * 46)
a1 = str(input('Aluno 1 = '))
a2 = str(input('Aluno 2 = '))
a3 = str(input('Aluno 3 = '))
a4 = str(input('Aluno 4 = '))
lista = [a1, a2, a3, a4]
r = random.choice(lista)
print('O fudido sorteado é : {}'.format(r))
# Tentei importar math ao invés de random

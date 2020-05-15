from random import shuffle
print('=' * 46)
print('{:^46}'.format('FILÃO DO VICENTÃO'))
print('=' * 46)
a1 = str(input('Aluno: '))
a2 = str(input('Aluno: '))
a3 = str(input('Aluno: '))
a4 = str(input('Aluno: '))
lista = [a1, a2, a3, a4]
s = shuffle(lista)
print('A ordem será: ')
print(lista)


import math

print('=' * 46)
print('{:^46}'.format('INTEIRÃO DO VICENTÃO'))
print('=' * 46)

n = float(input('Nº float: '))

i = math.floor(n)

print('A parte inteira de {} é {}'.format(n, i))
# poderia ter sido math.trunc ou int(n)


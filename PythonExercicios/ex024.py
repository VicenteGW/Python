print('=' * 46)
print('{:^46}'.format('CITY DO VICENTÃO'))
print('=' * 46)
c = str(input('Digite sua cidade: '))
l = c.lower()
d = l.split()

print(
    'Sua cidade começa com Santo?',
    #d[0].find('santo')
    'santo' in d[0]
)

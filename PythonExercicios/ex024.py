print('=' * 46)
print('{:^46}'.format('CITY DO VICENTÃO'))
print('=' * 46)
c = str(input('Digite sua cidade: '))
l = c.lower(), c.split()

print(
    'Sua cidade começa com Santo?',
    #l[0].find('santo')
    'santo' in l[0]
)

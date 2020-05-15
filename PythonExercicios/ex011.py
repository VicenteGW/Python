print('=' * 46)
print('{:^46}'.format('PICASSO DO VICENTÃO'))
print('=' * 46)
# tinta pinta 2 metros quad
# l = xxxx ele considerou um argumento ambiguo, mudei para c

h = float(input('Altura da parede: '))
c = float(input('Largura da parede: '))
a = h * c
t = a / 2
print(' Serão {}m² para pintar. \n Será necessário {}L de tinta.'.format(a, t))

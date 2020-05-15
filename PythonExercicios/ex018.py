import math
print('=' * 46)
print('{:^46}'.format('ANGLÃO DO VICENTÃO'))
print('=' * 46)
a = float(input('Valor do angulo em questão = '))
r = math.radians(a)
s = (math.sin(r))
c = (math.cos(r))
t = (math.tan(r))
print(' O angulo {} possui: \n Seno = {:.2f} \n Cosseno = {:.2f} \n Tangente = {:.2f}'.format(a, s, c, t))
# ESQUECI DE CONVERTER PARA RADIANOS


print('=' * 46)
print('{:^46}'.format('HIPOTENUSÃO DO VICENTÃO'))
print('=' * 46)

import math
b = float(input('Valor em cm do lado (cateto) 1 = '))
c = float(input('Valor em cm do lado (cateto) 2 = '))
a = math.hypot(b, c)
# a = (math.pow(b, 2) + (math.pow(c, 2))) / 2 FIZ ERRADOOOO
print('O valor da hipotenusa em cm é = {:.2f}'.format(a))
# poderia ter sido math.hypot(b, c)

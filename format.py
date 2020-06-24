# position args
n = 'my name is {} e sou {}'.format('vicente', 'ateu')
print(n)

# F-strings
v = 'vicente'
a = 'ateu'

m = f'my name is {v.upper()} e sou {a}'
print(m)

#-------------------------------

mat = f'4 vezes 4 é {4 * 4}'
print(mat)

#-------------------------------

for n in range(1, 11): 
    sen = f'o valor é {n:03}'
    print(sen)
    #{n:.4f} = terá .4 floats

#-------------------------------

t = ['vic', 'laika', 'test']
o = ' ola '
tj = f'{o.join(t)}'
print(tj)
    # .join() coloca coisas da lista e repete o texto


#-------------------------------


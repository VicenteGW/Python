print('=' * 46)
print('{:^46}'.format('ANÁLISE STR DO VICENTÃO'))
print('=' * 46)

n = str(input('Digite seu Nome: '))
sp = n.replace(' ','')
div = n.split()
print(
    n.upper(),
    n.lower(),
    sp,
    len(sp),
    len(div[0])
)

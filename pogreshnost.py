import statistics as stat
from decimal import *
import math

def deltas_and_mean():
    n = int(input('Number of experements: '))
    l = [Decimal(input(f'Experement {i+1}: ')) for i in range(n)]
    sl = []
    print(l)
    mean = stat.mean(l)
    print(f'The mean is {mean}')
    for i,ti in enumerate(l, 1):
        dti = ti - mean
        sl.append(dti*dti)
        print(f'delta t for {i} is {dti}')
        print(f'delta t sqrd for {i} is {dti*dti}')
    print('the sum is', sum(sl))
def magnetic_induction():
#    n = int(input('Number of experements: '))
#    l = [Decimal(input(f'Experement {i+1}: ')) for i in range(n)]
    while True:
        i = float(input('Enter_current: '))
        print((1.25663706*(10**-6)*i*1450/math.sqrt(0.06**2+0.03**2)))
def deltas_ebanutie():
    l = []
    while True:
        inp = input()
        if inp == '':
            break
        else:
            l.append(float(inp))
    for i in range(len(l)-1):
        print(l[i], l[i]-l[i+1])

deltas_and_mean()
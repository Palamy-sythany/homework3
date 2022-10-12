from math import *
def equation(a,b,c):
    delta=pow(b,2)-4*a*c
    if delta > 0:
        print('x1=',(-b + sqrt(delta))/(2*a))
        print('x2=',(-b - sqrt(delta))/(2*a))
    elif delta==0:
        print('x1=x2=',(-b/(2*a)))
    else:
        print('no result')
a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
equation(a,b,c)
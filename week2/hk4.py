import math
x1 =1
x2 =3
x =(x1+x2)/2
while abs(x-math.sqrt(2))> math.exp(-10):
    x = (x1+x2)/2
    if x*x>2 :
        x2 = x
    elif x*x<2 :
        x1 = x
print(x)
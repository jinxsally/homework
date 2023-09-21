#牛顿法：f(x)=x^2 - c,f'(x)=2x
#取点（x0,y0),根据牛顿法，得到迭代方程式:x = -y0/2x0 +x0
import math
def sqrt(x,c) :

    y = math.pow(x,2) -x
    while abs(x*x-c)>math.exp(-20):
        x = -y/(2*x) + x
        y = x**2 -c
    return x
#c为2
c = 2#要求解的根的平方
x = c/2#g即x，初值c/2
print(sqrt(x,c))
print(math.sqrt(c))

#c更改为2000
c = 2000
x = c/2
print(sqrt(x,c))
print(math.sqrt(c))

#牛顿法：f(x)=x^2 - c,f'(x)=2x
#取点（x0,y0),根据牛顿法，得到迭代方程式:x = -y0/2x0 +x0
import math
x = 2
y = math.pow(x,2) -2#此时c为2
while abs(x-math.sqrt(2)>math.exp(-20)):
    x = -y/(2*x) + x
    y = x**2 -2
print(x)
print(math.sqrt(2))
x = 2000
y = math.pow(x,2) -2#此时c为2
while abs(x-math.sqrt(2)>math.exp(-20)):
    x = -y/(2*x) + x
    y = x**2 -2
print(x)
print(math.sqrt(2))
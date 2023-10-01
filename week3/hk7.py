a = eval(input())
b = eval(input())
#更相减损法
while a!= b :
    if a<b:
        a,b = b,a
    a = a-b
print('最大公约数为：',b)
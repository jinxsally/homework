import math

n = float(input())
a = []#存储得到的二进制编码
c = []#存储得到整数部位的二进制编码
b = math.floor(n)
d = round(n - b,5)
#print(b,d)#检验
while b>0:
    c.append(b%2)
    b = math.floor(b/2)

for i in range(8):
    a.append(math.floor(d*2))
    if d*2 >=1:
        d = d*2 -1
    else:
        d = d*2
list.reverse(c)
s1 = " ".join(map(str,c))
s2 = " ".join(map(str,a))
print(s1+'.'+s2)
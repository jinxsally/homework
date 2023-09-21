n =eval(input())
import math
#动态规划求解
a = []#设置列表存储每步最优解
for i in range(1,n+2):#初始化值
    a.append(1)
def count(n):
    if n==2 :
        return a[2]
    for i in range(3,n+1):
        for j in range(2,i+1):
            a[i] = max(max(a[i],j*(i-j)),j*a[i-j])#此步意为，在a[i]初始值，把j作为一个乘数进行求解最大值，且j把能取的都取了
    return a[n]

print(count(n))
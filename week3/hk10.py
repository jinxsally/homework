n = eval(input())
A = []
for i in range(0,n):
    A.append(eval(input()))
B = []
for i in range(0,n):
    B.append(1)
    for j in range(0,n):
        if j !=i:
           B[i] *= A[j]

print(B)
x = range(10,60,10)
import math
y = []
for i in x :
    y.append( math.pow(2,i))
print(y)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()



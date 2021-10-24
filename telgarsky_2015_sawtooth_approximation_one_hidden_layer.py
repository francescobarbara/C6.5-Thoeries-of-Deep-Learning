import matplotlib.pyplot as plt
import numpy as np

def relu(x):
    if x < 0:
        return 0
    
    return x
  
    
    
def val(x, m):
    out = relu(2**m * x)
    print(out)
    for i in range(1, 2**m+1):
        out += (-1)**(i) * 2 * relu(2**m * (x - i/(2**m)))
        print(out)
    return out

m = 3  #change this how you would like     
x = np.arange(0,1, 1/100)
y = [None]*len(x)
for i in range(len(x)):
    y[i] = val(x[i], m)
    
plt.figure()
plt.plot(x,y)



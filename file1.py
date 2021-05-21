111#import copy
222#import os.path
import numpy as np
#import random as rd
import math
import matplotlib.pyplot as plt
from scipy import *
from scipy.integrate import *

#%%
def wL(x,nu):
    return (x**(nu-1))*np.exp(-x)/math.gamma(nu)




#%%

print("Проверяем работу Гамма функции")
print (math.gamma(3+1))



#%%

print(wL(2,1))
x=np.linspace(0,5,100)
#print(x)
y1= wL(x,1)
y2= wL(x,2)
y3 = wL(x,3)
plt.plot(x,y1,x,y2,x,y3)



#%%
nu = 2
Нормировка = quad(wL,0,Inf,args=2)
print(Нормировка)


#%%


x = int(float("5.5"))
print(x)






#%%
 

#%%




import math 
import numpy as np
import matplotlib.pyplot as plt

## numpy para uso de vetores e math para escalar ##

# faça uma busca incremental para identificar os subintervalos nos quais ocorre mudança de sinal dentro do intervalo [3,6] para a função f(x) = sin(10x) + cos(3x)####

def f(x):
    return np.sin(10*x) + np.cos(3*x)

# def busca_incremental(a, b, passo):
#     x = a
#     while x < b:
#         if f(x) * f(x + passo) < 0:
#             print(f"Mudança de sinal entre {x} e {x + passo}")
#         x += passo

# busca_incremental(3, 6, 0.1)



### como o professor ###

#vetor 
# ## x= np.linspace (start, stop, n)
n = 100
x = np.linspace(3,6,n)
xb = []
nb = 0
## busca incremental irá buscar onde há mudança de sinal ou raiz ##

# print("y = ", y)

# print teste

for i in range(n-1):
    xl = x[i]
    xu = x[i+1]

    if (f(xl)*f(xu) < 0):
        nb += 1
        xb.append([xl, xu])
    else:    
        print("não há intervalo")
print("xb =", xb)
print("numero de subintervalos =", nb)

plt.figure()
plt.plot(x,f(x), '-b',label= "f(x) = sin(10x) + cos(3x)")
plt.plot(x,np.linspace(0,0,100), '-r')
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()


# A = np.array([[1, 2], [3,4]])
# print(A)





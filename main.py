#
# importe a biblioteca do arquivo ex01.py

from ex01 import *


# exercício 4 da lista 1
massa = 10 # kg
# F =?
u = 0.6
F = forca_atrito_estatica(u, massa * 9.8)
print(f"A força de atrito estática é {F} N")

# exercício 7 da lista 1
m = 40 # kg
F = 80 # N
a = 0 
# u = ?' # coeficiente de atrito cinético

# F - Fa = m * a
# Fa = m * a + F
# u = Fa / (m * 9.8) # sem função
# com função abaixo
u = coeficiente_atrito_cinetico(F, m, a)
print(f"O coeficiente de atrito cinético é {u}")
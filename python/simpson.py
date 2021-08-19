from ecuaciones import function
from numpy import linspace

def simpson(a, b, h, f = function):
    n = (b - a) / h
    points = list(linspace(a, b, n + 1))
    suma = 0
    for i, x in enumerate(points):
        if i == 0 or i == n:
            suma += f(x)
        elif i % 2 == 0:
            suma += 2 * f(x)
        else:
            suma += 4 * f(x)
    aprox = (h / 3) * suma
    return aprox

d = simpson(-1, 1, 2 / 400000000)
print(d)
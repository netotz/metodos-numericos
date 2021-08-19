from math import log, ceil
from ecuaciones import caso1

def countSteps(d, error):
    calc = (log(d) - log(error)) / log(2)
    return ceil(calc)

def bisection(x1, x2, count = 1, error = 0.01, f = caso1):
    delta = abs(x2 - x1)
    if count == 1:
        print("This process will take", countSteps(delta, error), "iterations.")
    print("\n----------", count, "----------")
    print("x1 =", x1, "      x2 =", x2)

    xm = (x1 + x2) / 2
    print("xm =", xm)
    print("|x2 - x1| =", delta)

    if delta <= error:
        print("alpha = xm =", xm)
        return xm

    product = f(x1) * f(xm)
    print("f(x1) = f(", x1, ") =", f(x1))
    print("f(xm) = f(", xm, ") =", f(xm))
    print("f(x1)f(xm) =", product)
    if product <= 0:
        print("alpha -> (", x1, ",", xm, ")")
        print("x2 = xm =", xm)
        return bisection(x1, xm, count + 1)
    else:
        print("alpha -> (", xm, ",", x2, ")")
        print("x1 = xm =", xm)
        return bisection(xm, x2, count + 1)
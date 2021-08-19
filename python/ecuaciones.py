from math import sqrt, cos, tan

def caso1(x):
    return x ** 4 - 9 * x ** 3 - 2 * x ** 2 + 120 * x - 130

def dif_caso1(x):
    return 4 * x ** 3 - 27 * x ** 2 - 4 * x + 120

def sec(theta):
    return 1 / cos(theta)

def caso2(P, A = 1, c = 1, r = 1, sigma = 40000, E = 30 * 10**6, L = 6, e = 0.35):
    return P/A - sigma**2/((c*e*sec((L*sqrt(P/(A*E)))/(2*r)))/r**2+1)

def dif_caso2(P, A = 1, c = 1, r = 1, sigma = 40000, E = 30 * 10**6, L = 6, e = 0.35):
    return (c*L*sigma**2*e*sec((L*sqrt(P/(A*E)))/(2*r))*tan((L*sqrt(P/(A*E)))/(2*r)))/(4*A*r**3*E*sqrt(P/(A*E))*((c*e*sec((L*sqrt(P/(A*E)))/(2*r)))/r**2+1)**2) + 1/A

def function(x):
    return ((x ** 7) * sqrt(1 - x ** 2)) / (sqrt(2 - x) ** 13)
from ecuaciones import caso1

def interpolation(x1, x2, i = 2, error = 0.01, f = caso1):
    if i == 2:
        print(">> f = inline('x.^4-9*x.^3-2*x.^2+120*x-130')")
        print("\nf =\n\n\tInline function:\n\tf(x) = x.^4-9*x.^3-2*x.^2+120*x-130\n")

        print('>> x1 = %g; x2 = %g;' % (x1, x2))
        print('>> y1 = f(x1);')
    
    print('>> y{0} = f(x{0});'.format(i))

    xi = ((x1 * f(x2)) - (x2 * f(x1))) / (f(x2) - f(x1))
    print('>> x{1} = ((x1 * y{0}) - (x{0} * y1)) / (y{0} - y1)'.format(i, i + 1))
    print('\nx%d =\n\n\t%g\n' % (i + 1, xi))

    delta = abs((xi - x2) / x2)
    print('>> abs((x{1} - x{0}) / x{0})'.format(i, i + 1))
    print('\nans =\n\n\t%g\n' % delta)
    print('>> %% %g <= %g ? ' % (delta, error), end = '')

    if delta <= error:
        print('T')
        print('>> %% alfa = x%d = %g' % (i + 1, xi))
        print('>> %% comprobacion')
        print('>> f(x%d)' % (i + 1))
        print('\nans =\n\n\t%g\n' % f(xi))
        return xi
    else:
        print('F')
        print('>> %% siguiente iteracion')
        return interpolation(x1, xi, i + 1)

print('\n>> %% PROBLEMA 3')
y = interpolation(-4, -3)
print('\n>> %% PROBLEMA 4')
y = interpolation(1, 2)
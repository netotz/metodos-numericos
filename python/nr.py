from ecuaciones import caso2, dif_caso2

def NewtonRaphson(xi, i = 0, error = 0.01, f = caso2, df = dif_caso2):
    print('\n>> %% i = %d' % i)
    if i == 0:
        print(">> f = inline('x.^4-9*x.^3-2*x.^2+120*x-130')")
        print("\nf =\n\n\tInline function:\n\tf(x) = x.^4-9*x.^3-2*x.^2+120*x-130\n")
        print(">> df = inline('4x.^3-27*x.^2-4*x.^+120')")
        print("\ndf =\n\n\tInline function:\n\tdf(x) = 4x.^3-27*x.^2-4*x.^+120\n")
        print('>> x%d = %g;' % (i, xi))

    print('f(x%d) = %g' % (i, f(xi)))
    print('df(x%d) = %g' % (i, df(xi)))
    
    x_next = xi - (f(xi) / df(xi))
    print('>> x{1} = x{0} - (f(x{0}) / df(x{0}))'.format(i, i + 1))
    print('\nx%d =\n\n\t%g\n' % (i + 1, x_next))

    delta = abs(x_next - xi)
    print('>> abs(x%d - x%d)' % (i + 1, i))
    print('\nans =\n\n\t%g\n' % delta)

    print('>> %% %g <= %g ? ' % (delta, error), end = '')
    if delta <= error:
        print('T')
        print('>> %% alfa = x%d = %g' % (i + 1, x_next))
        print('>> %% comprobacion')
        print('>> f(x%d)' % (i + 1))
        print('\nans =\n\n\t%g\n' % f(xi))
        return x_next
    else:
        print('F')
        return NewtonRaphson(x_next, i + 1)

print('>> %% Caso 2')
y = NewtonRaphson(4112335.167120566)
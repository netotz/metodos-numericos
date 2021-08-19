from ecuaciones import caso1

def repeatStr(string, times):
    output = ''
    while times > 0:
        output += string
        times -= 1
    return output

def BirgeVieta(coeffs, x_i = None, count = 0, error = 0.001):
    print('\n---------i = %d---------' % count)
    if x_i is None:
        x_i = - (coeffs[-1] / coeffs[-2])

    n = len(coeffs)

    p = [1]
    ps = [1, 1]
    for i in range(1, n):
        _p = coeffs[i] + p[i - 1] * x_i
        p.append(_p)

        if i >= 2:
            _ps = p[i - 1] + ps[i - 1] * x_i
            ps.append(_ps)

        print('p%d = %3.4f\tps%d = %3.4f' % (i, p[i], i, ps[i]))

    placers = repeatStr('  %7.4f', n - 1)
    string = '\n%2.4f|  1' + placers
    params = [x_i]
    params.extend([c for c in coeffs[1:]])
    print(string % tuple(params))

    string = '        +  ' + placers
    params = tuple(x_i * _p for _p in p[:-1])
    print(string % params)

    unders = ['_' for i in range(60)]
    print(''.join(unders))

    string = '          1' + placers + ' = f(x%d)'
    params = [_p for _p in p[1:]]
    params.append(count)
    print(string % tuple(params))

    placers2 = repeatStr('  %7.4f', n - 2)
    string = '        +  ' + placers2
    params = tuple(x_i * _ps for _ps in ps[1:-1])
    print(string % params)

    print(''.join(unders))

    string = '          1' + placers2 + " = f'(x%d)"
    params = [_ps for _ps in ps[2:]]
    params.append(count)
    print(string % tuple(params))

    x_next = x_i - (p[-1] / ps[-1])
    print('\nx%d = %g' % (count + 1, x_next))

    delta = abs(x_next - x_i)
    print('delta = %g <= 0.001 ? ' % delta)
    return x_next if delta <= error else BirgeVieta(coeffs, x_next, count + 1)

f = [1, -9, -2, 120, -130]
BirgeVieta(f, 7)
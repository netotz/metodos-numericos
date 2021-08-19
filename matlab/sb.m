fprintf("\n%%%%%% problema 1\n");
a = bisection(-4, -3, 0.01, 1);
fprintf("\n%%%%%% problema 2\n");
b = bisection(1, 2, 0.01, 1);

function output = caso1(x)
    output = x .^ 4 - 9 * x .^ 3 - 2 * x .^ 2 + 120 * x - 130;
end

function root = bisection(x1, x2, err, count)
    if count == 1
        fprintf(">> f = inline('x.^4-9*x.^3-2*x.^2+120*x-130')\n");
        fprintf("\nf =\n\n\tInline function:\n\tf(x) = x.^4-9*x.^3-2*x.^2+120*x-130\n\n")
    end

    fprintf("%%%% iteracion %d\n", count);
    fprintf(">> x1 = %g, x2 = %g;\n", x1, x2);

    xm = (x1 + x2) / 2;
    fprintf(">> xm = (x1 + x2) / 2\n");
    fprintf("\nxm =\n\n\t%g\n\n", xm);

    delta = abs(x2 - x1);
    fprintf(">> abs(x2 - x1)\n");
    fprintf("\nans =\n\n\t%g\n\n", delta);
    if delta <= err
        fprintf("%% %g <= %g, alfa = %g\n", delta, err, xm);
        fprintf("%% comprobacion\n");
        fprintf(">> f(xm)\n")
        fprintf("\nans =\n\n\t%g\n\n", caso1(xm));
        root = xm;
        return
    end

    f_x1 = caso1(x1);
    fprintf(">> f(x1)\n");
    fprintf("\nans =\n\n\t%g\n\n", f_x1);
    f_xm = caso1(xm);
    fprintf(">> f(xm)\n");
    fprintf("\nans =\n\n\t%g\n\n", f_xm);

    product = f_x1 * f_xm;
    fprintf(">> %g * %g\n", f_x1, f_xm);
    fprintf("\nans =\n\n\t%g\n\n", product);
    fprintf("%% %g <= 0 ? ", product);
    if product <= 0
        fprintf("T\n");
        fprintf("%% alfa esta en el intervalo (%g, %g)\n", x1, xm);
        root = bisection(x1, xm, err, count + 1);
    else
        fprintf("F\n");
        fprintf("%% alfa esta en el intervalo (%g, %g)\n", xm, x2);
        root = bisection(xm, x2, err, count + 1);
    end
end
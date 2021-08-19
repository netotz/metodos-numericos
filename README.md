# Métodos numéricos

Ejercicios y tareas de la clase de Métodos numéricos en FIME, UANL, realizados en el 2019.

Las tareas debían ser realizadas en el REPL de MATLAB, iteración por iteración sin usar loops, así que preferí usar Python, formateando los outputs de consola para simular que los cálculos fueron hechos en el REPL de MATLAB y paso por paso lol

Ahora que lo pienso hubiera sido mejor imprimir directamente a un archivo... se aceptan pull requests :p

Ejemplo:
```
$ py ili.py

>> %% PROBLEMA 3
>> f = inline('x.^4-9*x.^3-2*x.^2+120*x-130')

f =

        Inline function:
        f(x) = x.^4-9*x.^3-2*x.^2+120*x-130  

>> x1 = -4; x2 = -3;
>> y1 = f(x1);
>> y2 = f(x2);
>> x3 = ((x1 * y2) - (x2 * y1)) / (y2 - y1)

x3 =

        -3.49198

>> abs((x3 - x2) / x2)

ans =

        0.163993

>> % 0.163993 <= 0.01 ? F
>> %% siguiente iteracion
>> y3 = f(x3);
>> x4 = ((x1 * y3) - (x3 * y1)) / (y3 - y1)

x4 =

        -3.58306

>> abs((x4 - x3) / x3)

ans =

        0.0260829

>> % 0.0260829 <= 0.01 ? F
>> %% siguiente iteracion
>> y4 = f(x4);
>> x5 = ((x1 * y4) - (x4 * y1)) / (y4 - y1)

x5 =

        -3.5975

>> abs((x5 - x4) / x4)

ans =

        0.00403061

>> % 0.00403061 <= 0.01 ? T
>> % alfa = x5 = -3.5975
>> %% comprobacion
>> f(x5)

ans =

        -1.05804


>> %% PROBLEMA 4
>> f = inline('x.^4-9*x.^3-2*x.^2+120*x-130')

f =

        Inline function:
        f(x) = x.^4-9*x.^3-2*x.^2+120*x-130

>> x1 = 1; x2 = 2;
>> y1 = f(x1);
>> y2 = f(x2);
>> x3 = ((x1 * y2) - (x2 * y1)) / (y2 - y1)

x3 =

        1.30303

>> abs((x3 - x2) / x2)

ans =

        0.348485

>> % 0.348485 <= 0.01 ? F
>> %% siguiente iteracion
>> y3 = f(x3);
>> x4 = ((x1 * y3) - (x3 * y1)) / (y3 - y1)

x4 =

        1.23365

>> abs((x4 - x3) / x3)

ans =

        0.00383039

>> % 0.00383039 <= 0.01 ? T
>> % alfa = x5 = 1.22892
>> %% comprobacion
>> f(x5)

ans =

        0.0272083



```
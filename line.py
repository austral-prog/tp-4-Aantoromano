def line():
    A= float (input("Ingrese el coeficiente A: "))
    B= float (input("Ingrese el coeficiente B: "))
    X1= float (input('Ingrese el coeficiente X1: '))
    X2= float(input('Ingrese el coeficiente X2: '))

    print (f'El coeficiente A de su ecuación de la recta es: {A}')
    print (f'El coeficiente B de su ecuación de la recta es: {B}')
    print (f'El coeficiente X1 de su ecuación de la recta es: {X1}')
    print (f'El coeficiente X2 de su ecuación de la recta es: {X2}')

    print()
    print('Para la sigueinte ecuación:')
    print(f"\t Y= {A}X + {B}")

    print()
    print (f'\tDados los sigueinte puntos:')

    Y1= (A * X1) + B #110.99999
    Y2= (A * X2) + B #-79.6699999
    print(f'P1 ({X1}, {Y1})')
    print (f'P2 ({X2}, {Y2})')

    print()

    distancia= (X1-X2)**2 + (Y1-Y2)**2
    distancia= distancia **(1/2) 

    print(f'La distancia entre ellos es: {distancia}')

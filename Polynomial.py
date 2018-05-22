
X = []
Y = []
M = []
B = []

def set_x_at(xi):
    """ Esta funcion recibe como parametro un lista de numeros en x.
        Solo se ejecuta una vez.
    """
    if not len(X):
        X.append([1]*len(xi))
        X.append(xi)
        t = [0] * len(xi)
        for i in range(0, len(xi)):
            t[i] = xi[i]**2
        X.append(t)
    else:
        raise Exception('Ya existen coordenadas en X')

def set_y(y):
    global Y
    """ Esta funcion recibe como parametro un lista de numeros en y """
    if not len(Y):
        Y = y
    else:
        raise Exception('Ya existen coordenadas en y')

def get_model():
    """ Nos regresa el modelo de la regresion lineal """
    if not len(X) and not len(Y):
        raise Exception('Las coordenadas en X y/o Y no han sido asigandas')           
    else:
        __generate_m()
        __generate_b()
        # Falta usar Gauss
    global X
    global Y
    global M
    global B
    X = []
    Y = []
    M = []
    B = []


def __generate_m():
    """ Esta funcion genera el vector M = Xt * X. Esta funcion es privada.
        Y solo se ejecuta en la funcion get_model().
    """
    for i in range(0, len(X)):
        t = [0] * len(X)
        for j in range(0, len(X)):
            for k in range(0, len(Y)):
                t[j] += X[i][k] * X[j][k]
        M.append(t)

def __generate_b():
    global B
    B = [0] * len(X)
    for i in range(0, len(X)):
        for j in range(0, len(Y)):
            B[i] += X[i][j] * Y[j]
        
def main():
    x = [0,1,2,3,4,5]
    y = [2.1,7.7,13.6,27.2,40.9,61.1]

    set_x_at(x)

    print 'X =',X

    set_y(y)

    print 'Y =',Y

    get_model()

    print 'M =',M
    print 'B =',B
    print 'Falta usar gaus-jorgan'

if __name__ == '__main__':
    main()
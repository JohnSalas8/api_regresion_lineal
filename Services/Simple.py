import json
from copy import deepcopy

class Simple:
    def __init__(self):
        self.X = []
        self.Y = []
        self.M = []
        self.B = []

    def set_x_at(self, xi):
        """ Esta funcion recibe como parametro un lista de numeros en x """
        if not len(self.X):
            self.X.append([1]*len(xi))
        self.X.append(xi)

    def set_y(self, y):
        """ Esta funcion recibe como parametro un lista de numeros en y """
        if not len(self.Y):
            self.Y = y
        else:
            raise Exception('Ya existen coordenadas en y')

    def gen_lineal_sys(self):
        """ Nos regresa el modelo de la regresion lineal """
        if not len(self.X) and not len(self.Y):
            raise Exception('Las coordenadas en X y/o Y no han sido asigandas')           
        else:
            self.__generate_m()
            self.__generate_b()
            # Falta usar Gauss
    
    def clear(self):
        self.X = []
        self.Y = []
        self.M = []
        self.B = []

    # M = X^t * X
    def __generate_m(self):
        """ Esta funcion genera el vector M = X^t * X. Esta funcion es privada.
            Y solo se ejecuta en la funcion gen_lineal_sys().
        """
        for i in range(0, len(self.X)):
            t = [0] * len(self.X)
            for j in range(0, len(self.X)):
                for k in range(0, len(self.Y)):
                    t[j] += self.X[i][k] * self.X[j][k]
            self.M.append(t)

    # B = X^t * Y
    def __generate_b(self):
        """ Genera el vector B para armar el sistema lineal"""
        self.B = [0] * len(self.X)
        for i in range(0, len(self.X)):
            for j in range(0, len(self.Y)):
                self.B[i] += self.X[i][j] * self.Y[j]
    
    # Genera la diagonal de unos con los ceros debajo
    def __gen_zero_down(self):
        """ Genera la diagonal de unos con ceros debajo """
        t = len(self.M)
        for i in range(0, t-1):
            p = self.M[i][i]
            for j in range(i, len(self.M)):
                self.M[i][j] = self.M[i][j] / p
            self.B[i] /= p
            for j in range(i+1, len(self.M)):
                p2 = -self.M[j][i]
                for k in range(0, len(self.M)):
                    self.M[j][k] = self.M[j][k] + p2 * self.M[i][k]
                self.B[j] = self.B[j] + p2 * self.B[i]
    
    # La diagonal de unos ya esta hecha ahora hay que hacer ceros hacia arriba
    def __gen_zero_up(self):
        """ Hace ceros los numeros arriba de la diagonal de unos; por eso
            se ejecuta primero __gen_zero_down """
        i = len(self.M) -1
        while i!=-1:
            if self.M[i][i]!=1:
                self.B[i] = self.B[i] / self.M[i][i]
                self.M[i][i] = 1
            j = i
            while j!=0:
                p = -self.M[j-1][i]
                self.M[j-1][i] = self.M[j-1][i] + p * self.M[i][i]
                self.B[j-1] = self.B[j-1] + p * self.B[i]
                j -= 1
            i -= 1
    
    # Concatena los datos para generar el modelo
    def __get_model(self):
        """ Devuelve en String la cadena que hace referencia al modelo de regresion lineal """
        model = 'y ='
        for i in range(0, len(self.B)):
            if self.B[i]>0:
                model += ' + '
            else:
                model += ' '
            model += str(self.B[i])
            if i!=0:
                model += 'x'
        return model

    def get_result(self, x, y):
        self.set_x_at(x)

        vjson = {}

        vjson['X'] = self.X

        self.set_y(y)

        vjson['Y'] = self.Y

        self.gen_lineal_sys()   # Genera los vectores M y B

        vjson['M'] = deepcopy(self.M)
        vjson['B'] = deepcopy(self.B)

        self.__gen_zero_down()  # Genera la diagonal de unos y ceros abajo
        
        vjson['ME'] = deepcopy(self.M)
        vjson['AE'] = deepcopy(self.B)  # B se convierte en A

        self.__gen_zero_up()    # Genera los ceros arriba de la diagonal de unos

        vjson['AF'] = self.B
        vjson['MF'] = self.M

        vjson['model'] = self.__get_model() # Genera el formato del modelo

        return vjson

if __name__ == '__main__':
    X = []
    Y = []

    for x in [12, 10, 40, 50, 30]:
        X.append(float(x))
    
    for y in [400, 390, 1200, 1900, 950]:
        Y.append(float(y))

    print json.dumps(
        Simple().get_result(
            X,
            Y
        ),
        indent=4
    )
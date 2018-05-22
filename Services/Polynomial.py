import json

class Polynomial:
    def __init__(self):
        self.X = []
        self.Y = []
        self.M = []
        self.B = []

    def set_x_at(self, xi):
        """ Esta funcion recibe como parametro un lista de numeros en x.
            Solo se ejecuta una vez.
        """
        if not len(self.X):
            self.X.append([1]*len(xi))
            self.X.append(xi)
            t = [0] * len(xi)
            for i in range(0, len(xi)):
                t[i] = xi[i]**2
            self.X.append(t)
        else:
            raise Exception('Ya existen coordenadas en self.X')

    def set_y(self, y):
        """ Esta funcion recibe como parametro un lista de numeros en y """
        if not len(self.Y):
            self.Y = y
        else:
            raise Exception('Ya existen coordenadas en y')

    def get_model(self):
        """ Nos regresa el modelo de la regresion lineal """
        if not len(self.X) and not len(self.Y):
            raise Exception('Las coordenadas en self.X y/o self.Y no han sido asigandas')           
        else:
            self.__generate_m()
            self.__generate_b()
            # Falta usar Gauss

    def clear(self):
        self.X = []
        self.Y = []
        self.M = []
        self.B = []


    def __generate_m(self):
        """ Esta funcion genera el vector self.M = Xt * self.X. Esta funcion es privada.
            self.Y solo se ejecuta en la funcion get_model().
        """
        for i in range(0, len(self.X)):
            t = [0] * len(self.X)
            for j in range(0, len(self.X)):
                for k in range(0, len(self.Y)):
                    t[j] += self.X[i][k] * self.X[j][k]
            self.M.append(t)

    def __generate_b(self):
        self.B = [0] * len(self.X)
        for i in range(0, len(self.X)):
            for j in range(0, len(self.Y)):
                self.B[i] += self.X[i][j] * self.Y[j]
            
    def get_result(self, x, y):
        vjson = {}
        self.set_x_at(x)

        vjson['X'] = self.X

        self.set_y(y)

        vjson['Y'] = self.Y

        self.get_model()

        vjson['M'] = self.M
        vjson['B'] = self.B

        self.clear()

        return json.dumps(vjson, indent=4)

if __name__ == '__main__':
    print Polynomial().get_result(
        [0,1,2,3,4,5],
        [2.1,7.7,13.6,27.2,40.9,61.1]
    )
import json
from copy import deepcopy

class Multiple:
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

    def get_model(self):
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

    def __generate_m(self):
        """ Esta funcion genera el vector M = Xt * X. Esta funcion es privada.
            Y solo se ejecuta en la funcion get_model().
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
            

    def get_result(self, x1, x2, y):
        self.set_x_at(x1)
        self.set_x_at(x2)

        vjson = {}

        vjson['X'] = self.X

        self.set_y(y)

        vjson['Y'] = self.Y

        self.get_model()

        vjson['M'] = deepcopy(self.M)
        vjson['B'] = deepcopy(self.B)

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
        
        vjson['ME'] = deepcopy(self.M)
        vjson['AE'] = deepcopy(self.B)

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
                print self.M[j][i], p
                j -= 1
            print ''
            i -= 1

        vjson['AF'] = self.B
        vjson['MF'] = self.M
        
        return vjson

if __name__ == '__main__':
    print Multiple().get_result(
        [0,2,2.5,1,4,7],
        [0,1,2,3,6,2],
        [5,10,9,0,3,27]
    )
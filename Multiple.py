
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
            

    def main(self, x1, x2, y):
        self.set_x_at(x1)
        self.set_x_at(x2)

        print 'X =',self.X

        self.set_y(y)

        print 'Y =',self.Y

        self.get_model()

        print 'M =',self.M
        print 'B =',self.B
        print 'Falta usar gaus-jorgan'

        self.clear()


if __name__ == '__main__':
    Multiple().main(
        [0,2,2.5,1,4,7],
        [0,1,2,3,6,2],
        [5,10,9,0,3,27]
    )
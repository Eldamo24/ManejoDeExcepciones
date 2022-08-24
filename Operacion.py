class Operacion:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1

    @num1.setter
    def num1(self, num1):
        self._num1 = num1

    @property
    def num2(self):
        return self._num2

    @num2.setter
    def num2(self, num2):
        self._num2 = num2

    def suma(self):
        return self._num1 + self._num2

    def resta(self):
        return self._num1 - self._num2

    def multiplicacion(self):
        return self._num1 * self._num2

    def division(self):  #Comprobamos que no ocurra una division por cero
        try:            #Si ocurre, mostramos mensaje por pantalla y retornamos 0 como resultado
            return self._num1 / self._num2
        except ZeroDivisionError:
            print("Intentas dividir por cero pero no es posible...")
        finally:
            return 0

    def __str__(self):
        return f"Numero 1: {self._num1}, Numero 2: {self._num2}"
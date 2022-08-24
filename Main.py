from Operacion import Operacion

def crearOperacion(): #Controlamos la excepcion ValueError al ingresar un dato
    try:                 #que sea de un tipo distinto al esperado
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        return Operacion(num1, num2)
    except ValueError:
        print("Uno de los datos no es de el tipo que deberia ser")
        return Operacion(0,0)

op = crearOperacion()
print(op)
print(f"Suma: {op.suma()}")
print(f"Resta: {op.resta()}")
print(f"Multiplicacion: {op.multiplicacion()}")
print(f"Division: {op.division()}")

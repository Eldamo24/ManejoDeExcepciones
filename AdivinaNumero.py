from random import randint

num = 0
numAleatorio = randint(1, 100)
intentos = 0

while num != numAleatorio:
    try:
        print(f"Intento numero: {intentos + 1}")
        num = int(input("Adivine el numero... Ingrese numero entre 1 y 100: "))
        if num < numAleatorio:
            print(f"El numero que buscas es mayor a {num}")
        elif num > numAleatorio:
            print(f"El numero que buscas es menor a {num}")
        else:
            print(f"Lo lograste, {num} es igual a {numAleatorio}")
    except ValueError:
        print("El dato ingresado no es valido")
    finally:
        intentos += 1

print(f"Gano en {intentos} intentos")
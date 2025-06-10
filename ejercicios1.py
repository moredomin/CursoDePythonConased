# ========================
# Variables y operadores
# ========================
# Ejercicio 1:
# Crea un programa que declare dos variables, una con tu nombre y otra con tu edad.
# Muestrelos por pantalla de la siguiente forma:
# "Hola, me llamo Juan y tengo 20 años."

nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
print("Hola, me llamo", nombre, "y tengo", edad, "años.")

# Ejercicio 2:
# Ingrese dos números por teclado y muestre por pantalla cual es el mayor de los dos.

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if (numero1 > numero2):
    print(numero1)
else:
    print(numero2)

# Ejercicio 3:
# Ingrese 3 números por teclado y muestre por pantalla el mayor de los tres.

primernumero = float(input("Ingrese el primer número: "))
segundonumero = float(input("Ingrese el segundo número: "))
tercernumero = float(input("Ingrese el tercer número: "))

if (primernumero > segundonumero):
    if (primernumero > tercernumero):
        print(numero1)
    else:
        print(tercernumero)
elif (segundonumero > primernumero):
    if(segundonumero > tercernumero):
        print(segundonumero)
    else:
        print(tercernumero)

# Ejercicio 4:
# Ingrese 3 números por teclado y muestrelos ordenados de menor a mayor.

primero = float(input("Ingrese el primer número: "))
segundo = float(input("Ingrese el segundo número: "))
tercero = float(input("Ingrese el tercer número: "))

if (primero > segundo and primero > tercero):
    if (segundo > tercero): 
        print(tercero, segundo, primero)
    else:
        print(segundo, tercero, primero)
elif (segundo > primero and segundo > tercero):
    if (primero > tercero):
        print(tercero, primero, segundo)
    else:
        print(primero, tercero, segundo)
elif (tercero > primero and tercero > segundo):
    if(primero > segundo):
        print(segundo, primero, tercero)
    else:
        print(primero, segundo, tercero)



# Ejercicio 5:
# Ingrese un número por teclado y muestre por pantalla si es par o impar.

numeroaevaluar = int(input("Ingrese un numero: "))

if (numeroaevaluar % 2 == 0):
    print("Su número es par")
else:
    print("Su número es impar")



# Ejercicio 6:
# Ingrese el precio de un producto y el porcentaje de descuento. Al final, muestre por pantalla 
# el precio final del producto con el descuento aplicado, el descuento que se hizo, y el precio original.
# Ej: Precio final: 80.0, Descuento: 20.0%, Precio original: 100.0

precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

preciofinal = precio * descuento / 100 
print("Su precio final total correspondiente es de", preciofinal)


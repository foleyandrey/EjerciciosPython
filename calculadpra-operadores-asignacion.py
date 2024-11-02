print("Calculadora con operador de asignación")
print("Menu de opciones: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division exacta")
print("6. Exponente")
print("7. Modulo o resto\n")

opcion = int(input("Introduce la opcion a desarrollar: "))

if opcion ==1:
    print("Elegiste la operación de la Suma")
    numero = int(input("Ingresa el primer número: "))
    numero += int(input("Ingresa el segundo número: "))
    print(f"El resultado de la suma es: {numero}")

elif opcion ==2:
    print("Elegiste la operación de la Resta")
    numero = int(input("Ingresa el primer número: "))
    numero -= int(input("Ingresa el segundo número: "))
    print(f"El resultado de la resta es: {numero}")

elif opcion == 3:
    print("Elegiste la operación de la Multiplicación")
    numero = int(input("Ingresa el primer número: "))
    numero *= int(input("Ingresa el segundo número: "))
    print(f"El resultado de la multiplicacion es: {numero}")

elif opcion == 4:
    print("Elegiste la operación de la Division")
    numero = int(input("Ingresa el primer número: "))
    numero /= int(input("Ingresa el segundo número: "))
    print(f"El resultado de la division es: {numero}")

elif opcion == 5:
    print("Elegiste la operación de la Division Exacta")
    numero = int(input("Ingresa el primer número: "))
    numero //= int(input("Ingresa el segundo número: "))
    print(f"El resultado de la division exacta es: {numero}")

elif opcion == 6:
    print("Elegiste la operación de la Potenciación")
    numero = int(input("Ingresa el primer número: "))
    numero **= int(input("Ingresa el exponente que desee elevar: "))
    print(f"El resultado de la pontencia es: {numero}")

elif opcion == 7:
    print("Elegiste la operación de la Modulo")
    numero = int(input("Ingresa el primer número: "))
    numero %= int(input("Ingresa el segundo número: "))
    print(f"El resultado del Módulo es: {numero}")

else:
    print("Nos vemos.")

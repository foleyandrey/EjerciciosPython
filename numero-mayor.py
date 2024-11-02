#Nombre del sistema
print("Sistema para determinar el numero mayor")

#Ingreso de numeros por teclado
numero_uno = int(input("Ingresa el primer número: "))
numero_dos = int(input("Ingresa el segundo número: "))
numero_tres = int(input("Ingresa el tercer número: "))
print(f"Lo números ingresados son: {numero_uno}, {numero_dos}, {numero_tres}\n")

#Proceso del sistema
if numero_uno > numero_dos and numero_uno > numero_tres:
    print(f"El {numero_uno}, es el mas grande de los tres")
elif numero_dos > numero_tres and numero_dos > numero_uno:
    print(f"El {numero_dos}, es el mas grande de los 3")
elif numero_tres>numero_dos and numero_tres > numero_uno:
    print(f"El {numero_tres}, es el mayor de los entres.")
else:
    print("Nos vemos")

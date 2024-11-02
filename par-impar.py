#Vista de usuario
print("Determinar si el numero es par o impar\n")

#Ingreso por teclado
numero = int(input("Ingresa el numero: "))

#Proceso de comparacion
if numero%2 ==0:
    print(f"El {numero} es par.")
elif numero % 2 ==1:
    print(f"El {numero}, es impar.")    
else:
    print("Nos vemos.")

print("Sistema vacional\n")#Salto de linea para que no se vea muy pegado el código

#Ingreso de datos por teclado
nombre = input("Cual es su nombre: ")#Para saber con formalidad el nombre de la persona
clave = int(input("Ingrese la clave del departamento que pertenece: ")) #Segun el requerimiento de la empresa
tiempo = float(input("Tiempo de servicio: ")) #Si lo pongo float es por el hecho que un trabajador puede estar 1 año y 2 meses, y se lo representa en float 1.2

#Proceso de desarrollo
if clave ==1:
    print(f"Hola {nombre}, Bienvenido perteneces a Informatica")
    if tiempo >=1:
        print("Te corresponde 6 días de vacaciones")
    elif tiempo >= 2 and tiempo <= 6:
        print("Te corresponde 14 dias de vacaciones")
    elif tiempo >=7:
        print("Te corresponde 20 días de vaciones")
    else:
        print("Tu tiempo de servicio, aún no cumple los requisitos")

elif clave ==2:
    print(f"Hola {nombre}, Bienvenido perteneces a Recursos Humanos")
    if tiempo >=1:
        print("Te corresponde 7 días de vacaciones")
    elif tiempo >= 2 and tiempo <= 6:
        print("Te corresponde 15 dias de vacaciones")
    elif tiempo >=7:
        print("Te corresponde 22 días de vaciones")
    else:
        print("Tu tiempo de servicio, aún no cumple los requisitos")

elif clave ==3:
    print(f"Hola {nombre}, Bienvenido perteneces a Logistica")
    if tiempo >=1:
        print("Te corresponde 10 días de vacaciones")
    elif tiempo >= 2 and tiempo <= 6:
        print("Te corresponde 20 dias de vacaciones")
    elif tiempo >=7:
        print("Te corresponde 30 días de vaciones")
    else:
        print("Tu tiempo de servicio, aún no cumple los requisitos")
else:
    print("Hasta luego, nos vemos.")

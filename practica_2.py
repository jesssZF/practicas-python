#cadenas / strings
nombre = input ("Introduce tu nombre: ")
print(f"Hola {nombre}")

#entero
edad = 19
#flotante
altura = 1.69


#convertir flotante
edadString = str(edad)

print(edad+edad)
print(edadString+edadString)

print(type(edad))

booleanos= False

edad2=input("introduce tu edad: ")
#castear edad
edad2 = int(edad2)
if edad2 >= 18 and edad2 < 100:
    print("Eres mayor de edad")
elif edad2 >= 200:
    print("Eres inmortal")
elif edad2 <= 0:
        print("no existes")
else:
        print("Eres menor de edad")

#for
for i in range(0,10):
    print(i)

#estructuras de control switch no hayyy
dia = input("introduce un dia: ")
dia = int(dia)
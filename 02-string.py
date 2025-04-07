texto =("Hola mundo")
print (texto.upper())
print (texto.lower())
print (texto.find("m"))

texto = ("Hola mundo")
print (texto)
print (texto.replace("mundo", "pequeño saltamontes"))
print (texto)   

texto =("Hola mundo")
print ("mundo" in texto)
print ("hola" in texto)

print(4+6)
suma=(4+6)
print(suma)
resta=print (45-32)
multi=(3*5)
print(multi)
divi=print (54/12)
print(54%12)
print(2 ** 4)

n1 = 10
n2 = 13
print(n1<n2)
print(n1>n2)
print(n1>=n2)
print(n1<=n2)
print(n1==n2)

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

print(nombre)
print(edad)
print(type(nombre))
print(type(edad))


notas = float(input("Digite su nota: "))

if notas >= 4.5:
    print("Alumno aprobó con Honores")
if notas >= 3:
    print("Alumno aprobo")
if notas <= 3:
    print("Alumno reprobo")
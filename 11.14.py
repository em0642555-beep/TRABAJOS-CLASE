nombres = ["Angel", "Karla", "Luis","Mateo", "Maria", "Luis", "Karla"]
print(f"Los nombres que se tienen son: {nombres}")
nombreBuscar=input("¿Que nombre deseas buscar?: ")
encontrado = False
contador = 0
i = 0
while i <len(nombres):
    if nombres[i] ==nombreBuscar:
        encontrado = True
        contador = contador+1
        print("Encontrado en la posicion:",i)
        i=i+1
if encontrado==True:
    print("Nombre encontrado")
    print("Aparece",contador, "veces")
    if contador>1:
        nombres.remove(nombreBuscar)
    else:
        print("El nombre no se repite")
else:
    print("Nombre no encontrado")
print(nombres)
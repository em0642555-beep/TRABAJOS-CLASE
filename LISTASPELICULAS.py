#Programa que agrega peliculas a una lista
#Ponerle nombre a una lista
peliculas=[ ]
#Preguntar cuantas peliculas
cantPeliculas=int(input("Ingresa la cantidad de peliculas que vas a agregar: "))
#Valor inicial para el while
i=0
#Mientras i sea menor a la cantidad ejecuta
while i<=cantPeliculas:
    #Preguntar peliculas
    peli=input("Ingresa peli: ")
    #Agrega pelicula a la lista
    peliculas.append(peli)
    #Muestra la lista
    print(peliculas)
    i=i+1
#Buscar una pelicula en la lista
#Preguntar la plei a buscar
peliBuscar=input("Que peli buscas")
if peliBuscar in peliculas:
    print("Si esta")
else:
    print("No esta pero dejame la agreago")
    peliculas.append(peliBuscar)
    print(peliculas)
#Solicitar una pelicula para borrar
pelBorrar=input("Cual quieres borrar ")
#Borra la pelicula
peliculas.remove(pelBorrar)
#Muestra la lista
print(peliculas)

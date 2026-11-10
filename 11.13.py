numeros =[]
resultados =[]
i = 0
while i <5:
    num =int(input("Ingresa un numero"))
    numeros.append(num)
    i=i+1
multiplicador=int(input("¿Por cuanto deseas multiplicar?: "))
for num in numeros:
    resultado=num*multiplicador
    resultados.append(resultado)
print("Numeros originales: ",numeros)
print("Resultados: ",resultados)
#EXTRA

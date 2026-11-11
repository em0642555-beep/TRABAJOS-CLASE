numeros= []
i=0
while i<10:
    num=int(input("Ingresa un numero: "))
    numeros.append(num)
    i=i+1
print("Numeros pares: ")
for num in numeros:
    if num % 2 == 0:
        print(num)
numpares=[]
for num in numeros:
    if num %2==0:
        numpares.append(num)
    print(numpares)
#Programa para calcular areas
#Area cuadrada; lado x lado
lado=float(input("Ingresa lado "))
areaCuadrado=lado*lado 
print("El area es ", areaCuadrado)
print(f"El area es {areaCuadrado}")
#Area de un Triangulo
Base=float(input("Ingresa la base "))
altura=float(input("Ingresa la altura"))
areaTriangulo=Base*altura/2
print("El Area es ", areaTriangulo)
print(f"El area es {areaTriangulo}")
#Area de un Trapecio
BaseMayor=float(input("Ingrese la base mayor "))
baseMenor=float(input("Ingresa la base menor "))
Altura=float(input("Ingresa la altura "))
AreaTrapecio=BaseMayor+baseMenor*Altura/2
print("El area del ", AreaTrapecio)
print(f"El area es {AreaTrapecio}")
#Area Circulo
pi=3.1416
Radio=float(input("Ingrese el Radio "))
AreaCirculo=pi*(Radio*Radio)
print("El area del circulo es ", AreaCirculo)
print(f"El area del circulo {AreaCirculo}")
#Area Pentagono
lado=float(input("Ingrese lado "))
Apotema=float(input("Ingrese el apotema "))
Perimetro=lado*5
AreaPentajono=Perimetro*Apotema/2
print("El area es ",AreaTrapecio)
print(f"El area es {AreaPentajono}")
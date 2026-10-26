Edad=int(input("Ingrese tu edad "))
Sexo=(input("Ingrese su Sexo"))
if Sexo=="Hombre" and Edad>=18:
    print("Puedes sacar cartilla militar!! ")
elif Sexo=="Mujer" and Edad<18:
     print("No puedes sacar tu cartilla!! ")
else:
     print("No valido")
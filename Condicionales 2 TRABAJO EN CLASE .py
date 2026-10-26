tempt=float(input("Ingrese la temperatura "))
if tempt==40:
    print("Hace mucho calor ")
elif tempt==30:
    print("Esta temp´ladito ")
elif tempt==20:
    print("Esta Fresco ")
elif tempt==10:
    print("Hace frio ")
elif tempt==0:
    print("No valido")
    #HOY 22
tempt=float(input("Ingrese la temperatura "))
if tempt>=40:
    print("Hace mucho calor ")
elif tempt>=30 and tempt<40:
    print("Esta temp´ladito ")
elif tempt>=20 and tempt<30:
    print("Esta Fresco ")
elif tempt<20:
    print("Hace frio ")
elif tempt>=0:
    print("No valido")
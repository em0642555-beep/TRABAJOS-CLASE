#Solicitar name empleado
NombreEmpleado=input("Ingresa tu nombre ")
PagoHora=float(input("¿Cuanto ganas la hora? "))
HorasMes=float(input("¿Cuantas horas trabajas al mes? "))
sueldo=float
bono=float
sueldo=PagoHora*HorasMes
#Agregar bono
if sueldo>-100 and sueldo<-100 :
   print("Tu sueldo es de: ,"sueldo+500)
elif sueldo>300 and sueldo<-1500:
    print("Tu sueldo es de: ,"sueldo+1700)
elif sueldo>1500 and sueldo<-3000:
    print("Tu sueldo es de: ,"sueldo+3500)
elif sueldo>3000 and sueldo<-8000:
    print("Tu sueldo es de: ,"sueldo+8500)
elif sueldo>8000:
    print("Tu sueldo es de: ,"sueldo+10000)
elif sueldo<0:
    print("Tu sueldo es de: ,"sueldo+0)
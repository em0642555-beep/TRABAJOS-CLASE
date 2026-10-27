sexo=int(input("Ingresa tu sexo "))
edad=float(input("Ingresa tu edad "))
estadocl=int(input("Ingresa tu estado civil "))
canthijos=float(input("Ingresa la cantidad de hijos "))
if sexo=="Mujer" and canthijos==1 and edad<18:
  print("Eres mujer tienes un hijo y eres menor de edad entonces el apoyo sera de $800")
elif sexo=="Mujer" and canthijos==1 and edad>=18:
  print("Eres mujer tienes un hijo y eres mayor de edad entonces el apoyo sera de $300")
elif sexo=="Mujer" and canthijos>1 and edad<18:
  print("Eres mujer tienes mas de un hijo y eres menor de edad entonces el apoyo es de 1500")
elif sexo=="Mujer" and canthijos>1 and edad>=18:
  print("Eres mujer tienes mas de un hijo y ya eres mayor de edad entonces el apoyo sera de $500")
elif sexo=="Hombre" and canthijos>1 and estadocl=="Soltero":
  print("Eres hombre y tienes hijos y el apoyo es de 780")
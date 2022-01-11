#Aquí quiero me de desarrolleis un programa con una función, que reciba una lista y un valor, y devulva las veces que aparece el valor en la lista;
#Para que se detecte la lista y el valor, tienen que ir escritos entre comillas.
#Si la lista introducida contine más de una palabra, tiene que ir escrita dentro de corchetes y las palabras introducidas deben estar separadas por comas.

lista = input("Introduce una lista: ")
valor = input("Introduce un valor: ")
cont = 0
cont1 = 0
total = 0

for l in lista:
  if l == valor:
    cont = cont + 1
  else:
    cont1 = cont1 + 1
    
total = cont + cont1

if cont == 1:
  print("De un total de ")
  print(total)
  print(" posibilidades, el valor ")
  print(valor)
  print(" se repite ")
  print(cont)
  print(" vez.")
else:
  print("De un total de ")
  print(total)
  print(" posibilidades, el valor ")
  print(valor)
  print(" se repite ")
  print(cont)
  print(" veces.")

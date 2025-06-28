#Los loop son los bucles que permetira que se repita una misma accion hasta que salga

#for (Para cada elemento en una secuencia)

fruits =["manzana","banana","narajan","kiwi"]

for i in fruits:
  print(i)



#Recorrer un rango de numero

for i in range(0,5):
  print(f"Numero:{i} ")


mylist = ["python","php","java","javascript","C++"]

for language in mylist:
  if language == "javascript":
    print("JAVASCRIPT encontrado, saliendo del bucle. ")
    break
  print(f"lenguaje de programacion: {language}")

#Usando contienue para saltar un elemento especifico

for language in mylist:
  if language == "java":
    print("Saltando java")
    continue
  print(f"lenguaje de programacion: {language}")


#Bucle while (mientras se cumpla una condicion)

count = 0

while count < 20:
  print(f"Contador: {count}")
  count +=1


print("/n otro caso del while")
choise =input("Para iniciar escriba iniciar: ")
choise=("INICIAR")

while choise.lower()=="iniciar":
  number = int(input("ingre un numero :"))
  number2 = int(input("ingre un numero :"))
  print(f"La suma de {number} y {number2} es: {number+number2}")
  choise = input("Para continuar escriba iniciar o cualquier otra tecla para salir:")
print("Gracias por usar la calculadora. Hasta luego")
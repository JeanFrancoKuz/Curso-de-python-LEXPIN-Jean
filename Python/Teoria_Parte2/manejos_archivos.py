#metodos de archivos se refiere a metodos y tecnicas nativos de python para leer,escribir,modificar y eliminar

#Abriendo un archivo para lectura

#Se utiliza el metodo open() para abrir un archivo en modo de lectura

#El primer argumento es el nombre del archivo, y el segundo es el modo en que se abre el archivo

#MODOS DE LOS ARCHIVOS

# "r" (read): Abre el archivo para lectura. Si el archivo no existe, genera un error.

# "w" (write): Abre el archivo para escritura. Si el archivo no existe, lo creo

# "a" (append): Abre el archivo para escritura, agregando contenido al final del archivo. Si el archivo no existe, lo crea.

#" x" (create): abre el archivo para escritura, creando

#LEER UN ARCHIVO

try:
  document = open("./Python/Teoria_Parte2/Prueba_manejo_archivos/history.txt", "r")
  print(document.read())
  document.close()
except Exception as e:
  print(e)

#ESCRIBIR UN ARCHIVO

try:
  document = open("./Python/Teoria_Parte2/Prueba_manejo_archivos/holita.txt", "w")
  content=input("Escribe el contenido que quieres tener adentro, ayyy chinazoo  ")
  document.write(content)
  document.close()

  document = open("./Python/Teoria_Parte2/Prueba_manejo_archivos/holita.txt", "r")
  print(document.read())
  document.close()
except Exception as e:
  print(e)

#Agregar contenido a un archivo existente
try:
  #Aqui crea un archivo
  document = open("./Python/Teoria_Parte2/Prueba_manejo_archivos/holota.txt", "w")
  document.write("Aqui hay algo ya creado quieres echarla algo encima ")
  document.close()
  #Aqui agrega algo mas con APPEND
  document = open("./Python/Teoria_Parte2/Prueba_manejo_archivos/holota.txt", "a")
  content=input("Ponle algo encima que lo deseaa mamon ")
  document.write(content)
  document.close()
#AQUI LO LEE
  document = open("./Python/Teoria_Parte2/Prueba_manejo_archivos/holota.txt", "r")
  print(document.read())
  document.close()
except Exception as e:
  print(e)

#Eliminar un archivo

# import os

# try:
#   os.remove("./Python/Teoria_Parte2/Prueba_manejo_archivos/holota.txt")
# except Exception as e:
#   print (e)

#Manipular archivos .csv()

#Para utilizar necesitamos importar la libreria 

import csv

#Los metodos son:

#csv.writer() para escribir en un archivo .csv
#csv.reader() para leer un archivo .csv
#csv.DictWriter() Para escribir en un archivo .csv son diccionarios
#csv.Dictreader() para leer un archivo .csv con diccionarios

contacts = [{"nombre": "Jean", "telefono": "4123971034"},
            {"nombre": "Fabiola", "telefono": "4242653244"},
            {"nombre": "Sussan", "telefono": "4126307464"},
            {"nombre": "jesusito", "telefono": "66666666"},]

with open("./Python/Teoria_Parte2/Prueba_manejo_archivos/contacts.csv","w", newline="") as file:
  writer = csv.DictWriter(file, fieldnames=["nombre", "telefono"])
  writer.writeheader()
  writer.writerows(contacts)

with open("./Python/Teoria_Parte2/Prueba_manejo_archivos/contacts.csv","r") as file:
  reader =csv.DictReader(file)
  for row in reader:
    print(row["nombre"],row["telefono"])

#AGREGAR UN APPEND
with open("./Python/Teoria_Parte2/Prueba_manejo_archivos/contacts.csv","a") as file:
  writer= csv.DictWriter(file,fieldnames=["nombre","telefono","email"])
  writer.writeheader()
  writer.writerows(contacts)











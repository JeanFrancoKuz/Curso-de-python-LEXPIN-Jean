#match nos sirve para evaluar una variable y ejercutar un bloque de codigo dependiendo del valor de esa variable

print("ingrese un numero del 1 al 5")
number = input("numero :")

match number:
  case "1":
    print("El numero es 1")
  case "2":
    print("El numero es 2")
  case "3":
    print("El numero es 3")
  case "4":
    print("El numero es 4")
  case "5":
    print("El numero es 5")
  case _:
    print("El numero tiene que ser entre 1 al 5")

#El guion bajo (_) se usa como comodin para capturar cualquier valor que no coincido con los casos anteriores

print("Seleccion de idioma")
language = input("ingrese el idioma (es,en,fr): ")

match language:
  case "es":
    print("Seleccionaste español")
  case "en":
    print("Seleccionaste ingles")
  case "fr":
    print("Seleccionaste frances")
  case _:
    print("No se ha seleccionado ningun idioma5")

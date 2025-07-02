"""
Nivel Básico
1)
Función simple:
Crea una función saludar() que imprima "¡Hola, bienvenido al curso!".

2)
Función con parámetros:
Crea una función area_rectangulo(largo, ancho) que calcule y retorne el área de un rectángulo.

3)
Función con condicional:
Crea una función es_par(numero) que retorne True si el número es par y False si es impar.


"""

# Crea una función saludar() que imprima "¡Hola, bienvenido al curso!"


def saludos(nombre):
  print(f"¡Hola, bienvenido al curso! {nombre}")

saludos("jean")

#2) Función con parámetros: Crea una función area_rectangulo(largo, ancho) que calcule y retorne el área de un rectángulo.

def areadeunrectangulo(base=0,altura=0):
  area= base * altura
  print(f"La area de tu rectangulo seria esta {area}")

areadeunrectangulo(6,4)

#3)Función con condicional: Crea una función es_par(numero) que retorne True si el número es par y False si es impar.

def par_impar(numero):
  if numero%2 == 0:
    print("Es true")
  else:
    print(" Esfalse")

par_impar(2)
par_impar(3)
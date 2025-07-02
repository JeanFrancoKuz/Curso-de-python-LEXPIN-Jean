"""
Nivel Intermedio (Funciones + Lambdas)
1)
Lambda básica:
Crea una lambda que eleve un número al cuadrado. Pruébala con el número 5.

2)
Lambda con condicionales:
Crea una lambda que reciba un número y retorne:
"Positivo" si es mayor que 0.
"Negativo" si es menor que 0.
"Cero" si es igual a 0.

3) No se puede hacer con lambda debido a que son muchos cacos 
Lambda con match-case:
Crea una lambda que reciba una letra (minúscula) y usando match-case retorne:
"Vocal" si es 'a', 'e', 'i', 'o', 'u'.
"Consonante" para cualquier otra letra.
"""

#1)Lambda básica: Crea una lambda que eleve un número al cuadrado. Pruébala con el número 5.

potenciacion = lambda num1: num1**2
print(f"potenciacion de 5 al cuadro es {potenciacion(5)} ")

#2) Lambda con condicionales: Crea una lambda que reciba un número y retorne:"Positivo" si es mayor que 0."Negativo" si es menor que 0."Cero" si es igual a 0.

enteros =lambda num: "positivo" if num>0 else "negativo" if num<0  else 0 

print(f" El numero es {enteros(5)} ")
print(f" El numero es {enteros(-3)} ")
print(f" El numero es {enteros(0)} ")

#3)Lambda con match-case:Crea una lambda que reciba una letra (minúscula) y usando match-case retorne:"Vocal" si es 'a', 'e', 'i', 'o', 'u'."Consonante" para cualquier otra letra.


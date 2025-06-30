# Ejercicio 1: Contador Selectivo
# Enunciado:  
# Escribe un programa que pida al usuario un número entero positivo "n". Luego, imprime todos los números del 1 al "n" que cumplan una de estas condiciones:
# 1. El número es múltiplo de 3.
# 2. El número es mayor que 10 y menor que 20.
# 3. El número es igual a 25 o 50.  
# Si el número no cumple ninguna condición, no se imprime.


print("Este programa funciona para contar asi que elige un numero")

numero = int(input("Aqui puedes escogerlo: "))
count = 1
while count <= numero:
    if count % 3 == 0 or (10 < count < 20) or (count == 25 or count == 50):
      print(f"El numero {count} cumple una de las condiciones")
    count += 1
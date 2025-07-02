#Ejercicio 2:
#Crea un programa que simule la validacion de una contraseña
#1 Define una contraseña secreta EJEMPLO LO QUE SEA
#2 Pide al usuario que ingrese una contraseña
#3 El programa debe:
#   -Permitir hasta 3 intentos.
#   -Si la contraseña es correcta, mensaje de validacion
#    - Permitir hasta 3 intentos.
#    - Si la contraseña es correcta, muestra "¡Acceso concedido!" y termina.
#    - Si es incorrecta, muestra "Contraseña incorrecta. Intentos restantes: X" y permitir un  siguiente intento.
#    - Si se agotan los intentos, muestra "¡Cuenta bloquea!"


print("Programa contraseña")
contraseña="python123"
intentos= 0
max_intentos=3
while intentos <= max_intentos:
  texto=input("Introduce la contaseña: ")
  if texto == contraseña:
    print("¡Acceso concedido!")
  else:
    intentos+=1
    intentos_restantes = max_intentos-intentos
    if intentos_restantes > 0:
      print(f"Contraseña incorrecta. Intentos restantes: {intentos_restantes}")
    else:
      print("¡Cuenta bloqueada!")


"""
Crea un programa en Python que haga lo siguiente:

1.  Muestra un menú al usuario con al menos tres opciones diferentes. Estas opciones deben ser operaciones matemáticas simples 
(suma, resta, multiplicación, división) o cualquier otra acción que se te ocurra (por ejemplo, saludar, decir un chiste). 
Asegúrate de que una de las opciones sea "Salir".
2.  Pide al usuario que elija una opción ingresando un número o una palabra clave.
3.  Usa condicionales (if, elif, else) para:
      * Ejecutar la operación correspondiente a la elección del usuario.
      * Si el usuario elige una operación matemática, pídele los números necesarios y luego muestra el resultado.
      * Si el usuario elige "Salir", imprime un mensaje de despedida.
      * Si el usuario ingresa una opción no válida, muestra un mensaje indicando que la opción es incorrecta.

¡Mucha suerte! ya les subo el repo
"""

print("\tMENU CALCULADORA")
print("1. Desea realizar una Suma")
print("2. Desea realizar una Resta")
print("3. Desea realizar una Multiplicacion")
print("4. Desea realizar una Division")
print("5. Desea realizar una Division sin decimales")
print("6. Desea realizar una Potenciacion")
print("7. Salir")
opcion = int(input("Digite una opcion de menu: "))

if opcion ==1:
  Num1 = int(input("Escribe el numero que quiera para realizar la operacion "));
  Num2 = int(input("Escribe el numero que quiera para realizar la operacion "));
  suma=Num1+Num2;
  print(f"Este seria el resultado de la suma {suma}")
elif opcion ==2:
  Num1 = int(input("Escribe el numero que quiera para realizar la operacion "));
  Num2 = int(input("Escribe el numero que quiera para realizar la operacion "));
  resta=Num1-Num2;
  print(F"Este seria el resultado de la resta:{resta}")
elif opcion ==3:
  Num1 = int(input("Escribe el numero que quiera para realizar la operacion "));
  Num2 = int(input("Escribe el numero que quiera para realizar la operacion "));
  Multiplicacion=Num1*Num2;
  print(F"Este seria el resultado de la Multiplicacion:{Multiplicacion}")
elif opcion ==4:
  Num1 = int(input("Escribe el numero que quiera para realizar la operacion "));
  Num2 = int(input("Escribe el numero que quiera para realizar la operacion "));
  Division=Num1/Num2;
  residuo=Num1%Num2;
  print(F"Este seria el resultado de la Division:{Division}")
  print(F"Este seria el residuo de la division:{residuo}")
elif opcion ==5:
  Num1 = int(input("Escribe el numero que quiera para realizar la operacion "));
  Num2 = int(input("Escribe el numero que quiera para realizar la operacion "));
  Divisionsindecimales=Num1//Num2;
  residuo=Num1%Num2;
  print(F"Este seria el resultado de la Division:{Divisionsindecimales}")
  print(F"Este seria el residuo de la division:{residuo}")
elif opcion ==6:
  Num1 = int(input("Escribe el numero que quiera para realizar la operacion "));
  Num2 = int(input("Escribe el numero que quiera para realizar la operacion "));
  potenciacion=Num1**Num2;
  print(F"Este seria el resultado de la Potenciacion:{potenciacion}")
elif opcion==7:
  print("Hasta luego chamo")
else:
  print("Esta opcion no existe")




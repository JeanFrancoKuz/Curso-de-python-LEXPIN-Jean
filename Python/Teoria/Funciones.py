#Es un bloque aislado de codigo reutilizable


#Estructura palabra reservada def + nombre de mi funcion + parentesis() + : dos puntos dentro de lo que se quiera ejecutar

def saludar():
  print(f"hola desde mi funcion ")

#usar mi funcion
saludar()

def suma():
  valone = 5
  valtwo = 2
  print(f"la suma de {valone} y {valtwo} es: {valone + valtwo}")

suma()

#Las funciones pueden recibir valores cambiantes, dichos valores se llaman parametros

def rest(num1,num2):
  print(f"La resta de {num1} y {num2} es: {num1 - num2}")

rest(7,8)
rest(9,5)
rest(100,20)

#Retorno de valores

def mult(num1=0,num2=0):
  mult = num1 * num2
  return mult

sumtwo= mult(10,5)+5
print(sumtwo)

#sepuede solicitar valores al usuario y pasarlos como argumentos a la funcion
numone = int(input("Ingrese un numero"))
numtwo = int(input("Ingrese otro numero"))

sumtwo = mult(numone,numtwo)

print(f"El resultado que retorna mi funcion mult es: {sumtwo}")

#Funciones lambda, seran funciones pequeñas, anonimas y definidas en una sola linea de codigo

division = lambda num1, num2: num1 / num2

#Uso de funcion lambda
print(f"la division de {numone} y {numtwo} es: {division(numone,numtwo)}")

#callback seran funciones que le pasaremos como argumento a otras funciones

def process(list, callback):
  return [callback(item) for item in list]

results = process([1,2,3,4], lambda number: number*2)

print(f"El resultado de la funcion es este : {results}")
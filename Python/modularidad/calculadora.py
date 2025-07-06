def sum(a, b):
  return a + b

def rest(a, b):
  return a - b

#la variable __name__ es una variable especial que contiene el nombre del modulo actual

#cuando se ejecuta como modulo principal el valor de __name__ es __main__, cuando es importado el valor de __name__ es el nombre del modulo
print(f"El modulo actual es: {__name__}")

if __name__ == "__main__":
  print("El modulo se esta ejecutando como modulo principal")
  numberOne = 10
  numberTwo = 5

  sum = numberOne + numberTwo

  print(f"La suma de {numberOne} + {numberTwo} es igual a {sum}")
  
  rest = numberOne - numberTwo

  print(f"La resta de {numberOne} - {numberTwo} es igual a {rest}")
  

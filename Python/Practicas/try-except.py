#Manejo de excepciones se refiere a la forma en que python maneja los errores que pueden ocurrir durante la ejecucion de un programa


#Python tiene la estructura try-except para manejar excepciones.

"""
Ejercicio que salta el error zerodivision
"""

# def divide_number(num1,num2):
#   return num1/num2

# result=divide_number(10/0)

# print("finalizado el programa")

def safe_divide_number(num1,num2):
  try:
    val=num1/num2
    return val
  except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")
    return None
  except TypeError:
    print("Error: Los valores deben ser numero.")
    return None
  finally:
    print("Intentode division finalizado")
  

result = safe_divide_number(10,0)  

print("finalizado el programa")
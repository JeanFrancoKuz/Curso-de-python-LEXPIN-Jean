print("iniciando el modulo principal")

import calculadora as cal
from helpers import herramientas

sum = cal.sum(10, 5)

rest = cal.rest(10, 5)

print(f"La suma es: {sum}")

print(f"La resta es: {rest}")

herramientas.hello("jean")

herramientas.goodbye("jean")

circle_area = herramientas.obtain_circle_area(10)
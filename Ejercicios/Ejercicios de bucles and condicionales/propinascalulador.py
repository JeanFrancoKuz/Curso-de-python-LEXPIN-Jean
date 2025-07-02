"""
Ejercicio 1: Calculadora de Propinas
Contexto: Acabas de cenar en un restaurante y quieres calcular la propina  
Tareas: 
1. Pedir al usuario el total de la cuenta  
2. Preguntar si el servicio fue excelente (15%), bueno (12%) o regular (10%)  
3. Calcular la propina según la calidad del servicio  
4. Preguntar si dividir la cuenta entre N personas  
5. Mostrar:  
  - Total con propina  
  - Propina individual  
  - Total por persona
"""

check_cuenta = float(input("Cual fue el total de la cuenta: "))
servicio = input("Escoga como fue su servicio (excelente, bueno, regular): ")


match servicio.lower():
  case "excelente":
    propina = check_cuenta*0.15
    total = propina+check_cuenta
    print(f"Escogio Excelente el total de la propina seria: {propina}  y el total de su cuenta seria {total} ")
  case "bueno" :
    propina = check_cuenta*0.12
    total = propina+check_cuenta
    print(f"Escogio Bueno el total de la propina seria: {propina}  y el total de su cuenta seria {total} ")
  case "regular":
    propina = check_cuenta*0.10
    total = propina+check_cuenta
    print(f"Escogio Regular el total de la propina seria: {propina}  y el total de su cuenta seria {total} ")
  case _:
    print("Esa opcion no existe señor")
dividir = input("¿Desea dividir la cuenta entre varias personas? (si/no): ").lower()

if dividir == "si":
  personas =int(input("Entre cuántas personas desea dividir la cuenta "))
  total_separado= total/personas
  print(f"Entonces quedamos que el total de la propina seria {propina} y el total por persona seria {total_separado}")
else:
  print(f"Entonces quedamos que el total de la propina seria {propina} y el total seria {total}")



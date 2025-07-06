"""
Ejercicio 3: Verificador de Clima para Viaje  
Contexto: Estás planeando una salida y necesitas verificar el clima  
Tareas: 
1. Pedir temperatura actual (en °C)  
2. Preguntar si está lloviendo (sí/no)  
3. Preguntar si hay alerta meteorológica (sí/no)  
4. Decidir si es buen momento para salir:  
- Temperatura entre 18°C y 28°C  
- No debe estar lloviendo  
- No debe haber alerta meteorológica  
5. Mostrar recomendación personalizada:  
- Si hace mucho calor: "Lleva protección solar"  
- Si hace frío: "Usa abrigo"  
- Si todas las condiciones son ideales: "¡Día perfecto!" 
"""


current_temperature = float(input("¿Cuál es la temperatura actual (°C)? "))

llueve = input("¿Está lloviendo el día de hoy? (si/no): ").lower()
alerta = input("¿Hay alguna alerta meteorológica? (si/no): ").lower()

if llueve == "si" or alerta == "si":
    print("No es buen momento para salir.")
    if llueve == "si":
        print("Está lloviendo.")
    if alerta == "si":
        print("Hay una alerta meteorológica.")

elif 18 <= current_temperature <= 28:
    print("¡Día perfecto!")
else:
    if current_temperature < 18:
        print("Hace frío. Usa abrigo.")
    elif current_temperature > 28:
        print("Hace calor. Lleva protección solar.")














# current_temperature =float(input("Cual es la temperatura actual: "))

# encuesta = input("¿Esta lloviendo el dia de hoy? (si/no): ").lower()
# if (encuesta=="no"):
#   encuesta2 = input("¿Hay alguna alerta metereologica? (si/no): ").lower()
#   if (encuesta2=="no"):
#     print("Verifiquemos que la temperatura sea la adecuada")
#     if (18 < current_temperature > 28):
#       print("Es un buen dia para salir")
#     else:
#       print("Hoy debemos quedarnos en casa por la tempeperatura")
#   else:
#     print("Hay alerta creo que deberiamos qudarnos")
# else:
#   print("Hoy no se sale esta lloviendo")
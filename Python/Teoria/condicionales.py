#Son estructuras que permiten que el programa tome diferentes caminos de ejecucion dependiendo de si una condicion se cumple.

# if (si)

age  = 18

if age >= 18:
  print("Eres mayor de edad puedes pasar")
# else (Sino se cumple la condicion haz lo siguiente)
else:
  print("Eres menor de edad no puedes pasar")
  
notes = 4

if notes >= 7:
  print("Aprobado con nota apenas decente")

# elif (Sino si, si se cumple esta condicion haz lo siguiente)
elif notes >= 5:
  print("Aprobado, pero necesitas mejorar y mucho")
else:
  print("Reprobado, necesitas estudiar mas para poder pasar")
  

# operador ternario: es una forma compacta de escribir un condicional if-else

#Su  sintaxis es: variable = valor_si_verdadero if condicion else valor_si_falso
isAdult = "Eres mayor de edad" if age >= 18 else "Eres menor de edad"

print(isAdult)
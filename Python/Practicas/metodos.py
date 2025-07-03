#Metodos para string

#Es una funcion asociada a un objeto, dicho objeto puede ser una lista,variable,clase,un diccionario, un objeto, etc.

name = "herasi"

#len() Devuelve la longitud de mi string

print(f"La longitud de mi string es: {len(name)}")

#count() devuelve la cantidad de veces que aparece una subcadena dentro de mi string

text = "ok, chicos, esto es un texto, de muletillas, ok"

print(f"La cantidad de ',' en mi string es : {text.count(",")}")

#Upper() convierte mi string todo en mayuscula

print(f"Mi string escribira todo en mayuscula: {text.upper()}")

#lowe() convierte mi string todo en miniscula

print(f"Mi string escribira todo en mayuscula: {text.lower()}")

#capitalize() Este metodo convierte la primera letra del string a mayuscula

print(f"Mi string escribira todo en mayuscula: {name.capitalize()}")

#replace() reemplaza una subcadena por otra

user_status = "El usuario se encuentra online"

print(f"El usuario se encuentra  {user_status}")

user_status= user_status.replace("online","onfline")
print(f"El usuario se encuentra  {user_status}")

#split() divide mi string en una lista

my_super_text = "Hola mundo, estamos aqui felices aprendiendo python, en Lexpin"

my_world_list =my_super_text.split(",")

print(my_world_list)

print("-"*50)

#strip() permite eliminar un caracter en especifico de el inicio y el final de nuestro string

my_super_text1 = "---Hola mundo, estamos aqui felices aprendiendo python, en Lexpin---"

my_super_text_awesome = my_super_text1.strip("-")

print(my_super_text_awesome)

#join() une los elementos de una lista (array) en un solo string separados por un caracter



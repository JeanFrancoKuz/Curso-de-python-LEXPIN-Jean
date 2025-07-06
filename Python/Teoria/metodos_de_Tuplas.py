#Un metodo es una funcion asociada a un objeto (Dicho objeto puede ser una variable, una lista, un diccionario, un objeto, una clase, etc.)

#Metodos de Tuplas

myTuple = ("Javier","Paula","Herasi", "Alejandro", "Cris", "Norland")

#len() devuelve la longitud de mi tupla

print(f"la longitud de mi tupla es: {len(myTuple)}")

#count(): nos permite contar la cantidad de veces que aparece un elemento en una tupla

print(f"la cantidad de 'Cris' en mi tupla es: {myTuple.count('Cris')}")

#index(): nos permite obtener el indice de un elemento en una tupla

print(f"El indice de 'Cris' en mi tupla es: {myTuple.index('Cris')}")
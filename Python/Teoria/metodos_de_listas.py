#Un metodo es una funcion asociada a un objeto (Dicho objeto puede ser una variable, una lista, un diccionario, un objeto, una clase, etc.)

#Metodos de Listas

names = ["Javier","Paula","Herasi", "Alejandro", "Cris", "Norland"]

#len() devuelve la longitud de mi lista

print(f"la longitud de mi lista es: {len(names)}")


#append() nos permite agregar un elemento al final de la lista

names.append(input("Ingrese un nombre: "))

print(names)

#extend(): nos permite agregar varios elementos al final de la lista

names.extend(["manuel","Andrea","Juan","Andres"])

print(names)


#insert(position, element): nos permite inserta un elemento, pero en una posicion especificada


names.insert(2, "Andres")

print(names)


#remove(element): nos permite eliminar el primer elemento que coincida con el valor pasado como argumento

names.remove("Andres")

print(names)

#index(element): nos devolvera la posicion del primer elemento que coincida con el valor pasado como argumento

print(names.index("Paula"))

#count(element): cuenta la cantidad de veces que se repite un elemento retornando un entero

cellphones = ["iPhone 14", "iPhone 14 Pro", "iPhone 14 Pro Max", "iPhone 14", "iPhone 14 Pro", "iPhone 14 Pro Max"]

print(cellphones.count("iPhone 14"))


#sort(): nos permite ordenar una lista de menor a mayor (defecto)

names.sort()

print(names)

numbers = [13,35,565,433,232,657,0,23,1,5]

numbers.sort(reverse=True)

print(numbers)

#reverse(): nos permite invertir el orden de una lista

names.reverse()

print(names)

#clear(): nos permite eliminar todos los elementos de una lista

names.clear()

print(f"La lista se encuentra vacia: {names}")

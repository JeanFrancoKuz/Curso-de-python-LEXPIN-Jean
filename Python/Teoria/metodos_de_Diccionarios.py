#Un metodo es una funcion asociada a un objeto (Dicho objeto puede ser una variable, una lista, un diccionario, un objeto, una clase, etc.)

#Metodos de Diccionarios

person = {
  "name": "Norland",
  "age": 23,
  "country": "Venezuela"
}


#get(value): nos va a permitir obtener un valor asociado a una clave de un dicicionario

print(person.get("name"))

#keys(): nos va a permitir obtener todas las claves de un diccionario

print(person.keys())

#values(): nos va a permitir obtener todos los valores de un diccionario

print(person.values())

#setdefault(key, value): nos va a permitir agregar un valor a un diccionario si no existe, lo crea, si existe, le cambia el valor

person.setdefault("last_name", "Rodriguez")

print(person)

#modificar un valor

person["name"] = "Jesus"

#Forma de acceder a un valor de un diccionario
print(person["name"])


#Nosotros podemos convertir un diccionario a JSON para mostrarlo comodamente

#JSON significa Javascript Object Notation

import json

print(json.dumps(person, indent=4))

#Podemos convertir un JSON a un diccionario

person_json = '{"name": "Norland", "age": 23, "country": "Venezuela"}'

person = json.loads(person_json)

print(person_json)


#items(): nos va a permitir obtener todas las claves y valores de un diccionario traidas en una lista de tuplas

print(person.items())

#pop(Key): este metodo eliminara la clave dadad y devuelve su valor asociado

citys = {
  "Venezuela": "Caracas",
  "Colombia": "Bogota",
  "Peru": "Lima"
}

citys.pop("Venezuela")

print(citys)


#popitem(): nos va a permitir eliminar una clave y su valor al azar

citys = {
  "Venezuela": "Caracas",
  "Colombia": "Bogota",
  "Peru": "Lima"
}

citys.popitem()

print(citys)

#update({"key": "value"}): nos va a permitir agregar los valores de un diccionario a otro

person = {
  "name": "Norland",
  "age": 23,
  "country": "Venezuela"
}

#Podemos actualizar el valor de una clave
person.update({"name": "Jesus"})


#Y tambien podemos agregar nuevas claves
person.update({"last_name": "Rodriguez", "profession": "Programmer"})

print(person)

#copy(): nos va a permitir copiar un diccionario, esta es una copia superficial

personCopy = person.copy()

print(personCopy)

#clear(): nos va a permitir eliminar todos los elementos de un diccionario

person.clear()

print(person)
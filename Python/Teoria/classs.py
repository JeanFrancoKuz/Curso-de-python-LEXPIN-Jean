#La POO (Programacion Orientada a Objetos) es un paradigma de programacion que nos permite crear objetos que contienen tanto datos como metodos para manipular esos datos.

#Clase es una plantilla o molde que define las caracteristicas y comportamientos de un objeto.


class Person:
  #Esto no cambia, son atributos estaticos
  # name = "Delvis"
  # age = 23
  # country = "Venezuela"
  
  def __init__(self, name, age, country) :
    #Atributos dinamicos de clase
    self.name = name
    self.age = age
    self.country=country
    
  #Podemos tener metodos dentro de una clase, estos son funciones que pertenecen a la clase
    
  def greet(self):
    print(f"Hola, mi nombre es {self.name}, tengo {self.age} años y soy de {self.country}")
  
  def goodbye(self):
    print(f"Adios, hasta la proxima amiguitos")
    
#Instaciar una clase es crear un objeto a partir de la clase, esto se hace llamando a la clase como si fuera una funcion.

personOne = Person("Delvis", 23, "Venezuela")

personTWo = Person("Herasi", 47, "Venezuela")

#Acceder a los atributos de la clase
    
print(f"Mi nombre es {personOne.name}, tengo {personOne.age} años y soy de {personOne.country}")
#Lllamemos a nuestra segunda persona
print(f"Mi nombre es {personTWo.name}, tengo {personTWo.age} años y soy de {personTWo.country}")

#llamar a los metodos de la clase

personOne.goodbye()

#Acceder a los atributos con el aitrbuto especial __dict__

print(f"Los atributos de personOne son : {personOne.__dict__}")

#Extencion de la clase, podemos crear una clase que herede de otra clase, esto se llama herencia

#Si yo creo una clase student, esta heredara todos los atributos, su manejo y todos los metodos de la clase person

class Student(Person):

  def __init__(self, name, age, country,career):
    #llamamos al constructor de la clase padre
    super().__init__(name,age,country)
    #atributos adicionales de la clase student
    self.career = career

  def study(self):
    print(f"Estoy estudiando {self.career}")

studentOne = Student("Alejandro",34,"Venezuela", "adm. Financiria")

print(f"Mi nombre es {studentOne.name}, tengo {studentOne.age} años y soy de {studentOne.country} y estudio {studentOne.career}")

#Crear la clase professor que herede de la clase Person y tenga su propia variable llamada, class, y su metodo darClass

class Professor(Person):
  def __init__(self, name, age, country,classs):
    super().__init__(name,age,country)
    self.classs = classs
  
  def darClass(self):
    print(f"Estoy dando clases {self.classs}")
  
profesorOne = Professor("Delvis",23,"Venezuela", "Programacion en Python")

print(f"Mi nombre es {profesorOne.name}, tengo {profesorOne.age} años soy de {profesorOne.country} y enseño {profesorOne.classs}")

profesorOne.darClass()
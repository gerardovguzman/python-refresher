'''
Este código define una clase Person con un constructor que inicializa 
los atributos name y age, y dos métodos especiales: __str__, que 
devuelve una representación amigable del objeto, y __repr__, que 
devuelve una representación más técnica y detallada. Luego, se crea 
una instancia de Person llamada bob y se muestra su representación en 
la consola. Esto demuestra cómo utilizar la programación orientada a 
objetos en Python y cómo personalizar la representación de las 
instancias de clase.
'''

class Person:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"<('{self.name}',{self.age})>"



bob = Person("Bob",35)
gera = Person("Gera",44)
print(bob)
print(gera)


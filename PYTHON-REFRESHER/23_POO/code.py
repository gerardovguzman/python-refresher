'''ESTA FUNCIÓN NO SABE NADA ACERCA DEL ALUMNO
LA FUNCIÓN SOLO OPERA CON LO QUE RECIBE

student = {"name":"Rolf","grades":(89,90,93,78,90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))
'''

'''
CUANDO LA FUNCIÓN ESTÁ DENTRO DE UNA CLASE SE LLAMA MÉTODO
SI A LA VARIABLE student = Student() LO QUE SE HACE ACÁ ES LLAMAR A LA CLASE
Y AUTOMÁTICAMENTE SE EJECUTARÁ EL MÉTODO INIT
Y CREARÁ ALGO LLAMADO self Y PODEMOS MODIFICAR LA PROPIEDAD name DENTRO DEL OBJETO self
Y DARLE UN VALOR
AHORA ESA PROPIEDAD NAME Y EL VALOR QUE SE LE DEN, PASARÁ A FORMAR PARTE
DE student, AL HABERLE ASIGNADO LA CLASE
student = Student()

OBJETO self
PROPIEDAD name
METODO __init__
CLASE Student
'''

'''
este código define una clase Student que inicializa un estudiante con un 
nombre, edad y calificaciones. Luego, crea una instancia de Student y calcula 
el promedio de sus calificaciones utilizando el método average, 
imprimiendo el resultado en la consola.
'''

class Student:  #clase Student
    def __init__(self,name, grades):  #método __init__    objeto self
        self.name = name  #propiedad name
        self.grades = grades
    
    def average_grades(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob",(100,100,93,78,90))
student2 = Student("Rolf",(90,90,93,78,90))

'''
print(student.name)
print(student2.name)
print(student.average_grades())
print(student2.average_grades())'
'''

print(f"Hi! Your name is", student.name ,"and the average of your grades is", student.average_grades())
print(f"Hi! Your name is", student2.name ,"and the average of your grades is", student2.average_grades())



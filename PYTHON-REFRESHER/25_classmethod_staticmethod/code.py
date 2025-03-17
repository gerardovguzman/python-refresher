class Classtest:

# LOS METODOS DE INSTANCIA SE USAN PARA LA 
# MAYORÍA DE LAS COSAS, CUANDO SE DESEE PRODUCIR 
# UNA ACCION QUE UTILICE LOS DATOS DENTRO DEL OBJETO 
# QUE SE CREÓ ANTERIORMENTE
    def instance_method(self):
        print(f"Called instance_method of {self}")


# LOS METODOS DE CLASE SE USAN A MENUDO COMO 
# FÁBRICAS
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

# SE USAN PARA COLOCAR UN METODO DENTRO DE UNA CLASE
# 
    @staticmethod
    def static_method():
        print(f"Called static_method.")

#Classtest.class_method()
#Classtest.static_method()

######################################################

class Book:
    TYPES = ("hardcover","paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return(f"<Book: {self.name}, {self.book_type}, weithing {self.weight}g>")
# PARA BOOK_TYPE NO HACEMOS NINGUNA VALIDACIÓN, PODEMOS 
# PONER CUALQUIER COSA AHÍ.. 
#  SE CREARÁ UN METODO QUE TENGA EN CUENTA EL NOMNRE 
# Y EL PESO, Y EL OBJETO SE CREARÁ CON BOOK_TYPE 
# HARDCOVER EN ESTE CASO
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 10)
    
book = Book.hardcover("Harry Potter",1500)
book2 = Book.paperback("Moby Dick",800)
print(book)
print(book2)



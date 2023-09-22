# Creación de una clase en Python que representa una matriz.
# Para este ejercicio, deberás crear una clase que representa una matriz.
# Las operaciones que esta clase debe permitir son la creación de una matriz a partir 
# de una lista de listas, la impresión de la matriz en una forma legible, y el cálculo de 
# la transpuesta de la matriz. Asegúrate de que cada método tenga una única responsabilidad.

class Matriz():
    def __init__(self, elementos):
        self.elementos = elementos

class ToDo(Matriz):
    def imprimir(self):
        for fila in self.elementos:
            print(fila)

    def transpuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])
    
m = Matriz([[1, 2], [3, 4]])
todo1 = ToDo(m.elementos)
todo1.imprimir()

print()

m_transpuesta = todo1.transpuesta()
todo2 = ToDo(m_transpuesta.elementos)
todo2.imprimir()
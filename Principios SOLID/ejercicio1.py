# Creación de una clase en Python que representa una matriz.
# Para este ejercicio, deberás crear una clase que representa una matriz.
# Las operaciones que esta clase debe permitir son la creación de una matriz a partir 
# de una lista de listas, la impresión de la matriz en una forma legible, y el cálculo de 
# la transpuesta de la matriz. Asegúrate de que cada método tenga una única responsabilidad.

class Matriz():
    def __init__(self, elementos):
        self.elementos = elementos

class Transpuesta(Matriz):
    def __init__(self, elementos: list):
        super().__init__(elementos)

    def transpuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])

class Imprimir(Matriz):
    def __init__(self, elementos: list):
        super().__init__(elementos)

    def imprimir(self):
        for fila in self.elementos: 
        # Hacer recursiva para datos más grandes, no hacer bucle porque sino se peta
            print(fila)

m = Imprimir([[1, 2], [3, 4]])
m.imprimir()
print()
t = Transpuesta(m.elementos)
Imprimir(t.transpuesta().elementos).imprimir()
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
     
class Lanzador():
    # Creame un metodo que llame a la función imprimir y a la función transpuesta y me recoja los datos de la matriz con un input y un output.
    def __init__(self):
        self.elementos = []
        self.cantidad_filas = int(input("Introduce la cantidad de filas: "))
        self.cantidad_columnas = int(input("Introduce la cantidad de columnas: "))
        self.create_matrix()
        self.matriz = Matriz(self.elementos)
        self.transpuesta = Transpuesta(self.elementos)
        self.imprimir = Imprimir(self.elementos)
    
    def create_matrix(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f"Introduce el elemento {i+1},{j+1}: ")))
            self.elementos.append(fila)

    def lanzar(self):
        print('La matriz es: ')
        self.imprimir.imprimir()
        print('La matriz transpuesta es: ')
        transpuesta_result = self.transpuesta.transpuesta()
        imprimir_transpuesta = Imprimir(transpuesta_result.elementos)
        imprimir_transpuesta.imprimir()

class Main():
    def __init__(self):
        self.lanzar = Lanzador()
        self.lanzar.lanzar()

if __name__ == "__main__":
    Main()
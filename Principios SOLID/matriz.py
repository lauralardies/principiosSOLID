class Matriz():
    def __init__(self, elementos):
        self.elementos = elementos

    def imprimir(self):
        for fila in self.elementos:
            print(fila)

    def transpuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])
    
m = Matriz([[1, 2], [3, 4]])
m.imprimir()
print()
m_transpuesta = m.transpuesta()
m_transpuesta.imprimir()
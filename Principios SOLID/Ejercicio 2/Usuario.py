class Usuario():
    def __init__(self, nombre, apellido, dinero, direccion, telefono, email, password, n_pedidos):
        self.nombre = nombre
        self.apellido = apellido
        self.dinero = dinero
        self.direccion = direccion
        self.telefono = telefono
        self.email = email 
        self.password = password
        self.n_pedidos = n_pedidos
        
    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido} - Dinero: {self.dinero} - Pedidos: {self.n_pedidos}"
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dinero": self.dinero,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
            "password": self.password,
            "n_pedidos": self.n_pedidos
        }
class DataBaseManager():
    def __init__(self, connection_string):
        self.connection_string = connection_string

class Authenticator():
    # Para autenticar necesitamos un login y register.
    def __init__(self, user_database):
        self.user_database = user_database

class OrderManager():
    # Gestión de los pedidos.
    def __init__(self, api_key): # (api_key viene del Register)
        self.api_key = api_key

class PaymentProcessor():
    # Pagos.
    def __init__(self, database_manager, authenticator, payment_processor):
        self.database_manager = database_manager
        self.authenticator = authenticator
        self.payment_processor = payment_processor

# Recuerda hacer doctest!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


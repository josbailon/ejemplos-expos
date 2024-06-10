class Logger:
    def __init__(self, name):
        # Constructor de la clase Logger
        self.name = name  # Nombre del logger

    def log(self, message):
        # Método para registrar un mensaje en el log
        print(f"[{self.name}]: {message}")  # Imprime el mensaje con el nombre del logger

# Crear múltiples instancias de Logger
logger1 = Logger("Logger 1")  # Instancia 1 del Logger
logger2 = Logger("Logger 2")  # Instancia 2 del Logger

# Registrar mensajes en cada instancia
logger1.log("Mensaje 1 desde Logger 1")
logger2.log("Mensaje 2 desde Logger 2")

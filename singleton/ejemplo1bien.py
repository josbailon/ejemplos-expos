import threading

class Logger:
    _instance = None  # Instancia única del Logger
    _lock = threading.Lock()  # Lock para garantizar la seguridad en entornos multihilo

    def __new__(cls, *args, **kwargs):
        # Método para crear una nueva instancia si no existe una ya
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        # Constructor de la clase Logger
        self.logs = []  # Lista para almacenar los mensajes de log

    def log(self, message):
        # Método para registrar un mensaje en el log
        self.logs.append(message)  # Agrega el mensaje a la lista de logs
        print("[LOG]:", message)  # Imprime el mensaje en la consola

# Obtener la instancia única del Logger
logger1 = Logger()  # Instancia 1 del Logger
logger2 = Logger()  # Instancia 2 del Logger

# Registrar mensajes en la instancia única
logger1.log("Mensaje 1 desde Logger 1")
logger2.log("Mensaje 2 desde Logger 2")

# Verificar que logger1 y logger2 sean la misma instancia
print(logger1 is logger2)  # Devuelve True

from abc import ABC, abstractmethod

# Producto abstracto
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass


# Productos concretos
class Carro(Transporte):
    def entregar(self):
        print("Entrega por carretera en un carro.")


class Bicicleta(Transporte):
    def entregar(self):
        print("Entrega rápida en una bicicleta.")


class Barco(Transporte):
    def entregar(self):
        print("Entrega internacional por barco.")



# Creador abstracto
class TransporteFactory(ABC):
    @abstractmethod
    def crear_transporte(self):
        pass


# Creadores concretos
class CarroFactory(TransporteFactory):
    def crear_transporte(self):
        return Carro()


class BicicletaFactory(TransporteFactory):
    def crear_transporte(self):
        return Bicicleta()


class BarcoFactory(TransporteFactory):
    def crear_transporte(self):
        return Barco()


# Cliente
def realizar_entrega(factory: TransporteFactory):
    transporte = factory.crear_transporte()
    transporte.entregar()


# Ejecución
realizar_entrega(CarroFactory())
realizar_entrega(BicicletaFactory())
realizar_entrega(BarcoFactory())

#listo leido


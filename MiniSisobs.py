from abc import ABC, abstractmethod

# =======================
# PATRÓN OBSERVER
# =======================

class Sujeto:
    def __init__(self):
        self.observadores = []
        self.estado = None

    def agregar(self, observador):
        self.observadores.append(observador)

    def eliminar(self, observador):
        self.observadores.remove(observador)

    def notificar(self):
        for obs in self.observadores:
            obs.actualizar(self.estado)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"\n[Centro de control] Estado cambiado a: {nuevo_estado}")
        self.notificar()


class Observador(ABC):
    @abstractmethod
    def actualizar(self, estado):
        pass


# =======================
# PATRÓN FACTORY METHOD
# =======================

# Producto abstracto
class Transporte(Observador, ABC):
    @abstractmethod
    def entregar(self):
        pass


# Productos concretos
class Carro(Transporte):
    def entregar(self):
        print("🚗 Entrega por carretera en carro.")

    def actualizar(self, estado):
        print(f"🚗 El conductor del carro fue notificado: {estado}")


class Bicicleta(Transporte):
    def entregar(self):
        print("🚲 Entrega rápida en bicicleta.")

    def actualizar(self, estado):
        print(f"🚲 El repartidor en bicicleta fue notificado: {estado}")


class Barco(Transporte):
    def entregar(self):
        print("🚢 Entrega internacional por barco.")

    def actualizar(self, estado):
        print(f"🚢 El capitán del barco fue notificado: {estado}")


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


# =======================
# CÓDIGO CLIENTE
# =======================

def main():
    # Centro de control (sujeto observado)
    centro_control = Sujeto()

    # Fábricas de transporte
    fabrica_carro = CarroFactory()
    fabrica_bici = BicicletaFactory()
    fabrica_barco = BarcoFactory()

    # Crear transportes
    carro = fabrica_carro.crear_transporte()
    bici = fabrica_bici.crear_transporte()
    barco = fabrica_barco.crear_transporte()

    # Suscribir transportes al centro de control
    centro_control.agregar(carro)
    centro_control.agregar(bici)
    centro_control.agregar(barco)

    # Cada transporte realiza una entrega
    print("\n--- Iniciando entregas ---")
    carro.entregar()
    bici.entregar()
    barco.entregar()

    # Cambia el estado del sistema (y notifica)
    centro_control.cambiar_estado("⚠️ Alerta de tormenta en la zona costera")
    centro_control.cambiar_estado("✅ Clima despejado, entregas retomadas")

if __name__ == "__main__":
    main()
#listo leido tambien

class Observador:
  def actualizar(self, bateria):
    pass

class ObservadorTiempo(Observador):
  def actualizar(self, bateria):
    print("Tiempo restante de la batería:", bateria.tiempo)

class ObservadorCarga(Observador):
  def actualizar(self, bateria):
    print("Tanto por ciento de carga de la batería:", bateria.carga)

class Bateria:
  def __init__(self):
    self.conectado = False
    self.cargando = False
    self.carga = 0
    self.tiempo = 0
    self.observadores = []
  
  def registrar_observador(self, observador):
    self.observadores.append(observador)
  
  def notificar_observadores(self):
    for observador in self.observadores:
      observador.actualizar(self)


# Creamos una batería y registramos dos observadores en ella
bateria = Bateria()
observador_tiempo = ObservadorTiempo()
observador_carga = ObservadorCarga()
bateria.registrar_observador(observador_tiempo)
bateria.registrar_observador(observador_carga)

# Modificamos el estado de la batería y notificamos a los observadores
bateria.conectado = True
bateria.cargando = True
bateria.carga = 100
bateria.tiempo = 60
bateria.notificar_observadores()

import random
import pandas as pd

class Elemento:
  def __init__(self, umbral):
    self.conectado = False
    self.umbral = umbral

  def conectar(self):
    self.conectado = True

  def desconectar(self):
    self.conectado = False

  def medida(self):
    return 0.0

  def disparar_alarma(self):
    if self.conectado and self.medida() > self.umbral:
      print("¡Alarma disparada por el elemento", self, "!")

class DetectorHumo(Elemento):
  def medida(self):
    return random.random()

class SensorTemperatura(Elemento):
  def medida(self):
    return random.random() * 100

class SensorPresion(Elemento):
  def medida(self):
    return random.random() * 10

class ElementoCompuesto(Elemento):
  def __init__(self, umbral):
    super().__init__(umbral)
    self.elementos = []

  def agregar_elemento(self, elemento):
    self.elementos.append(elemento)

  def medida(self):
    medidas = [e.medida() for e in self.elementos]
    df = pd.DataFrame(medidas, columns=["medidas"])
    return df["medidas"].mean()

  def disparar_alarma(self):
    if self.conectado and self.medida() > self.umbral:
      print("¡Alarma disparada por el elemento compuesto", self, "!")

class SistemaAlarma:
  def __init__(self):
    self.elementos = []

  def agregar_elemento(self, elemento):
    self.elementos.append(elemento)

  def disparar_alarmas(self):
    for elemento in self.elementos:
      elemento.disparar_alarma()

# Creamos un sistema de alarma y agregamos varios elementos a él
sistema_alarma = SistemaAlarma()

detector_humo1 = DetectorHumo(0.5)
detector_humo1.conectar()
sistema_alarma.agregar_elemento(detector_humo1)

detector_humo2 = DetectorHumo(0.7)
detector_humo2.conectar()
sistema_alarma.agregar_elemento(detector_humo2)

sensor_temperatura1 = SensorTemperatura(50.0)
sensor_temperatura1.conectar()
sistema_alarma.agregar_elemento(sensor_temperatura1)

sensor_presion1 = SensorPresion(5.0)
sensor_presion1.conectar()
sistema_alarma.agregar_elemento(sensor_presion1)

# Creamos un elemento compuesto y agregamos varios elementos a él
elemento_compuesto = ElementoCompuesto(0.6)
elemento_compuesto.conectar()

detector_humo3 = DetectorHumo(0.5)
detector_humo3.conectar()
elemento_compuesto.agregar_elemento(detector_humo3)

sensor_temperatura2 = SensorTemperatura(50.0)
sensor_temperatura2.conectar()
elemento_compuesto.agregar_elemento(sensor_temperatura2)

sistema_alarma.agregar_elemento(elemento_compuesto)

# Disparamos las alarmas del sistema de alarma
sistema_alarma.disparar_alarmas()
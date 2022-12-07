class Base:
  def __init__(self, nombre, ambulancias, tiempo_medio_asistencia):
    self.nombre = nombre
    self.ambulancias = ambulancias
    self.tiempo_medio_asistencia = tiempo_medio_asistencia

class BaseCompuesta(Base):
  def __init__(self, nombre, bases):
    self.nombre = nombre
    self.bases = bases
    self.ambulancias = sum(base.ambulancias for base in bases)
    self.tiempo_medio_asistencia = sum(base.tiempo_medio_asistencia for base in bases) / len(bases)

  def agregar_base(self, base):
    self.bases.append(base)
    self.ambulancias += base.ambulancias
    self.tiempo_medio_asistencia = sum(base.tiempo_medio_asistencia for base in self.bases)

      
  def quitar_base(self, base):
    self.bases.remove(base)
    self.ambulancias -= base.ambulancias
    self.tiempo_medio_asistencia = sum(base.tiempo_medio_asistencia for base in self.bases) / len(self.bases)


# Creamos una base llamada "Medina del Campo" con 10 ambulancias y un tiempo medio de asistencia de 15 minutos
base_medina_del_campo = Base("Medina del Campo", 10, 15)

# Creamos una base llamada "Hospital Clínico Universitario" con 5 ambulancias y un tiempo medio de asistencia de 10 minutos
base_hospital_clinico = Base("Hospital Clínico Universitario", 5, 10)

# Creamos una unidad administrativa llamada "Valladolid" que agrupa a las bases "Medina del Campo" y "Hospital Clínico Universitario"
unidad_valladolid = BaseCompuesta("Valladolid", [base_medina_del_campo, base_hospital_clinico])

# Imprimimos los datos de la unidad administrativa "Valladolid"
print("Nombre de la base:", unidad_valladolid.nombre)
print("Número de ambulancias:", unidad_valladolid.ambulancias)
print("Tiempo medio de asistencia:", unidad_valladolid.tiempo_medio_asistencia)
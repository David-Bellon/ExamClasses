class Ordenador:
    def __init__(self, nombre_fabricante, modelo, precio_venta, componentes):
        self.nombre_fabricante = nombre_fabricante
        self.modelo = modelo
        self.precio_venta = precio_venta
        self.componentes = componentes

    def modificar_configuracion(self, accion, componente):
        if accion == "añadir":
            self.componentes.append(componente)
        elif accion == "quitar":
            self.componentes.remove(componente)
        elif accion == "cambiar":
            for i in range(len(self.componentes)):
                if isinstance(self.componentes[i], type(componente)):
                    self.componentes[i] = componente
                    break

    def precio_total(self):
        precio_total = self.precio_venta
        for componente in self.componentes:
            precio_total += componente.precio_venta
        return precio_total


class Componente:
    def __init__(self, nombre_fabricante, modelo, precio_venta):
        self.nombre_fabricante = nombre_fabricante
        self.modelo = modelo
        self.precio_venta = precio_venta


class UnidadCentral:
    def __init__(self, nombre_fabricante, modelo, precio_venta):
        self.nombre_fabricante = nombre_fabricante
        self.modelo = modelo
        self.precio_venta = precio_venta

class DispositivoEntrada(Componente):
    def __init__(self, nombre_fabricante, modelo, precio_venta, tipo_conector, puertos_validos):
        super().__init__(nombre_fabricante, modelo, precio_venta)
        self.tipo_conector = tipo_conector
        self.puertos_validos = puertos_validos


class Teclado(DispositivoEntrada):
    def __init__(self, nombre_fabricante, modelo, precio_venta, tipo_conector, puertos_validos):
        super().__init__(nombre_fabricante, modelo, precio_venta, tipo_conector, puertos_validos)


class Raton(DispositivoEntrada):
    def __init__(self, nombre_fabricante, modelo, precio_venta, tipo_conector, puertos_validos):
        super().__init__(nombre_fabricante, modelo, precio_venta, tipo_conector, puertos_validos)


class TabletaGrafica(DispositivoEntrada):
    def __init__(self, nombre_fabricante, modelo, precio_venta, tipo_conector, puertos_validos):
        super().__init__(nombre_fabricante, modelo, precio_venta, tipo_conector, puertos_validos)


class DispositivoSalida(Componente):
    def __init__(self, nombre_fabricante, modelo, precio_venta, puertos_validos):
        super().__init__(nombre_fabricante, modelo, precio_venta)
        self.puertos_validos = puertos_validos


class Pantalla(DispositivoSalida):
    def __init__(self, nombre_fabricante, modelo, precio_venta, puertos_validos):
        super().__init__(nombre_fabricante, modelo, precio_venta, puertos_validos)


class Impresora(DispositivoSalida):
    def __init__(self, nombre_fabricante, modelo, precio_venta, puertos_validos):
        super().__init__(nombre_fabricante, modelo, precio_venta, puertos_validos)


class ImpresoraLaser(Impresora):
    def __init__(self, nombre_fabricante, modelo, precio_venta, puertos_validos, tipo_cartucho, num_paginas_impresas):
        DispositivoSalida.__init__(self, nombre_fabricante, modelo, precio_venta, puertos_validos)
        super().__init__(nombre_fabricante, modelo, precio_venta, puertos_validos)
        self.tipo_cartucho = tipo_cartucho
        self.num_paginas_impresas = num_paginas_impresas


class PantallaTactil(DispositivoEntrada, DispositivoSalida):
    def __init__(self, nombre_fabricante, modelo, precio_venta, tipo_conector, puertos_validos):
        super().__init__(nombre_fabricante, modelo, precio_venta, tipo_conector, puertos_validos)

# Creamos una unidad central, un teclado y un ratón
uc = UnidadCentral("Intel", "i7-9700K", 300)
teclado = Teclado("Logitech", "K120", 20, "USB", [1, 2])
raton = Raton("Logitech", "M185", 15, "USB", [1])

# Creamos una pantalla y una impresora láser
pantalla = Pantalla("LG", "24MK400H-B", 100, [1])
impresora = ImpresoraLaser("HP", "LaserJet Pro MFP M477fdw", 300, [1], "CF410A", 0)

# Creamos un ordenador con una unidad central, un teclado, un ratón, una pantalla y una impresora láser
ordenador = Ordenador(uc, teclado, raton, pantalla, impresora)

# Mostramos el precio total del ordenador
print(ordenador.precio_total())  # Debería mostrar 735

# Añadimos una tableta gráfica al ordenador
tableta = TabletaGrafica("Wacom", "Intuos S", 80, "USB-C", [1, 2])
ordenador.anadir_componente(tableta)

# Mostramos el precio total del ordenador
print(ordenador.precio_total())  # Debería mostrar 815

# Quitamos el teclado del ordenador
ordenador.quitar_componente(teclado)

# Mostramos el precio total del ordenador
print(ordenador.precio_total())  # Debería mostrar 795

# Cambiamos la unidad central del ordenador
nueva_uc = UnidadCentral("AMD", "Ryzen 5 3600", 200)
ordenador.cambiar_componente(nueva_uc)

# Mostramos el precio total del ordenador
print(ordenador.precio_total())  # Debería mostrar 975
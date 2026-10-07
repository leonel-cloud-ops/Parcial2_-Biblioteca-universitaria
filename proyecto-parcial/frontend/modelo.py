class MaterialBiblioteca:
    def __init__(self, titulo, codigo, disponibilidad=True):
        self.titulo = titulo
        self.codigo = codigo
        self.disponibilidad = disponibilidad

    def calcular_dias_prestamo(self):
        return 0

    def mostrar_informacion(self):
        return f"Código: {self.codigo} | Título: {self.titulo}"


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, codigo, autor):
        super().__init__(titulo, codigo)
        self.autor = autor

    def calcular_dias_prestamo(self):
        return 7

    def mostrar_informacion(self):
        return f"Libro: {self.titulo} | Autor: {self.autor} | Días: {self.calcular_dias_prestamo()}"


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, codigo, numero_edicion):
        super().__init__(titulo, codigo)
        self.numero_edicion = numero_edicion

    def calcular_dias_prestamo(self):
        return 3

    def mostrar_informacion(self):
        return f"Revista: {self.titulo} | Edición: N°{self.numero_edicion} | Días: {self.calcular_dias_prestamo()}"
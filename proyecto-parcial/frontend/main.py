from modelo import Libro,Revista

libro1 = Libro("Cien años de soledad", "L-001", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "L-002", "Miguel de Cervantes")

revista1 = Revista("National Geographic", "R-101", 345)
revista2 = Revista("Scientific American", "R-102", 521)

inventario_biblioteca = [libro1, libro2, revista1, revista2]

print("=== RECORRIDO DEL INVENTARIO ===")
print()



for material in inventario_biblioteca:
    print(material.mostrar_informacion())
    print("-" * 100)
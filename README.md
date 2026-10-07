 Sistema de Gestión de Biblioteca Universitaria

## Nombre del Equipo
** Equipo 5

---

## Integrantes
 ** Andrade Gómez, Henry Abdiel
 ** Acevedo Villacorta, Jose Leonel
 ** Portillo Rivera, Mario Antonio
 ** Avelar Rivera, Edgar Alexander
 ** Cardoza Chiquillo, Jasson Wilfredo  

---

## Escenario Seleccionado "A"
Demostración de Sistema de Préstamo de Recursos para Biblioteca Universitaria.

El proyecto simula el catálogo y flujo de préstamos de una biblioteca académica que gestiona dos categorías principales de materiales: *Libros* y *Revistas*, diferenciando sus reglas de préstamo según sus características técnicas.

---

## Descripción de la Solución Desarrollada
Se diseñó un sistema híbrido compuesto por una simulación de lógica orientada a objetos en Python y un prototipo de interfaz gráfica web. La solución permite estructurar, organizar y visualizar el catálogo de materiales de una biblioteca, aplicando reglas de préstamo diferenciadas según el tipo de recurso (*Libro* o *Revista*).

---

## Arquitectura POO en Python

### 1. Clase Padre y Clases Hijas
* **Clase Padre (`MaterialBiblioteca`):** Contiene los atributos generales de cualquier recurso de la biblioteca (`titulo`, `codigo`, `disponible`) y define los métodos base `mostrar_informacion()` y `calcular_dias_prestamo()`.
* **Clase Hija (`Libro`):** Hereda de `MaterialBiblioteca` e incluye el atributo específico `autor`.
* **Clase Hija (`Revista`):** Hereda de `MaterialBiblioteca` e incluye el atributo específico `numero_edicion`.

### 2. Método Sobrescrito
Se sobrescribieron dos métodos principales en las clases hijas:
1. `calcular_dias_prestamo()`:
   * En `Libro` devuelve **7 días**.
   * En `Revista` devuelve **3 días**.
2. `mostrar_informacion()`: Redefine la salida en pantalla para incluir los detalles específicos de cada tipo de material junto con sus días de préstamo correspondientes.

### 3. Explicación de cómo se aplica el Polimorfismo
El **polimorfismo** se aplica al almacenar instancias de distintas clases (`Libro` y `Revista`) dentro de una misma colección o lista (`catalogo`). Al iterar esta lista en un solo bucle (`for material in catalogo:`), el sistema invoca el método `mostrar_informacion()` en cada objeto sin necesidad de verificar previamente si es un libro o una revista; Python detecta dinámicamente el tipo de objeto y ejecuta la versión del método que corresponde a su clase específica.

---

## Función de HTML, CSS y JavaScript dentro de la Solución

* **HTML (Estructura):** Proporciona la maquetación base del portal web, definiendo la cabecera, los contenedores del catálogo, las tarjetas informativas para cada material y los botones de solicitud.
* **CSS (Presentación y Estilo):** Aplica un diseño visual (*Grid Layout*), estilos de tipografía, colores de estado (*Disponible/No disponible*) y tarjetas (*cards*) para presentar los materiales de forma clara, profesional y fácil de leer.
* **JavaScript (Interactividad):** Captura el evento de clic sobre los botones de préstamo para evaluar la disponibilidad y despliega una ventana emergente (*alert*) indicando la confirmación de la solicitud con el límite de días según el tipo de recurso.

---

## Distribución de Responsabilidades (Frontend vs. Backend)

### Responsabilidades del Frontend
* Presentar la interfaz gráfica al usuario de manera clara, visual y adaptable (responsive).
* Capturar las interacciones de los estudiantes o usuarios (clics en botones, selección de materiales).
* Mostrar alertas, mensajes emergentes y cambios visuales inmediatos de disponibilidad.
* Enviar solicitudes de datos hacia el servidor y renderizar la información recibida.

### Responsabilidades del Backend
* Gestionar la lógica de negocio central (reglas de préstamos, cálculo de fechas de devolución y penalizaciones).
* Mantener la persistencia de los datos consultando y actualizando una base de datos real (almacenar libros, revistas y registros de usuarios).
* Validar la autenticación de los usuarios y verificar si tienen préstamos pendientes o multas antes de autorizar un nuevo recurso.
* Procesar las operaciones POO de forma segura en el servidor y exponerlas mediante un servicio API REST hacia el frontend.

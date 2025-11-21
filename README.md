# Caso Práctico: **Luces y Sombras del Uso de LLMs en el Mantenimiento del Software**

Bienvenido al caso práctico donde exploraremos cómo los **Modelos de Lenguaje (LLMs)** pueden ayudar y a veces dificultar el **mantenimiento de software**.

## 🧩 Escenario

Imagina la siguiente situación:

> *Sois nuevos trabajadores en una gran empresa que os ha contratado hace unos meses. Tras un periodo de adaptación al estilo de trabajo, se os asigna vuestra primera gran tarea individual: entender un código en Python desarrollado por un antiguo empleado que ya no está en la empresa. Este código es fundamental para el próximo proyecto, y vuestro jefe quiere que lo entendáis, lo analicéis y realicéis las modificaciones necesarias, ya que la semana que viene deberéis presentarlo a vuestros superiores.*

Por suerte, vuestros “ángeles de la guarda”, **David y Adrián**, os guiarán para que vuestro jefe no os despida y podáis conservar este trabajo que tanto esfuerzo os costó conseguir. Utilizaremos una IA que nos ayudará a detectar errores y mejorar la legibilidad del código.

La herramienta seleccionada es **Codium**, una plataforma de revisión de código con IA que detecta errores y propone mejoras para mantener la calidad.

A continuación se detallan los pasos previos, los pasos principales y las tareas necesarias para superar la práctica y entregar el mejor resultado posible.

---

# 🛠️ Pasos Previos

Aseguraos de tener lo siguiente:

- Visual Studio Code instalado.
- Python 3 instalado. Si no lo tenéis, podéis descargarlo desde:  
  https://www.python.org/downloads/
- Extensión **Qodo** (icono de oso hormiguero) instalada en VSCode.
- Haber **forkeado** este repositorio:  
  https://github.com/davidabuinESI/LucesySombrasMantenimientoLLM.git  
  Añadiéndole vuestro nombre.
- Haber clonado vuestro repositorio forkeado para obtener los archivos **`app.py`** y **`app_test.py`**.

---

# 📋 Pasos a Seguir

1. Abrir el repositorio clonado en VSCode.
2. Crear un archivo Markdown llamado **`AnalisisNombre.md`**, reemplazando *Nombre* por el vuestro.
3. Realizar un **análisis individual** del archivo `app.py`.  
   En vuestro Markdown deberéis anotar los cambios y mejoras que aplicaríais al código.
4. Ejecutar los tests y **apuntar el resultado**.  
   Para ello, basta con ejecutar el archivo `app_test.py`.
5. Abrir el chat de Qodo e insertar el siguiente mensaje (en inglés, para obtener mejores resultados):

    Refactor this code to make it clean, use descriptive variable names, add Type Hints and docstrings. Refactor and improve this code in a new file called "RefactoringName.py".
*(cambiar "Name" por vuestro nombre)*

6. Comparar `app.py` con `RefactoringName.py`.  
Debéis observar las diferencias entre vuestras ideas y las modificaciones propuestas por la IA.
7. Añadir a vuestro Markdown las principales diferencias encontradas entre vuestro análisis y la refactorización de la IA.
8. Ejecutar nuevamente el test.  
- ¿Habéis obtenido el mismo resultado?  
- Si no, ¿a qué se debe?  
Responded a estas preguntas en el Markdown.
9. Revisar el código refactorizado por la IA e intentar detectar:
- Modificaciones innecesarias  
- Introducción de bugs lógicos  
- Deuda técnica añadida por la refactorización  
10. Subir a vuestro repositorio forkeado:
 - El archivo Markdown  
 - El archivo generado por la IA (**`RefactoringName.py`**)

---

# 📦 Archivos a Entregar

- Archivo Python **`RefactoringName.py`** generado por la IA.
- Archivo Markdown **`AnalisisNombre.md`** con análisis, respuestas y comparaciones.
- En la entrega del campus:

      - Enlace a vuestro repositorio forkeado (en los comentarios)
      - El archivo Markdown creado.

---

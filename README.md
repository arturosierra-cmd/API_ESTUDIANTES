# API de Estudiantes 📚
Este repositorio contiene una API REST desarrollada en Flask para gestionar información básica de estudiantes. La API permite realizar operaciones CRUD, como crear, listar y actualizar estudiantes en una base de datos simulada en memoria.

Funcionalidades
Crear estudiante: Permite agregar un nuevo estudiante proporcionando nombre y edad.
Listar estudiantes: Recupera la lista completa de estudiantes registrados.
Endpoint de bienvenida: Muestra un mensaje de bienvenida en la raíz de la API.
Estructura del Proyecto
app.py: Archivo principal que contiene los endpoints de la API.
requirements.txt: Lista de dependencias necesarias para ejecutar la API.
test/: Carpeta que contiene pruebas unitarias para los endpoints de la API.
Requisitos
Python 3.6 o superior
Flask
Pylint y Pytest para pruebas y análisis de código
Ejecución
Clonar el repositorio.
Crear un entorno virtual y activar.
Instalar las dependencias: pip install -r requirements.txt
Ejecutar la API: python app.py
Acceder a http://127.0.0.1:5000 para probar los endpoints.
Integración Continua
Este repositorio incluye un archivo Jenkinsfile para la integración continua, que se activa automáticamente con cada git push. Las etapas del pipeline incluyen:

Instalación de dependencias
Análisis de código con Pylint
Ejecución de pruebas unitarias con Pytest

### By: GILBERTO ARTURO SIERRA RAX

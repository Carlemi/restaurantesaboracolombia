# Tiendita Sabor a colombia
***
Este es un proyecto, donde el backend está basado en el libro Django 4 by example de Antonio Melé
Hemos implementado en su mayoría código escrito del libro, es un proyecto django, el cual está sujeto a mejorar con el paso del tiempo, debido a que la tecnología es escalable y robusta.

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
5. [FAQs](#faqs)

1. Tenemos el backend del proyecto, creado con Django tradicional, en su versión 4.2 para poder tener compatibilidad con algunas dependencias utilizadas en el proyecto, debido a que como la última versión de Django está reciente, puede que le faltara algún soporte a algunas dependencias, es una tienda online, que permite seleccionar los productos, tiene varias categorías de productos, los cuales agregas a un carrito el cual te permite, seguir comprando o realizar el pago, o añadir más al stock del mismo producto, eliminarlo.

2. las tecnologías utilizadas, son Python 3.12
Django 4.2 para el backend, para el manejo de la base de datos, por ahora lo utilizaremos con el manejador por defecto que trae django que es Sqlite3, más adelanta a medida que crezca la base de datos, migraremos a postgres, para el front por el momento utilizamos HTML5, CSS3 y Jinja2 que es el motor de plantillas de Django.

3. clonar el repositorio, generar un directorio donde utilizarlo, crear un entorno virtual, instalar la versión de Django, generar el ficher requirement.txt para las dependencias, ejecutar python manage.py runserver (para tener en cuenta, el proyecto aún no está alojado en un servidor, por lo tanto dentro de las dependencias, manejamos tecnologías para tareas asíncronas, las cuales son rabbitmq, celery con flower para la interfaz gráfica de los mensajes, stripe para el sistema de pagos, son dependencias que hay que instalar y configurar dependiendo del entorno en el que se trabaje, ya sea linux, Mac, o windows.)
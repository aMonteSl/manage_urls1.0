## Descarga de Documentos Web

Este repositorio contiene un conjunto de clases y programas en Python diseñados para facilitar la descarga y gestión de documentos web. 

#### Clases

1. **Clase Robot**: Esta clase proporciona un "robot" capaz de descargar y mostrar documentos web. Cumple con las siguientes especificaciones:
   - Se instancia con la URL del documento web como argumento.
   - Método `retrieve`: Descarga el documento de la URL especificada si aún no ha sido descargado. Muestra un mensaje en pantalla indicando que se está descargando.
   - Método `show`: Muestra en pantalla el contenido del documento descargado, utilizando `retrieve` si es necesario.
   - Método `content`: Devuelve el contenido del documento descargado como una cadena de caracteres.

2. **Clase Cache**: Esta clase proporciona una cache de documentos y cumple con las siguientes especificaciones:
   - No acepta argumentos para la instanciación.
   - Método `retrieve`: Descarga el documento correspondiente a la URL especificada si aún no ha sido descargado.
   - Método `show`: Muestra en pantalla el contenido del documento correspondiente a la URL especificada, utilizando `retrieve` si es necesario.
   - Método `show_all`: Muestra un listado de todas las URLs cuyos documentos se han descargado.
   - Método `content`: Devuelve el contenido del documento correspondiente a la URL especificada, utilizando `retrieve` si es necesario.

#### Recursos

- Se recomienda el uso del módulo estándar de Python `urllib.request` para la descarga de documentos.
- [Documentación del módulo urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [Ejemplos del módulo urllib.request](https://docs.python.org/3/library/urllib.request.html#examples)

#### Programa Principal

El programa principal crea al menos dos objetos de la clase `Robot`, llama a varios de sus métodos, y crea al menos dos objetos de la clase `Cache`, llamando también a varios de sus métodos para demostrar su funcionamiento.


## Descarga de Documentos Web con Módulos

#### Enunciado

Este ejercicio requiere la implementación de un programa con la misma funcionalidad que "Descarga de documentos web" (ejercicio 16.9), pero usando módulos separados para la clase `Robot` y la clase `Cache`. El programa principal, que será otro archivo, implementará la misma funcionalidad de prueba de las clases.




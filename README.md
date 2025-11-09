# Patrones de diseño

https://refactoring.guru/es/design-patterns/catalog

## Patrones Creacionales

Son patrones que proporcionan mecanismos de creación de objetos que ayudan a tener mayor flexibilidad y reutilización de código.

### Singleton

* Este patron se puede utilizar para la gestión de recursos compartidos, por ejemplo se pueden utilizar para controlar la creación de instancias que se conectan a bases de datos.

* Permite asegurar de que una clase tenga una unica instancia, por lo que proporciona un punto de acceso global a dicha instancia.


### Factory Method

* Este patron proporciona una interfaz para crear objetos en una superclase.

* La idea es desacoplar el código de productos concretos de los creadores, por ejemplo para la implementación de un RAG, en la fase de indexación de documentos, podemos tener multiples tipos de documentos, donde podemos tener diferente lógica, por ejemplo, una lógica para procesar pdfs, otra para imagenes, otra para exceles, etc. a esto se le llaman productos. Luego tenemos una superclase creadora. Esto permite que el código cliente solo conozca la superclase creadora y no directamente las clases concretas de cada producto.
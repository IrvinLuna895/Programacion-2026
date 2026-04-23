En esta versión se mejora el diseño separando responsabilidades entre Entidad y Contacto. La clase Cuenta ahora solo valida datos mediante condicionales y devuelve valores booleanos, sin imprimir mensajes. La clase Menu interpreta esos resultados y se encarga de toda la interacción con el usuario.

Este cambio evita mezclar lógica de negocio con presentación, logrando un código más limpio, modular y acorde a principios básicos de diseño.

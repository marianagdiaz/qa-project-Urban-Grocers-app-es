# Pruebas de Creación de Kit de Producto

Este proyecto realiza pruebas para verificar la creación de kits de productos a través de una API. Utiliza `requests` para interactuar con el servicio web y `pytest` para ejecutar las pruebas automatizadas.

## Estructura del Proyecto

El proyecto contiene tres archivos principales:

1. **`sender_stand_request.py`**: Contiene las funciones que interactúan con la API para crear un usuario y crear kits.
2. **`data.py`**: Contiene los datos de configuración como el cuerpo de las solicitudes y los encabezados.
3. **`test_create_kit.py`**: Contiene las pruebas para la creación de kits, tanto positivas como negativas.

## Archivos del Proyecto

### `sender_stand_request.py`

Este archivo define las funciones para enviar solicitudes a la API, incluida la creación de un nuevo usuario y la creación de kits de productos.

* post_new_user: Envía una solicitud POST para crear un nuevo usuario y obtiene un auth_token necesario para las solicitudes posteriores.
* post_new_client_kit: Envía una solicitud POST para crear un nuevo kit, utilizando el auth_token obtenido al crear el usuario.
data.py
Este archivo contiene las configuraciones y los datos utilizados para las solicitudes.


### `data.py`
Este archivo contiene las configuraciones y los datos utilizados para las solicitudes.

* `header`: Contiene los encabezados necesarios para la autenticación y el tipo de contenido. 
* `kit_body`: Define la estructura básica del cuerpo de solicitud para crear un nuevo kit.
* `user_body`: Define la estructura básica del cuerpo de solicitud para crear un nuevo usuario.

### `test_create_kit.py`
Este archivo contiene las pruebas para verificar la creación de kits de productos. Las pruebas cubren tanto casos positivos como negativos.

Casos positivos: Verifican la creación exitosa de un kit con diferentes tipos de nombre (de una sola letra, con caracteres especiales, con espacio, etc.).
Casos negativos: Verifican que se produzcan errores de validación cuando el nombre del kit no cumple con los requisitos (vacío, demasiado largo, solo números, etc.).

### `Ejecución de las pruebas`
Para ejecutar todas las pruebas, usa pytest. Asegúrate de tener el entorno adecuado y los archivos de configuración correctamente definidos:


*pytest*

Este comando ejecutará todas las pruebas definidas en test_create_kit.py, verificando la correcta creación de los kits según los diferentes escenarios.

### **Notas**

* El archivo configuration.py debe contener las URL y rutas necesarias para las solicitudes.
* Las respuestas de la API deben estar bien configuradas para devolver un auth_token que permita realizar las solicitudes subsecuentes.
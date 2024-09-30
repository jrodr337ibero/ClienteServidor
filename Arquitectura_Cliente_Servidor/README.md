Esta aplicación demuestra cómo implementar una arquitectura cliente-servidor simple usando Python y Flask


- Python 3.x
- Flask (`pip install Flask`)
- Requests (`pip install requests`)


client.py  Cliente que se comunica con el servidor
server.py  Servidor basado en Flask

1. Servidor

El archivo `server.py` contiene la clase `Server`, que define el servidor utilizando Flask. El servidor expone dos rutas principales:

Ruta `/saludo` (GET): Devuelve un saludo personalizado.
Ruta `/data` (POST): Recibe datos del cliente y responde con un mensaje indicando que los datos fueron recibidos correctamente.

Para iniciar el servidor, ejecuta el siguiente comando en tu terminal:
python server.py

El archivo client.py contiene la clase Client, que permite interactuar con el servidor haciendo solicitudes GET y POST.

Saludar (GET):

El cliente puede enviar una solicitud al servidor para recibir un saludo personalizado.

Esto hará una solicitud a http://127.0.0.1:5000/saludar y devolverá un mensaje de saludo en formato JSON:

El cliente puede enviar datos JSON al servidor y recibir una confirmación de que los datos fueron recibidos correctamente.

Esto hará una solicitud POST a http://127.0.0.1:5000/data y devolverá la siguiente respuesta JSON:


Después de iniciar el servidor, puedes ejecutar el cliente usando el siguiente comando:

python client.py

El cliente enviará una solicitud GET para saludar y una solicitud POST para enviar datos, mostrando las respuestas en la terminal.
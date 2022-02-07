# El juego de la vida
Hola! Esta es mi versión del juego de la vida de John Horton Conway, para poder jugar a él es muy sencillo y solo debes serguir estos pasos:

>1. Crear un entorno virtual introduciendo el siguiente comando en la terminal ```python -m venv venv```
>2. Abrir el entorno virtual con los siguientes comandos: para Windows ```venv\Scripts\activate``` o para MAC ```venv\bin\activate```
>3. Introducir el siguiente comando en la terminal: pip install requirements.txt
>4. Luego de haber preparado tu equipo, ejecuta el script main.py y comienza a jugar

### Reglas
Las reglas del juego son las siguientes:
- Si una célula está viva y tiene dos o tres vecinas vivas, sobrevive. 
- Si una célula está muerta y tiene tres vecinas vivas, renace. 
- Si una célula está viva y tiene más de tres vecinas vivas, muere.

Puedes usar el click para dar via a una célula, usar la barra espacio para pausar el juego y la tecla del número 0 para cerrar la ventana.

Si quieres añadir más entidades o modificar alguna al inicio solo debes hacerlo en el ```__init__``` del fichero escenas.py.

Espero que lo disfrutes!

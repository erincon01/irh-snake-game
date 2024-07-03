# my fist game: Snake Game

## Descripción

he creado esta aplicación con propósito de aprendizaje.
cada directorio tendrá una versión funcional con su propio propósito.

## Estructura

Descripción de que se hace en cada archivo:
- main.py

    - se llama a la función config_loader para cargar desde config.ini la configuración.
    - se crean llama a la función que crea los objetos (en archivo object_creator.py)
    - se crea el gestor de eventos (desde el archivo event_handler.py)
    - se inicia la aplicación.

- config_loader.py

Este archivo tiene la definición del objeto/clase Config.
El objeto tiene las variables de configuración del juego.
Revisa el archivo ocnfig_loader.py; algunas de las variables que tiene son:

    - self.width = 800
    - self.height = 600
    - self.title = 'Pyglet Game'
    - self.movement = 5
    - self.object_size = 50
    - self.direction = 'right'

- event_handler.py
- object_creator.py
- config.ini


## dependencies

https://pyglet.readthedocs.io/en/latest/programming_guide/quickstart.html
pip install pyglet

not used:
pip install arcade pyinstaller
https://www.pygame.org/news

learning references:
https://geekflare.com/python-game-development-libraries-frameworks/

s
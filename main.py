import pyglet
from config_loader import Config
from event_handler import EventHandler
from object_creator import create_objects

# Definir la variable global config
config = Config()

def main():
    # Cargar configuración desde el archivo
    config.load_config('config.ini')

    # Crear ventana
    window = pyglet.window.Window(width=config.width, height=config.height, caption=config.title)

    pyglet.gl.glClearColor(0.0, 0.0, 0.2, 1.0)    

    # Crear objetos del juego
    objects = create_objects(config)
    
    # Crear manejador de eventos
    event_handler = EventHandler(window, objects, config)

    # Registrar eventos
    window.push_handlers(event_handler)
    
    # Registrar la función de actualización
    pyglet.clock.schedule_interval(event_handler.update, 1/60.0)  # Actualiza 60 veces por segundo

    # Iniciar la aplicación Pyglet
    pyglet.app.run()

if __name__ == '__main__':
    main()

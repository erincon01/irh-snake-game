import pyglet
from config_loader import Config
from event_handler import EventHandler
from object_creator import create_objects

def main():
    # Cargar configuración desde el archivo
    config = Config()
    config.load_config('.\\lab1\config.ini')

    # Crear ventana
    window = pyglet.window.Window(width=config.width, 
                                  height=config.height, 
                                  caption=config.title)
    
    # Establecer el color de fondo de la ventana en azul oscuro
    pyglet.gl.glClearColor(0.1, 0.1, 0.3, 1.0)
    
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

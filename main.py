import configparser
import pyglet
from pyglet import shapes

# Inicializar y leer el archivo de configuración
config = configparser.ConfigParser()
config.read('config.ini')

# Cargar valores de configuración
width = config['SCREEN']['width']
height = config['SCREEN']['height']
title = config['SCREEN']['title']

# Crear la ventana de Pyglet
window = pyglet.window.Window(width=int(width), height=int(height), 
                              caption=title, resizable=False)

# Crear la etiqueta de texto
label = pyglet.text.Label('circulo',
                          font_name='Times New Roman',
                          font_size=12,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')

# Crear un batch para optimizar el renderizado
batch = pyglet.graphics.Batch()

# Crear un círculo rojo
circle_size = 100
circle = shapes.Circle(x=window.width // 2,
                       y=window.height // 2,
                       radius=circle_size // 2,
                       color=(255, 0, 0), batch=batch)

# Definir el evento on_draw
@window.event
def on_draw():
    window.clear()
    pyglet.gl.glClearColor(0.5, 0.5, 1, 1)
    batch.draw()
    label.draw()

# Definir el evento on_key_press para manejar las teclas presionadas
@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.RIGHT:
        circle.x += 25
        label.x += 25
    elif symbol == pyglet.window.key.LEFT:
        circle.x -= 25
        label.x -= 25
    elif symbol == pyglet.window.key.UP:
        circle.y += 25
        label.y += 25
    elif symbol == pyglet.window.key.DOWN:
        circle.y -= 25
        label.y -= 25

# Ejecutar la aplicación
pyglet.app.run()

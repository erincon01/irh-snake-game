import configparser
import pyglet
from pyglet import shapes, window
import pyglet.clock as clock

# Inicializar y leer el archivo de configuración
config = configparser.ConfigParser()
config.read('config.ini')

# Cargar valores de configuración
width = config['Configuracion Pantalla']['width']
heigh = config['Configuracion Pantalla']['height']
title = config['Configuracion Pantalla']['title']
movement = config['Configuracion Pantalla']['movement']
circle_size = config['Configuracion Pantalla']['circle_size']
# Convertir valores a enteros
width = int(width)
heigh = int(heigh)
movement = int(movement)
circle_size = int(circle_size)
direction = "right"

# Crear la ventana de Pyglet
window = window.Window(width=width, height=heigh, 
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
circle_size = circle_size
circle = shapes.Circle(x=window.width // 2,
                       y=window.height // 2,
                       radius=circle_size // 2,
                       color=(255, 0, 0), batch=batch)

# Crear un rectángulo amarillo
rectangle = shapes.Rectangle(x=0, y=0, width=window.width, height=50, color=(255, 255, 0), batch=batch)

# crea un rombo verde
diamond = shapes.Rectangle(x=0, y=0, width=window.width, height=50, color=(0, 255, 0), batch=batch)

def callback(dt):
    global direction
    if direction == "right":
        circle.x += movement
        label.x += movement
        # if circle.x > window.width:
        #     circle.x = 0
        #     label.x = 0
        #     direction = "down"
    elif direction == "down":
        circle.y -= movement
        label.y -= movement
        # if circle.y < 0:
        #     circle.y = window.height
        #     label.y = window.height
        #     direction = "left"
    elif direction == "left":
        circle.x -= movement
        label.x -= movement
        # if circle.x < 0:
        #     circle.x = window.width
        #     label.x = window.width
        #     direction = "up"
    elif direction == "up":
        circle.y += movement
        label.y += movement
        # if circle.y > window.height:
        #     circle.y = 0
        #     label.y = 0
        #     direction = "right"

clock.schedule_interval(callback, 0.5)

# Definir el evento on_draw
@window.event
def on_draw():
    window.clear()
    pyglet.gl.glClearColor(0.5, 0.5, 1, 1)
    batch.draw()
    label.draw()
    rectangle.draw()
    diamond.draw()

# función que indica que hacer cuando se presiona una tecla
@window.event
def on_key_press(symbol, modifiers):
    global direction
    global movement
    if symbol == pyglet.window.key.RIGHT:
        if direction == "right":
            movement += 10
        direction = "right"
    elif symbol == pyglet.window.key.LEFT:
        if direction == "left":
            movement += 10
        direction = "left"
    elif symbol == pyglet.window.key.UP:
        if direction == "up":
            movement += 10
        direction = "up"
    elif symbol == pyglet.window.key.DOWN:
        if direction == "down":
            movement += 10
        direction = "down"

# @window.event
# def on_mouse_motion(x, y, dx, dy):
#     # Actualizar la posición del círculo a las coordenadas del mouse
#     circle.x = x
#     circle.y = y
#     # Actualizar la posición del rectángulo a las coordenadas del mouse
#     rectangle.x = x
#     rectangle.y = y

# Ejecutar la aplicación
pyglet.app.run()


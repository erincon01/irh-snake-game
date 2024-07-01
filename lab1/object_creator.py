import pyglet
import random 

def create_objects(config):
    """
    Crea los objetos del juego basados en la configuración.

    :param config: Instancia de Config con la configuración.
    :return: Diccionario con los objetos del juego.
    """
    objects = {}

    # Crear una etiqueta de texto
    label_1 = pyglet.text.Label(
        str(config.objects_count),
        font_name='Times New Roman',
        font_size=12,
        x=10, y=10,
        anchor_x='left', anchor_y='bottom',
        color=(255, 0, 0, 255)
    )

    x_random = random.randint(0, config.width)
    y_random = random.randint(0, config.height)

    # Crear un círculo rojo en el centro
    square_1 = pyglet.shapes.Rectangle(
        x = x_random, y = y_random,
        width=config.object_size, height=config.object_size,
        color=(255, 0, 0)
    )
    square_1.direction = "right"  # Establecer dirección inicial

    x_random = random.randint(0, config.width)
    y_random = random.randint(0, config.height)

     # Crear un círculo amarillo en la esquina izquierda
    square_2 = pyglet.shapes.Rectangle(
        x = x_random, y = y_random,
        width=config.object_size, height=config.object_size,
        color=(255, 255, 0)
    )
    square_2.direction = "up"  # Establecer dirección inicial

    objects['label'] = label_1
    objects['temp_square_1'] = square_1
    objects['temp_square_2'] = square_2

# crea 100 cuadrados de colores aleatorios, y los añade al diccionario de objetos, y los pones en ubicaciones aleatorioas utilizando el método random de antes
    for i in range(config.objects_count):
        x_random = random.randint(0, config.width)
        y_random = random.randint(0, config.height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        square = pyglet.shapes.Rectangle(
            x=x_random, y=y_random,
            width=config.object_size, height=config.object_size,
            color=color
        )

# añadir un label en la misma posición con el número de índice del cuadrado
        label = pyglet.text.Label(
            str(i),
            font_name='Times New Roman',
            font_size=12,
            x=x_random, y=y_random,
            anchor_x='left', anchor_y='bottom',
            color=(255, 255, 255, 255)
        )
        square.direction = random.choice(["up", "down", "left", "right"])
        label.direction = square.direction
        objects[f'square_{i}'] = square
        objects[f'label_{i}'] = label

    return objects

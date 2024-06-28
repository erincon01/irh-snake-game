import pyglet

def create_objects(config):
    """
    Crea los objetos del juego basados en la configuración.

    :param config: Instancia de Config con la configuración.
    :return: Lista de objetos del juego.
    """
    objects = []
    # Crear objetos según la configuración
    label = pyglet.text.Label(
        "-",
        font_name='Times New Roman',
        font_size=12,
        x=config.width // 2, y=config.height // 2,
        anchor_x='center', anchor_y='center'
    )

# crear un circulo rojo en el centro
    circle = pyglet.shapes.Circle(
        x=config.width // 2, y=config.height // 2,
        radius=config.circle_size, color=(255, 0, 0)
    )

    objects.append(label)
    objects.append(circle)

    return objects

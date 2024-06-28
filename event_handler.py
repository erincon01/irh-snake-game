import pyglet

class EventHandler:
    def __init__(self, window, objects, config):
        self.window = window
        self.objects = objects
        self.config = config
        self.movement = config.movement
        self.direction = config.direction
        # Inicializar posiciones
        self.x = config.width // 2
        self.y = config.height // 2

    def on_draw(self):
        self.window.clear()
        for obj in self.objects:
            obj.draw()

    def on_key_press(self, symbol, modifiers):
        # Manejar eventos de teclado usando self.config
        if symbol == pyglet.window.key.RIGHT:
            self.direction = "right"
        elif symbol == pyglet.window.key.LEFT:
            self.direction = "left"
        elif symbol == pyglet.window.key.UP:
            self.direction = "up"
        elif symbol == pyglet.window.key.DOWN:
            self.direction = "down"

        # Actualizar la configuración global
        self.config.direction = self.direction

    def update(self, dt):
        if self.direction == "right":
            self.x += self.movement * dt
        elif self.direction == "left":
            self.x -= self.movement * dt
        elif self.direction == "up":
            self.y += self.movement * dt
        elif self.direction == "down":
            self.y -= self.movement * dt

        # Asegurarse de que los objetos se actualizan con la nueva posición
        for obj in self.objects:
            if isinstance(obj, pyglet.text.Label):
                obj.x = self.x
                obj.y = self.y
            elif isinstance(obj, pyglet.shapes.Circle):
                obj.x = self.x
                obj.y = self.y


import pyglet

class EventHandler:
    def __init__(self, window, objects, config):
        self.window = window
        self.objects = objects
        self.config = config
        self.x_step = config.x_step
        self.y_step = config.y_step

    def on_draw(self):
        self.window.clear()
        for obj in self.objects.values():
            obj.draw()

    def on_key_press(self, symbol, modifiers):
        # Manejar eventos de teclado usando self.config
        if symbol == pyglet.window.key.RIGHT:
            self.update_direction('right')
        elif symbol == pyglet.window.key.LEFT:
            self.update_direction('left')
        elif symbol == pyglet.window.key.UP:
            self.update_direction('up')
        elif symbol == pyglet.window.key.DOWN:
            self.update_direction('down')

    def update_direction(self, direction):
        # Cambiar la dirección de todos los círculos
        for name, obj in self.objects.items():
            if isinstance(obj, pyglet.shapes.Rectangle):
                obj.direction = direction

    def update(self, dt):
        for name, obj in self.objects.items():
            if isinstance(obj, pyglet.shapes.Rectangle) or isinstance(obj, pyglet.shapes.Circle):
                if obj.direction == "right":
                    obj.x += self.x_step * dt
                    if obj.x + self.config.object_size > self.config.width:
                        obj.direction = "left"
                elif obj.direction == "left":
                    obj.x -= self.x_step * dt
                    if obj.x < 0:
                        obj.direction = "right"
                elif obj.direction == "up":
                    obj.y += self.y_step * dt
                    if obj.y + self.config.object_size > self.config.height:
                        obj.direction = "down"
                elif obj.direction == "down":
                    obj.y -= self.y_step * dt
                    if obj.y < 0:
                        obj.direction = "up"
                # obtener el índice del objeto
                index = int(name.split('_')[-1])
                self.objects[f'label_{index}'].x = obj.x
                self.objects[f'label_{index}'].y = obj.y

    # Definir la función que gestione eventos de ratón
    def on_mouse_press(self, x, y, button, modifiers):
        # si la posición x, y coincide con un objeto, elimina el objeto
        for name, obj in self.objects.items():
            if isinstance(obj, pyglet.shapes.Rectangle):
                if obj.x < x < obj.x + self.config.object_size and obj.y < y < obj.y + self.config.object_size:
                    # obtener el índice del objeto
                    index = int(name.split('_')[-1])
                    # elimilar el label del objeto
                    del self.objects[f'label_{index}']
                    del self.objects[name]
                    # decrementar en contador de objects_count
                    self.config.objects_count -= 1
                    # pintar en el label el nuevo valor de objects_count
                    self.objects['label'].text = str(self.config.objects_count)
                    #break
        print(f"Mouse button {button} pressed at ({x}, {y})")

    def on_mouse_release(self, x, y, button, modifiers):
        print(f'Mouse released at ({x}, {y}) with button {button} and modifiers {modifiers}')

    def on_mouse_motion(self, x, y, dx, dy):
        print(f'Mouse moved to ({x}, {y}) with delta ({dx}, {dy})')

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print(f'Mouse dragged to ({x}, {y}) with delta ({dx}, {dy}), buttons {buttons}, modifiers {modifiers}')

    def on_mouse_enter(self, x, y):
        print(f'Mouse entered at ({x}, {y})')

    def on_mouse_leave(self, x, y):
        print(f'Mouse left at ({x}, {y})')

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        print(f'Mouse scrolled at ({x}, {y}) with scroll ({scroll_x}, {scroll_y})')

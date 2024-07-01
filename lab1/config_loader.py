import configparser

class Config:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.title = 'Pyglet Game'
        self.x_step = 5
        self.y_step = 5
        self.object_size = 50
        self.direction = 'right'
        self.objects_count = 100

    def load_config(self, file_path):
        """
        Carga la configuración desde un archivo INI.
        :param file_path: Ruta al archivo de configuración.
        """
        config = configparser.ConfigParser()
        config.read(file_path)

        try:
            self.width = int(config['Configuracion Pantalla']['width'])
            self.height = int(config['Configuracion Pantalla']['height'])
            self.title = config['Configuracion Pantalla']['title']
            self.x_step = int(config['Configuracion Pantalla']['x_step'])
            self.y_step = int(config['Configuracion Pantalla']['y_step'])
            self.object_size = int(config['Configuracion Pantalla']['object_size'])
            self.objects_count = int(config['Configuracion Pantalla']['objects_count'])

        except KeyError as e:
            print(f"Error: Missing key {e} in the configuration file.")
        except ValueError as e:
            print(f"Error: Invalid value {e} in the configuration file.")

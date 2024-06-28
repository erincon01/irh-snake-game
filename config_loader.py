import configparser

class Config:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.title = 'Pyglet Game'
        self.movement = 5
        self.circle_size = 50
        self.direction = 'right'

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
            self.movement = int(config['Configuracion Pantalla']['movement'])
            self.circle_size = int(config['Configuracion Pantalla']['circle_size'])
            self.direction = config['Configuracion Pantalla']['direction']
        except KeyError as e:
            print(f"Error: Missing key {e} in the configuration file.")
        except ValueError as e:
            print(f"Error: Invalid value {e} in the configuration file.")

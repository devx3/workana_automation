import os
import shutil
import json


class Config(object):

    CONFIG_FILE = os.path.join(os.getcwd(), 'config.json')

    def up(self):
        ''' Start up the class '''
        self.create_file()

        with open(self.CONFIG_FILE) as config_file:
            self.config = json.load(config_file)

    def get(self, attribute):
        ''' Get the Configuration Value '''
        assert isinstance(attribute, str), "Attribute must be a string"
        assert '.' in attribute, "Attribute must be separated by dot"

        section, configuration = attribute.split('.')

        return self.config['config'][section][configuration]

    def file_exists(self):
        ''' Check if config file exists '''
        return os.path.exists(self.CONFIG_FILE)

    def create_file(self):
        ''' Create the config file if NOT exists '''
        if not self.file_exists():
            config_example = self.CONFIG_FILE+'.example'
            shutil.copyfile(config_example, self.CONFIG_FILE)

    def update(self, attribute, value):
        attribute = str(attribute)
        value = str(value)
        assert isinstance(attribute, str), "Attribute must be a string"
        assert '.' in attribute, "Attribute must be separated by dot"
        assert isinstance(value, str), "Value must be a string"

        section, configuration = attribute.split('.')

        self.config['config'][section][configuration] = value

        try:
            with open(self.CONFIG_FILE, 'w') as file:
                json.dump(self.config, file, indent=4)
            return True
        except Exception:
            return False

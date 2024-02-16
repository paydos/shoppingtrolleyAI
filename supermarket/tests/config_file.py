from configparser import ConfigParser
import os
  
path = 'settings'
config_file = 'locations.ini'


config = ConfigParser()
config.read(os.path.join(path, config_file))

for section in config.sections():
    print(f"Section: {section}")
    for key in config[section]:
        print(f"{key} = {config[section][key]}")
    print()

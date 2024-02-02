from configparser import ConfigParser
import os









class Aisle:
    
    
    
    
    
    
    
    def __init__(self, aisle_number, aisle_name) -> 'Aisle':
        self.products = []
        self.name = aisle_name
        self.number = aisle_number
        
        #* TODO: Add Aisle location
        
        self.path = '../settings'
        self.config_file = 'locations.ini'
              
        
        # instantiate
        config = ConfigParser()

        # parse existing file
        config.read(os.path.join(self.path, self.config_file))

        # read values from a section
        
        self.location = config.get(aisle_name, 'location')
        self.length = config.getint(aisle_name, 'length')

    
        
    
    def add_product(self, product):
        self.products.append(product)
        
    
        
        

class Beacon(Aisle):
    def __init__(self, aisle_number) -> None:
        super().__init__(aisle_number=aisle_number)
        self.coordinates = 'COORDINATES'
        self.max_signal_dB = 100
        self.min_signal_dB = 0
    pass

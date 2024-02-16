from configparser import ConfigParser

import json
import os


class PlaceableObject:
    """
    Parent class for placeable objects in the supermarket grid.
    
    Contains core info:
        - Config file
    
    """
    
    # Paths
    path = 'supermarket/settings'
    
    config_file = 'locations.ini'
    
    # Parser file (locations.ini)
    config = ConfigParser()

    # parse existing file
    config.read(os.path.join(path, config_file))
        
    


class Aisle(PlaceableObject):
    """
    Aisle (aka shelves) is PlaceableObject, with_
        - location
        - length (of the aisle)
        - products (of the whole shelve)
    
    
    """
    
    def __init__(self, aisle_number, aisle_name) -> 'Aisle':
        super().__init__()
        
        # Products
        self.products = () # Products are stored in a single tuple with format ('category1', [{'name':'Product_name', 'price': 1.3}, ...])
        
            
        self.name = aisle_name
        self.number = aisle_number
        
        
                
        self.path = 'supermarket/settings'
        self.config_file = 'locations.ini'
    

        # read values from a section
        self.location = PlaceableObject.config.get(aisle_name, 'location')
        self.length = PlaceableObject.config.getint(aisle_name, 'length')
        
        self.location_properties = {'Location':self.location,
                                    'Length': self.length}
    
    def populateAisle(self, group_of_products: dict):
        self.products = group_of_products
        
        
            
        
    
    
    def _add_product(self, product):
        self.products.append(product) 
        
        
        
        
        

class Beacon(Aisle):
    def __init__(self, aisle_number) -> None:
        super().__init__(aisle_number=aisle_number)
        self.coordinates = 'COORDINATES'
        self.max_signal_dB = 100
        self.min_signal_dB = 0
    pass


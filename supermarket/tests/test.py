from core.supermarket_layout import Supermarket
from core.supermarket_objects import Aisle
from configparser import ConfigParser
from lib.data_pipeline import Pipeline



if __name__ == '__main__':
    
    
    super_size = (20, 32)

    config = ConfigParser()
    
    # Read aisles config
    config.read('supermarket/settings/locations.ini')
    aisles = list(config.sections())
    
    # Read supermarket config
    config.read('supermarket/settings/supermarket_properties.ini')
    size = tuple(config.get('SUPERMARKET', 'size'))
    
    print(type(size))
        
    a = Pipeline(len(aisles))
    
    supermarket = Supermarket(size)

    
    for i, aisle in enumerate(aisles):
        supermarket.add_aisle(Aisle(aisle_number=i, aisle_name=aisle))
        supermarket.aisles['AISLE_1'].populateAisle(next(iter(supermarket.stock.items())))

    supermarket.show_layout()
    
    print(supermarket.aisles.keys())
    print((supermarket.aisles['AISLE_1'].products[1]))
from core.supermarket_layout import Supermarket
from core.supermarket_objects import Aisle




supermarket = Supermarket((15, 20))




supermarket.add_aisle(Aisle(aisle_number=3, aisle_name='AISLE_1'))

supermarket.show_layout()
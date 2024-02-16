import pandas as pd
import json
from settings.paths import database_path

class Pipeline:
    """
    
    Pipelines the data pre-processing.
    Parameters:
    - no_aisles: Number of total Aisles, given by the supermarket. This is done to avoid having a longer product list than number of Aisles.
    
        
    """
    def __init__(self, no_aisles) -> None:
        self.no_aisles = no_aisles
        
        # Get the csv
        df = pd.read_csv(database_path)
        
        # TODO Get 1k products (Could probably make it dynamic)
        thousand_prods = df.sample(1000)

        # Get all categories
        categories = thousand_prods['category'].unique()

        supermarket = {}

        # Limiting to the first 14 categories
        limited_categories = categories[:self.no_aisles] # Should be limited to the number of Aisles

        for cat in limited_categories:
            # Convert the selected DataFrame to a list of dictionaries instead of numpy array to avoid serialization issues
            supermarket[cat] = thousand_prods[thousand_prods['category'] == cat][['name', 'price']].to_dict('records')

        # Save the supermarket dictionary to a JSON file
        with open('supermarket/data/products.json', 'w') as file:
            json.dump(supermarket, file)


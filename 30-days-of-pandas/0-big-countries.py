# 595. Big Countries
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Define the threshold for area (in square kilometers)
    area_limit = 3000000
    
    # Define the threshold for population (number of people)
    population_limit = 25000000
    
    # Filter countries that are big by area or population
    big_countries = world[(world['area'] >= area_limit) | (world['population'] >= population_limit)]
    
    # Select the required columns: name, population, and area
    result = big_countries[['name', 'population', 'area']]
    
    # Return the resulting DataFrame
    return result

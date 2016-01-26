# Python 3
import pandas as pd

world_food_facts = pd.read_csv('FoodFacts.csv')
world_food_facts.countries = world_food_facts.countries.str.lower()
fr_datetimes = world_food_facts[world_food_facts.countries == 'france']
    
def mean(l):
    return float(sum(l)) / len(l)

if __name__ == '__main__':
    print(world_food_facts)

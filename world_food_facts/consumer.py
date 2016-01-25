# Python 3
import pandas as pd

world_food_facts = pd.read_csv('FoodFacts.csv')
world_food_facts.countries = world_food_facts.countries.str.lower()
    
def mean(l):
    return float(sum(l)) / len(l)

if __name__ == '__main__':
    print(world_food_facts.countries[1000:1050])

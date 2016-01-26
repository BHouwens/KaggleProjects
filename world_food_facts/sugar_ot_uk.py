# Python 3
from consumer import world_food_facts, mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

world_sugars = world_food_facts[world_food_facts.sugars_100g.notnull()]

def get_by_country(country):
    return world_sugars[world_sugars.countries == country]

uk_entries = get_by_country('united kingdom')
uk_entries = uk_entries.ix[pd.to_datetime(uk_entries.created_datetime).order().index]

x_entries = uk_entries.created_datetime
y_entries = uk_entries.sugars_100g
y_pos = np.arange(len(x_entries))

plt.plot(y_pos, y_entries)
plt.xticks(y_pos, x_entries)
plt.show()
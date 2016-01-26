# Python 3
from consumer import world_food_facts, mean
import numpy as np
import matplotlib.pyplot as plt

world_sugars = world_food_facts[world_food_facts.sugars_100g.notnull()]

# Gives back list of sugar contents for country
def return_sugars(country):
    return world_sugars[world_sugars.countries == country].sugars_100g.tolist()
    
# Get list of sugars per 100g for some countries
fr_sugars = return_sugars('france') + return_sugars('en:fr')
za_sugars = return_sugars('south africa')
uk_sugars = return_sugars('united kingdom') + return_sugars('en:gb')
us_sugars = return_sugars('united states') + return_sugars('en:us') + return_sugars('us')
sp_sugars = return_sugars('spain') + return_sugars('españa') + return_sugars('en:es')
nd_sugars = return_sugars('netherlands') + return_sugars('holland')
au_sugars = return_sugars('australia') + return_sugars('en:au')
cn_sugars = return_sugars('canada') + return_sugars('en:cn')
de_sugars = return_sugars('germany')

countries = ['France', 'South Africa', 'UK', 'USA', 'Spain', 'Netherlands', 'Australia', 'Canada', 'Germany']
sugars_l = [mean(fr_sugars), 
            mean(za_sugars), 
            mean(uk_sugars), 
            mean(us_sugars), 
            mean(sp_sugars), 
            mean(nd_sugars),
            mean(au_sugars),
            mean(cn_sugars),
            mean(de_sugars)]
            
if __name__ == '__main__':
    y_pos = np.arange(len(countries))
    
    plt.bar(y_pos, sugars_l, align='center', alpha=0.5)
    plt.title('Average total sugar content per 100g')
    plt.xticks(y_pos, countries)
    plt.ylabel('Sugar/100g')
    
    plt.show()
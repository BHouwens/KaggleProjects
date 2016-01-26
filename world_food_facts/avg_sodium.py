# Python 3
from consumer import world_food_facts, mean
import numpy as np
import matplotlib.pyplot as plt

world_sodium = world_food_facts[world_food_facts.sodium_100g.notnull()]

def return_sodium(country):
    return world_sodium[world_sodium.countries == country].sodium_100g.tolist()
    
# Get list of sodium per 100g for some countries
fr_sodium = return_sodium('france') + return_sodium('en:fr')
za_sodium = return_sodium('south africa')
uk_sodium = return_sodium('united kingdom') + return_sodium('en:gb')
us_sodium = return_sodium('united states') + return_sodium('en:us') + return_sodium('us')
sp_sodium = return_sodium('spain') + return_sodium('españa') + return_sodium('en:es')
ch_sodium = return_sodium('china')
nd_sodium = return_sodium('netherlands') + return_sodium('holland')
au_sodium = return_sodium('australia') + return_sodium('en:au')
jp_sodium = return_sodium('japan') + return_sodium('en:jp')
de_sodium = return_sodium('germany')

countries = ['France', 'South Africa', 'UK', 'USA', 'Spain', 'China', 'Netherlands', 'Australia', 'Japan', 'Germany']
sodium_l = [mean(fr_sodium), 
            mean(za_sodium), 
            mean(uk_sodium), 
            mean(us_sodium), 
            mean(sp_sodium), 
            mean(ch_sodium),
            mean(nd_sodium),
            mean(au_sodium),
            mean(jp_sodium),
            mean(de_sodium)]


if __name__ == '__main__':
    y_pos = np.arange(len(countries))
    
    plt.bar(y_pos, sodium_l, align='center', alpha=0.5)
    plt.title('Average sodium content per 100g')
    plt.xticks(y_pos, countries)
    plt.ylabel('Sodium/100g')
    
    plt.show()
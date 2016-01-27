# Python 3
import pandas as pd
from sklearn.cross_validation import train_test_split

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

x = train[train.columns[2:79]]
y = train.Response

if __name__ == '__main__':
    print(x)

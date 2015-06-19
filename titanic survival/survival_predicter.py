import csv
from data_present import Data
from ensemble import Ensemble
from sklearn.metrics import accuracy_score

counter = 892
data = Data()
submission = [['PassengerId', 'Survived']]

# Set up pred
ensemble = Ensemble(data)
ensemble.pred = map(int, ensemble.pred)

for entry in ensemble.pred:
	submission.append([counter, entry])
	counter += 1

with open('submission.csv', 'wb') as f:
    writer = csv.writer(f)
    for val in submission:
        writer.writerow(val)



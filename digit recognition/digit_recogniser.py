import csv
from sklearn.ensemble import RandomForestClassifier
from setup.data import Data

data = Data()
counter = 1
final = [['ImageId', 'Label']]

# set up the pred
clf = RandomForestClassifier(n_estimators=500, min_samples_split=6,n_jobs=-1)
clf.fit(data.features_train, data.labels_train)

pred = clf.predict(data.features_test)

for entry in pred:
	final.append([counter, entry])
	counter += 1

with open('submission.csv', 'wb') as f:
    writer = csv.writer(f)
    for val in final:
        writer.writerow(val)
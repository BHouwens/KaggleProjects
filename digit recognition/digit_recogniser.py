import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier

csv_f = csv.reader(open('train.csv'))
csv_t = csv.reader(open('test.csv'))
total_features, total_labels = [], []
total_test = []

# training set and testing set
features_train, labels_train = [], []
features_test = []

# set up training data
for row in csv_f:
    total_features.append(row[1:])
    total_labels.append(row[0])

# delete headings
del total_features[0]
del total_labels[0]

# typecast everything to ints
total_labels = map(int, total_labels)
total_features = [list(map(int, i)) for i in total_features]

features_train = np.array(total_features)
labels_train = np.array(total_labels)


# set up testing data
for row in csv_t:
	total_test.append(row)

del total_test[0]
total_test = [list(map(int, i)) for i in total_test]

features_test = np.array(total_test)


# set up the pred
clf = RandomForestClassifier(n_estimators=500, min_samples_split=6,n_jobs=-1)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)


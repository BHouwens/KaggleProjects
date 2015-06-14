from sklearn.ensemble import RandomForestClassifier
from setup_data import Data

data = Data()

# set up the pred
clf = RandomForestClassifier(n_estimators=500, min_samples_split=6,n_jobs=-1)
clf.fit(data.features_train, data.labels_train)

pred = clf.predict(data.features_test)

print pred[0]
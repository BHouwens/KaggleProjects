from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.lda import LDA
from sklearn.tree import DecisionTreeClassifier


class Ensemble:

	def __init__(self, data):
		self.rf = RandomForestClassifier(n_estimators=80, n_jobs=-1, min_samples_split=45, criterion='entropy')
		self.lda = LDA()
		self.dec = DecisionTreeClassifier(criterion='entropy')
		self.ada = AdaBoostClassifier(n_estimators=500, learning_rate=0.25)

		self.make_prediction(data)


	def make_prediction(self, data):
		'''
		Make an ensemble prediction
		'''
		self.rf.fit(data.features_train, data.labels_train)
		self.lda.fit(data.features_train, data.labels_train)
		self.dec.fit(data.features_train, data.labels_train)
		self.ada.fit(data.features_train, data.labels_train)

		pre_pred = []
		self.pred = []

		ada_pred = self.ada.predict(data.features_test)
		rf_pred = self.rf.predict(data.features_test)
		lda_pred = self.lda.predict(data.features_test)
		dec_pred = self.dec.predict(data.features_test)

		for i in range(len(rf_pred)):
			pre_pred.append([ rf_pred[i], lda_pred[i], dec_pred[i], ada_pred[i] ])

		for entry in pre_pred:
			pred_list = sorted(entry, key=entry.count, reverse=True)
			self.pred.append(pred_list[0])
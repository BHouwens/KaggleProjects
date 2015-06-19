from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.lda import LDA
from sklearn.qda import QDA

class Classifiers:
	'''
	Compare the general performance of a number of sklearn classifiers
	'''

	def __init__(self):
		self.classifiers = [
			KNeighborsClassifier(3),
		    SVC(kernel="linear", C=0.025),
		    SVC(gamma=2, C=1),
		    DecisionTreeClassifier(),
		    RandomForestClassifier(n_estimators=700, min_samples_split=15, n_jobs=-1),
		    AdaBoostClassifier(),
		    GaussianNB(),
		    LDA(),
		    QDA()
		]

		self.acc = []

	def compare(self, data):
		'''
		Run comparison of classifiers

		data: (list or np.array) Data to compare with 

		'''
		for entry in self.classifiers:
			clf = entry

			clf.fit(data.features_train, data.labels_train)
			pred = clf.predict(data.features_test)
			acc = accuracy_score(data.labels_test, pred)
			self.acc.append(acc)

			print str(entry)
			print ''
			print ''
			print 'has a score of: ' + str(acc)
			print ''
			print '========='
			print ''

	def cull(self, val):
		'''
		Cull any classifiers that don't perform well enough

		val : (float) Threshold below which to cull

		'''
		for index, entry in enumerate(self.acc):
			if entry < val:
				self.acc.remove(entry)
				self.classifers.remove(self.classifiers[index])

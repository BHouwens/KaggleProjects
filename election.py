from statistics import mode
from nltk.classify import ClassifierI

class Election(ClassifierI):
	'''
	Decision tree-like combo classifier specifically
	for NLP
	'''
	def __init__(self, *args):
		self.classifiers = args

	def vote(self, training_set):
		votes = []
		for c in self.classifiers:
			v = c.classify(training_set)
			votes.append(v)

		return mode(votes)

	def unanimity(self, training_set):
		votes = []
		for c in self.classifiers:
			v = c.classify(training_set)
			votes.append(v)

		choice = votes.count(mode(votes))
		return choice / len(votes)

import csv
import numpy as np


class Data:
	'''
	Set up all data
	'''

	def __init__(self):
		self.features_train = []
		self.labels_train = []
		self.features_test = []

		csv_f = csv.reader(open('train.csv'))
		csv_t = csv.reader(open('test.csv'))
		total_features, total_labels = [], []
		total_test = []

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

		# define training features and labels
		self.features_train = np.array(total_features)
		self.labels_train = np.array(total_labels)

		# set up testing data
		for row in csv_t:
			total_test.append(row)

		del total_test[0]
		total_test = [list(map(int, i)) for i in total_test]

		self.features_test = np.array(total_test)
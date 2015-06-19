import csv
import numpy as np
from matplotlib import pyplot as plot

class Data:

	def __init__(self):
		self.features_train = []
		self.labels_train = []
		self.features_test = []
		self.labels_test = []

		self.csv_train = csv.reader(open('train.csv'))
		self.csv_test = csv.reader(open('test.csv'))

		self.final_pred()

	def split_train_test(self, total_features, total_labels):
		'''
		Create a good train/test split.
		'''
		length = len(total_features)
		split = length * 80 / 100

		# Set up training data
		for i in range(split):
			self.features_train.append(total_features[i])
			self.labels_train.append(total_labels[i])

		# Set up testing data
		for i in range(split - 1, length):
			self.features_test.append(total_features[i])
			self.labels_test.append(total_labels[i])

		self.features_train = np.array(self.features_train)
		self.features_test = np.array(self.features_test)



	def plot(self):
		'''
		Plot survival based on any two features. Blue indicates survival, red indicates death.
		'''
		survived_x, survived_y = [], []
		died_x, died_y = [], []

		header = self.csv_train.next()

		# Age, sex comparison
		for row in self.csv_train:
			if not row[5] == '':
				if row[1] == '1':
					if row[4] == 'female':
						survived_y.append(1)
					else:
						survived_y.append(0)

					survived_x.append(float(row[5]))

				else:
					if row[4] == 'female':
						died_y.append(1)
					else:
						died_y.append(0)

						
					died_x.append(float(row[5]))



		plot.scatter(survived_x, survived_y)
		plot.scatter(died_x, died_y, color="r")
		plot.title('Titanic Survival')
		plot.xlabel('Age')
		plot.ylabel('Sex - Female = 1, Male = 0')

		plot.show()



	def initial_pred(self):
		'''
		Initial prediction to get a sense of accuracy before submitting
		'''

		# Split and set data for training and testing
		total_features = []
		total_labels = []

		for row in self.csv_train:
			age = row[5]
			sex = row[6]
			parch = row[7]
			fare = row[9]

			# handle all null values
			# we can't exclude these entries for final submission

			if age == '':
				age = 0.1
			if parch == '':
				parch = 0.1
			if fare == '':
				fare = 0.1

			if sex == '':
				sex = 0.1
			elif sex == 'female':
				sex = 1
			else:
				sex = 0

			total_features.append([row[2], sex, age, parch, fare])
			total_labels.append(row[1])


		del total_features[0]
		del total_labels[0]

		# convert to floats
		total_features = [list(map(float, i)) for i in total_features]
		total_labels = map(float, total_labels)

		self.split_train_test(total_features, total_labels)



	def final_pred(self):
		'''
		Final prediction with submission testing data. 
		The prediction relies on only a handful of important features.
		'''
		for row in self.csv_train:
			age = row[5]
			sex = row[6]
			parch = row[7]
			fare = row[9]

			# handle all null values
			# we can't exclude these entries for final submission

			if age == '':
				age = 0.1
			if parch == '':
				parch = 0.1
			if fare == '':
				fare = 0.1

			if sex == '':
				sex = 0.1
			elif sex == 'female':
				sex = 1
			else:
				sex = 0

			self.features_train.append([row[2], sex, age, parch, fare])
			self.labels_train.append(row[1])

		del self.features_train[0]
		del self.labels_train[0]

		# convert to floats
		self.features_train = [list(map(float, i)) for i in self.features_train]
		self.labels_train = map(float, self.labels_train)

		for row in self.csv_test:
			age = row[4]
			sex = row[3]
			parch = row[6]
			fare = row[8]

			# handle all null values
			# we can't exclude these entries for final submission

			if age == '':
				age = 0.1
			if parch == '':
				parch = 0.1
			if fare == '':
				fare = 0.1

			if sex == '':
				sex = 0.1
			elif sex == 'female':
				sex = 1
			else:
				sex = 0

			# class, sex, age, parch, fare
			self.features_test.append([row[1], sex, age, parch, fare])

		del self.features_test[0]
		self.features_test = [list(map(float, i)) for i in self.features_test]

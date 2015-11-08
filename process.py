##
## @Author: Geoffrey Bauduin <bauduin.geo@gmail.com>
##

import cv2 as opencv
import numpy as np
from matplotlib import pyplot as plt

class Processer:
	
	def __init__(self):
		letters, l_letters = self.__loadLetters("./letters.png")
		digits, l_digits = self.__loadDigits("./digits.png")
		self.train_labels = l_letters
		train = letters
		self.knn = opencv.KNearest()
		self.knn.train(train,self.train_labels)

	def __loadDigits(self, filename):
		image = opencv.imread(filename)
		gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
		cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
		# (50,100,20,20)
		x = np.array(cells)
		data = x.reshape(-1, 400).astype(np.float32)
		labels = np.arange(10)
		return data, np.repeat(labels, 500)[:,np.newaxis]

	def __loadLetters(self, filename):
		image = opencv.imread(filename)
		gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
		cells = [np.hsplit(row, 84) for row in np.vsplit(gray, 52)]
		# (52,84,20,20)
		x = np.array(cells)
		data = x.reshape(-1, 400).astype(np.float32)
		labels = np.arange(10, 62)
		return data, np.repeat(labels,84)[:,np.newaxis]
		

	def compare(self, filename):
		image = opencv.imread(filename)
		gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
		resized = opencv.resize(gray, (20, 20))
		x = np.array(resized)
		test = x.reshape(-1, 400).astype(np.float32)
		ret, result, neighbours, dist = self.knn.find_nearest(test,k=4)
		matches = result==self.train_labels
		correct = np.count_nonzero(matches)
		accuracy = correct * 100.0 / result.size
		print self.train_labels
		print correct
		print ret
		print "result:", result
		print neighbours
		print dist

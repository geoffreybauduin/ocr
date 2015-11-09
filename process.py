##
## @Author: Geoffrey Bauduin <bauduin.geo@gmail.com>
##

import cv2 as opencv
import numpy as np
from matplotlib import pyplot as plt

class Processer:
	
	def __init__(self):
		image = opencv.imread("./all.png")
		gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
		cells = [np.hsplit(row, 84) for row in np.vsplit(gray, 102)]
		# (102,84,20,20)
		x = np.array(cells)
		data = x.reshape(-1, 400).astype(np.float32)
		k = np.arange(52)
		for i in range(52, 62):
			for j in range(0, 5):
				k = np.append(k, i)
		self.train_labels = np.repeat(k, 84)[:,np.newaxis]
		train = data
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

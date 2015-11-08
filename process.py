##
## @Author: Geoffrey Bauduin <bauduin.geo@gmail.com>
##

import cv2 as opencv
import numpy as np
from matplotlib import pyplot as plt

class Processer:
	
	def __init__(self):
		img = opencv.imread('./digits.png')
		gray = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)
		cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
		# (50,100,20,20)
		x = np.array(cells)
		train = x.reshape(-1,400).astype(np.float32)
#		test = x.reshape(-1,400).astype(np.float32)
#		print train
#		print len(train)
		k = np.arange(10)
		self.train_labels = np.repeat(k,500)[:,np.newaxis]
#		test_labels = train_labels.copy()
		self.knn = opencv.KNearest()
		self.knn.train(train,self.train_labels)
#		ret,result,neighbours,dist = knn.find_nearest(test,k=4)
#		matches = result==test_labels
#		correct = np.count_nonzero(matches)
##		accuracy = correct*100.0/result.size
#		print accuracy	

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

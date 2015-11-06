##
## @Author: Geoffrey Bauduin <bauduin.geo@gmail.com>
##

import cv2 as opencv

class Processer:
	
	def __init__(filename):
		self.image = opencv.imread(fiename)
		if self.image == None:
			raise Exception("Cannot load " + filename)
		
	def __smallize():
		self.image = opencv.resize(self.image, 50, 50)
		pass
		
	def __rgb2gray():
		opencv.cvtColor(self.image, self.image, opencv.CV_RGB2GRAY)
		pass
		
	def __orph_gradient():
		pass
	
	def __binarization():
		pass
	
	def __calc_rotate():
		pass
		
	def __rotate():
		pass
		
	def __line_horizontally():
		pass
		
	def __word_detection():
		pass
		
	def __fusion_word():
		pass
	
	def __fix_line():
		pass
		
	def __sort_result():
		pass
		
	def run():
		self.__smallize()
		self.__rgb2gray()
		self.__orph_gradient()
		self.__binarization()
		self.__calc_rotate()
		self.__rotate()
		self.__line_horizontally()
		self.__word_detection()
		self.__fusion_word()
		self.__fix_line()
		self.__sort_result()
import cv2
from sys import argv
import os

cv2_images = []
current_index = 0

def LoadPictures(folder):
	global cv2_images
	images = []
	for image in os.listdir(folder):
		if image.endswith('.jpg'):
			images.append(image)
	images = sorted(images)
	for image in images:
		# os.listdir()  returns the names of the files in the folder without
		# the name of the folder included. For imread to work, join the name
		# of the folder to the name of the image separated by a '/'.
		cv2_images.append(cv2.imread(folder + '/' + image))

def HandleKeyboard():
	global current_index
	key = chr(cv2.waitKey(0))
	if key == 'a':
			# advance in the 'negative' direction.
			current_index -= 1
			if current_index == -1:
				# If the current index has become negative, cycle
				# back to the last image in the list.
				current_index = len(cv2_images) - 1
	elif key == 's':
		current_index += 1
		if current_index == len(cv2_images):
			# If the current index is equal to the number of images,
			# we must cycle back to the first image (at index 0).
			current_index = 0
	return key
	
def main(folder):
	LoadPictures(folder)
	key = ''
	while key != 'q':
		cv2.imshow('Flipbook', cv2_images[current_index])
		cv2.setWindowTitle('Flipbook', 'Flipbook [{:d}]'.format(current_index))
		key = HandleKeyboard()

if __name__ == "__main__":
	folder = '.'
	if len(argv) > 1:
		folder = argv[1]
	main(folder)

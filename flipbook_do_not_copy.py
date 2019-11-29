import cv2

files = ['0.jpg', '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg']
images = []
for filename in files:
	images.append(cv2.imread(filename))

current_index = 0
key = ''
while key != 'q':
	cv2.imshow('Muybridge Horse', images[current_index])
	key = chr(cv2.waitKey(0))
	if key == 'a':
		current_index = current_index - 1
	elif key == 's':
		current_index = current_index + 1
	current_index = current_index % len(files)
cv2.destroyAllWindows()

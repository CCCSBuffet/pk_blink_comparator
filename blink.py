import cv2

# Create an empty list and populate it with two pictures.
images = []
images.append(cv2.imread('p1.jpg'))
images.append(cv2.imread('p2.jpg'))
current_index = 0
key = ''
while key != 'q':
    cv2.imshow('Pluto', images[current_index])
    cv2.setWindowTitle('Pluto', 'Pluto Image: {:d}   -   \'q\' to quit'.format(current_index)))
    key = chr(cv2.waitKey(0))
    current_index = 1 - current_index
cv2.destroyAllWindows()

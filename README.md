# OpenCV Tutorial

### Installation
`pip install opencv-python` 

Verify the installation
~~~
>>> import cv2
>>> cv2.__version__
~~~

### Working with Image
~~~
import cv2

# reading an image
img = cv2.imread(image_src, flag) 
'''
  flag could be 0, 1, -1
  0 - grayscale image
  1 - color image
  -1 - image with alpha channel
'''

#showing images
cv2.imshow('window title', img)
key = cv2.waitKey(0)
'''
  wait key will take number of second to show image in milli seconds
  if you give 0, then it will wait for the key
'''

# Saving a file
cv2.imwrite('name to file', img)
cv2.destroyAllWindows()
~~~

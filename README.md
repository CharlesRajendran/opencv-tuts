# OpenCV Tutorial

### Installation
`pip install opencv-python` 

Verify the installation
~~~
>>> import cv2
>>> cv2.__version__
~~~

### Working with Image

#### reading an image
~~~
import cv2

'''
  flag could be 0, 1, -1
  0 - grayscale image
  1 - color image
  -1 - image with alpha channel
'''
img = cv2.imread(image_src, flag) 
~~~

#### showing images
~~~
'''
  wait key will take number of second to show image in milli seconds
  if you give 0, then it will wait for the key
'''
cv2.imshow('window title', img)
key = cv2.waitKey(0)
~~~

#### Saving a file
~~~
cv2.imwrite('name to file', img)
cv2.destroyAllWindows()
~~~

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

### Working with Video

#### Video Capture

- ##### Create an instance of the video capturing object and give the camera source it as the argument
~~~
import cv2

# This value could be 0 or -1 for the default camera source,
# then for additional capturing devices we can use 2, 3 and so on.
capture = cv2.VideoCapture(0)
~~~
- ##### The below code will capture the frames continuously unless I press `q`
  - `ret` will have whether it is true or not and the frame will have the actual frame.
  - `imshow` - is to render the frames
~~~
while(True):
    ret, frame = capture.read()
    cv2.imshow('Recording', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
~~~

- ##### Release the connections
~~~
capture.release()
cv2.destroyAllWindows()
~~~
[Complete Code](https://github.com/CharlesRajendran/opencv-tuts/blob/master/src/2-video-capture.py)
#### Convert the color video to grayscale
- instead of printing the frame, convet it to gray scale using `cvtColor` function
~~~
grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('Recording', grayscale)
~~~
[Complete Code](https://github.com/CharlesRajendran/opencv-tuts/blob/master/src/3--grayscale-video-capture.py)

#### Write the video to a file.
- ##### This can be done with `cv2` 's `VideoWriter` class
  - like in the below code, it expect some parameters
~~~
filename = "cam.avi"
videoCodec = cv2.VideoWriter_fourcc(*'XVID')
framerate = 20.0
resolution = (640, 480)

videoWriter = cv2.VideoWriter(filename, videoCodec, framerate, resolution)
~~~

- ##### Write it with a method of VideoWrite Class
~~~
if ret == True:
        videoWriter.write(frame)
~~~

- ##### Finally release the object connection
~~~
videoWriter.release()
~~~
[Complete Code](https://github.com/CharlesRajendran/opencv-tuts/blob/master/src/4-video-write.py)

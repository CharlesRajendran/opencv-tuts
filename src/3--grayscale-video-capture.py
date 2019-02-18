import cv2

capture = cv2.VideoCapture(0)
'''
    Video capture object has some methods such as whether the file is opened or not and etc.
    Video captured framesize and etc.
        capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
'''

while(capture.isOpened()):
    ret, frame = capture.read()

    # Convert the video frame to grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Recording', grayscale)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

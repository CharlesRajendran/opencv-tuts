import cv2

capture = cv2.VideoCapture(0)

filename = "cam.avi"
videoCodec = cv2.VideoWriter_fourcc(*'XVID')
framerate = 20.0
resolution = (640, 480)

videoWriter = cv2.VideoWriter(filename, videoCodec, framerate, resolution)


while(capture.isOpened()):
    ret, frame = capture.read()

    if ret == True:
        videoWriter.write(frame)
        
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Recording', grayscale)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
capture.release()
videoWriter.release()
cv2.destroyAllWindows()

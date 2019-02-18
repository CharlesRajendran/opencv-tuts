import cv2

# This value could be 0 or -1 for the default camera source,
# then for additional capturing devices we can use 2, 3 and so on.
capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
    cv2.imshow('Recording', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

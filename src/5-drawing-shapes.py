import cv2

img = cv2.imread('img.jpg', 1)

# Draw a line to the image
b = 255
g = 0
r = 0
thickness = 10
img = cv2.line(img, (0, 0), (300, 300), (b, g, r), 10)

# Draw an arrow line
img = cv2.arrowedLine(img, (0, 300), (300, 300), (0, 0, 255), 10)

# Rectangle
'''
(0, 0)------------|
|                 |
|                 |
----------------(255, 255)
'''
img = cv2.rectangle(img, (0,0), (255, 255), (0, 255, 0), 5)
# We can fill the rectangle with -1 for thickness

# Text
font = cv2.FONT_HERSHEY_PLAIN
fontSize = 14
fontColor = (0, 255, 255)
thickness = 10
line_type = cv2.LINE_AA
img = cv2.putText(img, 'TC', (200, 200), font, fontSize, fontColor, thickness, line_type)

cv2.imshow('Image Practice', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
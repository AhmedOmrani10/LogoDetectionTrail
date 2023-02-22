import cv2
import numpy as np

img = cv2.imread("images/img1.jpg")
alpha = 0.4
beta = -10




result = cv2.addWeighted(img,alpha,np.zeros(img.shape,img.dtype),0,beta)
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,70,255,0)
cv2.imshow("AI",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rectanglesList = []

# Look for the outer bounding boxes (no children):
for _, c in enumerate(contours):

    # Get blob area:
    currentArea = cv2.contourArea(c)
    # Set a min area threshold:
    minArea = 25

    if currentArea > minArea:

        # Approximate the contour to a polygon:
        contoursPoly = cv2.approxPolyDP(c, 3, True)
        # Get the polygon's bounding rectangle:
        boundRect = cv2.boundingRect(contoursPoly)

        # Store rectangles in list:
        rectanglesList.append(boundRect)

        # Get the dimensions of the bounding rect:
        rectX = boundRect[0]
        rectY = boundRect[1]
        rectWidth = boundRect[2]
        rectHeight = boundRect[3]

        # Set bounding rect:
        color = (0, 0, 255)
        cv2.rectangle(img, (int(rectX), int(rectY)),
                   (int(rectX + rectWidth), int(rectY + rectHeight)), color, 2 )
        

        

cv2.imshow("Rectangles", img)
cv2.waitKey(0)

print(len(rectanglesList))


import urllib.request
import cv2 as cv
import numpy as np

frame =  None
key = None
rectanglesList = []
alpha = 0.4
beta = -10
print("Start")

while True:
    imgResponse = urllib.request.urlopen("http://192.168.154.38/capture?")
    print("s")
    imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    frame = cv.imdecode(imgNp,-1)
    result = cv.addWeighted(frame, alpha, np.zeros(frame.shape, frame.dtype), 0, beta)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 70, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


    for _, c in enumerate(contours):

        # Get blob area:
        currentArea = cv.contourArea(c)
        # Set a min area threshold:
        minArea = 25

        if currentArea > minArea:
            # Approximate the contour to a polygon:
            contoursPoly = cv.approxPolyDP(c, 3, True)
            # Get the polygon's bounding rectangle:
            boundRect = cv.boundingRect(contoursPoly)
            convertedBoundRect = list(boundRect)
            convertedBoundRect.append(currentArea)

            # Store rectangles in list:
            rectanglesList.append(convertedBoundRect)

            # Get the dimensions of the bounding rect:
            rectX = boundRect[0]
            rectY = boundRect[1]
            rectWidth = boundRect[2]
            rectHeight = boundRect[3]

            # Set bounding rect:
            color = (0, 0, 255)
            cv.rectangle(frame, (int(rectX), int(rectY)),
                          (int(rectX + rectWidth), int(rectY + rectHeight)), color, 2)
    cv.imshow('Window',thresh)
    print("The logo is composed by " + str(len(rectanglesList)) + " objects")
    key = cv.waitKey(500)
    if key == (ord('q')):
        break

    print('Then END')


cv.destroyAllWindows()



# Look for the outer bounding boxes (no children):











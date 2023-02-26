# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
# %%
# Read logo image
logoFileName = "images/Logo-ConvertImageH.jpg"
img = cv2.imread(logoFileName)
# Set contrast & brightness
alpha = 0.4
beta = -10

# %%
# Reduce contrast & brightness
result = cv2.addWeighted(img,alpha,np.zeros(img.shape,img.dtype),0,beta)
# Convert to grayscale image
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
# Convert to binary image
ret,thresh = cv2.threshold(gray,70,255,0)
# Display the logo
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# as opencv loads in BGR format by default, we want to show it in RGB.
#plt.show()
#cv2.imshow("AI",thresh)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
# %%
# Find objects (All objects in the logo)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


rectanglesList = []
imgCopy = img.copy()
# Look for the outer bounding boxes (no children):
for _, c in enumerate(contours):

    # Get blob area:
    currentArea = cv2.contourArea(c)
    # Set a min area threshold (there are 2 objects with an area equal to 0)
    minArea = 0

    if currentArea > minArea:

        print("currentArea = " + str(currentArea))
        # Approximate the contour to a polygon:
        contoursPoly = cv2.approxPolyDP(c, 3, True)
        # Get the polygon's bounding rectangle:
        boundRect = cv2.boundingRect(contoursPoly)

        tmp = list(boundRect)
        tmp.append(currentArea)
        # Store rectangles in list:
        rectanglesList.append(tmp)

        # Get the dimensions of the bounding rect:
        rectX = boundRect[0]
        rectY = boundRect[1]
        rectWidth = boundRect[2]
        rectHeight = boundRect[3]

        # Set bounding rect:
        color = (0, 0, 255)
        cv2.rectangle(imgCopy, (int(rectX), int(rectY)),
                   (int(rectX + rectWidth), int(rectY + rectHeight)), color, 2 )

plt.imshow(cv2.cvtColor(imgCopy, cv2.COLOR_BGR2RGB))
#cv2.imshow("Logo detection", img)
#cv2.waitKey(0)

print("The logo is composed by " + str(len(rectanglesList)) + " objects")

# %% Find the largest bounding box area
#print(type(rectanglesList))
#print(type(rectanglesList[1]))
#print(rectanglesList)

orderedArea = sorted(rectanglesList, key=itemgetter(4), reverse=True)
print(orderedArea)
imgCopy2 = img.copy()
color = (0, 255, 0)
indObj = 1
cv2.rectangle(imgCopy2, (int(orderedArea[indObj][0]), int(orderedArea[indObj][1])),
                   (int(orderedArea[indObj][0] + orderedArea[indObj][2]), int(orderedArea[indObj][1] + orderedArea[indObj][3])), color, 2 )
plt.imshow(cv2.cvtColor(imgCopy2, cv2.COLOR_BGR2RGB))
# %%
print(orderedArea[0][0])
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.imshow(img)
# %%

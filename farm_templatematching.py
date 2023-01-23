import cv2
import numpy as np

farm_image = cv2.imread('farm.png', cv2.IMREAD_UNCHANGED)
wheat_image = cv2.imread('needle.png', cv2.IMREAD_UNCHANGED)

# cv2.imshow('Farm', farm_image)
# cv2.waitKey()
# cv2.destroyAllWindows()

# cv2.imshow('Needle', wheat_image)
# cv2.waitKey()
# cv2.destroyAllWindows()

result = cv2.matchTemplate(farm_image, wheat_image, cv2.TM_CCOEFF_NORMED)

# cv2.imshow('Result', result)
# cv2.waitKey()
# cv2.destroyAllWindows()

#this function is op, auto calculates coordinates for max and min results
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#accessing x and y coordinates, allowing us to calc height and width
w = wheat_image.shape[1]
h = wheat_image.shape[0]
cv2.rectangle(farm_image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255,255), 2)

# cv2.imshow('Farm', farm_image)
# cv2.waitKey()
# cv2.destroyAllWindows()

#creating threshold, keep array of y and x locations linked that are within threshold

threshold = 0.60
yloc, xloc = np.where(result >= threshold)

#for loop that increments x and y, creating rectangle at each point
# for (x, y) in zip(xloc, yloc):
#     cv2.rectangle(farm_image, (x, y), (x+w, y+h), (0,255,255), 2)

# cv2.imshow('Farm', farm_image)
# cv2.waitKey()
# cv2.destroyAllWindows()

#grouping rectangles together to limit overlapping 
#adds them to list as duplicates to account for scenairo where theres only 
rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])

rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

#redrawing rectangles after fixing grouping issue
for (x, y, w, h) in rectangles:
    cv2.rectangle(farm_image, (x, y), (x+w, y+h), (0,255,255), 2)

cv2.imshow('Farm', farm_image)
cv2.waitKey()
cv2.destroyAllWindows()
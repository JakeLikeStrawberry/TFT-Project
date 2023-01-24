import cv2
import numpy as np

giants_belt = cv2.imread('Item_Images/giantsbelt.png', cv2.IMREAD_UNCHANGED)
spatula = cv2.imread('Item_Images/spatula.png', cv2.IMREAD_UNCHANGED)
chainvest = cv2.imread('Item_Images/chainvest.png', cv2.IMREAD_UNCHANGED)
rod = cv2.imread('Item_Images/rod.png', cv2.IMREAD_UNCHANGED)
recurve = cv2.imread('Item_Images/recurve.png', cv2.IMREAD_UNCHANGED)
critglove = cv2.imread('Item_Images/critglove.png', cv2.IMREAD_UNCHANGED)


#TEST
while True: 

    nilah = cv2.imread('Character_Images/nilah.png', cv2.IMREAD_UNCHANGED)
    board_image = cv2.imread('Misc_Images/TEMPLATE_TEST.png', cv2.IMREAD_UNCHANGED)
    test1 = cv2.matchTemplate(board_image, nilah, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(test1)
    w = nilah.shape[1]
    h = nilah. shape[0]
    cv2.rectangle(board_image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255,255), 2)
    cv2.imshow('Test', board_image)
    cv2.waitKey()
    cv2.destroyAllWindows()

hi = 1

 
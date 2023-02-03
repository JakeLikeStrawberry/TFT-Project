import sys
import keyboard
import time
import cv2
import numpy as np
from character import Character
import mss
import threading
from pynput.mouse import Button, Controller
import pyautogui

pyautogui.PAUSE = 0

#ITEM INSTANTIATION
giants_belt = cv2.imread('Item_Images/giantsbelt.png', cv2.IMREAD_UNCHANGED)
spatula = cv2.imread('Item_Images/spatula.png', cv2.IMREAD_UNCHANGED)
chainvest = cv2.imread('Item_Images/chainvest.png', cv2.IMREAD_UNCHANGED)
rod = cv2.imread('Item_Images/rod.png', cv2.IMREAD_UNCHANGED)
recurve = cv2.imread('Item_Images/recurve.png', cv2.IMREAD_UNCHANGED)
critglove = cv2.imread('Item_Images/critglove.png', cv2.IMREAD_UNCHANGED)
negatron = cv2.imread('Item_Images/negatron3d.png', cv2.IMREAD_UNCHANGED)
bfsword = cv2.imread('Item_Images/bfsword.png', cv2.IMREAD_UNCHANGED)
tear = cv2.imread('Item_Images/tear3d.png', cv2.IMREAD_UNCHANGED)

#CHARACTER INSTANTIATIONS
#DUELIST
fiora = cv2.imread('Character_Images/fiora.png', cv2.IMREAD_UNCHANGED)
Fiora = Character(fiora, 2, [[critglove, chainvest], [negatron, giants_belt], [bfsword, giants_belt]])
gangplank = cv2.imread('Character_Images/gangplank.png', cv2.IMREAD_UNCHANGED)
Gangplank = Character(gangplank, 1, [[critglove, recurve], [bfsword, critglove], [recurve, negatron]])
kayle = cv2.imread('Character_Images/kayle.png', cv2.IMREAD_UNCHANGED)
Kayle = Character(kayle, 1, [[recurve, rod], [bfsword, recurve], [critglove, tear]])
nilah = cv2.imread('Character_Images/nilah.png', cv2.IMREAD_UNCHANGED)
Nilah = Character(nilah, 3, [[rod, chainvest], [tear, giants_belt], [chainvest, chainvest]])
vayne = cv2.imread('Character_Images/vayne.png', cv2.IMREAD_UNCHANGED)
Vayne = Character(vayne, 3, [[tear, tear], [rod, critglove], [critglove, tear]])
yasuo = cv2.imread('Character_Images/yasuo.png', cv2.IMREAD_UNCHANGED)
Yasuo = Character(yasuo, 3, [[critglove, tear], [chainvest, recurve], [negatron, bfsword]])
zed = cv2.imread('Character_Images/zed.png', cv2.IMREAD_UNCHANGED)
Zed = Character(zed, 4, [[bfsword, chainvest], [recurve, negatron], [critglove, recurve]])

#OX FORCE


#bini


#CHARACTER TRAIT ARRAYS
duelist = [Fiora, Gangplank, Kayle, Nilah, Vayne, Yasuo, Zed]



#Character Template Test
# nilah = cv2.imread('Character_Images/nilah.png', cv2.IMREAD_UNCHANGED)
board_image = cv2.imread('Misc_Images/TEMPLATE_TEST.png', cv2.IMREAD_UNCHANGED)
# test1 = cv2.matchTemplate(board_image, nilah, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(test1)
# w = nilah.shape[1]
# h = nilah. shape[0]
# cv2.rectangle(board_image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255,255), 2)
# cv2.imshow('Test', board_image)
# cv2.waitKey()
# cv2.destroyAllWindows()


#Item Template Test
#negatron.astype(np.float32)
#negatron = cv2.cvtColor(rod, cv2.COLOR_BGRA2BGR)
# test2 = cv2.matchTemplate(board_image, negatron, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(test2)
# w = negatron.shape[1]
# h = negatron.shape[0]
# cv2.rectangle(board_image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255,255), 2)
# cv2.imshow('Test2', board_image)
# cv2.waitKey()
#rod image needs to converted
# hello = len(rod.shape)
# hey = rod.shape[2]
# print(hello)

pyautogui.PAUSE = 0
sct = mss.mss()
 
threshold = 0.60
dimensions_shop = {
        'left': 243,
        'top': 851,
        'width':1257,
        'height':229

}
#getting length of list for loop
duelist_size = 7

while True:
    for num in range(0, duelist_size): 
        #initializing screenshot from shop coords
        scr = np.array(sct.grab(dimensions_shop))
        #still dont know what this does, may not be necessary
        scr_remove = scr[:, :, :3]
        #getting result from shop screenshot and duelist image
        result = cv2.matchTemplate(scr_remove, duelist[num].charImage, cv2.TM_CCOEFF_NORMED)
        #getting the max value (seeing if its above threshold) and location of that value
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #not sure what this does
        src = scr.copy()

        #if the value is greater than threshold, click at coords
        if max_val > threshold:
            pyautogui.click(max_loc[0], max_loc[1])
        #if not, wait 10 seconds (can be increased/decreased)
        else:
            time.sleep(10)

        #quit 
        if keyboard.is_pressed('q'):
            break

            




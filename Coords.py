import pyautogui, cv2, numpy as np
from matplotlib import pyplot as plt

def PyAutoGui_Coords():
    image = pyautogui.screenshot()
    position = pyautogui.locateOnScreen('dyno.png')
    if position != None:
        return position.left + position.width + 75, position.top, position.width, position.height-20
    else:
        print('Я не нашёл динозавра...')
        return 0, 0, 0, 0

def OpenCV_Coords():
    Dino = cv2.imread('Dino.png', cv2.IMREAD_GRAYSCALE) #берём образец динозаврика
    w, h = Dino.shape[::-1]
    image = pyautogui.screenshot()
    Shot = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY, )
    res = cv2.matchTemplate(Shot, Dino, cv2.TM_CCOEFF)
    min_val, max_val, bottom_right, top_left = cv2.minMaxLoc(res)
    #Draw_Rectangle_Plot(Shot, top_left, w, h) #Раскомментируйте это, если желаете посмотреть как ЦВ нашёл динозавра.
    return top_left[0]+w+75, top_left[1], w-10, h-16


def Draw_Rectangle_Plot(Shot, top_left, w, h):
    cv2.rectangle(Shot, top_left, [top_left[0]+w, top_left[1]+h-15], 255, 4)
    plt.subplot(1,1,1)
    plt.imshow(Shot, cmap='gray')
    plt.axis('off')
    plt.suptitle("Detected object is...")
    plt.show()

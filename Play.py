import pyautogui, cv2, numpy as np
from mss import mss

def tap_series():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    pyautogui.sleep(0.15) 
    pyautogui.keyUp('space')  
    pyautogui.keyDown('down')
    return 1

def Play(x, y, width, height):
    if x != 0 and y != 0 and width != 0 and height != 0:
        pyautogui.press('space')    #Начинаем игру
        pyautogui.keyDown('down')   #Фактически динозавр почти всегда в присяди для "безопасного"(нет) забега.
        obj = {'top': y, 'left': x,  'width': width * 2 + 15, 'height': height}
        Color_sample = np.sum(np.array(mss().grab(obj), dtype=np.uint8)) - 10
        with mss() as sct:
            while True:
                img = np.sum(np.array(sct.grab(obj), dtype=np.uint8))
                if img < Color_sample:  #Здесь применяется очень мощная технология. Цвет - это значения. Так вот, 
#мы просто проверяем сумму всех цветов нашей области относительно суммы этой же области в момент начала игры - 
# если цвет упал, значит мы наткнулись на препятствие.
                    obj['left'] += tap_series() #Отрабатываем нажатия клавиш попутно сдвигая левую координату, чтобы "догнать игру".
    else:
        print("Они точно не вымерли?\nПрограмма завершила свою работу.")
import os, time, pyautogui, keyboard, cv2
import numpy as np
import Play, Coords

def Start_with_pyautoGui():
    x, y, width, height = Coords.PyAutoGui_Coords()
    Play.Play(x, y, width, height)

def Start_with_cv2():
    x, y, width, height = Coords.OpenCV_Coords()
    Play.Play(x, y, width, height)

Start_with_pyautoGui()
#Start_with_cv2()
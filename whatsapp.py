from matplotlib.pyplot import hist2d
import pyautogui
import time
time.sleep(3)
count=0
while count<=10:
    pyautogui.typewrite("amazing")
    pyautogui.press("enter")
    pyautogui.typewrite("smart")
    pyautogui.press("enter")
    pyautogui.typewrite("cool")
    pyautogui.press("enter")
    
    count=count+1
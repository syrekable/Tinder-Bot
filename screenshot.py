import pyautogui
import json

coords = json.load(open('./res/coords_img.json'))

def takeScreenshot(fname,coordsMode):
    if coordsMode:
        img = pyautogui.screenshot(fname,region=(coords['left_x'],coords['top_y'],coords['width'],coords['height']))
    else:
        img = pyautogui.screenshot(fname,region=(0,0,1980,1080))
    return img
import pyautogui
import json

coords_like = json.load(open('./res/coords_btn_like.json'))
coords_dislike = json.load(open('./res/coords_btn_dislike.json'))

def like():
   pyautogui.click((coords_like['x'],coords_like['y']))

def dislike():
   pyautogui.click((coords_dislike['x'],coords_dislike['y']))
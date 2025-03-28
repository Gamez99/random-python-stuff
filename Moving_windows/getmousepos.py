import pyautogui

def get_pos():
    return [pyautogui.position().x, pyautogui.position().y]
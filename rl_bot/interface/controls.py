import pyautogui

class RLInterface:
    def __init__(self):
        pass

    def get_screen_size(self):
        return pyautogui.size()
    
    def forward(self, duration=-1):
        pyautogui.keyDown('w')
        if duration > 0:
            pyautogui.keyUp('w')
            pyautogui.sleep(duration)

    def backward(self, duration=-1):
        pyautogui.keyDown('s')
        if duration > 0:
            pyautogui.keyUp('s')
            pyautogui.sleep(duration)
    
    def left(self, duration=-1):
        pyautogui.keyDown('a')
        if duration > 0:
            pyautogui.keyUp('a')
            pyautogui.sleep(duration)
    
    def right(self, duration=-1):
        pyautogui.keyDown('d')
        if duration > 0:
            pyautogui.keyUp('d')
            pyautogui.sleep(duration)
    
    def jump(self, amount=1, freq=0.1):
        for _ in range(amount):
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
            pyautogui.sleep(freq)


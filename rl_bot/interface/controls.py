import pyautogui

from enum import Enum

class Directions(Enum):
    FORWARD = 1
    BACKWARD = 2
    FORWARD_LEFT = 3
    FORWARD_RIGHT = 4
    BACKWARD_LEFT = 5
    BACKWARD_RIGHT = 6

    def is_forward_facing(self) -> bool:
        return self == Directions.FORWARD or self == Directions.FORWARD_LEFT or self == Directions.FORWARD_RIGHT
    
    def is_backward_facing(self) -> bool:
        return self == Directions.BACKWARD or self == Directions.BACKWARD_LEFT or self == Directions.BACKWARD_RIGHT
    

class RLInterface:
    def __init__(self):
        pass

    def get_screen_size(self):
        return pyautogui.size()
    
    def forward(self, duration=-1):
        pyautogui.keyDown('w')
        if duration > 0:
            pyautogui.sleep(duration)
            pyautogui.keyUp('w')

    def backward(self, duration=-1):
        pyautogui.keyDown('s')
        if duration > 0:
            pyautogui.sleep(duration)
            pyautogui.keyUp('s')
    
    def left(self, direction: Directions, duration=-1):
        pyautogui.keyDown('a')
        dir = 'w' if direction.is_forward_facing() else 's'
        pyautogui.keyDown(dir)
        if duration > 0:
            pyautogui.sleep(duration)
            pyautogui.keyUp(dir)
            pyautogui.keyUp('a')
    
    def right(self, direction: Directions, duration=-1):
        pyautogui.keyDown('d')
        dir = 'w' if direction.is_forward_facing() else 's'
        pyautogui.keyDown(dir)
        if duration > 0:
            pyautogui.sleep(duration)
            pyautogui.keyUp(dir)
            pyautogui.keyUp('d')
    
    def jump(self, amount=1, freq=0.1):
        for _ in range(amount):
            pyautogui.keyDown('space')
            pyautogui.keyUp('space')
            if amount > 1:
                pyautogui.sleep(freq)


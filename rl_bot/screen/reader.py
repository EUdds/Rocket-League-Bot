from PIL import ImageGrab
import win32gui


class RLManager:
    def __init__(self):
        self.hwnd = None
    
    def _get_rl_window(self):
        def enum_cb(hwnd, unused):
            winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
        toplist, winlist = [], []
        win32gui.EnumWindows(enum_cb, toplist)
        rl = [(hwnd, title) for hwnd, title in winlist if 'rocket league' in title.lower()]
        if len(rl) > 0:
            rl = rl[0]
            hwnd = rl[0]
            return hwnd
        else:
            raise ValueError("Rocket League window not found")

    def grab_rl_frame(self, show: bool=False) -> ImageGrab.Image: 
        if self.hwnd is None:
            self.hwnd = self._get_rl_window()
        win32gui.SetForegroundWindow(self.hwnd)
        bbox = win32gui.GetWindowRect(self.hwnd)
        img = ImageGrab.grab(bbox)
        if show:
            img.show()
        return img


if __name__ == '__main__':
    manager = RLManager()
    manager.grab_rl_frame(show=True)
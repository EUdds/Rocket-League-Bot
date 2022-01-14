from rl_bot.interface.controls import RLInterface
def test_imports():
    interface = RLInterface()
    assert interface.get_screen_size() == (1920, 1200)

def test_forward():
    interface = RLInterface()
    interface.forward(duration=0.5)
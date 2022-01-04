import gui
import init

try:
    l = init.login()
    temp = l.check()
    l.close()
    win = gui.Window(temp)
except:
    print("Error")
    pass
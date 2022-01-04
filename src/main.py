import gui
import init

try:
    l = init.login()
    temp = l.check()
    #TODO: l.close doesnt work, try and fix
    l.close()
    win = gui.Window(temp)
except:
    print("Error")
    pass
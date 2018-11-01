# 180/200 - PD Great work. A few more getters would be good; but you have shown you understand!

from screens import *
from getInput import *
import story1
import story2
import story3


print showSplash()
raw_input("Press Enter to Start")

go = True
while go:
    print showMenu()
    response = getMenuInput()
    if response == "Q":
        go = False
        print "I can't believe you escaped... We will get you next time!"
    elif response == "1":
        print story1.playMadlibs()
    if response == "2":
        print story2.playMadlibs()
    if response == "3":
        print story3.playMadlibs()
        raw_input("Press Enter to Continue")
    else:
        print "OMG Got invalid menu option!!!"

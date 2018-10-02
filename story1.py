from getInput import *

def playMadlibs():
    place1 = getWord("Enter a place: ")
    friend1 = getWord ("Enter a friend name: ")
    numClowns = getNumber("Enter a number: ", 2, 500)
    clowns1 = getWord("Enter a pluaral clown name: ")
    place2 = getWord ("Enter a place inside place1: ")
    
    
    output = ""
    output += "One day I was walking through " + place1
    output += ". Suddenly " + place1
    output += " started filling up with " + numClowns + " " + clowns1
    output += ". " + friend1
    output += " and I ran and hid in " + place2 + "" "."
    
    
    
    return output

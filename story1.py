from getInput import *

def playMadlibs():
    place1 = getWord("Enter a place: ")
    friend1 = getWord ("Enter a friend name: ")
    numClowns = getNumber("Enter a number: ", 2, 500)
    clowns1 = getPlural("Enter a pluaral clown name: ")
    place2 = getWord ("Enter a place inside place1: ")
    object1 = getWord ("Enter an object: ")
    verb1 = getWord ("Enter a verb ending in ing: ")
    verb2 = getWord ("Enter a verb: ")
    verb3 = getWord ("Enter a verb: ")
    
     
    output = ""
    output += "One day I was walking through " + place1
    output += ". Suddenly " + place1
    output += " started filling up with " + numClowns + " " + clowns1
    output += ". " + friend1
    output += " and I ran and hid in a " + place2 + "" "."
    output += " All the " + clowns1 + " started running in our direction. "
    output += friend1 + " pulled out a " + object1 + " and started " + verb1
    output += ". " 
    output += "The " + clowns1 + " broke into the " + place2 + " and the " + object1 + " rendered useless."
    output += " To escape I had to " + verb2 + " out of " + place2 + " and " + verb3 + " to saftey. " 
    return output

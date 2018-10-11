from getInput import *


def playMadlibs():
    place1 = getWord ("Enter a place: ")
    friend1 = getWord ("Enter a friend name:")
    clown1 = getWord ("Enter a clown name:")
    clownarmy1 = getWord ("Enter a clown army name:")
    civilian1 = getWord ("Enter a civilian name:")
    place2 = getWord ("Enter a place inside place1:")
    name1 = getWord ("Enter a name for yourself:")
    object1 = getWord ("Enter a weapon to use:")
    escaperoute1 = getWord ("Enter an escape route to block:")
    


    output = ""
    output += "We were all ready to go attack " + place1 + " everyone was ready. " 
    output += "Me and " + friend1 + " were putting on our clown suits. "
    output += "When we were loading in the truck " + clown1 + " asked me if I brought the special tool. "
    output += "We have a huge number of clowns with us, our name is " + clownarmy1 + " and we aren't happy clowns. "
    output += "We enter " + place1 + " a bunch of people escape, there are about 2 people left to capture. "
    output += "We see " + civilian1 + " sprinting to " + place2 + " we all sprint after them. "
    output += "I see one of them and say, Hi my name is " + name1 + " come on out. "
    output += "I pull out " + object1 + " start running after them. "
    output += "I tell " + clown1 + " to go block off " + escaperoute1 + " and he runs away to do that. "
    output += "I see them running to " + escaperoute1 + " and I think they are going to beat " + clown1 + " to it. "
    output += "I see them escape just before " + clown1 + " gets there. "
    output += "C'mon guys! We were supposed to get them, we are " + clownarmy1 + " we never loose!"
    return output

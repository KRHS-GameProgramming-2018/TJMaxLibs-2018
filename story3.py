from getInput import *

def playMadlibs():
    place1 = getWord ("Enter the place from previous story: ")
    worker1 = getWord ("Enter a worker: ")
    clown1 = getWord ("Enter a clown name: ")
    clownarmy1 = getWord ("Enter a clown army name: ")
    verb1 = getWord ("Enter a verb: ")
    object1 = getWord ("Enter an object: ")
    verb2 = getWord ("Enter a verb ending in ing: ")
    worker2 = getWord ("Enter a boy worker name: ")
    civilian1 = getWord ("Enter a civilian name: ")
    
    output = "" 
    output += "One day, me and " + worker1 + "were working at our local " + place1 + " when suddenly we heard a sound. "
    output += "The sound came from the back of the store where " + worker2 + " usually hung out during work. "
    output += "We decided to go and check it out. We got there to find a face that I recognized. "
    output += "It was " + civilian1 + " , the brother of " + worker2 + "who was nowhere to be seen. "
    output += "I saw a " + object1 + " fly across the room and i followed it to see it land in front of a cheap looking clown. "
    return output

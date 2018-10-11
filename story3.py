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
    output += "I saw a " + object1 + " leave his hand and " + verb1 + " across the room and i followed it to see it land in front of a cheap looking clown. "
    output += "We both recognized the clown to be " + worker2 + " and we knew what was going on. "
    output += " He was mad that his mom let " + civilian1 + "have a party in her basement but not him. He was triggered so he became " + clown1 + ". "
    output += "He knew his brother was scared of clowns so he formed the " + clownarmy1 + " and came to scare him. "
    output += "Me, " + civilian1 + ", and his friend left to go eat while " + clown1 + " and " + clownarmy1 + " started " + verb2 + " on the ground. "
    return output

def getMenuInput():
    goodInput = False
    while not goodInput:
        response = raw_input(" > ")
        if (response == "1" 
            or response == "One"):
            response = "1"
            goodInput = True
        if (response == "2"
            or response == "Two"):
            response = "2"
            goodInput = True    
        if (response == "Q"
              or response == "Quit"
              or response == "q"
              or response == "quit"
              or response == "X"
              or response == "Exit"):
              response = "Q"
              goodInput = True        
        if (response == "3"
            or response == "Three"):
            response = "3"
            goodInput = True
        else:
            print "Ha! You thought you could escape us! Now the Clowns are coming after you, best bet is to finish the story!"
    return response
    
def getWord(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "The clowns won't like those words!"
    return word
    
def getNumber(prompt, minNumber, maxNumber):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt+" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") ")
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        goodInput = True
        for character in word:
            if character not in nums:
                print "not a number"
                goodInput = False
                break
        if goodInput and (int(word) < minNumber or int(word) > maxNumber):
            goodInput = False
            print "Out of Range"
        
            
    return word

def isSwear(word):
    swearList = ["poop",
                "piss" ,
                "Fuck" ,
                "shit" ,
                "pussy" ,
                "fuck" ,
                "Pussy" ,
                "Shit" ,
                "Crap" ,
                "crap" ,
                "Fucker" ,
                "fucker" ,
                "cunt" ,
                "Cunt" ,
                "Bitches" ,
                "bitch" ,
                "Bitch" ,
                "FuCk" ,
                "fUcK" ,
                "FUCK" ,
                "nigger" ,
                "NiGgEr" ,
                "Nigga" ,
                "nigga" ,
                "minecraft" ,
                "porn" ,
                "faggot" ,
                "Faggot" ,
                "fAgGoT" ,
                "Mother Fucker" ,
                "Ass" ,
                "Nazi" ,
                "Choad",
                "Cock",
                "Butt Fucker",
                "Fuck Me Backwards",
                "Damn",
                "Queer",
                "Ligma",
                "Ninja",
                "Suckma",
                "Fuckma", ]
                
                
                
    if word in swearList:
        return True
    else:
        return False

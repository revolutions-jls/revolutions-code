def religionfree():
    while True:
        answer = raw_input("Are your people free to follow their ideals? [y/n] : ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print "i'm not sure what you meant by that"
            continue

def govcontrol():
    while True:
        answer = raw_input("Does the government have totalitarian-esque control over the people? [y/n] : ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print "i'm not sure what you meant by that"
            continue
#tacobucks
def needsrespond():
    while True:
        answer = raw_input("Is the government responding to the needs of a sufficient portion of the people? [y/n] : ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print "i'm not sure what you meant by that"
            continue

def econstatus():
    while True:
        answer = raw_input("Is the economy failing or on a very apparent downturn? Are there high taxes or unfair labor laws? [y/n] : ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print "[i'm not sure what you meant by that]"
            continue

def outsidesupp():
    while True:
        answer = raw_input("Can either party [either the rebels or the government] procure outside support? [y/n] : ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print "[i'm not sure what you meant by that]"
            continue








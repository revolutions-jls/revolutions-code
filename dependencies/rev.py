#these functions are largely quite repetitive
#but we use them to keep the code in revflow.py a little less...
#catastrophic?
def religionfree():
    while True:
        answer = input("Are your people free to follow their ideals? [y/n] : ")
        if answer == "y":
            return False
        elif answer == "n":
            return True
        else:
            print ("[i'm not sure what you meant by that]")
            continue

def govcontrol():
    while True:
        answer = input("Does the government have totalitarian-esque control over the people? [y/n] : ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print ("[i'm not sure what you meant by that]")
            continue
#tacobucks
def needsrespond():
    while True:
        answer = input("Is the government responding to the needs of a sufficient portion of the people? [y/n] : ")
        if answer == "y":
            return False
        elif answer == "n":
            return True
        else:
            print ("[i'm not sure what you meant by that]")
            continue

def econstatus():
    while True:
        answer = input("Is the economy failing or on a very apparent downturn? Are there high taxes or unfair labor laws? [y/n] : ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print ("[i'm not sure what you meant by that]")
            continue

def outsidesupp():
    while True:
        answer = input("Can either party [either the rebels or the government] procure outside support? [y/n] : ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print ("[i'm not sure what you meant by that]")
            continue

def supprecieve():
    while True:
        answer = input("Which party is receiving the support, the rebels or the government?  [r/g] : ")
        if answer == "g":
            return False
        elif answer == "r":
            return True
        else:
            print ("[i'm not sure what you meant by that]")
            continue

def oppose():
    while True:
        answer = input("Are there people who oppose the power? [y/n] : ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print ("[i'm not sure what you meant by that]")
            continue

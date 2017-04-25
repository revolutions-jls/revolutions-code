import time
y = "y"
n = "n"
g = "g"
r = "r"
govcontrol = 7
outsidesupp = 7
religionfree = 7
oppose = 7
econstatus = 7
suppreceive = 7
# sean is garbage at coding
# eat it sean
gbfwycfd = "Go back from whence you came, foul Demon!"
safety = "You are doing okay. No revolution here."
print ("the")
time.sleep(1)
print ("revolutionary")
time.sleep(1)
print ("revolution")
time.sleep(1)
print ("flowchart")
time.sleep(1)
print ("made by Joe Salmon, Sean Hong, and Luke Dunn")
time.sleep(1)
print ("enjoy")
time.sleep(1)
print ("-- -- -- --")
time.sleep(1) #git test
while True:
    religionfree = raw_input("Are your people free to follow their ideals? [y/n] : ")
    if religionfree == y:
        while True:
            govcontrol = raw_input("Does the government have totalitarian-esque control over the people? [y/n] : ")
            if govcontrol == y:
                while True:
                    needsrespond = raw_input("Is the government responding to the needs of a sufficient portion of the people? [y/n] : ")
                    if needsrespond == y:
                        print ("There are a few anti-totalitarianists about. You may need more propaganda.")
                    elif needsrespond == n:
                        while True:
                            econstatus = raw_input("Is the economy failing or on a very apparent downturn? Are there high taxes or unfair labor laws? [y/n] : ")
                            if econstatus == y:
                                while True:
                                    outsidesupp = raw_input("Can either party [either the rebels or the government] procure outside support? [y/n] : ")
                                    if outsidesupp == y:
                                        while True:
                                            suppreceive = raw_input("Are the rebels or the government recieving the support? [r/g] : ")
                                            if suppreceive == r:
                                                print ("Viva de la Revolucion!")
                                            elif suppreceive == g:
                                                while True:
                                                    oppose = raw_input("Are there people opposing the government / current power? [y/n] : ")
                                                    if oppose == y:
                                                        print ("A possible civil war. Stockpile.")
                                                    elif oppose == n:
                                                        print "[that's not what I asked you]"
                                                    else:
                                                        print "[that's not what I asked you]"
                                                        continue
                                            else:
                                                print "[that's not what I asked you]"
                                                continue
                                    else:
                                        print "[that's not what I asked you]"
                                        continue
                            else:
                                print "[that's not what I asked you]"
                                continue
                    else:
                        print "[that's not what I asked you]"
                        continue
            elif govcontrol == n:
                while True:
                    needsrespond = raw_input("Is the government responding to the needs of a sufficient portion of the people? [y/n] : ")
                    if needsrespond == y:
                        print ("There are a few anti-totalitarianists about. You may need more propaganda.")
                    elif needsrespond == n:
                        while True:
                            econstatus = raw_input(
                                "Is the economy failing or on a very apparent downturn? Are there high taxes or unfair labor laws? [y/n] : ")
                            if econstatus == y:
                                while True:
                                    outsidesupp = raw_input(
                                        "Can either party [either the rebels or the government] procure outside support? [y/n] : ")
                                    if outsidesupp == y:
                                        while True:
                                            suppreceive = raw_input("Are the rebels or the government recieving the support? [r/g] : ")
                                            if suppreceive == r:
                                                print ("Viva de la Revolucion!")
                                            elif suppreceive == g:
                                                while True:
                                                    oppose = raw_input("Are there people opposing the government / current power? [y/n] : ")
                                                    if oppose == y:
                                                        print ("A possible civil war. Stockpile.")
                                                    if oppose == n:
                                                        print ("There is some civil unrest.")
                                                    else:
                                                        print "[that's not what I asked you]"
                                                        continue
                                            else:
                                                print "[that's not what I asked you]"
                                                continue
                                    elif outsidesupp == n:
                                        print ("There is some civil unrest.")
                                    else:
                                        print "[that's not what I asked you]"
                                        continue
                            if econstatus == n:
                                print gbfwycfd
                            else:
                                print "[that's not what I asked you]"
                                continue
                    else:
                        print "[that's not what I asked you]"
                        continue
            else:
                print "[that's not what I asked you]"
                continue
    elif religionfree == n:
            govcontrol = raw_input("Does the government have totalitarian-esque control over the people? [y/n] : ")
            if govcontrol == y:
                needsrespond = raw_input("Is the government responding to the needs of a sufficient portion of the people? [y/n] : ")
                if needsrespond == y:
                    print ("There is some civil unrest.")
                elif needsrespond == n:
                    econstatus = raw_input("Is the economy failing or on a very apparent downturn? Are there high taxes or unfair labor laws? [y/n] : ")
                    if econstatus == y:
                        outsidesupp = raw_input("Can either party [either the rebels or the government] procure outside support? [y/n] : ")
                        if outsidesupp == y:
                            suppreceive = raw_input("Are the rebels or the government recieving the support? [r/g] : ")
                            if suppreceive == r:
                                print ("Viva la Revolution!")
                            if suppreceive == g:
                                oppose = raw_input("Are there people opposing the government / current power? [y/n] : ")
                                if oppose == y :
                                    print ("A possible civil war. Stockpile.")
                                if oppose == n:
                                    print ("There is some civil unrest.")
                        if outsidesupp == n:
                            print ("There is some civil unrest.")
                    if econstatus == n:
                        outsidesupp = raw_input(
                            "Can either party [either the rebels or the government] procure outside support? [y/n] : ")
                        if outsidesupp == y:
                            suppreceive = raw_input("Are the rebels or the government recieving the support? [r/g] : ")
                            if suppreceive == r:
                                print ("Viva la Revolution!")
                            if suppreceive == g:
                                oppose = raw_input("Are there people opposing the government / current power? [y/n] : ")
                                if oppose == y:
                                    print ("A possible civil war. Stockpile.")
                                if oppose == n:
                                    print ("There is some civil unrest.")
            elif govcontrol == n:
                needsrespond = raw_input("Is the government responding to the needs of a sufficient portion of the people? [y/n] : ")
                if needsrespond == y:
                    if govcontrol == y:
                        if needsrespond == y:
                            print ("A lack of general freedom will probably cause some civil unrest.")
                        elif needsrespond == n:
                            econstatus = raw_input(
                                "Is the economy failing or on a very apparent downturn? Are there high taxes or unfair labor laws? [y/n] : ")
                            if econstatus == y:
                                outsidesupp = raw_input(
                                    "Can either party [either the rebels or the government] procure outside support? [y/n] : ")
                                if outsidesupp == y:
                                    suppreceive = raw_input(
                                        "Are the rebels or the government receiving the support? [r/g] : ")
                                    if suppreceive == r:
                                        print ("Viva de la Revolucion!")
                                    if suppreceive == g:
                                        oppose = raw_input(
                                            "Are there people opposing the government / current power? [y/n] : ")
                                        if oppose == y:
                                            print ("A possible civil war. Stockpile.")
                                        if oppose == n:
                                            print ("There is some civil unrest.")
                    elif govcontrol == n:
                        print ("A lack of idealistic freedom may cause civil unrest.")
                elif needsrespond == n:
                    econstatus = raw_input("Is the economy failing or on a very apparent downturn? Are there high taxes or unfair labor laws? [y/n] : ")
                    if econstatus == y:
                        outsidesupp = raw_input("Can either party [either the rebels or the government] procure outside support? [y/n] : ")
                        if outsidesupp == y:
                            suppreceive = raw_input("Are the rebels or the government recieving the support? [r/g] : ")
                            if suppreceive == r:
                                print ("Viva de la Revolucion!")
                            if suppreceive == g:
                                oppose = raw_input("Are there people opposing the government / current power? [y/n] : ")
                                if oppose == y:
                                    print ("A possible civil war. Stockpile.")
                                if oppose == n:
                                    print ("There is some civil unrest.")
                        if outsidesupp == n:
                            outsidesupp = raw_input(
                                "Can either party [either the rebels or the government] procure outside support? [y/n] : ")
                            if outsidesupp == y:
                                suppreceive = raw_input("Are the rebels or the government recieving the support? [r/g] : ")
                                if suppreceive == r:
                                    print ("Viva de la Revolucion!")
                                if suppreceive == g:
                                    oppose = raw_input("Are there people opposing the government / current power? [y/n] : ")
                                    if oppose == y:
                                        print ("A large amount of the people are unhappy, presumably with the lack of ability to make idealistic choices and the government's lack of response. With a little more motivation, revolution or even civil war could occur.")
                                    if oppose == n:
                                        print ("An amount of the people are unhappy, and this could lead to other things given the right push.")
                    if econstatus == n:
                        outsidesupp = raw_input(
                            "Can either party [either the rebels or the government] procure outside support? [y/n] : ")
                        if outsidesupp == y:
                            suppreceive = raw_input("Are the rebels or the government recieving the support? [r/g] : ")
                            if suppreceive == r:
                                print ("Viva de la Revolucion!")
                            if suppreceive == g:
                                oppose = raw_input("Are there people opposing the government / current power? [y/n] : ")
                                if oppose == y:
                                    print ("A possible civil war. Stockpile.")
                                if oppose == n:
                                    print ("There is some civil unrest.")
                        if outsidesupp == n:
                            outsidesupp = raw_input(
                                "Can either party [either the rebels or the government] procure outside support? [y/n] : ")
                            if outsidesupp == y:
                                suppreceive = raw_input("Are the rebels or the government receiving the support? [r/g] : ")
                                if suppreceive == r:
                                    print ("Viva de la Revolucion!")
                                if suppreceive == g: # don't plagiarize me - bad things might happen :D
                                    oppose = raw_input("Are there people actively opposing the government / current power? [y/n] : ")
                                    if oppose == y:
                                        print ("A large amount of the people are unhappy, presumably with the lack of ability to make idealistic choices and the government's lack of response. With a little more motivation, revolution or even civil war could occur.")
                                    if oppose == n:
                                        print (
                                        "An amount of the people are unhappy, and this could lead to other things given the right push.")
            else:
                print "[that's not what I asked you]"
                continue
    else:
        print "[that's not what I asked you]"
        continue

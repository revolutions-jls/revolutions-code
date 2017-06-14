#coded by j. salmon as walmart-givenchii
#luke did none of this
from dependencies import rev as r
import time
#update 5/29/17
#so i tested it and found a lot of bugs
#serves me right i suppose?
#   -joe
placeholder = "[we don't serve your kind here]"
#print (placeholder)
intro = input("intro? [y/n] : ")
if intro == "y":
    print ("the")
    time.sleep(1.5)
    print ("revolutionary")
    time.sleep(1.5)
    print ("revolution")
    time.sleep(1.5)
    print ("flowchart")
    time.sleep(1.5)
    print ("(now with functions)")
    time.sleep(1.5)
    print ("made by Joe Salmon, Sean Hong, and Luke Dunn")
    time.sleep(1.5)
    print ("enjoy")
    time.sleep(1.5)
    print ("-- -- -- --")
time.sleep(1.5)
if r.oppose():
    if r.govcontrol():
        if r.needsrespond():
            if r.econstatus():
                if r.religionfree():
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("Even though you may have been able to procure some amount of outside support, chances are it won't be enough. You've done pretty much everything wrong, and it would be very unlikely for a revolution to not occur.")
                        else:
                            print ("Seven wrongs do NOT make a right, no matter what anyone tells you. You are the poster child for creating horrific political states. Just call it quits, dude. You're absolutely screwed. Get ready for a revolution or very possibly a civil war. In fact, it's rather suprising it hasn't happened already.")
                    else:
                        print ("This is what we in the business like to call a 'volatile situation.' You are literally right on the edge of a revolution. The one thing that would mean your doom at this point would be outside support for the rebels. If that happens, say bye-bye. ")
                else:
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("'Welcome to Haiti. Let me show you our slaves. We're very proud of them. Oh, crap! They've gone and overthrown the government with the help of the Spanish!' Let me phrase this dramatically: 'Oh, how the tables have turned!' That's right, ladies and gentlemen, you've got a revolution.")
                        else:
                            print ("You're in a tight spot. A really, really tight spot. In fact, the only thing keeping you from a revolution right now are whoever decided to lend your lucky self a hand. Be very, very careful and don't give anyone any more reasons than they already have to mess you up.")
                    else:
                        print ("This is what we in the business like to call a 'volatile situation.' You are literally right on the edge of a revolution. The one thing that would mean your doom at this point would be outside support for the rebels. If that happens, say bye-bye. ")
            else:
                if r.religionfree():
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("Sorry, friend. I think chances are you've got a revolution on your hands. You've dont nearly everything wrong and the rebels have found someone willing to back them up. But hey, at least your country isn't broke, right! That would really suck.")
                        else:
                            print ("So you can get some support, and your economy and labor situation isn't have bad. But people aren't allowed to follow their ideals, live freely, nor do they have their needs fulfilled. Hate to break it to you, but that sounds like the ticket for a revolt.")
                    else:
                        print ("'Don't move. There's a revolution on your back. Here, let me swat it before it revolts.' That would be your outside support talking, if you had any. Lucky for you, neither do the rebels, so you're probably okay for the time being. This is a solid 'civil unrest' if you were to ask.")
                else:
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("Conditions aren't great for the people, but there's idealistic freedom. Also, they have support. Looks to be right between civil unrest and very close to revolution.")
                        else:
                            print ("There is without a doubt some civil unrest, but nothing you (and your support network) can't deal with in time. You're probably ok.")
                    else:
                        print ("There is without a doubt some civil unrest, but nothing you can't deal with in time. You're probably ok.")
        else:
            if r.econstatus():
                if r.religionfree():
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("You might have totalitarian control, and the rebels might have a bit of support, and you might be heading towards a revolution if things get worse enough, but you're responding to the people's needs and that's not too bad. A solid 'civil unrest.'")
                        else:
                            print ("Things are looking up, man! You've got someome backing you and you're responding to the needs of the people. However, they still lack a lot of freedom and wouldn't be opposed to more. About the definition of civil unrest.")
                    else:
                        print ("A revolution would totally be possible assuming the rebels get support, but not definite. It wouldn't be wise to worry too much. Just stay watchful. ")

                else:
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("Roses are red / Castro's the best / You've got on your hands / some civil unrest.")#a mastahpeece
                        else:
                            print ("")
                    else:
                        print ("c")
            else:
                if r.religionfree():
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("Congratulations, you're probably fine for now. Unless you're the Ming Dynasty, in which the old goverment enlists the help of their mortal enemies to take out the rebel government. They end up getting screwed over and there it all goes.")
                        else:
                            print ("You're done for. Bad economy, no care for the people and a significant number of people against you with outside support backing them.")
                    else: #where everything dies
                        print ("I would be careful if I were you. The possibility for a massive revolt is very low, but that can change very quickly if the rebels get enough support.")
                else:
                    print ("e") #im making an ending here because if no one religionfrees the power, you're probably fine
    else:
        if r.needsrespond():
            if r.econstatus():
                if r.religionfree():
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("You might not have totalitarian control over the people, but you're not responding to their needs either and your economy's gone down the gutter. Not only are there rebels, they also  have support. It would be wise to watch for a revolution.")
                        else:
                            print ("You might not have totalitarian control over the people, but you're not responding to their needs either and your economy's gone down the gutter. But, you've got assistance in dealing with the rebels, so... you're probably fine for now.")
                    else:
                        print ("Noone's happy, but no one has the capability to do anything about it. Looks like civil unrest.")
                else:
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("i")
                        else:
                            print ("You're in a bit of a tight spot, assuming you're not Cuba, in which case you're totally screwed. Otherwise, due to the massive economic problems and your lack of care about the people, people are not very happy and bad things can and will happen when the pendulum swings back around. You may be able to keep things under control, however, since you do have the outside support. Stay safe, man. And watch out for anybody named Castro. ")
                    else:
                        print ("j")
            else:
                if r.religionfree():
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("k")
                        else:
                            print ("l")
                    else:
                        print ("m")
                else:
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("n")
                        else:
                            print ("o")
                    else:
                        print ("p")
        else:
            if r.econstatus():
                if r.religionfree():
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("q")
                        else:
                            print ("r")
                    else:
                        print ("s")
                else:
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("t")
                        else:
                            print ("u")
                    else:
                        print ("v")
            else:
                if r.religionfree():
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("w")
                        else:
                            print ("x")
                    else:
                        print ("y")
                else:
                    if r.outsidesupp():
                        if r.supprecieve():
                            print ("z")
                        else:
                            print ("1")
                    else:
                        print ("2")
else:
    print ("You're probably fine for now. If no one's trying to take you out, chances are it won't happen.")

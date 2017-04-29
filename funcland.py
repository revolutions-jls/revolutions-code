def religionfree():
    while True:
        rf = raw_input("Are your people free to follow their ideals? [y/n] : ")
        if rf == "y":
            print "meme"
            return "y"
        elif rf == "n":
            print "badmeme"
            return "n"
        else:
            print "i'm not sure what you meant by that"
            continue

if religionfree() == "1":
    print "meme"
elif religionfree() == "0":
    print "meme extreme"


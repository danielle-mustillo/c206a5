def writeWebPage(param, param2, param3):
    print "Hello"
    """ The following part of the program should regenerate a webpage."""
    
    try:
        input = open("room.html", "r")
        out = open("newRoom.html", "w");
        x = input.readlines();
        inputTuple = []
        for line in x:
            singleLine = line.rstrip()
            inputTuple.append(singleLine)
            out.write(singleLine)
    except IOError:
        print "problem"
    
    
    print x
    print 'Hello World'
    
writeWebPage(1,1,1)

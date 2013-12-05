#!/usr/bin/python
import cgi
import re

#some shit here
form = cgi.FieldStorage()

"""We decided as a team to create a copy of the room page here because the room page already has the required functionality we desire already (it does all of the functions already). Therefore, the user will eventually travel to game.py once they click on anything"""

"""get the input data from the form.
if there is data that doesn't exist for some reason (incorrect feeding page, etc), 
then just initialize to default commands. 
"""
global page
global coins
global gamestatus
global inventory1
global inventory2
global inventory3
global inventory4
global inventory5
global command

#the page, gamestatus and command variables are set to default because they are used internally in this site. 
page = 'room'
if form.has_key('coins'):
	coins = form.getvalue('coins')
else:
	coins = '100'
gamestatus = ""
if form.has_key('inventory1'):
	inventory1 = form.getvalue('inventory1')
else:
	inventory1 = ""
if form.has_key('inventory2'):
	inventory2 = form.getvalue('inventory2')
else:
	inventory2 = ""
if form.has_key('inventory3'):
	inventory3 = form.getvalue('inventory3')
else:
	inventory3 = ""
if form.has_key('inventory4'):
	inventory4 = form.getvalue('inventory4')
else:
	inventory4 = ''
if form.has_key('inventory5'):
	inventory5 = form.getvalue('inventory5')
else:
	inventory5 = ""
command = ""

print "Content-Type: text/html\n\n"

#convert the coin value to an integer for processing
try:
	coins = int(str(coins))
except ValueError:
	print "problem"

#reassign the gamestatus so the actions are not counted more than once (don't always get points)
if str(gamestatus)=="right":
	gamestatus = "right2"
	coins += 50
elif str(gamestatus)=="wrong":
	gamestatus = "wrong2"
	coins -= 50

#load the CSV file just incase we need it next
global rfile
try:
	rfile = open("INVENTORY.CSV","r+")
except IOError:
	rfile = open("INVENTORY.CSV", "w")

#each line is a new item, remove trailing backslash n. File is assumed to be a large file separated by backslash n.
lines = rfile.readlines();
for i in range(0,len(lines)):
	lines[i] = lines[i].rstrip()

#tells the user what last happened (right, wrong, or haven't played)
temp = str(command).split(' ')

if temp[0]=="drop":
	try:
		val = int(temp[1])
		if val > 5 or val < 1:
			gamemessage = "Inventory location %d doesn't exist!!!" % val
		elif val==1 and inventory1<>"":
			lines.append(str(inventory1))
			gamemessage = 'You now dropped %s' % inventory1
			inventory1 = ''
		elif val==2 and inventory2<>"":
			lines.append(str(inventory2))
			gamemessage = 'You now dropped %s' % inventory2
			inventory2 = ''
		elif val==3 and inventory3<>"":
			lines.append(str(inventory3))
			gamemessage = 'You now dropped %s' % inventory3
			inventory3 = ''
		elif val==4 and inventory4<>"":
			lines.append(str(inventory4))
			gamemessage = 'You now dropped %s' % inventory4
			inventory4 = ''
		elif val==5 and inventory5<>"":
			lines.append(str(inventory5))
			gamemessage = 'You now dropped %s' % inventory5
			inventory5 = ''
		else:
			gamemessage = "Inventory slot %d doesn't have anything" % val
	except ValueError:
		gamemessage = "I dont understand commander. Please tell me like this: \"drop #\""
#show all equiped items in inventory. 
elif temp[0]=="inventory":
	gamemessage = "Captain, your pack: "
	gamemessage += "<br> 1. %s" % inventory1
	gamemessage += "<br> 2. %s" % inventory2
	gamemessage += "<br> 3. %s" % inventory3
	gamemessage += "<br> 4. %s" % inventory4
	gamemessage += "<br> 5. %s" % inventory5
#show all the items in inventory.csv. 
elif temp[0]=="look":
	gamemessage = "Captain! Your equipement for battle: "
	for i in range(0, len(lines)):
		gamemessage = "%s<br> %d. %s" % (gamemessage,i,lines[i])
#here is the pickup command. Assumed correct input. 
elif temp[0]=="pickup":
	try:
		val = int(temp[1])
		if len(lines) <= val or val < 0:
			gamemessage = "Item %d does not exist" % val
		elif str(inventory1)=="":
			gamemessage = "Your are now equiping: %s" % lines[val]
			inventory1 = lines[val]
			lines.remove(lines[val])
		elif str(inventory2)=="":
			gamemessage = "You are now equiping: %s" % lines[val]
			inventory2 = lines[val]
			lines.remove(lines[val])
		elif str(inventory3)=="":
			gamemessage = "You are now equiping: %s" % lines[val]
			inventory3 = lines[val]
			lines.remove(lines[val])
		elif str(inventory4)=="":
			gamemessage = "You are now equiping: %s" % lines[val]
			inventory4 = lines[val]
			lines.remove(lines[val])
		elif str(inventory5)=="":
			gamemessage = "You are now equiping: %s" % lines[val]
			inventory5 = lines[val]
			lines.remove(lines[val])
		else: gamemessage = "Your pack is full commander!"
	except ValueError:
		gamemessage = "I don't understand commanderi. Please type \"pickup #\""
#if the user enters garbage as an order, or just nothing, these default statuses are displayed. 
else: 
	gamemessage = "In Orbit"
	if str(gamestatus)=="right2":
		gamemessage = "<font color=\"green\">Houston, Tranquility Base here. The eagle has landed... You have: %s dollars </font>" % coins
	elif str(gamestatus)=="wrong2":
		gamemessage = "<font color=\"red\">Housten, we have a problem... You have: %s dollars</font>" % coins

#now just write everything that has changed back to the file.
#if nothing changed, then just rewrite old information.
rfile.close()
wfile = open("INVENTORY.CSV", 'w')
for line in lines:
	wfile.write(line)
	wfile.write('\n')
wfile.close()

if coins <= 0:
	print '<a href="http://www.cs.mcgill.ca/~hzhao28/ass5/index.html"> You lost!!! You should log back in </a>'
elif form.getvalue('page')=="riddle":
	print """
	<html>
                <head>
                        <style type="text/css">
                                /* set up a new font*/
                                @font-face{
                                        font-family : nasa;
                                        src: url(nasa.ttf);
                                }
                                body {
                                        background-image: url('interior.jpg');
                                        background-size: 100% 100%;
                                        max-height: 100%;
                                        max-width: 100%;
                                        margin-left : auto;
                                        margin-right : auto;
                                        background-attachment:fixed;
                                        background-position: center;

                                        top: 0;
                                        left: 0;
                                }

                                #button {
                                        padding: 20px;
                                        background-image : url("hatch_big.jpg");
                                        background-size : 100% 100%;
                                        min-height : 150px;
                                        min-width : 200px;
                                        max-height : 200px;
                                        max-width : 200px;
                                }

                                #mission {
                                        padding: 20px;
                                        margin-left: auto;
                                        margin-right: auto;
                                        background-image : url("moon.jpg");
                                        background-size : 100% 100%;
                                        min-height : 400px;
                                        min-width : 400px;
                                        max-height : 400px;
                                        max-width : 400px;
                                }

                                #text-box{
                                        width: 600px;
                                        margin: 20px auto;
                                        padding: 10px;
                                        background-color: rgba(25,25,25,0.9);
                                        /*prefix to support box-shadow*/
                                        -webkit-box-shadow: 0 0 20px black;
                                        -moz-box-shadow: 0 0 20px black;
                                        box-shadow: 0 0 20px black;
                                }

                                #location-box{
                                        width: 600px;
                                        margin: 20px auto;
                                        padding: 10px;
                                        background-color: rgba(125,125,125,0.7);
                                        /*prefix to support box-shadow*/
                                        -webkit-box-shadow: 0 0 20px black;
                                        -moz-box-shadow: 0 0 20px black;
                                        box-shadow: 0 0 20px black;
                                }

                                #pad e
                                        paddina webpage : 20px;
                                }

                                #image-box{
                                        background-image : url("hatch_big.jpg");
                                        position: relative;
                                        min-height: 100px
                                        min-width: 100px;
                                        margin: 20px auto;
                                        padding: 1px;
                                        background-color: rgba(49,97,145,0.7);
                                        /*prefix to support box-shadow*/
                                        -webkit-box-shadow: 0 0 20px black;
                                        -moz-box-shadow: 0 0 20px black;
                                        box-shadow: 0 0 20px black;
                                }
                                p{
                                        text-align : justify;
                                        font : 20px nasa, Serif;
                                        margin : 0 0 0px 0;
                                        color : f9f6f2;
                                }
                                a, h1{
                                        text-align : center;
                                        color:f9f6f2;
                                        font-family:nasa
                                }


                                </style>
                </head>
<body>
        <div id="text-box">
        <h1> Welcome to your mission </h1>
        </div>

        <div id="location-box">
        <p> The fate of humanity rests in your hands. Answer this riddle to destroy the alien invasion!!!</p>
                <br>

        <p> Why didn't the sun go to college? </p> 
		<form name="answer" action="game.py" method="post">"""
	print "	<input type=\"hidden\" name=\"page\" value=\"room\">"
	#do not need game status, that is handled below!
	print "	<input type=\"hidden\" name=\"coins\" value=\"%d\">" % coins 
	print "	<input type=\"hidden\" name=\"inventory1\" value=\"%s\"> " % inventory1
	print "	<input type=\"hidden\" name=\"inventory2\" value=\"%s\"> " % inventory2
	print "	<input type=\"hidden\" name=\"inventory3\" value=\"%s\"> " % inventory3
	print "	<input type=\"hidden\" name=\"inventory4\" value=\"%s\"> " % inventory4
	print "	<input type=\"hidden\" name=\"inventory5\" value=\"%s\"> " % inventory5
	print """ <table border="0">
                                <tr>
                                        <td> <p> Answer: </p> </td>
                                </tr>
                                <tr>
                                        <td> <p> <input type="radio" name="gamestatus" value="right"> Because it already had a million degrees! </p> </td>
                                </tr>
                                <tr>
                                        <td> <p> <input type="radio" name="gamestatus" value="wrong"> Because it burned all the bridges there! </p> </td>
                                </tr>
                                <tr>
                                        <td> <input type="submit" value="Answer"> </td>
                                </tr>
                        </table>
                </form>
        </div>
        <div id="text-box">
                <br>
		<form name="back" action="game.py" method="post">
			<input type="hidden" name="page" value="room">"""
	print '		<input type="hidden" name="coins" value="%d">' % coins
	print '	 	<input type="hidden" name="inventory1" value="%s">' % inventory1
	print ' 	<input type="hidden" name="inventory2" value="%s">' % inventory2
	print '		<input type="hidden" name="inventory3" value="%s">' % inventory3
	print '		<input type="hidden" name="inventory4" value="%s">' % inventory4
	print '		<input type="hidden" name="inventory5" value="%s">' % inventory5
	print '		<input type="hidden" name="command" value="%s">' % command
        print """	<input type="submit" value="Back to Command Center">
		</form>        
	</div>


</body>

</html>
	"""
#this is the room page.
else:
	print """<html>
	<head>
	<style type="text/css">
		/* set up a new font*/
		@font-face{
			font-family : nasa;
			src: url(nasa.ttf);
		}
		body {
			background-image: url('interior.jpg');
			background-size: 100% 100%;
			max-height: 100%;
			max-width: 100%;
			margin-left : auto;
			margin-right : auto;
			background-attachment:fixed;
			background-position: center;
			
			top: 0;
			left: 0;
		}

		#button {
			padding: 20px;
			background-image : url("hatch_big.jpg");
			background-size : 100% 100%;
			min-height : 150px;
			min-width : 200px;
			max-height : 200px;
			max-width : 200px;
		}

		#cupola {
			padding: 20px;
			background-image : url("cupola.jpg");
			background-size : 100% 100%;
			min-height : 200px;
			min-width : 200px;
			max-height : 200px;
			max-width : 200px;
		}

		#tranquility {
			padding: 20px;
			background-image : url("tranquility.jpg");
			background-size : 100% 100%;
			min-height : 185px;
			min-width : 200px;
			max-height : 200px;
			max-width : 200px;
		}

		#destiny {
			padding: 20px;
			background-image : url("destiny.jpg");
			background-size : 100% 100%;
			min-height : 185px;
			min-width : 200px;
			max-height : 200px;
			max-width : 200px;
		}

		#exoplanet {
			padding: 20px;
			background-image : url("exoplanet.jpg");
			background-size : 100% 100%;
			min-height : 186px;
			min-width : 200px;
			max-height : 200px;
			max-width : 200px;
		}


		
		#mission {
			padding: 20px;
			
			background-image : url("moon.jpg");
			background-size : 100% 100%;
			min-height : 400px;
			min-width : 400px;
			max-height : 400px;
			max-width : 400px;
			margin-left: auto;
			margin-right: auto;
		}
		
		#text-box{
			width: 600px;
			margin: 20px auto;
			padding: 10px;
			background-color: rgba(25,25,25,0.9);
			/*prefix to support box-shadow*/
			-webkit-box-shadow: 0 0 20px black;
			-moz-box-shadow: 0 0 20px black;
			box-shadow: 0 0 20px black;
		}
		
		#location-box{
			width: 600px;
			margin: 20px auto;
			padding: 10px;
			background-color: rgba(125,125,125,0.7);
			/*prefix to support box-shadow*/
			-webkit-box-shadow: 0 0 20px black;
			-moz-box-shadow: 0 0 20px black;
			box-shadow: 0 0 20px black;
		}
		
		#pad {
			padding : 20px;
		}
		
		#image-box{
			background-image : url("hatch_big.jpg");
			position: relative;
			min-height: 100px
			min-width: 100px;
			margin: 20px auto;
			padding: 1px;
			background-color: rgba(49,97,145,0.7);
			/*prefix to support box-shadow*/
			-webkit-box-shadow: 0 0 20px black;
			-moz-box-shadow: 0 0 20px black;
			box-shadow: 0 0 20px black;
		}
		p{
			text-align : center;
			font : 20px nasa, Serif;
			margin : 0 0 0px 0;
			color : f9f6f2;
		}
		a, h1{
			text-align : center;
			color:f9f6f2;
			font-family:nasa
		}
		
		
		</style>
</head>

<body>

<div id="text-box">
	<h1> The Mission
	</h1>
	<form action="http://www.cs.mcgill.ca/~dmusti/comp206/ass5/game.py" method="POST"> """
	print	"<input type=\"hidden\" name=\"coins\" value=\"%s\">" % coins
	print	'<input type="hidden" name="gamestatus" value="%s"> ' % gamestatus
	print	"<input type=\"hidden\" name=\"inventory1\" value=\"%s\">" % inventory1
	print	"<input type=\"hidden\" name=\"inventory2\" value=\"%s\">" % inventory2
	print	"<input type=\"hidden\" name=\"inventory3\" value=\"%s\">" % inventory3
	print	"<input type=\"hidden\" name=\"inventory4\" value=\"%s\">" % inventory4
	print	"<input type=\"hidden\" name=\"inventory5\" value=\"%s\">" % inventory5
	print	"<input type=\"hidden\" name=\"command\" value=\"%s\">" % command
	print	"<input type=\"hidden\" name=\"page\" value=\"riddle\">"
	print """	<input type="submit" value="" id="mission"> </input>
	</form>
</div>

<div id="text-box">
	<p> Adjutant Message: <p> """
	#print out the user message for the user
	print '<p> %s <p>' % gamemessage
	print """
</div>
	
<div id="location-box">
	<table border="0" align="center">
		<tr>
			<td> <p> Destiny(US LAB) </p>
			</td>
			<td id="pad">
			</td>
			<td> <p> Tranquility (Node 3)</p>
			</td>
		</tr>
		<tr>
			<td>
				<a href="http://cs.mcgill.ca/~jhalpe5/RoomPage.html">
					<div id="destiny">
					</div>
				</a>
			</td>
			<td id="pad">
			</td>
			<td>
				<a href="http://www.cs.mcgill.ca/~ychen225/COMP206/room.html">
					<div id="tranquility">
					</div>
				</a>
			</td>
		</tr>
		<tr>
			<td> <p> Exoplanet #1029 </p>
			</td>
			<td id="pad">
			</td>
			<td> <p> The Cupola </p>
			</td>
		</tr>
		<tr>
			<td>
				<a href="http://www.cs.mcgill.ca/~bxu14/ass4/">
					<div id="exoplanet">
					</div>
				</a>
			</td>
			<td id="pad">
			</td>
			<td>
				<a href="http://cs.mcgill.ca/~hdevri/bumblebeeRoom.html">
					<div id="cupola">
					</div>
				</a>
			</td>
		</tr>
	</table>
</div>

<div id="text-box">
	<form action="http://www.cs.mcgill.ca/~dmusti/comp206/ass5/game.py" method="POST"> """
	print	"<input type=\"hidden\" name=\"coins\" value=\"%s\">" % coins
	print	'<input type="hidden" name="gamestatus" value="%s"> ' % gamestatus
	print	"<input type=\"hidden\" name=\"inventory1\" value=\"%s\">" % inventory1
	print	"<input type=\"hidden\" name=\"inventory2\" value=\"%s\">" % inventory2
	print	"<input type=\"hidden\" name=\"inventory3\" value=\"%s\">" % inventory3	
	print	"<input type=\"hidden\" name=\"inventory4\" value=\"%s\">" % inventory4
	print	"<input type=\"hidden\" name=\"inventory5\" value=\"%s\">" % inventory5
	print	"<input type=\"hidden\" name=\"page\" value=\"room\">"
	print """ <table border="0" align="center">
		<tr> 
			<td> <p> Your orders? </p> </td>
			<td id="pad"> </td>
			<td>  </td>
		</tr>  
		<tr> 
			<td> <input type="text" name="command" value""> </td>
			<td id="pad> </td>
			<td> <div class="button"> <input type="submit" value="" </div></td>
		</tr>
		</table>
	</form>
</div>
</body>

</html>"""

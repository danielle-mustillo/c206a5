#!/usr/bin/python
import cgi
import re

#some shit here
form = cgi.FieldStorage()

#parse input data
page = form.getvalue('page')
coins = form.getvalue('coins')
gamestatus = form.getvalue('gamestatus')
inventory1 = form.getvalue('inventory1')
inventory2 = form.getvalue('inventory2')
inventory3 = form.getvalue('inventory3')
inventory4 = form.getvalue('inventory4')
inventory5 = form.getvalue('inventory5')
command = form.getvalue('command')


print "Content-Type: text/html\n\n"

#initialize the coins if it wasn't initialized already.
if str(coins)=="None":
	coins = 100
	inventory1 = ""
	inventory2 = ""
	inventory3 = ""
	inventory4 = ""
	inventory5 = ""	

#convert the coin value to an integer for processing
try:
	coins = int(str(coins))
except ValueError:
	print "problem"

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

#each line is a new item
lines = rfile.readlines();
#lines[i] = lines[i].rstrip('\n')
print lines

#tells the user what last happened (right, wrong, or haven't played)
temp = str(command).split(' ')
print temp

global rfile
if temp[0]=="drop":
	try:
		val = int(temp[1])
		if val==1 and inventory1<>"None":
			lines.append(str(inventory1))
			gamemessage = 'You now dropped %s' % inventory1
			inventory1 = 'None'
		elif val==2 and inventory2<>"None":
			lines.append(str(inventory2))
			gamemessage = 'You now dropped %s' % inventory2
			inventory2 = 'None'
		elif val==3 and inventory3<>"None":
			lines.append(str(inventory3))
			gamemessage = 'You now dropped %s' % inventory3
			inventory3 = 'None'
		elif val==4 and inventory4<>"None":
			lines.append(str(inventory4))
			gamemessage = 'You now dropped %s' % inventory4
			inventory4 = 'None'
		elif val==5 and inventory5<>"None":
			lines.append(str(inventory5))
			gamemessage = 'You now dropped %s' % inventory5
			inventory5 = 'None'
	except ValueError:
		print "problem"
elif temp[0]=="inventory":
	gamemessage = " 1. %s" % inventory1
	gamemessage += "<br> 2. %s" % inventory2
	gamemessage += "<br> 3. %s" % inventory3
	gamemessage += "<br> 4. %s" % inventory4
	gamemessage += "<br> 5. %s" % inventory5
elif temp[0]=="look":
	gamemessage = "Captain! Your equipement for battle: "
	for i in range(0, len(lines)):
		gamemessage = "%s<br> %d. %s" % (gamemessage,i,lines[i])
elif temp[0]=="pickup":
	try:
		val = int(temp[1])
		if len(lines) < val or val < 0:
			gamemessage = "I dont understand"
		elif inventory1=="None":
			gamemessage = "Your are now equiping: %s" % lines[val]
			inventory1 = lines[val]
			lines.remove(lines[val])
		elif inventory2=="None":
			gamemessage = "You are now equiping:"
			inventory2 = lines[val]
			lines.remove(lines[val])
		elif inventory3=="None":
			gamemessage = "You are now equiping:"
			inventory3 = lines[val]
			lines.remove(lines[val])
		elif inventory4=="None":
			gamemessage = "Fuck"
			inventory4 = lines[val]
			lines.remove(lines[val])
		elif inventory5=="None":
			gamemessage = "fuck"
			inventory5 = lines[val]
			lines.remove(lines[val])
	except ValueError:
		gamemessage = "I don't understand commander"
else: 
	gamemessage = "In Orbit"
	if str(gamestatus)=="right2":
		gamemessage = "<font color=\"green\">Take Off!! You have: %s dollars </font>" % coins
	elif str(gamestatus)=="wrong2":
		gamemessage = "<font color=\"red\">Housten, we have a problem. You have: %s dollars</font>" % coins

#now just write everything that has changed back to the file.
#if nothing changed, then just rewrite old information.
rfile.close()
wfile = open("INVENTORY.CSV", 'w')
for line in lines:
	wfile.write(line)
wfile.close()

if form.getvalue('page')=="riddle":
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
	print "	<input type=\"hidden\" name=\"inventory1\" value=\"\"> "
	print "	<input type=\"hidden\" name=\"inventory2\" value=\"\"> "
	print "	<input type=\"hidden\" name=\"inventory3\" value=\"\"> " 
	print "	<input type=\"hidden\" name=\"inventory4\" value=\"\"> "
	print "	<input type=\"hidden\" name=\"inventory5\" value=\"\"> "
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
                <p> Because it already had a million degrees! </p>
                <br>
                <p> <a href="http://www.cs.mcgill.ca/~dmusti/comp206/ass5/room.html">Back to Command Center </a> </p>
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
	print	"<input type=\"hidden\" name=\"inventory1\" value=\"\">"
	print	"<input type=\"hidden\" name=\"inventory2\" value=\"\">"
	print	"<input type=\"hidden\" name=\"inventory3\" value=\"\">"
	print	"<input type=\"hidden\" name=\"inventory4\" value=\"\">"
	print	"<input type=\"hidden\" name=\"inventory5\" value=\"\">"
	print	"<input type=\"hidden\" name=\"command\" value=\"\">"
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

#!/usr/bin/python2
import commands
import cgi

print "content-type: text/html"
print 

print "<marquee hspace=10 vspace=10 height=40><font> CONTAINER AS A SERVICE</font></marquee>"
print "<center>"
print "<h2>AVAILABLE DOCKER IMAGES</h2>"
print "<pre>"
print "<h4>"
print commands.getoutput("sudo docker images")
print "</h4>"
print "</pre>"
print "</center>"
print "<center>"
print "<form action='container.py'>"
print "<select name='image'>"
z=1
for i in commands.getoutput("sudo docker images").split('\n'):
      if z==1 :
          z+=1
          pass
      else:
          j= i.split()
          print "<option>" + j[0] + ":" + j[1] + "</option>"
print "</select>"
print "Your Container Name : <input name='cname' />"
print "<input type='submit' value='Start' />"
print "</form>"
print "<h3>Launch Multiple Containers</h3><br/>"
print "<form action='mcontainer.py'>"
print "<select name='image'>"
z=1
for i in commands.getoutput("sudo docker images").split('\n'):
      if z==1 :
          z+=1
          pass
      else:
          j= i.split()
          print "<option>" + j[0] + ":" + j[1] + "</option>"
print "</select>"
print """
      Enter the Number : <input name='n' />
      Unique Id: <input name='id' />
      <input type='submit' value='start' />      
      """
print "</form><br/>"
print """
      <hr />
      <center>
      <h2> Create Your Own Image</h2>
      <form action="dockerimage.py">
      centos : <input name='os' value='centos' type='radio' /> ubuntu : <input name='os' value='ubuntu' type='radio' /> fedora : <input name='os' value='fedora' type='radio' />
      <br/>
      SSH Server : <input type='checkbox' name='ssh' value='ssh'/>
      <br/>
      Apache Server : <input type='checkbox' name='web' value='web' />
      <br/>
      Python2 : <input type='checkbox' name='python' value='python'/>
      <br/>
      Net-Tools : <input type='checkbox' name='ntool' value='ntool'/>
      <br/>
      Image Name: <input name="name" />
      <input type='submit' value='Create Image'>
      </center>
      """  



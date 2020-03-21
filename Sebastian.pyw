'''
1. Encrypt the database
2. suggestion of direcories / filename
3. weather / news
4. update DataBase and connect
5. self adjust screen size
6. remember
'''




import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from subprocess import *
import subprocess
import multiprocessing as mp
import wikipedia
import os
import random as rd
import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import threading

global busyIL
global lineedit, textedit1, textedit2, ctextedit, ctextedit1, ctextedit2
global label, window, engine, rate, chdir, cwd, runtime, uls, uls1, plm2
global stop, btnanet, btnavid, btnamus, temp_Words, p, labelo, movieo, moviemic
global listwidget, listobj, getAns, moviesfolder, songsfolder
p = threading.Thread(target=None)
runtime = 0
temp_Words = []
stop = ''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice' , voices[1].id)
engine.setProperty('rate' , rate-10)
chdir = ''
getAns = False
busyIL = False
cwd = os.getcwd()
moviesfolder = "D:/MOVIES"
songsfolder = "D:/SONGS"
class CustomWindow(QMainWindow):
    global lineedit, textedit1, textedit2, ctextedit, ctextedit1, ctextedit2
    global label, window, engine, rate, chdir, cwd, runtime, movie, plm, plm1

    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1020, 520)
        self.setGeometry(887, 32, 1020, 520)
        self.setFixedSize(1020,520)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        

    def paintEvent(self, event=None):
        color = QColor(51, 39 ,192)
        painter = QPainter(self)
        painter.setOpacity(0.6)
        painter.setBrush(color)
        painter.drawRect(self.rect())
        painter2 = QPainter(self)
        painter2.setPen(QPen(Qt.black, 23, Qt.SolidLine))
        painter2.drawEllipse(370,90,310,310)
        painter3 = QPainter(self)
        painter3.setPen(QPen(Qt.black, 10, Qt.SolidLine))
        painter3.drawLine(650, 320, 740, 390)
        painter3.drawLine(740, 390, 740, 420)
        painter3.drawLine(650, 245, 740, 245)
        painter3.drawLine(650, 150, 700, 90)
        painter3.drawLine(700, 90, 760, 90)
        painter3.drawLine(380, 320, 290, 390)
        painter3.drawLine(290, 390, 290, 420)
        painter3.drawLine(357, 245, 290, 245)
        painter3.drawLine(390, 150, 330, 90)
        painter3.drawLine(330, 90, 270, 90)


global listenerBusy
listenerBusy = False
def listen():
    global listenerBusy
    if not listenerBusy :
        print("not busy")
        listenerBusy = True
        r = sr.Recognizer() ; lt = ''
        
        with sr.Microphone() as source :
            r.adjust_for_ambient_noise(source, duration = 0.7)
            print ('say =')
            audio = r.listen(source)
            print("Listened")

        
        try :
            lt =  r.recognize_google(audio)
            lineedit.clear()
            lineedit.setText(str(lt))
            lineedit.setReadOnly( False )
            
        except :
            update_history("Sorry , I cant work offline ")
            engine.say("Sorry , I cant work offline ")
            engine.runAndWait()

        listenerBusy = False
        return
    else :
        return


def gifclicked(event):
    label.hide()
    labelmic.show()
    window.repaint()
    print("level 1")
    listen()
    print("level 2")
    labelmic.hide()
    label.show()
    window.repaint()
        
app = QApplication(sys.argv)
# Create the main window
window = CustomWindow()

movie =  QMovie("_includes/NG.gif")
label = QLabel(window)
label.setMovie(movie)
movie.start()
label.setFixedHeight(700)
label.setFixedWidth(700)
label.mousePressEvent = gifclicked
label.setScaledContents( True )
label.setSizePolicy( QSizePolicy.Ignored, QSizePolicy.Ignored )
label.move(170,-100)
label.hide()

############################
movieo =  QMovie("_includes/OFF.PNG")
labelo = QLabel(window)
movieo.start()
labelo.setMovie(movieo)
labelo.setFixedHeight(340)
labelo.setFixedWidth(340)
labelo.mousePressEvent = gifclicked
labelo.setScaledContents( True )
labelo.setSizePolicy( QSizePolicy.Ignored, QSizePolicy.Ignored )
labelo.move(360,65)


moviemic =  QMovie("_includes/mic0.PNG")
labelmic = QLabel(window)
moviemic.start()
labelmic.setMovie(moviemic)
labelmic.setFixedHeight(320)
labelmic.setFixedWidth(330)
labelmic.mousePressEvent = gifclicked
labelmic.setScaledContents( True )
labelmic.setSizePolicy( QSizePolicy.Ignored, QSizePolicy.Ignored )
labelmic.move(360,85)
labelmic.hide()

############################
uls = uls1 = plm = plm1 = plm2 = ''



def update_history(text):
    global uls, uls1
    uls1 = uls
    uls = text
    textedit1.setText(uls)
    textedit2.setText(uls1)

def print_history(*args):
    global plm, plm1, plm2
    a = list(args)
    plm1 = plm
    plm = plm2
    for i in range(len(a)):
        a[i] = str(a[i])

    plm2 = " ".join(a)
    
    ctextedit.setText(plm2)
    ctextedit1.setText(plm)
    ctextedit2.setText(plm1)


def inputL():
    global busyIL
    if not busyIL :
            busyIL = True
            global lineedit, textedit1, textedit2, ctextedit, ctextedit1, ctextedit2
            global label, window, engine, rate, chdir, cwd, runtime, uls, uls1
            global labelo, movieo
            
            
            text = lineedit.text()

            lineedit.setReadOnly( True )
            
            update_history(text)
            lineedit.clear()
            
            
            
            os.chdir(cwd)
            
            
            name = open('_includes/callme.txt' , 'r' ).read()
            
            
            
            
            if runtime == 0:
                runtime = 1        
                x = text 
                x = x.split(' ')
                if 'Sebastian' in x or 'sebastian' in x:
                     print_history('\nHello ' , name)
                     labelo.hide()
                     label.show()
                     window.update()
                     name = open('_includes/callme.txt' , 'r' ).read()
                     print_history('how may i help :')
                     hel = "Hello %s ....... "%name
                     engine.say(hel)
                     engine.say("how may i help you ")
                     engine.runAndWait()
                     busyIL = False
                     lineedit.setReadOnly( False )
                else :
                      runtime = 0
                      print_history("Thats not my name\nTo start System say : 'Hey Sebastian '")
                      engine.say("Thats not my name. To start System say : 'Hey Sebastian ")
                      engine.runAndWait()
                      time.sleep(0.2)
                      busyIL = False
                      lineedit.setReadOnly( False )
            elif len(text) < 2:
                print_history("Hmm..")
                engine.say("hmm")
                engine.runAndWait()
                time.sleep(0.2)
                busyIL = False
                lineedit.setReadOnly( False )
                return
            elif "RESET_010" == text :
                os.remove("_includes/msd.txt")
                print_history('Data Reset, Settings reset')
                print_history('RESET CODE 010')
                engine.say("ALL DATA AND SETTINGS RESET")
                engine.say("      .     RESET CODE  0   .   1    .    0   .  . ")
                engine.runAndWait()
                busyIL = False
                sys.exit(0)
            elif 'listen' in text :
                gifclicked()
                busyIL = False
            elif 'bye' in text or "Bye" in text :
                #print_history('Say good work .Support me through Paytm : 9827168348')
                engine.say("Bye Your Highness .    .   .   .  .  have a nice day ")
                engine.runAndWait()
                busyIL = False
                sys.exit(0)
            elif 'good' in text and 'work' in text :
                #print_history('Thanks for appriciation. Support me through Paytm at 9827168348')
                #engine.say("Thanks for appriciation. You can support my Devloper at given number")
                engine.runAndWait()
                busyIL = False
                lineedit.setReadOnly( False )
                return
            else :
                
                print("getAns = ",getAns)
                if not getAns :
                    print('\nLets start')
                    gotwork(text)
                    lineedit.setReadOnly( False )
                    busyIL = False
                    return
                else :
                    print("Answer")
                    getAnswer(text)
                    busyIL = False
                      

global pressedBusy
pressedBusy = False
def pressed():
    global pressedBusy, busyIL
    
    if not pressedBusy and not busyIL:
        pressedBusy = True
        print("pressed")
        #print_history('Say good work  .Support me through Paytm : 9556047048')
        engine.say("Bye Your Highness . have a nice day")
        engine.runAndWait()
        sys.exit(0)


#  STRING FUNCTIONS
def strcmpi(str1,str2) :
     len1 = len(str1)
     len2 = len(str2)
     str1 = list(str1)
     str2 = list(str2)
     x = 0
     while x < len1 :
          if 64 < ord(str1[x]) < 91 :
               str1[x] = chr(ord(str1[x]) + 32)
          x += 1
     x = 0
     while x < len2 :
          if 64 < ord(str2[x]) < 91 :
               str2[x] = chr(ord(str2[x])+32)
          x += 1
     if str1 == str2 :
          return 1
     else :
          return 0

def remove_marks(q):
	s = list(q)
	for _ in s:
		if '.' == _ or '?' == _ or '!' == _ :
			s.remove(_)
	return "".join(s)
    
def lower_case( str1 ) :
     str1 = remove_marks(str1)
     len1 = len(str1)
     str1 = list(str1)
     x = 0
     while x < len1 :
          if 64 < ord(str1[x]) < 91 :
               str1[x] = chr(ord(str1[x]) + 32)
          x += 1
     x = 0
     return ''.join(str1)

def startswithi(files , word ) :
     lw = len(word)
     lf = len(files)
     word = lower_case(word)
     files = lower_case(files)
     word = list(word)
     files = list(files)
     back = 1
     for x in range(0,lw) :
          if word[x] != files[x] :
               back = 0
               break
     return back
##############################################################

#   FILTER_Q
def openexe(meaningfull) :
     do = open('_includes/do.txt' , 'r').read()
     do = do.split('\n')
     exe = 0
     for x in meaningfull :
          if x in do :
               exe = 1
               meaningfull.remove(x)
     return 'exe' , meaningfull
    
def Q_words ( sen ) :
    questions = open('_includes/Questions.txt' , 'r').read()
    
    questions = questions.split('\n')
    sen = sen.split(' ')
    meaningfull = []
    search = 0
    print("q word => sen = %s ;\n questions = %s"%(sen,questions))
    for x in sen :
        if x not in questions and len(x) > 1:
            meaningfull.append(x)
        if x in questions :
                search = 1
            
    print("search = ",search)
            
    if search == 1:
        return 'search' , meaningfull
    else :
        return 'no_q_w' , meaningfull
        
def opennotepad (given ):
     given = given.split(' ')
     given = list(given)
     noteidx = given.index('note')
     meningfull = []
     work = 'notepad'
     noteidx += 1
     while noteidx < len(given) :
          meningfull.append(given[noteidx])
          noteidx += 1
     return work , meningfull
    
def remember_work (given) :
     work , words = Q_words(given)
     work = "remember"
     if work in words :
         words.remove(work)
     ime = open('_includes/ime.txt' , 'r' ).read()
     if 'know' in words :
          words = words.remove('know')
     ime = ime.split('\n')
    
     for i in ime :
         if i in words :
             words.remove(i)     
     return work , words

def checkme (give) :
     give = give.split(' ')
     found = False
     for _ in give :
          if 'me' == _ or 'my' == _ or 'mine' == _ :
               found = True
     return found     

def describe_work(given):
     given = given.split()
     work = 'describe'
     words = []
     for i in given :
          if not (i[0] == 'd' and i[1] == 'e' and i[2] == 's' and i[3] == 'c' ):
               words.append(i)
     return work, words
    
def applyLastFilter(given):
    given = given.split(' ')
    print("stage 1 = ", given)
    lastfilter = open("_includes/lastfilter.txt", 'r').read()
    lastfilter = lastfilter.split("\n")
    print("stage 2 = ", lastfilter)
    lastfilter = list(lastfilter)
    given = list(given)
    print(lastfilter, type(lastfilter))
    print(given, type(given))
    for r in lastfilter :
        for _ in given :
            if r == _ :
                given.remove(r)

        
    print("stage 3 = ", given)
    words = given
    return "search", words

def Start_filters (given) :
     given = lower_case(given)

     if startswithi(given, 'plea'):
          s = given.split(' ')

          for i in s:
               if i[0] == 'p' and i[1] == 'l' and i[2] == 'e' :
                    s.remove(i)
          given = " ".join(s)

     print("stage 1 : ",given)
     if 'write' in given and 'note' in given :
          work , words = opennotepad(given)
     elif 'search' in given :
         print("apllying filter")
         work, words = applyLastFilter(given)
         print("apllyed filter")
     elif ('open' in given or "show" in given) and ("manual" in given) :
         print("stage 2")
         HTMLNAME = ''

         HTMLNAME = str("file:///") + str(cwd)+("/_includes/manual.html")
         print(HTMLNAME)
         webbrowser.open(HTMLNAME, new=2)
         return None, None
     elif 'describe' in given or 'descrption' in given:
          work, words = describe_work(given)
     elif ('you' in given or 'your' in given) and ("youtube" not in given) :
          work , words = Q_words ( given )
          if len(words) == 0 :
              hj = "I am an AI which design to make your work easy"
              print_history(hj)
              engine.say(hj)
              engine.runAndWait()
              return None, None
          work = 'db'
     elif 'remember' in given:
         work, words = remember_work(given)
     elif checkme(given) :
          remember(given)
          return None, None
     else :
          work , words = Q_words(given)
          if work != 'search' :
               work , words = openexe(words) 
     return work , words

############################################################
#   WORK

def internet(words) :
     name = open('_includes/callme.txt' , 'r').read()
     hj = "lemme search to net ...."+str(name)
     print_history(hj)
     engine.say(hj)
     engine.runAndWait()
     import time
     print("browser Type")
     to = ' '.join(words)
     s1 = "https://www.google.co.in/search?q=%s&oq=%s&aqs=chrome..69i57j5l2j69i60l3.3458j0j8&sourceid=chrome&ie=UTF-8"%(to,to)
     webbrowser.open(s1, new=2)
def find(l,words) :
     
     los = []
     got_path = ''
     os.chdir(l)
     if 'video' in words :
          words.remove('video')
     if  'music' in words :
          words.remove('music')
     if 'movie' in words :
         words.remove('movie')
     if 'song' in words :
         words.remove('song')
          

        
     for (path , dirs , files) in os.walk(l) :
        for file in files :
             for word in words :
                  if startswithi(file, word) :
                      got_path = path
                      
     try :
          print("mp1 path = ",got_path)
          os.chdir(got_path)
          if len(los) != 0 :
               del los[:]
          
          for files in os.listdir(got_path):
               for word in words :
                    if startswithi(files, word) :
                         los.append(files)
          return los
     except :
          os.chdir(cwd)
          check = 0
          list_of_software = open('_includes/software.txt' , 'r' ).read()
          list_of_software = list_of_software.split('\n')
          for word in words :
               if word in list_of_software :
                    check = 1
          if check == 0 :
               
               internet(words)
               return None
          else :
              return None

def selectedItem():
    s = str(listwidget.currentItem().text())

    if s.endswith(".txt") or s.endswith(".py") :
        p = subprocess.Popen(["notepad.exe" , s])

    elif s.endswith(".mp3") or s.endswith(".aac") or s.endswith(".wav") :
        p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe",s])
               
    elif s.endswith(".mp4") or s.endswith(".mkv") or s.endswith(".flv") or s.endswith(".Flv") :
        p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe",s])
               
    else :    
        l = l + '/' + los[idx]
        print_history(l)

    ctextedit.show()
    ctextedit1.show()
    ctextedit2.show()
    listwidget.hide()
    lineedit.clear()
    window.update()
        
    return


def do_work(objects) :
     global lineedit, textedit1, textedit2, ctextedit, ctextedit1, ctextedit2
     global label, window, engine, rate, chdir, cwd, runtime, listwidget, listobj
     if  len(objects) > 1:
          idx = 0
          if True :
               for x in objects :
                    listwidget.addItem(str(x))
            
               ctextedit.hide()
               ctextedit1.hide()
               ctextedit2.hide()
               listwidget.show()
               lineedit.setText("Select any of the following.")
               window.update()
               
               engine.say("Got multiple Items of same name . select one of these")
               engine.runAndWait()

     else :
        s = str(objects[0])
        print("play = > ",s)
        if s.endswith(".txt") or s.endswith(".py") :
            p = subprocess.Popen(["notepad.exe" , s])

        elif s.endswith(".mp3") or s.endswith(".aac") or s.endswith(".wav") :
            p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe",s])
               
        elif s.endswith(".mp4") or s.endswith(".mkv") or s.endswith(".flv") or s.endswith(".Flv") :
            p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe",s])
      
        else :    
            l = l + '/' + los[idx]
            internet(s)
            print_history(l)

def assistBtnFunNet():
    global stop, temp_Words
    stop = 'net'
    print(temp_Words)
    internet(temp_Words)
    lineedit.show()
    btnanet.hide()
    btnavid.hide()
    btnamus.hide()
    btnamuc.hide()
    window.repaint()
    return
    
def assistBtnFunVid():
    global stop, temp_Words
    stop = 'off'
    print(temp_Words)
    path, softreport = moviesfolder, 0 #incomplete
    lineedit.show()
    btnanet.hide()
    btnavid.hide()
    btnamus.hide()
    btnamuc.hide()
    window.repaint()
    if softreport == 0 :
        objects = find(path,temp_Words)
        if objects != None :
            do_work(objects)
    return


def assistBtnFunMus():
    global stop, temp_Words
    stop = 'off'
    print(temp_Words)
    path, softreport = songsfolder, 0 #incomplete
    lineedit.show()
    btnanet.hide()
    btnavid.hide()
    btnamus.hide()
    btnamuc.hide()
    window.repaint()
    if softreport == 0 :
        objects = find(path,temp_Words)
        do_work(objects)

def assistBtnFunCan():    
    lineedit.show()
    btnanet.hide()
    btnavid.hide()
    btnamus.hide()
    btnamuc.hide()
    window.repaint()
    

    
def assist(words):
    global temp_Words
    temp_Words = words
    lineedit.hide()
    btnanet.show()
    btnavid.show()
    btnamus.show()
    btnamuc.show()
    window.repaint()
    
    
    

def luck(work , words) :
     global lineedit, textedit1, textedit2, ctextedit, ctextedit1, ctextedit2
     global label, window, engine, rate, chdir, cwd, runtime
     name = open('_includes/callme.txt' , 'r').read()
     print_history("Opening ...")
     engine.say(" opening .. ")
     engine.runAndWait()
     time.sleep(0.5)
     serachdir = ''
     
     softreport = 0
     listofsoftware = open('_includes/software.txt' , 'r' ).read()
     listofsoftware = listofsoftware.split('\n')
     if 'chrome' in words :
          p = subprocess.Popen(["C:/Users/KIIT/AppData/Local/Google/Chrome/Application/chrome.exe"])
          softreport = 1
     elif 'uc' in words :
          p = subprocess.Popen(["C:/Program Files (x86)/UCBrowser/Application/UCBrowser.exe"])
          softreport = 1
     elif 'player' in words :
          softreport = 1
          if 'video' in words :
               p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe"])
          elif 'music' in words :
               p = subprocess.Popen(["C:/Program Files/Windows Media Player/wmplayer.exe"])
     elif 'notepad' in words :
               softreport = 1
               p = subprocess.Popen(["notepad.exe"])
               
     elif  'exe' == work :
          softreport = 0
          if ('music' in words) or ('Music' in words) or ('song' in words) :
               serachdir = songsfolder 
          elif ('video' in words) or ('Video' in words) or ('VIDEO' in words) or ('movie' in words) :
               serachdir = moviesfolder
          else :
               serachdir, softreport = None, None
               assist(words)
               print_history('''Please assist me for better understanding.Is it a video or music also present in computer . Or I have to connect to internet .''')
               engine.say(" Actually M CONFUSED Please ASSIST ME ")
               engine.runAndWait()             
     return serachdir, softreport

def writeinnote(words) :
     global cwd
     os.chdir(cwd)
     nametxt = words[0] + '.txt'
     file = open(nametxt, 'w' , newline = '\n' )
     for word in words :
          towrite = word + ' '
          file.write(towrite)
     file.close()
     p = subprocess.Popen(["notepad.exe" , nametxt])
     print_history('done')     
     engine.say('done')
     engine.runAndWait()

def database ( words ) :
     global cwd
     name = open('_includes/callme.txt' , 'r').read()
     os.chdir(cwd)
     filesobj = open( '_includes/database.txt' , 'r+' )
     files = filesobj.read()
     files = files.split('\n')
     forend = 0 ; qind = 0
     for qna in files :
          qna = qna.split('?')
          for word in words :
               if word in qna[0] :
                    print_history(qna[1])
                    engine.say(qna[1])
                    engine.runAndWait()
                    forend = 1
                    break
          if forend == 1 :
               break
     if forend == 0 :
               
               print_history( "\nSorry , I dont know %s , I didnt thought about it "%name )
               print_history( "\nBy the way whats your point of view if I asked same\nTell me\n" )
               hj = "hm dont know whats your point of view "+str(name)
               engine.say(hj)
               engine.runAndWait()
               lineedit.setPlaceholderText("your Answer")
               
               global temp_Words, getAns
               getAns = True
               temp_Words = words
     filesobj.close()
     return
#hell
def getAnswer(text):
    global temp_Words, getAns
    getAns = False
    lineedit.clear()
    lineedit.setPlaceholderText("Chat")
    filesobj = open( '_includes/database.txt' , 'a' )
    towrite = str(temp_Words)+'?'+text+'\n'
    filesobj.write(towrite)
    filesobj.close()
    print_history( "It's a great reply." )
    lineedit.setReadOnly( False )
    return
    
      
def remember (words) :
     global lineedit, textedit1, textedit2, ctextedit, ctextedit1, ctextedit2
     global label, window, engine, rate, chdir, cwd, runtime

     name = open('_includes/callme.txt' , 'r').read()
     if ('call' in words and 'me' in words)  :
          fileobj = open( '_includes/callme.txt' , 'w+')
          words = words.split(" ")
          if 'is' in words :
              words.remove('is')
          if 'call' in words :
              words.remove('call') ; words.remove('me')
          usrname = words[0]
          fileobj.write(usrname)
          hj = 'give me new task %s'%usrname
          print_history('Okay , give me a new task %s'%usrname)
          engine.say(hj)
          engine.runAndWait()
     else :
          if ('dont' in words or "don't" in words) or ( ('not' in words or 'no' in words) and 'know' in words) :
               print_history("Oh I think some thing happend .")
               engine.say("Oh I think some thing happend .")
               engine.runAndWait()
          else :
               got = True
               file = open('_includes/rem.txt' , 'r').read()
               file = file.split('\n')
               _, words = Q_words(words)
               for memory in file :
                    memory = memory.split(':')
                    for each_word in words :
                         if strcmpi (memory[0] , each_word) :
                              got = False
                              print_history('yehh , I know ' + str(memory[1]) + ' is your '+ memory[0])
                              hj = 'yehh , I know ' + str(memory[1]) + ' is your '+ memory[0]
                              engine.say(hj)
                              engine.runAndWait()
                              
               if got :
                    filesobj1 = open( '_includes/rem.txt' , 'r+' )
                    files1 = filesobj1.read()
                    print_history('Okay , next time I remember this ')
                         
                    if 'my' in words :
                        words.remove('my')
                    nameidx = words.index('name')
                    words.remove('name')
                    if len(words[nameidx]) <=  2 :
                        nameidx += 1
                    line_to_write = ''.join(words[0]) + ":" + str(*words[1:]) +'\n'                    
                    filesobj1.write(line_to_write)
                    filesobj1.close()
     
          
def things_to_rem (words) :
     global lineedit, textedit1, textedit2, ctextedit, ctextedit1, ctextedit2
     global label, window, engine, rate, chdir, cwd, runtime

     fileobj1 = open('_includes/rem.txt' , 'r+' )
     file1 = fileobj1.read()

     print_history('Okay , next time I remember this ')
     
     if 'name' in words :
               if 'remember' in words :
                    words.remove('remember')
               if 'my' in words :
                    words.remove('my')
               nameidx = words.index('name')
               words.remove('name')
               if len(words[nameidx]) <=  2 :
                    nameidx += 1
               line_to_write = ''.join(words[:nameidx]) + ":" + str(words[nameidx]) + " " +str(words[nameidx+1])+'\n'

     fileobj1.write(line_to_write)
     fileobj1.close()
     
def get_data_from_wiki_background(to_des):
     global lineedit, textedit1, textedit2, ctextedit, ctextedit1, ctextedit2
     global label, window, engine, rate, chdir, cwd, runtime

     print("STARTING")
     global engine
     try :
          x = wikipedia.summary(to_des, sentences=2)
          p2 = []
          for i in x :
               if i == '\n' :
                     break
               if ord(i) < 256  :
                    if ord(i) != 58 and ord(i) != 59:
                         p2.append(i)
          data = ''.join(p2)
          print("FINDED DATA")
          engine.say(data)
          return
     except Exception as e:
          print("GOT EXCEPTION")
          option = str(e)
          nonet = option[:4]
          if nonet == 'HTTP' :
               engine.say("CHECK YOUR INTERNET CONNECTION")
               engine.runAndWait()
               return
          else :
               option = option.split('\n')
               engine.say("I am confused with these so try again and be more specific")
               engine.say(str(option[1]))
               engine.runAndWait()
               engine.say(str(option[2]))
               engine.runAndWait()
               engine.say()
               engine.runAndWait(str(option[3]))
               return
     return





def describe (words):
     global p
     to_des = " ".join(words)
     engine.say("Okay I will Find it out for you . until your next tesk")
     engine.runAndWait()
     p = threading.Thread(target=get_data_from_wiki_background, args=(to_des,))
     p.start()
     time.sleep(1)
     return None, None
     
     

def start_work(work , words) :
     if work == 'notepad' :
          writeinnote(words)
     elif work == "describe" :
          describe (words)
     elif  work == "search":
          internet(words)
     elif work == 'db' :
          database( words )
     elif work == 'exe' :
          path, softreport = luck(work , words)
          if path == None :
              return
          if softreport == 0 :
               objects = find(path,words)
               do_work(objects)
               return
     elif work == 'remember':
          remember(words)
     else :
          things_to_rem (words)

############################################################
'''
START
'''

def gotwork (sentence ) :
     print("stage 0")
     work , words = Start_filters(sentence)
     print("stage 3")
     print('work = ',work,'\nwords = ',words)
     if work != None and words != None :         
         start_work(work , words)
     return



'''
FRONT END
'''
listwidget = QListWidget(window)
listwidget.resize(350,540)
listwidget.setStyleSheet('''
                        QListWidget {
                        border: 3px solid black;
                        border-width: 1px;
                        background-color : rgba(247,36,115,220)}
                        ''')
listwidget.clicked.connect(selectedItem)
listwidget.hide()
listwidget.move(0, 4)



btnanet = QPushButton(window)
btnanet.setText('Internet')
btnanet.resize(120,40)
btnanet.setStyleSheet('''
                        QPushButton {
                        border: 3px solid black;
                        border-width: 1px;
                        border-radius: 13px;
                        background-color : rgba(247,36,115,180)}
                    ''')
btnanet.clicked.connect(assistBtnFunNet)
btnanet.hide()
btnanet.move(520,425)


btnavid = QPushButton(window)
btnavid.setText('Video')
btnavid.resize(120,40)
btnavid.setStyleSheet('''
                        QPushButton {
                        border: 3px solid black;
                        border-width: 1px;
                        border-radius: 13px;
                        background-color : rgba(247,36,115,180)}
                    ''')
btnavid.clicked.connect(assistBtnFunVid)
btnavid.hide()
btnavid.move(763,425)

btnamus = QPushButton(window)
btnamus.setText('Music')
btnamus.resize(120,40)
btnamus.setStyleSheet('''
                        QPushButton {
                        border: 3px solid black;
                        border-width: 1px;
                        border-radius: 13px;
                        background-color : rgba(247,36,115,180)}
                    ''')
btnamus.clicked.connect(assistBtnFunMus)
btnamus.hide()
btnamus.move(642,425)

btnamuc = QPushButton(window)
btnamuc.setText('Cancle')
btnamuc.resize(120,40)
btnamuc.setStyleSheet('''
                        QPushButton {
                        border: 3px solid black;
                        border-width: 1px;
                        border-radius: 13px;
                        background-color : rgba(247,36,115,180)}
                    ''')
btnamuc.clicked.connect(assistBtnFunCan)
btnamuc.hide()
btnamuc.move(890,425)
####################################################

cWords = []
ccallme = open('_includes/callme.txt', 'r').read()
cDb = open('_includes/database.txt', 'r').read()
cDb = " ".join(cDb.split('\n')).split(" ")
cWords.append("hey")
cWords.append("hello")
cWords.append("play")
cWords.append("video")
cWords.append("music")
cWords.append("Sebastian")
cWords.append(" Sebastian")
cWords.append(str(ccallme))
for _ in cDb :
    cWords.append(str(cDb))

completer = QCompleter(cWords)
completer.setCaseSensitivity(Qt.CaseInsensitive)
completer.setCompletionMode( QCompleter.InlineCompletion )

lineedit = QLineEdit(window)
lineedit.setFixedWidth(500)
lineedit.setCompleter(completer)
font = lineedit.font()
font.setPointSize(13)
lineedit.setFont(font)
lineedit.resize(10,70)
lineedit.setPlaceholderText("Chat")
lineedit.setStyleSheet('''
                        QLineEdit {
                        border: 2px solid black;
                        border-width: 3px;
                        border-radius: 10px;
                        background-color : rgba(247,36,115,180)}''')
lineedit.returnPressed.connect(inputL)
lineedit.move(515, 420)
textedit1 = QTextEdit(window)
textedit1.setReadOnly( True )
font = textedit1.font()
font.setPointSize(12)
textedit1.setFont(font)
textedit1.setPlaceholderText("History...")
textedit1.setWordWrapMode( QTextOption.WordWrap )
textedit1.resize(210,180)
textedit1.setStyleSheet('''
                        QTextEdit {
                        border: 3px solid black;
                        border-width: 5px;
                        border-radius: 15px;
                        background-color : rgba(247,36,115,180)}''')
textedit1.move(745, 180)
textedit2 = QTextEdit(window)
textedit2.setReadOnly( True )
font = textedit1.font()
font.setPointSize(12)
textedit2.setFont(font)
textedit2.setPlaceholderText("History...")
textedit2.setWordWrapMode(QTextOption.WordWrap)
textedit2.resize(210,110)
textedit2.setStyleSheet('''
                        QTextEdit {
                        border: 3px solid black;
                        border-width: 5px;
                        border-radius: 15px;
                        background-color : rgba(247,36,115,180)}''')
textedit2.move(765, 20)
ctextedit = QTextEdit(window)
ctextedit.setReadOnly(True)
ctextedit.setFixedWidth(500)
cfont = ctextedit.font()
cfont.setPointSize(12)
ctextedit.setFont(cfont)
ctextedit.resize(10,100)
ctextedit.setWordWrapMode( QTextOption.WordWrap )
ctextedit.setPlaceholderText("History...")
ctextedit.setStyleSheet('''
                        QTextEdit {
                        border: 2px solid black;
                        border-width: 3px;
                        border-radius: 10px;
                        background-color : rgba(247,36,115,180)}''')
ctextedit.move(00, 420)



ctextedit1 = QTextEdit(window)
ctextedit1.setReadOnly( True )
cfont1 = ctextedit1.font()
cfont1.setPointSize(12)
ctextedit1.setFont(cfont1)
ctextedit1.setPlaceholderText("History...")
ctextedit1.setWordWrapMode( QTextOption.WordWrap )
ctextedit1.resize(240,180)
ctextedit1.setStyleSheet('''
                        QTextEdit {
                        border: 3px solid black;
                        border-width: 5px;
                        border-radius: 15px;
                        background-color : rgba(247,36,115,180)}''')
ctextedit1.move(45, 180)
ctextedit2 = QTextEdit(window)
ctextedit2.setReadOnly( True )
cfont = textedit1.font()
cfont.setPointSize(12)
ctextedit2.setFont(cfont)
ctextedit2.setPlaceholderText("History...")
ctextedit2.setWordWrapMode( QTextOption.WordWrap )
ctextedit2.resize(215,110)
ctextedit2.setStyleSheet('''
                        QTextEdit {
                        border: 3px solid black;
                        border-width: 5px;
                        border-radius: 15px;
                        background-color : rgba(247,36,115,180)}
                        ''')

ctextedit2.move(55, 20)
btn = QPushButton(window)
btn.setText('X')
btn.setToolTip("<b>BYE !</b>") 
btn.resize(30,30)
btn.setStyleSheet('''
                        QPushButton {
                        border: 3px solid black;
                        border-width: 1px;
                        border-radius: 13px;
                        background-color : rgba(247,36,115,180)}
                ''')

''' START GUI '''

btn.clicked.connect(pressed)
btn.move(985,4)

def showWizard():
    global moviesfolder, songsfolder
    def getMoviesFolder():
        global mf
        mf = str(QFileDialog.getExistingDirectory())

    def getMusicFolder():
        global sf
        sf = str(QFileDialog.getExistingDirectory())

    app = QApplication(sys.argv)
    wizard = QWizard()
    wizard.setWizardStyle(QWizard.ModernStyle)


    pic = QPixmap("_includes/LogoSmall.png")

    wizard.setPixmap(QWizard.WatermarkPixmap, pic)
    wizard.setPixmap(QWizard.LogoPixmap, pic)
    wizard.setPixmap(QWizard.BannerPixmap, pic)

    page1 = QWizardPage()
    page1.setTitle("INTRODUCTION")

    lineedit = QLineEdit()
    labelN = QLabel("Name : ")
    hLayout1 = QVBoxLayout(page1)
    hLayout1.addWidget(labelN)
    hLayout1.addWidget(lineedit)


    labelM = QLabel("Do you have any movies folder : ")
    btnM = QPushButton("Yes, I have")
    btnM.clicked.connect(getMoviesFolder)
    hLayout1.addWidget(labelM)
    hLayout1.addWidget(btnM)


    labels = QLabel("Do you have any music folder : ")
    btns = QPushButton("Yes, I have")
    btns.clicked.connect(getMusicFolder)
    hLayout1.addWidget(labels)
    hLayout1.addWidget(btns)



    page1.registerField('myField*',
                        lineedit,
                        lineedit.text(),
                        lineedit.textChanged)

    #########################################

    page2 = QWizardPage()
    page2.setFinalPage(True)
    page2.setTitle("Details")

    global label, l1, l2
    label = QLabel()
    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel("RESTART THE APP")
    hLayout2 = QVBoxLayout(page2)
    hLayout2.addWidget(label)
    hLayout2.addWidget(l1)
    hLayout2.addWidget(l2)
    hLayout2.addWidget(l3)

    #######  CONNECT SIGNAL AND ADD PAGES
    global name, mf, sf
    name = mf = sf = ''
    def func() :
        global moviesfolder, songsfolder
        global label, l1, l2
        f = open("_includes/msd.txt", 'w')
        f.write(sf)
        f.write("\n")
        f.write(mf)
        f.close()
        name = str(page1.field("myField"))
        f = open("_includes/callme.txt", 'w')
        f.write(name)
        f.close()
        
        label.setText(name)
        l1.setText("Music : %s"%sf)
        l2.setText("Movies : %s"%mf)
        

        

    nxt = wizard.button(QWizard.NextButton)
    nxt.clicked.connect(func)
    wizard.addPage(page1)
    wizard.addPage(page2)
    wizard.show()
    sys.exit(app.exec_())
    


if __name__ == "__main__" :
    
    
    if not os.path.isfile("_includes/msd.txt"):
        showWizard()
    else :
        f = open("_includes/msd.txt", 'r').read()
        f = f.split("\n")
        moviesfolder, songsfolder = f[1], f[0]
        

    name = '_includes/Splash' + str(rd.randint(1,8)) + ".jpeg" #rd.randint(1,1)
    splashMovie =  QPixmap(name)
    splashscreen = QSplashScreen(splashMovie)
    splashscreen.show()
    time.sleep(3)
    window.show()
    splashscreen.finish(window)
    sys.exit(app.exec_())




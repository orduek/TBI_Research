# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:01:15 2015

@author: orduek
Corsi Block Expreiment in Psychopy.
This experiment is spatial memory experiment as in the WMS
"""

from psychopy import core, visual, gui, data, misc, event, sound
import time, os
# now turn to right folder
directory=os.getcwd()  # get folder
os.chdir(directory) # use it

#folder='/home/ord/Experiments_BP_Clinic/PCT/' #specify the folder of result files to be saved in
# savine last experiment data
try:#try to get a previous parameters file
    expInfo = misc.fromFile('corsi.pickle')
except:#if not there then use a default set
    expInfo = {'subject no':''}
expInfo['dateStr']= data.getDateStr() #add the current time
# dialouge box for name of subject and file
dlg = gui.DlgFromDict(expInfo, title='Corsi Task', fixed=['dateStr'])
if dlg.OK:
    misc.toFile('corsi.pickle', expInfo)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit

# check if folder exist and if not, create it
if not os.path.exists('results'):
    os.makedirs('results')

fileName = expInfo['subject no'] + expInfo['dateStr']
dataFile = open(directory+'/results/'+fileName+'.csv', 'w')#a simple text file with 'comma-separated-values'
dataFile.write('nTrial,trialList,ans,press,block,rt,length\n')


# make a functino that will get mouse click position

# adjust sequence of presentation
mywin = visual.Window(fullscr=False,monitor="testMonitor",allowGUI=False,rgb=[1,1,1])
### Build rectangles
rect1=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(-0.8,0.8),fillColor="Blue")
rect2=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(0.25,0.82),fillColor="Blue")
rect3=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(0.8,0.5),fillColor="Blue")
rect4=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(-0.1,0.3),fillColor="Blue")
rect5=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(0.6,0.1),fillColor="Blue")
rect6=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(-0.5,-0.2),fillColor="Blue")
rect7=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(-0.82,-0.6),fillColor="Blue")
rect8=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(-0.2,-0.7),fillColor="Blue")
rect9=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(0.4,-0.4),fillColor="Blue")
rect10=visual.Rect(mywin,width=0.3,height=0.3,units='norm',pos=(0.8,-0.7),fillColor="Blue")
rectList={'rect1':rect1,'rect2':rect2,'rect3':rect3,'rect4':rect4,'rect5':rect5,'rect6':rect6,'rect7':rect7,'rect8':rect8,'rect9':rect9,'rect10':rect10} #set dictionary of rectangles and their names to run trials

gosound=sound.Sound('A',octave=3, sampleRate=44100, secs=0.8, bits=8)


# set nTrial as numerator of trials
block="f" # will say if forward or backwards
nTrial=range(1,17) # 16 trials forward
nTrialbk=range(1,17) # 16 trials backwards
n=0 # numerator to use later to choose how many numbers of mouse clicks should be pressed.
ans=5 # integet of 1=correct, 0=incorrect responses
numerr=0 # numerator errors
trialErr=0 # decide if trial is error or not
errAmount=0 # counting how many error in trials
length=0
# set positions of rectangles
#positions=[(-0.8,0.8),(0.25,0.82),(0.8,0.5),(-0.1,0.3),(0.6,0.1),(-0.5,-0.2),(-0.82,-0.6),(-0.2,-0.7),(0.4,-0.4),(0.8,-0.7)]
# set the filler rectangle
myMouse=event.Mouse()
#picture=visual.ImageStim(mywin,'/home/ord/Dropbox/CreActive/Task/Corsi/Corsi.jpg',size=2)
# Build all rectangles for corsi
def buildRect():
    # Build and draw all rectangles for corsi
    rect1.draw()
    rect2.draw()
    rect3.draw()
    rect4.draw()
    rect5.draw()
    rect6.draw()
    rect7.draw()
    rect8.draw()
    rect9.draw()
    rect10.draw()

def expTrial(nTrial):
    # This function should build the sequence of trials in the experiment. It builds a list of strings that is used as keys in dictionaty of rectList.
    # 3-10, 7-4
    # 1-9-3,8-2-7
    # 4-9-1-6, 10,6,2,7
    # 4,1,9,3,8,10 ; 9-2-6-7-3-5
    if nTrial==1:
        trialList=('rect3','rect10')
    elif nTrial==2:
        trialList=('rect7','rect4')
    elif nTrial==3:
        trialList=('rect1','rect9','rect3')
    elif nTrial==4:
        trialList=('rect8','rect2','rect7')
    elif nTrial==5:
        trialList=('rect4','rect9','rect1','rect6')
    elif nTrial==6:
        trialList=('rect10','rect6','rect2','rect7')
    elif nTrial==7:
        trialList=('rect6','rect5','rect1','rect4','rect7')
    elif nTrial==8:
        trialList=('rect5','rect7','rect9','rect8','rect2')
    elif nTrial==9:
        trialList=('rect4','rect1','rect9','rect3','rect8','rect10')
    elif nTrial==10:
        trialList=('rect9','rect2','rect6','rect7','rect3','rect5')
    elif nTrial==11:
        trialList=('rect10','rect1','rect6','rect4','rect8','rect5','rect7')
    elif nTrial==12:
        trialList=('rect2','rect6','rect3','rect8','rect2','rect10','rect1')
    elif nTrial==13:
        trialList=('rect7','rect3','rect10','rect5','rect7','rect8','rect4','rect9')
    elif nTrial==14:
        trialList=('rect6','rect9','rect3','rect2','rect1','rect7','rect10','rect5')
    elif nTrial==15:
        trialList=('rect5','rect8','rect4','rect10','rect7', 'rect3', 'rect1','rect9','rect6')
    elif nTrial==16:
        trialList=('rect8','rect2','rect6','rect1','rect10','rect3','rect7','rect4','rect9')
    return trialList
def expTrialBack(nTrialbk): # make trials of the backward part of Corsi task.
    if nTrialbk==1:
        trialListbk=('rect7','rect4')
    elif nTrialbk==2:
        trialListbk=('rect3','rect10')
    elif nTrialbk==3:
        trialListbk=('rect8','rect2','rect7')
    elif nTrialbk==4:
        trialListbk=('rect1','rect9','rect3')
    elif nTrialbk==5:
        trialListbk=('rect10','rect6','rect2','rect7')
    elif nTrialbk==6:
        trialListbk=('rect4','rect9','rect1','rect6')
    elif nTrialbk==7:
        trialListbk=('rect5','rect7','rect9','rect8','rect2')
    elif nTrialbk==8:
        trialListbk=('rect6','rect5','rect1','rect4','rect8')
    elif nTrialbk==9:
        trialListbk=('rect9','rect2','rect6','rect7','rect3','rect5')
    elif nTrialbk==10:
        trialListbk=('rect4','rect1','rect9','rect3','rect8','rect10')
    elif nTrialbk==11:
        trialListbk=('rect2','rect6','rect3','rect8','rect2','rect10','rect1')
    elif nTrialbk==12:
        trialListbk=('rect10','rect1','rect6','rect4','rect8','rect5','rect7')
    elif nTrialbk==13:
        trialListbk=('rect6','rect9','rect3','rect2','rect1','rect7','rect10','rect5')
    elif nTrialbk==14:
        trialListbk=('rect7','rect3','rect10','rect5','rect7','rect8','rect4','rect9')
    elif nTrialbk==15:
        trialListbk=('rect8','rect2','rect6','rect1','rect10', 'rect3', 'rect7','rect4','rect9')
    elif nTrialbk==16:
        trialListbk=('rect5','rect8','rect4','rect10','rect7','rect3','rect1','rect9','rect6')
    return trialListbk
def changeColor (rect,color):
    rect.setFillColor(color=color)
    return rect
def checkMouse():
    #a=[0,0,0] # setting buttons list
    #a=myMouse.getPressed()
    while True:  # while left button wasn't pressed wait to press
    #handle key presses each frame
        for key in event.getKeys():
            if key in ['escape','q']:
                core.quit()
        if myMouse.isPressedIn(rect1):
            press=rect1
            rectprs='rect1'
            break
        elif myMouse.isPressedIn(rect2):
            press=rect2
            rectprs='rect2'
            break
        elif myMouse.isPressedIn(rect3):
            press=rect3
            rectprs='rect3'
            break
        elif myMouse.isPressedIn(rect4):
            press=rect4
            rectprs='rect4'
            break
        elif myMouse.isPressedIn(rect5):
            press=rect5
            rectprs='rect5'
            break
        elif myMouse.isPressedIn(rect6):
            press=rect6
            rectprs='rect6'
            break
        elif myMouse.isPressedIn(rect7):
            press=rect7
            rectprs='rect7'
            break
        elif myMouse.isPressedIn(rect8):
            press=rect8
            rectprs='rect8'
            break
        elif myMouse.isPressedIn(rect9):
            press=rect9
            rectprs='rect9'
            break
        elif myMouse.isPressedIn(rect10):
            press=rect10
            rectprs='rect10'
            break
    #else:
    #    a[0]=0
    return press, rectprs

def markRec(x):
  buildRect()
  changeColor(x,"yellow")
  x.draw()
  mywin.flip()

def unmarkRec(x):
  changeColor(x,"Blue")
  buildRect()
  mywin.flip()


buildRect()
#expTrial()
mywin.flip(clearBuffer=True)

for i in nTrial:
    block="forward"
    trialList=expTrial(i)
    for x in trialList: # run a loop inside the
        #mark rec
        length=len(trialList)
        rect=rectList[x]
        markRec(rect)
        core.wait(1)
        #unmark rec
        unmarkRec(rect)
    gosound.play()
    for n in trialList:
        trialClock=core.Clock() # open clock to measure reaction time
        press, rectprs  = checkMouse()
        RT=core.Clock.getTime(trialClock) # meaure reaction time
        if press==rectList[n]:  # checking for errros and counting errors in trial.
            ans=1
            numerr=numerr
        else:
            ans=0
            numerr=numerr+1
        markRec(press)
        core.wait(0.5)
        unmarkRec(press)
        event.clearEvents()
        dataFile.write('%i,%s,%i,%s,%s,%f,%i\n' %(i,n,ans,rectprs,block,RT,length))
        if numerr>0: # Defining trial as error.
            trialErr=1
        else:
            trialErr=0
    numerr=0
    if trialErr==1:
        errAmount=errAmount+1
    else:
        errAmount=0
    if errAmount>2: # choose how many error in a raw, before stopping experiment.
        break
    else:
        None
    core.wait(1)

# Finished the forward stage.
# Show a msg that moving to different stage
msg = visual.TextStim(mywin, pos=[0,0],text="Now backward",color="Black")
msg.draw()
mywin.flip()
core.wait(3) # wait for 3sec (can be changed to waitforkeys)
errAmount=0 # back to zero
numerr=0

for i in nTrialbk:
    block="backwards"
    trialListbk=expTrialBack(i)
    for x in trialListbk: # run a loop inside the
        #mark rec
        length=len(trialListbk)
        rect=rectList[x]
        markRec(rect)
        core.wait(1)
        #unmark rec
        unmarkRec(rect)
    gosound.play() # add sound at the end of presentation of trial
    for n in reversed(trialListbk):  # now reversing the order to check for errors
        trialClock=core.Clock()
        press, rectprs  = checkMouse()
        RT=core.Clock.getTime(trialClock)
        if press==rectList[n]:  # checking for errros and counting errors in trial.
            ans=1
            numerr=numerr
        else:
            ans=0
            numerr=numerr+1
        markRec(press)
        core.wait(0.5)
        unmarkRec(press)
        event.clearEvents()
        dataFile.write('%i,%s,%i,%s,%s,%f,%i\n' %(i,n,ans,rectprs,block,RT,length))
        if numerr>0: # Defining trial as error.
            trialErr=1
        else:
            trialErr=0
    numerr=0
    if trialErr==1:
        errAmount=errAmount+1
    else:
        errAmount=0
    if errAmount>2: # choose how many error in a raw, before stopping experiment.
        break
    else:
        None
    core.wait(1)
dataFile.close()

# open window
# present instructions

# present blank (corsi.jpg)
#
# present sequence (a function should decide which sequence)
# check mouse click -- light square accordingly
# check if correct or no
# write to file sequence, what was pressed - compare to what was presented
# give feedback

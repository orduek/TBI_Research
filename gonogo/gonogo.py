# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:39:25 2015
GO/NoGo task. Based on Cat and Mouse game from article of Simpson & Riggs, 2005.

@author: orduek
"""

# take pictures of cat and mouse
# training session: 4 trials - children are told to catch a mouse. when they press key a cage descends (rapidly) to catch it.
# training is go - nogo - go - nogo with feedback.
# stimulus displays for 3s with 1.5s intertrial interval.

# real session - 24. divided to 18 (go or nogo) and 6 (the opposite). stimulus display for 1,2 or 3s.  intertrial was 1.5s
# attched is a .odt document with the conditions (as suggested by Prof. Andrea Berger).

from psychopy import core, visual, gui, data, misc, event, sound
import time, os, random, numpy
# now turn to right folder
directory=os.getcwd()  # get folder
os.chdir(directory) # use it

#folder='/home/ord/Experiments_BP_Clinic/PCT/' #specify the folder of result files to be saved in
# savine last experiment data
try:#try to get a previous parameters file
    expInfo = misc.fromFile('gonogo.pickle')
except:#if not there then use a default set
    expInfo = {'subject no':'','Age':''}
expInfo['dateStr']= data.getDateStr() #add the current time
# dialouge box for name of subject and file
dlg = gui.DlgFromDict(expInfo, title='Go/NoGo Task', fixed=['dateStr'])
if dlg.OK:
    misc.toFile('gonogo.pickle', expInfo)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit

# check if folder exist and if not, create it
if not os.path.exists('results'):
    os.makedirs('results')

fileName = expInfo['subject no'] + expInfo['dateStr']
dataFile = open(directory+'/results/'+fileName+'.csv', 'w')#a simple text file with 'comma-separated-values'
dataFile.write('trialNo,trial,RT,press,answer\n')


# adjust sequence of presentation
mywin = visual.Window(fullscr=True,monitor="testMonitor",allowGUI=False,color="White") #rgb=[1,1,1])


# The script first need to check age.
# then- acording to age - divide conditions (in accordance with attached doc file.)
# build stumuli
fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)
redapple=visual.ImageStim(mywin,image='redapple.jpg',units='deg',pos=(0,0),size=8)
greenapple=visual.ImageStim(mywin,image='greenapple.jpg',units='deg',pos=(0,0),size=8)
basket=visual.ImageStim(mywin,image='applebasket.png',units='deg',pos=(-10,-4),size=15)
goodFeedback=visual.ImageStim(mywin, image="smiley.jpeg",units='deg',pos=(0,0),size=10)
badFeedback=visual.ImageStim(mywin, image="sadsmiley.jpeg",units='deg',pos=(0,0),size=10)
thanks=visual.ImageStim(mywin, image="thanks.png",units='deg', pos=(0,0),size=20)
cont=visual.ImageStim(mywin, image="continue.png",units='deg', pos=(0,0),size=10)
fixation = visual.GratingStim(mywin, color=-1, colorSpace='rgb', tex=None, mask='circle',size=0.01)
# the variables will be:
# age
# go number
# no go number
#stimulus exposure
# maximum time to react
# intertrial intervals (1.5s in all for now)
age=float(expInfo['Age'])
if age<=5:
    stimExp=2# stimulus exposure - should be changed with age (according to associated doc)
    maxTime=3 # maximum time for keypress
elif 5<age <=9:
    stimExp=1
    maxTime=1
else:
    stimExp=0.5
    maxTime=1

trialNo=0 # setting counter of trials


def training (stim1):
    x=20 # position of mouse
    if stim1==redapple:
        timeOfExp=core.CountdownTimer(stimExp)
        while timeOfExp.getTime()>0:
            press=0 # setting if pressed or not in order to show bad feedback
            x=x-0.5 # moving the mouse acros screen
            if x<-21:
                x=20
            else:
                x=x
            mywin.flip()
            stim1.pos=(x,0)
            stim1.draw()
            allKeys=event.getKeys()
            for thisKey in allKeys:
                if thisKey=='space':
                    press=1
                    basket.pos=(x,0)
                    stim1.draw()
                    basket.draw()
                    mywin.flip()
                    core.wait(1)
                    goodFeedback.draw()
                    mywin.flip()
                    core.wait(1)
                    timeOfExp=core.CountdownTimer(0)
        if press==0:
            mywin.flip()
            #badFeedback.draw()
            mywin.flip()
            core.wait(1)
    else:
        press=0
        timeOfExp=core.CountdownTimer(stimExp)
        while timeOfExp.getTime()>0:
            x=x-0.5 # moving the mouse acros screen
            if x<-21:
                x=20
            else:
                x=x
            mywin.flip()
            stim1.pos=(x,0)
            stim1.draw()
            allKeys=event.getKeys()
            for thisKey in allKeys:
                if thisKey=='space':
                    press=1
                    basket.pos=(x,0)
                    stim1.draw()
                    basket.draw()
                    mywin.flip()
                    core.wait(1)
                    #badFeedback.draw()
                    mywin.flip()
                    core.wait(1)
                    timeOfExp=core.CountdownTimer(0)
        if press==0:
            mywin.flip()  # clear all
            goodFeedback.draw()
            mywin.flip()
            core.wait(1)
def showTrial(stim1):
    press=0
    x=20 # position of mouse
    stim1.pos=(0,0) # reset position if moved to basket position previous trial
    if stim1==redapple:
        trial='Go'
        mywin.flip()
        # enter a while loop with presentation of simuli that countdown for end of presentation and pick up keyboard.
        timeOfExp=core.CountdownTimer(stimExp)
        while timeOfExp.getTime()>0 and press==0:
            stim1.draw()
            mywin.flip()
            allKeys=event.getKeys()
            for thisKey in allKeys:
                if thisKey=='escape':
                    core.quit()
                elif thisKey=='space':
                    RT=core.Clock.getTime(trialClock)
                    press=1 # key was pressed
                    answer=1 # correctly pressed key. i.e. hit
                    # should move the apple to basket
                    stim1.pos=(-10,-4)
                    stim1.draw()
                    basket.draw()
                    mywin.flip()
                    core.wait(1)

        # enter a while loop with remaining time without presentation of simulus
        timeofRt=core.CountdownTimer(maxTime-stimExp)
        while timeofRt.getTime()>0 and press==0:
            mywin.flip()
            allKeys=event.getKeys()
            for thisKey in allKeys:
                if thisKey=='escape':
                    core.quit()
                elif thisKey=='space':
                    RT=core.Clock.getTime(trialClock)
                    press=1 # key was pressed
                    answer=1 # correctly pressed key. i.e. hit
                    # should move the apple to basket
                    stim1.pos=(-10,-4)
                    stim1.draw()
                    basket.draw()
                    mywin.flip()
                    core.wait(1)

        if press==0:
            RT=core.Clock.getTime(trialClock)
            answer=0 # incorrect answer i.e. miss
            mywin.flip()
            #badFeedback.draw()
            core.wait(1)
        fixation.draw()
        mywin.flip()
        core.wait(1.5)
    if stim1==greenapple:
        trial='NoGo'
        mywin.flip()
        # enter a while loop with presentation of simuli that countdown for end of presentation and pick up keyboard.
        timeOfExp=core.CountdownTimer(stimExp)
        while timeOfExp.getTime()>0 and press==0:
            stim1.draw()
            mywin.flip()
            allKeys=event.getKeys()
            for thisKey in allKeys:
                if thisKey=='escape':
                    core.quit()
                elif thisKey=='space':
                    RT=core.Clock.getTime(trialClock)
                    press=1 # key was pressed
                    answer=0 # incorrectly pressed key. i.e. false alarm
                    # should move the apple to basket
                    stim1.pos=(-10,-4)
                    stim1.draw()
                    basket.draw()
                    mywin.flip()
                    core.wait(1)

        # enter a while loop with remaining time without presentation of simulus
        timeofRt=core.CountdownTimer(maxTime-stimExp)
        while timeofRt.getTime()>0 and press==0:
            mywin.flip()
            allKeys=event.getKeys()
            for thisKey in allKeys:
                if thisKey=='escape':
                    core.quit()
                elif thisKey=='space':
                    RT=core.Clock.getTime(trialClock)
                    press=1 # key was pressed
                    answer=0 # incorrectly pressed key. i.e. false alarm
                    # should move the apple to basket
                    stim1.pos=(-10,-4)
                    stim1.draw()
                    basket.draw()
                    mywin.flip()
                    core.wait(1)

        if press==0:
            RT=core.Clock.getTime(trialClock)
            answer=1 # correct answer i.e. correct rejection
            mywin.flip()
            #badFeedback.draw()
            core.wait(1)
        fixation.draw()
        mywin.flip()
        core.wait(1.5)
    return (trial, RT, press, answer)
# train 1
def trainsession(): # need to fix training function (maybe combine with showTrial)
    training(redapple)
    training(greenapple)
    training(redapple)
press=0
while press==0:
    trainsession()
    mywin.flip()
    cont.draw()
    mywin.flip()
    allKeys=event.waitKeys(keyList=['r','space'])
    for thisKey in allKeys:
        if thisKey=='space': # quit experiment
            press=1

# start sessions.
# Need to choose sessions according to age. (doc attached)

# list for ages 3-5:
# build function that builds list according to age
def buildList(age):
    x=['go','go']
    y=['nogo','nogo']
    if age<=5:
        x=x*12 # total 24 go
        y=y*4 # total 8 no go
    elif 5>age <=9:
        x=x*30
        y=y*10
    elif 9> age <=20:
        x=x*45
        y=y*15
    ageLst=x+y
    return(ageLst)


# load session list
# randomize it
# start running
ageLst=buildList(age)
random.shuffle(ageLst)

for i in ageLst:
    trialNo=trialNo+1
    trialClock=core.Clock()
    if i=='go':
        stim1=redapple
        trial,RT,press,answer = showTrial(stim1)
    elif i=='nogo':
        stim1=greenapple
        trial,RT,press, answer = showTrial(stim1)
    # show stimuli
    event.clearEvents()
    dataFile.write('%i,%s,%f,%i,%i\n' %(trialNo,trial,RT,press,answer))
    # measure RT
    # write to file (right/wrong, rt, stimulus, etc.)

dataFile.close()
core.wait(1)
thanks.draw()
mywin.flip()
core.wait(1)

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on 15 oct. 2015
ANT task. Created for the CreActive study. Based on Rueda et al. 2004.

@author: orduek
"""
from psychopy import core, visual, gui, data, misc, event, sound
import time, os, random, numpy

abspath = os.path.abspath(__file__)
directory = os.path.dirname(abspath)
os.chdir(directory)

try:#try to get a previous parameters file
    expInfo = misc.fromFile('ant.pickle')
except:#if not there then use a default set
    expInfo = {'subject no':'','age':''}
expInfo['dateStr']= data.getDateStr() #add the current time
# dialouge box for name of subject and file
dlg = gui.DlgFromDict(expInfo, title='ANT Task', fixed=['dateStr'])
if dlg.OK:
    misc.toFile('ant.pickle', expInfo)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit

# check if folder exist and if not, create it
if not os.path.exists('results'):
    os.makedirs('results')

fileName = 'ant' + expInfo['subject no'] + expInfo['dateStr']
dataFile = open(directory+'/results/'+fileName+'.csv', 'w')#a simple text file with 'comma-separated-values'
dataFile.write('trialNo,block,cue,direction,imagePos,congruency,correctAns,answer,rt,image\n')

stimListCong=['fish_lll.bmp','fish_rrr.bmp']
stimListInCong=['fish_lrl.bmp','fish_rlr.bmp']

#Open window
mywin = visual.Window(fullscr=True,monitor="testMonitor",allowGUI=False,color="Cyan")

# creating stilumi
fixation=visual.TextStim(mywin, text="+", units='deg',color="Black",pos=(0,0))
cueStimcenter=visual.TextStim(mywin, text="*", units='deg',color="Black",pos=(0,0))
cueStimUp=visual.TextStim(mywin, text="*", units='deg',color="Black",pos=(0,3))
cueStimDown=visual.TextStim(mywin, text="*", units='deg',color="Black",pos=(0,-3))
fishStim=visual.ImageStim(mywin, image="fish_lll.bmp", units='deg', pos=(0,3))

clapsound=sound.Sound(value='woohoo2.wav', secs=2)

# conditions: cue(double,none spatial[up,down]). flanker (congruent,incongruent). fish (up,down)
# We change a bit from Rueda and do only congruent and incongruent (not neutral). so we have two * 4 cues.
# Each block will consist of 32 trials with 16 congruent and 16 incongruent. ech 16 will be divided to 4 (upper cue, down cue, no cue, doublt cue)
# fixation random number from 400-1600ms. Cue 150ms. fixation 450ms. Target <1700ms (or no stop). feedback (2000ms).
# 8 conditions in equal proportions: two target types (congruent and incongruent) and four cues (no cue, central cue, double cue, spatial cue)
# Tha last is taken from Forns et al. 2014.

# build list of trials.
congList=['cong_no','cong_spatial','cong_center','cong_double'] # basic congruent list
incongList=['incong_no','incong_spatial','incong_center','incong_double'] # basic incongruent list

# position list
posList=[(0,3),(0,-3)]  #8 are coordianted with spatial. This list is for othr cus (center, double, no)
# build list of locations
spatialList=[cueStimUp,cueStimDown] *4

blockList=congList *4 + incongList*4
stimListCong=stimListCong*16
stimListInCong=stimListInCong*16

trialNo=0
def runBlock(block,blockList,stimListCong,stimListInCong,spatialList,posList):
    global trialNo
    trialNo=trialNo
    # randomize conditions
    random.shuffle(blockList)
    random.shuffle(spatialList)
    random.shuffle(stimListCong)
    random.shuffle(stimListInCong)
    random.shuffle(posList)
    # start experiment
    for i in blockList:
        trialNo=trialNo+1
        fixation.draw()
        mywin.flip()
        core.wait(random.uniform(0.4,1.6))
        stim=0
        if (i=='cong_no') or (i=='incong_no'): # congruent no Cue
            cue='NoCue'
            fixation.draw()
            mywin.flip()
            core.wait(0.1,hogCPUperiod=0)
        elif (i=='cong_double') or (i=='incong_double'):
            mywin.flip()
            cue='DoubleCue'
            fixation.draw()
            cueStimUp.draw()
            cueStimDown.draw()
            mywin.flip()
            core.wait(0.15,hogCPUperiod=0)
        elif (i=='cong_spatial') or (i=='incong_spatial'):
            mywin.flip()
            cue='SpatialCue'
            stim=spatialList.pop(0)
            fixation.draw()
            stim.draw()
            mywin.flip()
            core.wait(0.15,hogCPUperiod=0)
        elif (i=='cong_center') or (i=='incong_center'):
            mywin.flip()
            cue='CenterCue'
            fixation.draw()
            cueStimcenter.draw()
            core.wait(0.15,hogCPUperiod=0)
        mywin.flip()
        fixation.draw()
        core.wait(0.45,hogCPUperiod=0)  # wait before showing picture of animal
        if (i=='cong_no') or (i=='cong_double') or (i=='cong_center') or (i=='cong_spatial'):
            congruency='Cong'
            fishImage=stimListCong.pop(0)
            fishStim.setImage(fishImage)
            if stim==cueStimUp:
                imagePos='up'
                fishStim.pos=(0,3)
            elif stim==cueStimDown:
                imagePos='down'
                fishStim.pos=(0,-3)
            elif stim==0:
                position=posList.pop(0)
                if position==(0,3):
                    imagePos='up'
                elif position==(0,-3):
                    imagePos='down'
                fishStim.pos=position
            mywin.flip()
            fixation.draw()
            fishStim.draw()
            mywin.flip()

        elif (i=='incong_no') or (i=='incong_double') or (i=='incong_center') or (i=='incong_spatial'):
            congruency='InCong'
            fishImage=stimListInCong.pop(0)
            fishStim.setImage(fishImage)
            if stim==cueStimUp:
                imagePos='up'
                fishStim.pos=(0,3)
            elif stim==cueStimDown:
                imagePos='down'
                fishStim.pos=(0,-3)
            elif stim==0:
                position=posList.pop(0)
                if position==(0,3):
                    imagePos='up'
                elif position==(0,-3):
                    imagePos='down'
                fishStim.pos=position
            mywin.flip()
            fixation.draw()
            fishStim.draw()
            mywin.flip()
        trialClock=core.Clock()
        allKeys=event.waitKeys(maxWait=1.7,keyList=['q','p','escape'])
        if allKeys==None: # if no key was presses
            answer='None'
            rt=core.Clock.getTime(trialClock)
        else:
            for thisKey in allKeys:
                if thisKey=='escape':
                    core.quit()
                elif thisKey=='q':
                    answer='q'
                    rt=core.Clock.getTime(trialClock)
                elif thisKey=='p':
                    answer='p'
                    rt=core.Clock.getTime(trialClock)
        if (fishImage=='fish_lll.bmp') or (fishImage=='fish_rlr.bmp'):
            direction='left'
            if answer=='p':
                correctAns=0
            elif answer=='q':
                correctAns=1
        else:
            direction='right'
            if answer=='p':
                correctAns=1
            elif answer=='q':
                correctAns=0
        if correctAns==1:  # add whoowoo sound if answered right (can change to add it only in practice blocks)
            clapsound.play()

        fixation.draw()
        mywin.flip()
        core.wait(1)
        event.clearEvents()
        image=fishImage
        dataFile.write('%i,%i,%s,%s,%s,%s,%i,%s,%f,%s\n' %(trialNo,block,cue,direction,imagePos,congruency,correctAns,answer,rt,image))

# start with instructions
instMsg=visual.TextStim(mywin, text="Welcome.\nYou need to feed the fish. So when the fish looks left you need to give the food to the left. When looks right, you need to feed to the right", color="Black")
instMsg.draw()
mywin.flip()
event.waitKeys()

# show example
mywin.flip()
fixation.draw()
fishStim.draw()
mywin.flip()
allKeys=event.waitKeys(maxWait=1.7,keyList=['q','p','escape'])
if allKeys==None: # if no key was presses
    answer='None'

else:
    for thisKey in allKeys:
        if thisKey=='escape':
            core.quit()
        elif thisKey=='q':
            answer='q'
            clapsound.play()
        elif thisKey=='p':
            answer='p'
core.wait(1)
mywin.flip()
fishStim.setImage('fish_rrr.bmp')
fishStim.pos=(0,-3)
fixation.draw()
fishStim.draw()
mywin.flip()
allKeys=event.waitKeys(maxWait=1.7,keyList=['q','p','escape'])
if allKeys==None: # if no key was presses
    answer='None'
else:
    for thisKey in allKeys:
        if thisKey=='escape':
            core.quit()
        elif thisKey=='q':
            answer='q'
        elif thisKey=='p':
            answer='p'
            clapsound.play()
core.wait(1)
mywin.flip()
fishStim.setImage('fish_lrl.bmp')
fishStim.pos=(0,3)
fixation.draw()
fishStim.draw()
mywin.flip()
allKeys=event.waitKeys(maxWait=1.7,keyList=['q','p','escape'])
if allKeys==None: # if no key was presses
    answer='None'
else:
    for thisKey in allKeys:
        if thisKey=='escape':
            core.quit()
        elif thisKey=='q':
            answer='q'
        elif thisKey=='p':
            answer='p'
            clapsound.play()
core.wait(1)
mywin.flip()
fishStim.setImage('fish_rlr.bmp')
fishStim.pos=(0,-3)
fixation.draw()
fishStim.draw()
mywin.flip()
allKeys=event.waitKeys(maxWait=1.7,keyList=['q','p','escape'])
if allKeys==None: # if no key was presses
    answer='None'
else:
    for thisKey in allKeys:
        if thisKey=='escape':
            core.quit()
        elif thisKey=='q':
            answer='q'
            clapsound.play()
        elif thisKey=='p':
            answer='p'
core.wait(1)

instMsg.text="Ready for practice?"
instMsg.draw()
mywin.flip()
event.waitKeys()
# Now start practice trials (in a while loop so we can go back to it until ready)
endP=0 # set practice loop
while endP==0:
    # training block - 16 samples
    blockList=congList *2 + incongList*2
    stimListCong=stimListCong*4
    stimListInCong=stimListInCong*4
    spatialList=[cueStimUp,cueStimDown] *2
    posListPractice=posList * 6 # 12 trials without spatial cue
    runBlock(0,blockList,stimListCong,stimListInCong,spatialList,posListPractice) # training block, same length but only 1-back.
    instMsg.text="Ready to begin the game?"
    instMsg.draw()
    mywin.flip()
    allKeys=event.waitKeys()
    for thisKey in allKeys:
        if thisKey=='escape':
            core.quit()
        elif thisKey=='space':
            endP=1
        elif thisKey=='r':
            endP==0

# run first block
# 32 trials.
blockList=congList *4 + incongList*4
stimListCong=stimListCong*8
stimListInCong=stimListInCong*8
spatialList=[cueStimUp,cueStimDown] *4
posListPractice=posList * 12 # 24 trials without spatial cue
runBlock(1,blockList,stimListCong,stimListInCong,spatialList,posListPractice)

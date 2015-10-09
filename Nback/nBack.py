# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:30:16 2015

@author: ord
N-Back task - basis to use in TBI study (CreactKids)

"""

# build basic task (practice, 1-back, 2-back)
# Decide to use animals for small children and other for adolecsents.
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:01:15 2015

@author: orduek
Corsi Block Expreiment in Psychopy.
This experiment is spatial memory experiment as in the WMS
"""

from psychopy import core, visual, gui, data, misc, event, sound
import time, os, random
# now turn to right folder
directory=os.getcwd()  # get folder
os.chdir(directory) # use it

#folder='/home/ord/Experiments_BP_Clinic/PCT/' #specify the folder of result files to be saved in
# savine last experiment data
try:#try to get a previous parameters file
    expInfo = misc.fromFile('nBack.pickle')
except:#if not there then use a default set
    expInfo = {'subject no':''}
expInfo['dateStr']= data.getDateStr() #add the current time
# dialouge box for name of subject and file
dlg = gui.DlgFromDict(expInfo, title='nBack Task', fixed=['dateStr'])
if dlg.OK:
    misc.toFile('nBack.pickle', expInfo)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit

# check if folder exist and if not, create it
if not os.path.exists('results'):
    os.makedirs('results')

fileName = expInfo['subject no'] + expInfo['dateStr']
dataFile = open(directory+'/results/'+fileName+'.csv', 'w')#a simple text file with 'comma-separated-values'
dataFile.write('trialNo,block,trialCond,rt,response,answer,stimulus\n')

rectColor="DarkSlateBlue" # set retangle default color
# make a functino that will get mouse click position

# adjust sequence of presentation
mywin = visual.Window(fullscr=True,monitor="testMonitor",allowGUI=False,color="White") #rgb=[1,1,1])
### Build rectangles

# make stimuli list
animalList=['1.bmp','2.bmp','3.bmp','4.bmp','5.bmp','6.bmp','7.bmp','8.bmp','9.bmp','10.bmp']

fixation = visual.GratingStim(mywin, color=-1, colorSpace='rgb', tex=None, mask='circle',size=0.01)
targetImage=visual.ImageStim(mywin,image=animalList[1],units='deg',pos=(0,0),size=6)
distractorImage1=visual.ImageStim(mywin,image=animalList[2],units='deg',pos=(0,0),size=6)
distractorImage2=visual.ImageStim(mywin,image=animalList[3],units='deg',pos=(0,0),size=6)
thanks=visual.ImageStim(mywin,image='thanks.png',units='deg',pos=(0,0),size=8)
contin=visual.ImageStim(mywin,image='continue.png',units='deg',pos=(0,0))
# present stimulus for 1500ms
# interstimulus interval of 1000ms

# two block loads (1-back, 2-back)
# 25 trials per block
# first three of each block are not targets
# 33% of remaining (7) are targets.

# building list of trials for block
# list containing distractor or target (7 targets, 18 distractors. first three must be distractors)
distList=['distractor'] *3 # first two (the first will be set)
targetList=['distractor'] *15 + ['target'] *7 # list of 7 targets and 15 distractors
random.shuffle(targetList)
trialList=distList+targetList # full list
img=random.sample(animalList,1)
runList=[img]  # list that will be filled with pictures so I can go back 1,2 or more if needed
trialNo=0
stimExp = 1.5 #1500ms exposure of stimulus


def runBlock(n,block):
    global trialNo
    trialNo=trialNo
    random.shuffle(targetList)
    trialList=distList+targetList
    for i in trialList:
        trialCond=i
        trialClock=core.Clock()
        trialNo=trialNo+1
        if i=='distractor':
            distImg=random.sample(animalList,1)
            while distImg[0]==runList[len(runList)-n]:
                distImg=random.sample(animalList,1)
            distractorImage1.setImage(distImg[0])
            runList.append(distImg[0])
            stimulus=distImg[0] # setting new last image
            distractorImage1.draw()
            mywin.flip()
            allKeys=event.waitKeys(maxWait=1.5,keyList=['space','escape'])
            if allKeys==None:
                response=0
                answer=1
                rt=core.Clock.getTime(trialClock)
            else:
                response=1
                for thisKey in allKeys:
                    if thisKey=='escape':
                        core.quit()
                    elif thisKey=='space':
                        answer=0
                        rt=core.Clock.getTime(trialClock)

            mywin.flip()
            core.wait(1)
            # save answers to file
        else:

            target=runList[len(runList)-n]
            targetImage.setImage(target)
            runList.append(target)
            stimulus=target
            targetImage.draw()
            mywin.flip()
            allKeys=event.waitKeys(maxWait=1.5,keyList=['space','escape'])
            if allKeys==None:
                response=0
                answer=0
                rt=core.Clock.getTime(trialClock)

            else:
                response=1
                for thisKey in allKeys:
                    if thisKey=='escape':
                        core.quit()
                    elif thisKey=='space':
                        answer=1
                        rt=core.Clock.getTime(trialClock)

            mywin.flip()
            core.wait(1)
            #save to file (trialNo,condition,image,press,RT,correct/incorrect)
        event.clearEvents()
        dataFile.write('%i,%i,%s,%f,%i,%i,%s\n' %(trialNo,block,trialCond,rt,response,answer,stimulus))
# training block

# 1-back block
runBlock(1,1)
contin.draw()
mywin.flip()

event.waitKeys()

runBlock(2,2)
thanks.draw()
mywin.flip()
core.wait(2)
dataFile.close()
#mywin.flip()
#core.wait(4)
# 2-back block
#runBlock(2,2)
#block=2


# save file



# measure RT
# write to file (right/wrong, rt, stimulus, etc.)

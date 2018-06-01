#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.03), October 17, 2017, at 15:29
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = u'untitled'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation


aloneori=[45,135,270,90,225,0,180,315]
sameori=[270,0,315,180,90,45,135,225]
outori=[135,270,45,315,225,90,180,0]
emptyori=[0,45,135,225,90,315,270,180]
inori=[315,90,180,270,45,225,0,135]

RFsize=28;
mysf=0.08;
gratinginx=-17
gratinginy=-20
gratingoutx=13
gratingouty=10
myvel=0.04;
myori=45;
interval=6
direcchange=180     #   90 or 180

# Setup the Window
win0 = visual.Window(
    size=(400, 400),pos=(150,450), screen=3,
    allowGUI=False, allowStencil=False,
    monitor='DetectMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg')
win = visual.Window(
    size=(1280,1024),screen=1,
    allowGUI=False, allowStencil=False,
    monitor='DisplayMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Alone"
AloneClock = core.Clock()
grating = visual.GratingStim(win=win, name='grating',units=u'deg', 
    tex=u'sqr', mask=u'circle',
    ori=0, pos=[gratinginx, gratinginy], size=[RFsize,RFsize ], sf=mysf, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=512, interpolate=True, depth=0.0)
White = visual.Rect(win=win0, name='White',units=u'deg', 
    size=[90, 90],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)

# Initialize components for Routine "Allsame"
AllsameClock = core.Clock()
Background = visual.GratingStim(win=win, name='Background',units=u'deg', 
    tex=u'sqr', mask=None,
    ori=0 , pos=[0, 0], size=[120, 120], sf=mysf, phase=0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=512, interpolate=True, depth=0.0)
White2 = visual.Rect(win=win0, name='White2',units=u'deg', 
    size=[80, 80],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)

# Initialize components for Routine "out"
outClock = core.Clock()
Background_out = visual.GratingStim(win=win, name='Background_out',units=u'deg', 
    tex=u'sqr', mask=None,
    ori=0, pos=[0, 0], size=[120, 120], sf=mysf, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=512, interpolate=True, depth=0.0)
grating_out = visual.GratingStim(win=win, name='grating_out',
    tex=u'sqr', mask=u'circle',
    ori=0, pos=[gratingoutx, gratingouty], size=[RFsize, RFsize], sf=mysf, phase=0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=512, interpolate=True, depth=-1.0)
White3 = visual.Rect(win=win0, name='White3',units=u'deg', 
    size=[80, 80],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)

# Initialize components for Routine "Empty"
EmptyClock = core.Clock()
Background_empty = visual.GratingStim(win=win, name='Background_empty',units=u'deg', 
    tex=u'sqr', mask=None,
    ori=1.0, pos=[0, 0], size=[120,120], sf=mysf, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=512, interpolate=True, depth=0.0)
circle = visual.Polygon(win=win, name='circle',
    edges = 90, size=[RFsize, RFsize],
    ori=1.0, pos=[gratinginx, gratinginy],
    lineWidth=1, lineColor=[0,0,0], lineColorSpace=u'rgb',
    fillColor=[0,0,0], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)
White4 = visual.Rect(win=win0, name='White4',units=u'deg', 
    size=[80, 80],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)

# Initialize components for Routine "In"
InClock = core.Clock()
Background_in = visual.GratingStim(win=win, name='Background_in',units=u'deg', 
    tex=u'sqr', mask=None,
    ori=1.0, pos=[0, 0], size=[120, 120], sf=mysf, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=512, interpolate=True, depth=0.0)
grating_in = visual.GratingStim(win=win, name='grating_in',units=u'deg', 
    tex=u'sqr', mask=u'circle',
    ori=1.0, pos=[gratinginx, gratinginy], size=[RFsize, RFsize], sf=mysf, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=512, interpolate=True, depth=-1.0)
White5 = visual.Rect(win=win0, name='White5',units=u'deg', 
    size=[80, 80],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method=u'random', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "Alone"-------
    t = 0
    AloneClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating.setOri(aloneori[0])
    # keep track of which components have finished
    AloneComponents = []
    AloneComponents.append(grating)
    AloneComponents.append(White)
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Alone"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AloneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating* updates
        if t >= interval and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        elif grating.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating.setAutoDraw(False)
        if grating.status == STARTED:  # only update if being drawn
           grating.setPhase(myvel,'+')
        
        # *White* updates
        if t >= interval and White.status == NOT_STARTED:
            # keep track of start time/frame for later
            White.tStart = t  # underestimates by a little under one frame
            White.frameNStart = frameN  # exact frame index
            White.setAutoDraw(True)
        elif White.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AloneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Alone"-------
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "Allsame"-------
    t = 0
    AllsameClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background.setOri(sameori[0])
    # keep track of which components have finished
    AllsameComponents = []
    AllsameComponents.append(Background)
    AllsameComponents.append(White2)
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Allsame"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AllsameClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background* updates
        if t >= interval and Background.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background.tStart = t  # underestimates by a little under one frame
            Background.frameNStart = frameN  # exact frame index
            Background.setAutoDraw(True)
        elif Background.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background.setAutoDraw(False)
        if Background.status == STARTED:  # only update if being drawn
           Background.setPhase(myvel,'+')
        
        # *White2* updates
        if t >= interval and White2.status == NOT_STARTED:
            # keep track of start time/frame for later
            White2.tStart = t  # underestimates by a little under one frame
            White2.frameNStart = frameN  # exact frame index
            White2.setAutoDraw(True)
        elif White2.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllsameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Allsame"-------
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "out"-------
    t = 0
    outClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_out.setOri(outori[0])
    grating_out.ori=Background_out.ori
    grating_out.setOri(direcchange,'+')
    # keep track of which components have finished
    outComponents = []
    outComponents.append(Background_out)
    outComponents.append(grating_out)
    outComponents.append(White3)
    for thisComponent in outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "out"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_out* updates
        if t >= interval and Background_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_out.tStart = t  # underestimates by a little under one frame
            Background_out.frameNStart = frameN  # exact frame index
            Background_out.setAutoDraw(True)
        elif Background_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_out.setAutoDraw(False)
        if Background_out.status == STARTED:  # only update if being drawn
           Background_out.setPhase(myvel,'+')
        
        # *grating_out* updates
        if t >= interval and grating_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_out.tStart = t  # underestimates by a little under one frame
            grating_out.frameNStart = frameN  # exact frame index
            grating_out.setAutoDraw(True)
        elif grating_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_out.setAutoDraw(False)
        if grating_out.status == STARTED:  # only update if being drawn
           grating_out.setPhase(myvel,'+')
        
        # *White3* updates
        if t >= interval and White3.status == NOT_STARTED:
            # keep track of start time/frame for later
            White3.tStart = t  # underestimates by a little under one frame
            White3.frameNStart = frameN  # exact frame index
            White3.setAutoDraw(True)
        elif White3.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "out"-------
    for thisComponent in outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "Empty"-------
    t = 0
    EmptyClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_empty.setOri(emptyori[0])
    circle.setOri(0)
    # keep track of which components have finished
    EmptyComponents = []
    EmptyComponents.append(Background_empty)
    EmptyComponents.append(circle)
    EmptyComponents.append(White4)
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Empty"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EmptyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_empty* updates
        if t >= interval and Background_empty.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_empty.tStart = t  # underestimates by a little under one frame
            Background_empty.frameNStart = frameN  # exact frame index
            Background_empty.setAutoDraw(True)
        elif Background_empty.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_empty.setAutoDraw(False)
        if Background_empty.status == STARTED:  # only update if being drawn
           Background_empty.setPhase(myvel,'+')
        
        # *circle* updates
        if t >= interval and circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle.tStart = t  # underestimates by a little under one frame
            circle.frameNStart = frameN  # exact frame index
            circle.setAutoDraw(True)
        elif circle.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            circle.setAutoDraw(False)
        
        # *White4* updates
        if t >= interval and White4.status == NOT_STARTED:
            # keep track of start time/frame for later
            White4.tStart = t  # underestimates by a little under one frame
            White4.frameNStart = frameN  # exact frame index
            White4.setAutoDraw(True)
        elif White4.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmptyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Empty"-------
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    


    #------Prepare to start Routine "In"-------
    t = 0
    InClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating_in.setOri(inori[0])
    Background_in.ori=grating_in.ori
    Background_in.setOri(direcchange,'+')
    # keep track of which components have finished
    InComponents = []
    InComponents.append(Background_in)
    InComponents.append(grating_in)
    InComponents.append(White5)
    for thisComponent in InComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "In"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_in* updates
        if t >= interval and Background_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_in.tStart = t  # underestimates by a little under one frame
            Background_in.frameNStart = frameN  # exact frame index
            Background_in.setAutoDraw(True)
        elif Background_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_in.setAutoDraw(False)
        if Background_in.status == STARTED:  # only update if being drawn
           Background_in.setPhase(myvel,'+')
        # *grating_in* updates
        if t >= interval and grating_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_in.tStart = t  # underestimates by a little under one frame
            grating_in.frameNStart = frameN  # exact frame index
            grating_in.setAutoDraw(True)
        elif grating_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_in.setAutoDraw(False)
        if grating_in.status == STARTED:  # only update if being drawn
           grating_in.setPhase(myvel,'+')
        
        # *White5* updates
        if t >= interval and White5.status == NOT_STARTED:
            # keep track of start time/frame for later
            White5.tStart = t  # underestimates by a little under one frame
            White5.frameNStart = frameN  # exact frame index
            White5.setAutoDraw(True)
        elif White5.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()

#-------Ending Routine "In"-------
    for thisComponent in InComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)





    #11111111111111111111################





    
    #------Prepare to start Routine "out"-------
    t = 0
    outClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_out.setOri(outori[1])
    grating_out.ori=Background_out.ori
    grating_out.setOri(direcchange,'+')
    # keep track of which components have finished
    outComponents = []
    outComponents.append(Background_out)
    outComponents.append(grating_out)
    outComponents.append(White3)
    for thisComponent in outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "out"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_out* updates
        if t >= interval and Background_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_out.tStart = t  # underestimates by a little under one frame
            Background_out.frameNStart = frameN  # exact frame index
            Background_out.setAutoDraw(True)
        elif Background_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_out.setAutoDraw(False)
        if Background_out.status == STARTED:  # only update if being drawn
           Background_out.setPhase(myvel,'+')
        
        # *grating_out* updates
        if t >= interval and grating_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_out.tStart = t  # underestimates by a little under one frame
            grating_out.frameNStart = frameN  # exact frame index
            grating_out.setAutoDraw(True)
        elif grating_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_out.setAutoDraw(False)
        if grating_out.status == STARTED:  # only update if being drawn
           grating_out.setPhase(myvel,'+')
        
        # *White3* updates
        if t >= interval and White3.status == NOT_STARTED:
            # keep track of start time/frame for later
            White3.tStart = t  # underestimates by a little under one frame
            White3.frameNStart = frameN  # exact frame index
            White3.setAutoDraw(True)
        elif White3.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "out"-------
    for thisComponent in outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    

    


    #------Prepare to start Routine "In"-------
    t = 0
    InClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating_in.setOri(inori[1])
    Background_in.ori=grating_in.ori
    Background_in.setOri(direcchange,'+')
    # keep track of which components have finished
    InComponents = []
    InComponents.append(Background_in)
    InComponents.append(grating_in)
    InComponents.append(White5)
    for thisComponent in InComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "In"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_in* updates
        if t >= interval and Background_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_in.tStart = t  # underestimates by a little under one frame
            Background_in.frameNStart = frameN  # exact frame index
            Background_in.setAutoDraw(True)
        elif Background_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_in.setAutoDraw(False)
        if Background_in.status == STARTED:  # only update if being drawn
           Background_in.setPhase(myvel,'+')
        # *grating_in* updates
        if t >= interval and grating_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_in.tStart = t  # underestimates by a little under one frame
            grating_in.frameNStart = frameN  # exact frame index
            grating_in.setAutoDraw(True)
        elif grating_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_in.setAutoDraw(False)
        if grating_in.status == STARTED:  # only update if being drawn
           grating_in.setPhase(myvel,'+')
        
        # *White5* updates
        if t >= interval and White5.status == NOT_STARTED:
            # keep track of start time/frame for later
            White5.tStart = t  # underestimates by a little under one frame
            White5.frameNStart = frameN  # exact frame index
            White5.setAutoDraw(True)
        elif White5.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()

#-------Ending Routine "In"-------
    for thisComponent in InComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


    #------Prepare to start Routine "Allsame"-------
    t = 0
    AllsameClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background.setOri(sameori[1])
    # keep track of which components have finished
    AllsameComponents = []
    AllsameComponents.append(Background)
    AllsameComponents.append(White2)
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Allsame"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AllsameClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background* updates
        if t >= interval and Background.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background.tStart = t  # underestimates by a little under one frame
            Background.frameNStart = frameN  # exact frame index
            Background.setAutoDraw(True)
        elif Background.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background.setAutoDraw(False)
        if Background.status == STARTED:  # only update if being drawn
           Background.setPhase(myvel,'+')
        
        # *White2* updates
        if t >= interval and White2.status == NOT_STARTED:
            # keep track of start time/frame for later
            White2.tStart = t  # underestimates by a little under one frame
            White2.frameNStart = frameN  # exact frame index
            White2.setAutoDraw(True)
        elif White2.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllsameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Allsame"-------
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    #------Prepare to start Routine "Empty"-------
    t = 0
    EmptyClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_empty.setOri(emptyori[1])
    circle.setOri(0)
    # keep track of which components have finished
    EmptyComponents = []
    EmptyComponents.append(Background_empty)
    EmptyComponents.append(circle)
    EmptyComponents.append(White4)
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Empty"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EmptyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_empty* updates
        if t >= interval and Background_empty.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_empty.tStart = t  # underestimates by a little under one frame
            Background_empty.frameNStart = frameN  # exact frame index
            Background_empty.setAutoDraw(True)
        elif Background_empty.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_empty.setAutoDraw(False)
        if Background_empty.status == STARTED:  # only update if being drawn
           Background_empty.setPhase(myvel,'+')
        
        # *circle* updates
        if t >= interval and circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle.tStart = t  # underestimates by a little under one frame
            circle.frameNStart = frameN  # exact frame index
            circle.setAutoDraw(True)
        elif circle.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            circle.setAutoDraw(False)
        
        # *White4* updates
        if t >= interval and White4.status == NOT_STARTED:
            # keep track of start time/frame for later
            White4.tStart = t  # underestimates by a little under one frame
            White4.frameNStart = frameN  # exact frame index
            White4.setAutoDraw(True)
        elif White4.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmptyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Empty"-------
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #------Prepare to start Routine "Alone"-------
    t = 0
    AloneClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating.setOri(aloneori[1])
    # keep track of which components have finished
    AloneComponents = []
    AloneComponents.append(grating)
    AloneComponents.append(White)
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Alone"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AloneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating* updates
        if t >= interval and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        elif grating.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating.setAutoDraw(False)
        if grating.status == STARTED:  # only update if being drawn
           grating.setPhase(myvel,'+')
        
        # *White* updates
        if t >= interval and White.status == NOT_STARTED:
            # keep track of start time/frame for later
            White.tStart = t  # underestimates by a little under one frame
            White.frameNStart = frameN  # exact frame index
            White.setAutoDraw(True)
        elif White.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AloneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Alone"-------
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    


#222222222222222222222222222




    #------Prepare to start Routine "Empty"-------
    t = 0
    EmptyClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_empty.setOri(emptyori[2])
    circle.setOri(0)
    # keep track of which components have finished
    EmptyComponents = []
    EmptyComponents.append(Background_empty)
    EmptyComponents.append(circle)
    EmptyComponents.append(White4)
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Empty"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EmptyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_empty* updates
        if t >= interval and Background_empty.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_empty.tStart = t  # underestimates by a little under one frame
            Background_empty.frameNStart = frameN  # exact frame index
            Background_empty.setAutoDraw(True)
        elif Background_empty.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_empty.setAutoDraw(False)
        if Background_empty.status == STARTED:  # only update if being drawn
           Background_empty.setPhase(myvel,'+')
        
        # *circle* updates
        if t >= interval and circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle.tStart = t  # underestimates by a little under one frame
            circle.frameNStart = frameN  # exact frame index
            circle.setAutoDraw(True)
        elif circle.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            circle.setAutoDraw(False)
        
        # *White4* updates
        if t >= interval and White4.status == NOT_STARTED:
            # keep track of start time/frame for later
            White4.tStart = t  # underestimates by a little under one frame
            White4.frameNStart = frameN  # exact frame index
            White4.setAutoDraw(True)
        elif White4.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmptyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Empty"-------
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)



    #------Prepare to start Routine "Allsame"-------
    t = 0
    AllsameClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background.setOri(sameori[2])
    # keep track of which components have finished
    AllsameComponents = []
    AllsameComponents.append(Background)
    AllsameComponents.append(White2)
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Allsame"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AllsameClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background* updates
        if t >= interval and Background.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background.tStart = t  # underestimates by a little under one frame
            Background.frameNStart = frameN  # exact frame index
            Background.setAutoDraw(True)
        elif Background.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background.setAutoDraw(False)
        if Background.status == STARTED:  # only update if being drawn
           Background.setPhase(myvel,'+')
        
        # *White2* updates
        if t >= interval and White2.status == NOT_STARTED:
            # keep track of start time/frame for later
            White2.tStart = t  # underestimates by a little under one frame
            White2.frameNStart = frameN  # exact frame index
            White2.setAutoDraw(True)
        elif White2.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllsameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Allsame"-------
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
            
    #------Prepare to start Routine "out"-------
    t = 0
    outClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_out.setOri(outori[2])
    grating_out.ori=Background_out.ori
    grating_out.setOri(direcchange,'+')
    # keep track of which components have finished
    outComponents = []
    outComponents.append(Background_out)
    outComponents.append(grating_out)
    outComponents.append(White3)
    for thisComponent in outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "out"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_out* updates
        if t >= interval and Background_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_out.tStart = t  # underestimates by a little under one frame
            Background_out.frameNStart = frameN  # exact frame index
            Background_out.setAutoDraw(True)
        elif Background_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_out.setAutoDraw(False)
        if Background_out.status == STARTED:  # only update if being drawn
           Background_out.setPhase(myvel,'+')
        
        # *grating_out* updates
        if t >= interval and grating_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_out.tStart = t  # underestimates by a little under one frame
            grating_out.frameNStart = frameN  # exact frame index
            grating_out.setAutoDraw(True)
        elif grating_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_out.setAutoDraw(False)
        if grating_out.status == STARTED:  # only update if being drawn
           grating_out.setPhase(myvel,'+')
        
        # *White3* updates
        if t >= interval and White3.status == NOT_STARTED:
            # keep track of start time/frame for later
            White3.tStart = t  # underestimates by a little under one frame
            White3.frameNStart = frameN  # exact frame index
            White3.setAutoDraw(True)
        elif White3.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "out"-------
    for thisComponent in outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    

    


    #------Prepare to start Routine "In"-------
    t = 0
    InClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating_in.setOri(inori[2])
    Background_in.ori=grating_in.ori
    Background_in.setOri(direcchange,'+')
    # keep track of which components have finished
    InComponents = []
    InComponents.append(Background_in)
    InComponents.append(grating_in)
    InComponents.append(White5)
    for thisComponent in InComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "In"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_in* updates
        if t >= interval and Background_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_in.tStart = t  # underestimates by a little under one frame
            Background_in.frameNStart = frameN  # exact frame index
            Background_in.setAutoDraw(True)
        elif Background_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_in.setAutoDraw(False)
        if Background_in.status == STARTED:  # only update if being drawn
           Background_in.setPhase(myvel,'+')
        # *grating_in* updates
        if t >= interval and grating_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_in.tStart = t  # underestimates by a little under one frame
            grating_in.frameNStart = frameN  # exact frame index
            grating_in.setAutoDraw(True)
        elif grating_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_in.setAutoDraw(False)
        if grating_in.status == STARTED:  # only update if being drawn
           grating_in.setPhase(myvel,'+')
        
        # *White5* updates
        if t >= interval and White5.status == NOT_STARTED:
            # keep track of start time/frame for later
            White5.tStart = t  # underestimates by a little under one frame
            White5.frameNStart = frameN  # exact frame index
            White5.setAutoDraw(True)
        elif White5.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()

#-------Ending Routine "In"-------
    for thisComponent in InComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    #------Prepare to start Routine "Alone"-------
    t = 0
    AloneClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating.setOri(aloneori[2])
    # keep track of which components have finished
    AloneComponents = []
    AloneComponents.append(grating)
    AloneComponents.append(White)
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Alone"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AloneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating* updates
        if t >= interval and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        elif grating.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating.setAutoDraw(False)
        if grating.status == STARTED:  # only update if being drawn
           grating.setPhase(myvel,'+')
        
        # *White* updates
        if t >= interval and White.status == NOT_STARTED:
            # keep track of start time/frame for later
            White.tStart = t  # underestimates by a little under one frame
            White.frameNStart = frameN  # exact frame index
            White.setAutoDraw(True)
        elif White.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AloneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Alone"-------
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    

    

    




#3333333333333333333333333333333333
















    #------Prepare to start Routine "Empty"-------
    t = 0
    EmptyClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_empty.setOri(emptyori[3])
    circle.setOri(0)
    # keep track of which components have finished
    EmptyComponents = []
    EmptyComponents.append(Background_empty)
    EmptyComponents.append(circle)
    EmptyComponents.append(White4)
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Empty"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EmptyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_empty* updates
        if t >= interval and Background_empty.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_empty.tStart = t  # underestimates by a little under one frame
            Background_empty.frameNStart = frameN  # exact frame index
            Background_empty.setAutoDraw(True)
        elif Background_empty.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_empty.setAutoDraw(False)
        if Background_empty.status == STARTED:  # only update if being drawn
           Background_empty.setPhase(myvel,'+')
        
        # *circle* updates
        if t >= interval and circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle.tStart = t  # underestimates by a little under one frame
            circle.frameNStart = frameN  # exact frame index
            circle.setAutoDraw(True)
        elif circle.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            circle.setAutoDraw(False)
        
        # *White4* updates
        if t >= interval and White4.status == NOT_STARTED:
            # keep track of start time/frame for later
            White4.tStart = t  # underestimates by a little under one frame
            White4.frameNStart = frameN  # exact frame index
            White4.setAutoDraw(True)
        elif White4.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmptyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Empty"-------
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    


    #------Prepare to start Routine "In"-------
    t = 0
    InClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating_in.setOri(inori[3])
    Background_in.ori=grating_in.ori
    Background_in.setOri(direcchange,'+')
    # keep track of which components have finished
    InComponents = []
    InComponents.append(Background_in)
    InComponents.append(grating_in)
    InComponents.append(White5)
    for thisComponent in InComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "In"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_in* updates
        if t >= interval and Background_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_in.tStart = t  # underestimates by a little under one frame
            Background_in.frameNStart = frameN  # exact frame index
            Background_in.setAutoDraw(True)
        elif Background_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_in.setAutoDraw(False)
        if Background_in.status == STARTED:  # only update if being drawn
           Background_in.setPhase(myvel,'+')
        # *grating_in* updates
        if t >= interval and grating_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_in.tStart = t  # underestimates by a little under one frame
            grating_in.frameNStart = frameN  # exact frame index
            grating_in.setAutoDraw(True)
        elif grating_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_in.setAutoDraw(False)
        if grating_in.status == STARTED:  # only update if being drawn
           grating_in.setPhase(myvel,'+')
        
        # *White5* updates
        if t >= interval and White5.status == NOT_STARTED:
            # keep track of start time/frame for later
            White5.tStart = t  # underestimates by a little under one frame
            White5.frameNStart = frameN  # exact frame index
            White5.setAutoDraw(True)
        elif White5.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()

#-------Ending Routine "In"-------
    for thisComponent in InComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "Alone"-------
    t = 0
    AloneClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating.setOri(aloneori[3])
    # keep track of which components have finished
    AloneComponents = []
    AloneComponents.append(grating)
    AloneComponents.append(White)
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Alone"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AloneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating* updates
        if t >= interval and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        elif grating.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating.setAutoDraw(False)
        if grating.status == STARTED:  # only update if being drawn
           grating.setPhase(myvel,'+')
        
        # *White* updates
        if t >= interval and White.status == NOT_STARTED:
            # keep track of start time/frame for later
            White.tStart = t  # underestimates by a little under one frame
            White.frameNStart = frameN  # exact frame index
            White.setAutoDraw(True)
        elif White.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AloneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Alone"-------
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
            
            
    #------Prepare to start Routine "out"-------
    t = 0
    outClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_out.setOri(outori[3])
    grating_out.ori=Background_out.ori
    grating_out.setOri(direcchange,'+')
    # keep track of which components have finished
    outComponents = []
    outComponents.append(Background_out)
    outComponents.append(grating_out)
    outComponents.append(White3)
    for thisComponent in outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "out"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_out* updates
        if t >= interval and Background_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_out.tStart = t  # underestimates by a little under one frame
            Background_out.frameNStart = frameN  # exact frame index
            Background_out.setAutoDraw(True)
        elif Background_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_out.setAutoDraw(False)
        if Background_out.status == STARTED:  # only update if being drawn
           Background_out.setPhase(myvel,'+')
        
        # *grating_out* updates
        if t >= interval and grating_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_out.tStart = t  # underestimates by a little under one frame
            grating_out.frameNStart = frameN  # exact frame index
            grating_out.setAutoDraw(True)
        elif grating_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_out.setAutoDraw(False)
        if grating_out.status == STARTED:  # only update if being drawn
           grating_out.setPhase(myvel,'+')
        
        # *White3* updates
        if t >= interval and White3.status == NOT_STARTED:
            # keep track of start time/frame for later
            White3.tStart = t  # underestimates by a little under one frame
            White3.frameNStart = frameN  # exact frame index
            White3.setAutoDraw(True)
        elif White3.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "out"-------
    for thisComponent in outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    

    
    #------Prepare to start Routine "Allsame"-------
    t = 0
    AllsameClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background.setOri(sameori[3])
    # keep track of which components have finished
    AllsameComponents = []
    AllsameComponents.append(Background)
    AllsameComponents.append(White2)
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Allsame"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AllsameClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background* updates
        if t >= interval and Background.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background.tStart = t  # underestimates by a little under one frame
            Background.frameNStart = frameN  # exact frame index
            Background.setAutoDraw(True)
        elif Background.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background.setAutoDraw(False)
        if Background.status == STARTED:  # only update if being drawn
           Background.setPhase(myvel,'+')
        
        # *White2* updates
        if t >= interval and White2.status == NOT_STARTED:
            # keep track of start time/frame for later
            White2.tStart = t  # underestimates by a little under one frame
            White2.frameNStart = frameN  # exact frame index
            White2.setAutoDraw(True)
        elif White2.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllsameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Allsame"-------
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


            
            
            
            
            #44444444444444444444
            
            
            
            
            
            
    #------Prepare to start Routine "Alone"-------
    t = 0
    AloneClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating.setOri(aloneori[4])
    # keep track of which components have finished
    AloneComponents = []
    AloneComponents.append(grating)
    AloneComponents.append(White)
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Alone"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AloneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating* updates
        if t >= interval and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        elif grating.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating.setAutoDraw(False)
        if grating.status == STARTED:  # only update if being drawn
           grating.setPhase(myvel,'+')
        
        # *White* updates
        if t >= interval and White.status == NOT_STARTED:
            # keep track of start time/frame for later
            White.tStart = t  # underestimates by a little under one frame
            White.frameNStart = frameN  # exact frame index
            White.setAutoDraw(True)
        elif White.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AloneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Alone"-------
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "Allsame"-------
    t = 0
    AllsameClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background.setOri(sameori[4])
    # keep track of which components have finished
    AllsameComponents = []
    AllsameComponents.append(Background)
    AllsameComponents.append(White2)
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Allsame"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AllsameClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background* updates
        if t >= interval and Background.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background.tStart = t  # underestimates by a little under one frame
            Background.frameNStart = frameN  # exact frame index
            Background.setAutoDraw(True)
        elif Background.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background.setAutoDraw(False)
        if Background.status == STARTED:  # only update if being drawn
           Background.setPhase(myvel,'+')
        
        # *White2* updates
        if t >= interval and White2.status == NOT_STARTED:
            # keep track of start time/frame for later
            White2.tStart = t  # underestimates by a little under one frame
            White2.frameNStart = frameN  # exact frame index
            White2.setAutoDraw(True)
        elif White2.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllsameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Allsame"-------
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "out"-------
    t = 0
    outClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_out.setOri(outori[4])
    grating_out.ori=Background_out.ori
    grating_out.setOri(direcchange,'+')
    # keep track of which components have finished
    outComponents = []
    outComponents.append(Background_out)
    outComponents.append(grating_out)
    outComponents.append(White3)
    for thisComponent in outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "out"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_out* updates
        if t >= interval and Background_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_out.tStart = t  # underestimates by a little under one frame
            Background_out.frameNStart = frameN  # exact frame index
            Background_out.setAutoDraw(True)
        elif Background_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_out.setAutoDraw(False)
        if Background_out.status == STARTED:  # only update if being drawn
           Background_out.setPhase(myvel,'+')
        
        # *grating_out* updates
        if t >= interval and grating_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_out.tStart = t  # underestimates by a little under one frame
            grating_out.frameNStart = frameN  # exact frame index
            grating_out.setAutoDraw(True)
        elif grating_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_out.setAutoDraw(False)
        if grating_out.status == STARTED:  # only update if being drawn
           grating_out.setPhase(myvel,'+')
        
        # *White3* updates
        if t >= interval and White3.status == NOT_STARTED:
            # keep track of start time/frame for later
            White3.tStart = t  # underestimates by a little under one frame
            White3.frameNStart = frameN  # exact frame index
            White3.setAutoDraw(True)
        elif White3.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "out"-------
    for thisComponent in outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "Empty"-------
    t = 0
    EmptyClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_empty.setOri(emptyori[4])
    circle.setOri(0)
    # keep track of which components have finished
    EmptyComponents = []
    EmptyComponents.append(Background_empty)
    EmptyComponents.append(circle)
    EmptyComponents.append(White4)
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Empty"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EmptyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_empty* updates
        if t >= interval and Background_empty.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_empty.tStart = t  # underestimates by a little under one frame
            Background_empty.frameNStart = frameN  # exact frame index
            Background_empty.setAutoDraw(True)
        elif Background_empty.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_empty.setAutoDraw(False)
        if Background_empty.status == STARTED:  # only update if being drawn
           Background_empty.setPhase(myvel,'+')
        
        # *circle* updates
        if t >= interval and circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle.tStart = t  # underestimates by a little under one frame
            circle.frameNStart = frameN  # exact frame index
            circle.setAutoDraw(True)
        elif circle.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            circle.setAutoDraw(False)
        
        # *White4* updates
        if t >= interval and White4.status == NOT_STARTED:
            # keep track of start time/frame for later
            White4.tStart = t  # underestimates by a little under one frame
            White4.frameNStart = frameN  # exact frame index
            White4.setAutoDraw(True)
        elif White4.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmptyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Empty"-------
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    


    #------Prepare to start Routine "In"-------
    t = 0
    InClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating_in.setOri(inori[4])
    Background_in.ori=grating_in.ori
    Background_in.setOri(direcchange,'+')
    # keep track of which components have finished
    InComponents = []
    InComponents.append(Background_in)
    InComponents.append(grating_in)
    InComponents.append(White5)
    for thisComponent in InComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "In"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_in* updates
        if t >= interval and Background_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_in.tStart = t  # underestimates by a little under one frame
            Background_in.frameNStart = frameN  # exact frame index
            Background_in.setAutoDraw(True)
        elif Background_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_in.setAutoDraw(False)
        if Background_in.status == STARTED:  # only update if being drawn
           Background_in.setPhase(myvel,'+')
        # *grating_in* updates
        if t >= interval and grating_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_in.tStart = t  # underestimates by a little under one frame
            grating_in.frameNStart = frameN  # exact frame index
            grating_in.setAutoDraw(True)
        elif grating_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_in.setAutoDraw(False)
        if grating_in.status == STARTED:  # only update if being drawn
           grating_in.setPhase(myvel,'+')
        
        # *White5* updates
        if t >= interval and White5.status == NOT_STARTED:
            # keep track of start time/frame for later
            White5.tStart = t  # underestimates by a little under one frame
            White5.frameNStart = frameN  # exact frame index
            White5.setAutoDraw(True)
        elif White5.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()

#-------Ending Routine "In"-------
    for thisComponent in InComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)





#555555555555555555555555555










    
    #------Prepare to start Routine "out"-------
    t = 0
    outClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_out.setOri(outori[5])
    grating_out.ori=Background_out.ori
    grating_out.setOri(direcchange,'+')
    # keep track of which components have finished
    outComponents = []
    outComponents.append(Background_out)
    outComponents.append(grating_out)
    outComponents.append(White3)
    for thisComponent in outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "out"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_out* updates
        if t >= interval and Background_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_out.tStart = t  # underestimates by a little under one frame
            Background_out.frameNStart = frameN  # exact frame index
            Background_out.setAutoDraw(True)
        elif Background_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_out.setAutoDraw(False)
        if Background_out.status == STARTED:  # only update if being drawn
           Background_out.setPhase(myvel,'+')
        
        # *grating_out* updates
        if t >= interval and grating_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_out.tStart = t  # underestimates by a little under one frame
            grating_out.frameNStart = frameN  # exact frame index
            grating_out.setAutoDraw(True)
        elif grating_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_out.setAutoDraw(False)
        if grating_out.status == STARTED:  # only update if being drawn
           grating_out.setPhase(myvel,'+')
        
        # *White3* updates
        if t >= interval and White3.status == NOT_STARTED:
            # keep track of start time/frame for later
            White3.tStart = t  # underestimates by a little under one frame
            White3.frameNStart = frameN  # exact frame index
            White3.setAutoDraw(True)
        elif White3.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "out"-------
    for thisComponent in outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    

    


    #------Prepare to start Routine "In"-------
    t = 0
    InClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating_in.setOri(inori[5])
    Background_in.ori=grating_in.ori
    Background_in.setOri(direcchange,'+')
    # keep track of which components have finished
    InComponents = []
    InComponents.append(Background_in)
    InComponents.append(grating_in)
    InComponents.append(White5)
    for thisComponent in InComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "In"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_in* updates
        if t >= interval and Background_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_in.tStart = t  # underestimates by a little under one frame
            Background_in.frameNStart = frameN  # exact frame index
            Background_in.setAutoDraw(True)
        elif Background_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_in.setAutoDraw(False)
        if Background_in.status == STARTED:  # only update if being drawn
           Background_in.setPhase(myvel,'+')
        # *grating_in* updates
        if t >= interval and grating_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_in.tStart = t  # underestimates by a little under one frame
            grating_in.frameNStart = frameN  # exact frame index
            grating_in.setAutoDraw(True)
        elif grating_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_in.setAutoDraw(False)
        if grating_in.status == STARTED:  # only update if being drawn
           grating_in.setPhase(myvel,'+')
        
        # *White5* updates
        if t >= interval and White5.status == NOT_STARTED:
            # keep track of start time/frame for later
            White5.tStart = t  # underestimates by a little under one frame
            White5.frameNStart = frameN  # exact frame index
            White5.setAutoDraw(True)
        elif White5.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()

#-------Ending Routine "In"-------
    for thisComponent in InComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


    #------Prepare to start Routine "Allsame"-------
    t = 0
    AllsameClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background.setOri(sameori[5])
    # keep track of which components have finished
    AllsameComponents = []
    AllsameComponents.append(Background)
    AllsameComponents.append(White2)
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Allsame"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AllsameClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background* updates
        if t >= interval and Background.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background.tStart = t  # underestimates by a little under one frame
            Background.frameNStart = frameN  # exact frame index
            Background.setAutoDraw(True)
        elif Background.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background.setAutoDraw(False)
        if Background.status == STARTED:  # only update if being drawn
           Background.setPhase(myvel,'+')
        
        # *White2* updates
        if t >= interval and White2.status == NOT_STARTED:
            # keep track of start time/frame for later
            White2.tStart = t  # underestimates by a little under one frame
            White2.frameNStart = frameN  # exact frame index
            White2.setAutoDraw(True)
        elif White2.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllsameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Allsame"-------
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    #------Prepare to start Routine "Empty"-------
    t = 0
    EmptyClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_empty.setOri(emptyori[5])
    circle.setOri(0)
    # keep track of which components have finished
    EmptyComponents = []
    EmptyComponents.append(Background_empty)
    EmptyComponents.append(circle)
    EmptyComponents.append(White4)
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Empty"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EmptyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_empty* updates
        if t >= interval and Background_empty.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_empty.tStart = t  # underestimates by a little under one frame
            Background_empty.frameNStart = frameN  # exact frame index
            Background_empty.setAutoDraw(True)
        elif Background_empty.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_empty.setAutoDraw(False)
        if Background_empty.status == STARTED:  # only update if being drawn
           Background_empty.setPhase(myvel,'+')
        
        # *circle* updates
        if t >= interval and circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle.tStart = t  # underestimates by a little under one frame
            circle.frameNStart = frameN  # exact frame index
            circle.setAutoDraw(True)
        elif circle.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            circle.setAutoDraw(False)
        
        # *White4* updates
        if t >= interval and White4.status == NOT_STARTED:
            # keep track of start time/frame for later
            White4.tStart = t  # underestimates by a little under one frame
            White4.frameNStart = frameN  # exact frame index
            White4.setAutoDraw(True)
        elif White4.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmptyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Empty"-------
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #------Prepare to start Routine "Alone"-------
    t = 0
    AloneClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating.setOri(aloneori[5])
    # keep track of which components have finished
    AloneComponents = []
    AloneComponents.append(grating)
    AloneComponents.append(White)
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Alone"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AloneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating* updates
        if t >= interval and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        elif grating.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating.setAutoDraw(False)
        if grating.status == STARTED:  # only update if being drawn
           grating.setPhase(myvel,'+')
        
        # *White* updates
        if t >= interval and White.status == NOT_STARTED:
            # keep track of start time/frame for later
            White.tStart = t  # underestimates by a little under one frame
            White.frameNStart = frameN  # exact frame index
            White.setAutoDraw(True)
        elif White.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AloneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Alone"-------
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    






#66666666666666666



    #------Prepare to start Routine "Empty"-------
    t = 0
    EmptyClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_empty.setOri(emptyori[6])
    circle.setOri(0)
    # keep track of which components have finished
    EmptyComponents = []
    EmptyComponents.append(Background_empty)
    EmptyComponents.append(circle)
    EmptyComponents.append(White4)
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Empty"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EmptyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_empty* updates
        if t >= interval and Background_empty.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_empty.tStart = t  # underestimates by a little under one frame
            Background_empty.frameNStart = frameN  # exact frame index
            Background_empty.setAutoDraw(True)
        elif Background_empty.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_empty.setAutoDraw(False)
        if Background_empty.status == STARTED:  # only update if being drawn
           Background_empty.setPhase(myvel,'+')
        
        # *circle* updates
        if t >= interval and circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle.tStart = t  # underestimates by a little under one frame
            circle.frameNStart = frameN  # exact frame index
            circle.setAutoDraw(True)
        elif circle.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            circle.setAutoDraw(False)
        
        # *White4* updates
        if t >= interval and White4.status == NOT_STARTED:
            # keep track of start time/frame for later
            White4.tStart = t  # underestimates by a little under one frame
            White4.frameNStart = frameN  # exact frame index
            White4.setAutoDraw(True)
        elif White4.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmptyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Empty"-------
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)



    #------Prepare to start Routine "Allsame"-------
    t = 0
    AllsameClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background.setOri(sameori[6])
    # keep track of which components have finished
    AllsameComponents = []
    AllsameComponents.append(Background)
    AllsameComponents.append(White2)
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Allsame"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AllsameClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background* updates
        if t >= interval and Background.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background.tStart = t  # underestimates by a little under one frame
            Background.frameNStart = frameN  # exact frame index
            Background.setAutoDraw(True)
        elif Background.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background.setAutoDraw(False)
        if Background.status == STARTED:  # only update if being drawn
           Background.setPhase(myvel,'+')
        
        # *White2* updates
        if t >= interval and White2.status == NOT_STARTED:
            # keep track of start time/frame for later
            White2.tStart = t  # underestimates by a little under one frame
            White2.frameNStart = frameN  # exact frame index
            White2.setAutoDraw(True)
        elif White2.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllsameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Allsame"-------
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
            
    #------Prepare to start Routine "out"-------
    t = 0
    outClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_out.setOri(outori[6])
    grating_out.ori=Background_out.ori
    grating_out.setOri(direcchange,'+')
    # keep track of which components have finished
    outComponents = []
    outComponents.append(Background_out)
    outComponents.append(grating_out)
    outComponents.append(White3)
    for thisComponent in outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "out"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_out* updates
        if t >= interval and Background_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_out.tStart = t  # underestimates by a little under one frame
            Background_out.frameNStart = frameN  # exact frame index
            Background_out.setAutoDraw(True)
        elif Background_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_out.setAutoDraw(False)
        if Background_out.status == STARTED:  # only update if being drawn
           Background_out.setPhase(myvel,'+')
        
        # *grating_out* updates
        if t >= interval and grating_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_out.tStart = t  # underestimates by a little under one frame
            grating_out.frameNStart = frameN  # exact frame index
            grating_out.setAutoDraw(True)
        elif grating_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_out.setAutoDraw(False)
        if grating_out.status == STARTED:  # only update if being drawn
           grating_out.setPhase(myvel,'+')
        
        # *White3* updates
        if t >= interval and White3.status == NOT_STARTED:
            # keep track of start time/frame for later
            White3.tStart = t  # underestimates by a little under one frame
            White3.frameNStart = frameN  # exact frame index
            White3.setAutoDraw(True)
        elif White3.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "out"-------
    for thisComponent in outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    

    


    #------Prepare to start Routine "In"-------
    t = 0
    InClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating_in.setOri(inori[6])
    Background_in.ori=grating_in.ori
    Background_in.setOri(direcchange,'+')
    # keep track of which components have finished
    InComponents = []
    InComponents.append(Background_in)
    InComponents.append(grating_in)
    InComponents.append(White5)
    for thisComponent in InComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "In"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_in* updates
        if t >= interval and Background_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_in.tStart = t  # underestimates by a little under one frame
            Background_in.frameNStart = frameN  # exact frame index
            Background_in.setAutoDraw(True)
        elif Background_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_in.setAutoDraw(False)
        if Background_in.status == STARTED:  # only update if being drawn
           Background_in.setPhase(myvel,'+')
        # *grating_in* updates
        if t >= interval and grating_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_in.tStart = t  # underestimates by a little under one frame
            grating_in.frameNStart = frameN  # exact frame index
            grating_in.setAutoDraw(True)
        elif grating_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_in.setAutoDraw(False)
        if grating_in.status == STARTED:  # only update if being drawn
           grating_in.setPhase(myvel,'+')
        
        # *White5* updates
        if t >= interval and White5.status == NOT_STARTED:
            # keep track of start time/frame for later
            White5.tStart = t  # underestimates by a little under one frame
            White5.frameNStart = frameN  # exact frame index
            White5.setAutoDraw(True)
        elif White5.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()

#-------Ending Routine "In"-------
    for thisComponent in InComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    #------Prepare to start Routine "Alone"-------
    t = 0
    AloneClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating.setOri(aloneori[6])
    # keep track of which components have finished
    AloneComponents = []
    AloneComponents.append(grating)
    AloneComponents.append(White)
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Alone"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AloneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating* updates
        if t >= interval and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        elif grating.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating.setAutoDraw(False)
        if grating.status == STARTED:  # only update if being drawn
           grating.setPhase(myvel,'+')
        
        # *White* updates
        if t >= interval and White.status == NOT_STARTED:
            # keep track of start time/frame for later
            White.tStart = t  # underestimates by a little under one frame
            White.frameNStart = frameN  # exact frame index
            White.setAutoDraw(True)
        elif White.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AloneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Alone"-------
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    

    

    






#7777777777777777777777














    #------Prepare to start Routine "Empty"-------
    t = 0
    EmptyClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_empty.setOri(emptyori[7])
    circle.setOri(0)
    # keep track of which components have finished
    EmptyComponents = []
    EmptyComponents.append(Background_empty)
    EmptyComponents.append(circle)
    EmptyComponents.append(White4)
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Empty"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EmptyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_empty* updates
        if t >= interval and Background_empty.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_empty.tStart = t  # underestimates by a little under one frame
            Background_empty.frameNStart = frameN  # exact frame index
            Background_empty.setAutoDraw(True)
        elif Background_empty.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_empty.setAutoDraw(False)
        if Background_empty.status == STARTED:  # only update if being drawn
           Background_empty.setPhase(myvel,'+')
        
        # *circle* updates
        if t >= interval and circle.status == NOT_STARTED:
            # keep track of start time/frame for later
            circle.tStart = t  # underestimates by a little under one frame
            circle.frameNStart = frameN  # exact frame index
            circle.setAutoDraw(True)
        elif circle.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            circle.setAutoDraw(False)
        
        # *White4* updates
        if t >= interval and White4.status == NOT_STARTED:
            # keep track of start time/frame for later
            White4.tStart = t  # underestimates by a little under one frame
            White4.frameNStart = frameN  # exact frame index
            White4.setAutoDraw(True)
        elif White4.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EmptyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Empty"-------
    for thisComponent in EmptyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    


    #------Prepare to start Routine "In"-------
    t = 0
    InClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating_in.setOri(inori[7])
    Background_in.ori=grating_in.ori
    Background_in.setOri(direcchange,'+')
    # keep track of which components have finished
    InComponents = []
    InComponents.append(Background_in)
    InComponents.append(grating_in)
    InComponents.append(White5)
    for thisComponent in InComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "In"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = InClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_in* updates
        if t >= interval and Background_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_in.tStart = t  # underestimates by a little under one frame
            Background_in.frameNStart = frameN  # exact frame index
            Background_in.setAutoDraw(True)
        elif Background_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_in.setAutoDraw(False)
        if Background_in.status == STARTED:  # only update if being drawn
           Background_in.setPhase(myvel,'+')
        # *grating_in* updates
        if t >= interval and grating_in.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_in.tStart = t  # underestimates by a little under one frame
            grating_in.frameNStart = frameN  # exact frame index
            grating_in.setAutoDraw(True)
        elif grating_in.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_in.setAutoDraw(False)
        if grating_in.status == STARTED:  # only update if being drawn
           grating_in.setPhase(myvel,'+')
        
        # *White5* updates
        if t >= interval and White5.status == NOT_STARTED:
            # keep track of start time/frame for later
            White5.tStart = t  # underestimates by a little under one frame
            White5.frameNStart = frameN  # exact frame index
            White5.setAutoDraw(True)
        elif White5.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()

#-------Ending Routine "In"-------
    for thisComponent in InComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "Alone"-------
    t = 0
    AloneClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    grating.setOri(aloneori[7])
    # keep track of which components have finished
    AloneComponents = []
    AloneComponents.append(grating)
    AloneComponents.append(White)
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Alone"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AloneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating* updates
        if t >= interval and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t  # underestimates by a little under one frame
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        elif grating.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating.setAutoDraw(False)
        if grating.status == STARTED:  # only update if being drawn
           grating.setPhase(myvel,'+')
        
        # *White* updates
        if t >= interval and White.status == NOT_STARTED:
            # keep track of start time/frame for later
            White.tStart = t  # underestimates by a little under one frame
            White.frameNStart = frameN  # exact frame index
            White.setAutoDraw(True)
        elif White.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AloneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Alone"-------
    for thisComponent in AloneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
            
            
    #------Prepare to start Routine "out"-------
    t = 0
    outClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background_out.setOri(outori[7])
    grating_out.ori=Background_out.ori
    grating_out.setOri(direcchange,'+')
    # keep track of which components have finished
    outComponents = []
    outComponents.append(Background_out)
    outComponents.append(grating_out)
    outComponents.append(White3)
    for thisComponent in outComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "out"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = outClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_out* updates
        if t >= interval and Background_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background_out.tStart = t  # underestimates by a little under one frame
            Background_out.frameNStart = frameN  # exact frame index
            Background_out.setAutoDraw(True)
        elif Background_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background_out.setAutoDraw(False)
        if Background_out.status == STARTED:  # only update if being drawn
           Background_out.setPhase(myvel,'+')
        
        # *grating_out* updates
        if t >= interval and grating_out.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_out.tStart = t  # underestimates by a little under one frame
            grating_out.frameNStart = frameN  # exact frame index
            grating_out.setAutoDraw(True)
        elif grating_out.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            grating_out.setAutoDraw(False)
        if grating_out.status == STARTED:  # only update if being drawn
           grating_out.setPhase(myvel,'+')
        
        # *White3* updates
        if t >= interval and White3.status == NOT_STARTED:
            # keep track of start time/frame for later
            White3.tStart = t  # underestimates by a little under one frame
            White3.frameNStart = frameN  # exact frame index
            White3.setAutoDraw(True)
        elif White3.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "out"-------
    for thisComponent in outComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    

    
    #------Prepare to start Routine "Allsame"-------
    t = 0
    AllsameClock.reset()  # clock 
    frameN = -1
    routineTimer.add(interval+1)
    # update component parameters for each repeat
    Background.setOri(sameori[7])
    # keep track of which components have finished
    AllsameComponents = []
    AllsameComponents.append(Background)
    AllsameComponents.append(White2)
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Allsame"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AllsameClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background* updates
        if t >= interval and Background.status == NOT_STARTED:
            # keep track of start time/frame for later
            Background.tStart = t  # underestimates by a little under one frame
            Background.frameNStart = frameN  # exact frame index
            Background.setAutoDraw(True)
        elif Background.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            Background.setAutoDraw(False)
        if Background.status == STARTED:  # only update if being drawn
           Background.setPhase(myvel,'+')
        
        # *White2* updates
        if t >= interval and White2.status == NOT_STARTED:
            # keep track of start time/frame for later
            White2.tStart = t  # underestimates by a little under one frame
            White2.frameNStart = frameN  # exact frame index
            White2.setAutoDraw(True)
        elif White2.status == STARTED and t >= (interval + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            White2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AllsameComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            win0.flip()
    
    #-------Ending Routine "Allsame"-------
    for thisComponent in AllsameComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
win.close()
core.quit()

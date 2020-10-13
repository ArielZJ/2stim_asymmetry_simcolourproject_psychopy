#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Tue Oct 13 15:13:20 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'Simcolourproject_2stim_asymm_v1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/bethfisher/Documents/Simcolourproject_online/Simcolourproject_2stim_asymm_v1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "startup"
startupClock = core.Clock()
import pandas as pd
from psychopy import tools
import random as rnd
rnd.seed()

# Set path names for images
arrow1 = 'images/arrow1.png'
arrow2 = 'images/arrow2.png'
half_circle = 'images/circle_7.png'
half_circle_con = 'images/confidence_12.png'
trackpad1 = 'images/trackpad_button.png'
mouse_button1 = 'images/mouse_button.png'



# Initialize components for Routine "screen_scale"
screen_scaleClock = core.Clock()
oldt=0
x_size=8.560
y_size=5.398
screen_height=0

if win.units=='norm':
    x_scale=.05
    y_scale=.1
    dbase = .0001
    unittext=' norm units'
    vsize=2
elif win.units=='pix':
    x_scale=60
    y_scale=40
    dbase = .1
    unittext=' pixels'
    vsize=win.size[1]
else:
    x_scale=.05
    y_scale=.05
    dbase = .0001
    unittext=' height units'
    vsize=1
text_top = visual.TextStim(win=win, name='text_top',
    text='Resize this image to match the size of a credit card\nUp arrow for taller\nDown arrow for shorter\nLeft arrow for narrower\nRight arrow for wider',
    font='Arial',
    units='norm', pos=(0, .7), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_bottom = visual.TextStim(win=win, name='text_bottom',
    text='Press the space bar when done',
    font='Arial',
    units='norm', pos=(0, -.6), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ccimage = visual.ImageStim(
    win=win,
    name='ccimage', 
    image='card.png', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "Stim1_display_prac"
Stim1_display_pracClock = core.Clock()
Circle = visual.Polygon(
    win=win, name='Circle',units='pix', 
    edges=1000, size=(50,50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb255',
    opacity=1, depth=0.0, interpolate=True)
centre_cross4_2 = visual.ShapeStim(
    win=win, name='centre_cross4_2', vertices='cross',units='norm', 
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1.5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "response_prac"
response_pracClock = core.Clock()
response1disk_5 = visual.ImageStim(
    win=win,
    name='response1disk_5', 
    image='response1disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response2disk_5 = visual.ImageStim(
    win=win,
    name='response2disk_5', 
    image='response2disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_5 = visual.ImageStim(
    win=win,
    name='response3disk_5', 
    image='response3disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response4disk_5 = visual.ImageStim(
    win=win,
    name='response4disk_5', 
    image='response4disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk_5 = visual.ImageStim(
    win=win,
    name='response5disk_5', 
    image='response5disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response6disk_5 = visual.ImageStim(
    win=win,
    name='response6disk_5', 
    image='response6disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
response7disk_5 = visual.ImageStim(
    win=win,
    name='response7disk_5', 
    image='response7disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
response8disk_5 = visual.ImageStim(
    win=win,
    name='response8disk_5', 
    image='response8disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()
Circle_3 = visual.Polygon(
    win=win, name='Circle_3',
    edges=1000, size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb255',
    opacity=1, depth=-9.0, interpolate=True)
text_29 = visual.TextStim(win=win, name='text_29',
    text='Please choose the similarity level of the previously 2 cued circles\n0 => Most similar\n7 => Most different ',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "summary1_prac"
summary1_pracClock = core.Clock()
response1disk_8 = visual.ImageStim(
    win=win,
    name='response1disk_8', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response1disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response2disk_8 = visual.ImageStim(
    win=win,
    name='response2disk_8', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response2disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_8 = visual.ImageStim(
    win=win,
    name='response3disk_8', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response3disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response4disk_8 = visual.ImageStim(
    win=win,
    name='response4disk_8', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response4disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk_8 = visual.ImageStim(
    win=win,
    name='response5disk_8', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response5disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response6disk_8 = visual.ImageStim(
    win=win,
    name='response6disk_8', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response6disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
response7disk_8 = visual.ImageStim(
    win=win,
    name='response7disk_8', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response7disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
response8disk_8 = visual.ImageStim(
    win=win,
    name='response8disk_8', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response8disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()
rectangle_6 = visual.Rect(
    win=win, name='rectangle_6',
    width=(0.1, 0.08)[0], height=(0.1, 0.08)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)


text_34 = visual.TextStim(win=win, name='text_34',
    text='Please click on the green rectangle to continue',
    font='Arial',
    pos=(0, -0.27), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_35 = visual.TextStim(win=win, name='text_35',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "special_trial_prac"
special_trial_pracClock = core.Clock()
text_36 = visual.TextStim(win=win, name='text_36',
    text='SPECIAL TRIAL',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='RED', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "catch_prac"
catch_pracClock = core.Clock()
response1disk_7 = visual.ImageStim(
    win=win,
    name='response1disk_7', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response1disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response2disk_7 = visual.ImageStim(
    win=win,
    name='response2disk_7', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response2disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_7 = visual.ImageStim(
    win=win,
    name='response3disk_7', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response3disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response4disk_7 = visual.ImageStim(
    win=win,
    name='response4disk_7', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response4disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk_7 = visual.ImageStim(
    win=win,
    name='response5disk_7', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response5disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response6disk_7 = visual.ImageStim(
    win=win,
    name='response6disk_7', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response6disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
response7disk_7 = visual.ImageStim(
    win=win,
    name='response7disk_7', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response7disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
response8disk_7 = visual.ImageStim(
    win=win,
    name='response8disk_7', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response8disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mouse_7 = event.Mouse(win=win)
x, y = [None, None]
mouse_7.mouseClock = core.Clock()
# Set up catch trials 

catchtrialorderprac = []
for i in range(0,2):
    n = rnd.randint(1,7)
    catchtrialorderprac.append(n)
print(catchtrialorderprac)

text_32 = visual.TextStim(win=win, name='text_32',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
rectangle_5 = visual.Rect(
    win=win, name='rectangle_5',
    width=(0.1, 0.08)[0], height=(0.1, 0.08)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)

# Initialize components for Routine "summary2_prac"
summary2_pracClock = core.Clock()
response1disk_6 = visual.ImageStim(
    win=win,
    name='response1disk_6', 
    image='response1disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response2disk_6 = visual.ImageStim(
    win=win,
    name='response2disk_6', 
    image='response2disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_6 = visual.ImageStim(
    win=win,
    name='response3disk_6', 
    image='response3disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response4disk_6 = visual.ImageStim(
    win=win,
    name='response4disk_6', 
    image='response4disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk_6 = visual.ImageStim(
    win=win,
    name='response5disk_6', 
    image='response5disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response6disk_6 = visual.ImageStim(
    win=win,
    name='response6disk_6', 
    image='response6disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
response7disk_6 = visual.ImageStim(
    win=win,
    name='response7disk_6', 
    image='response7disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
response8disk_6 = visual.ImageStim(
    win=win,
    name='response8disk_6', 
    image='response8disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()
rectangle_4 = visual.Rect(
    win=win, name='rectangle_4',
    width=(0.1, 0.08)[0], height=(0.1, 0.08)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
pracnumber = 0;

text_30 = visual.TextStim(win=win, name='text_30',
    text='Please click on the green rectangle to continue',
    font='Arial',
    pos=(0, -0.27), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_31 = visual.TextStim(win=win, name='text_31',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "Stim1_display"
Stim1_displayClock = core.Clock()
Circle_1 = visual.Polygon(
    win=win, name='Circle_1',units='pix', 
    edges=1000, size=(50,50),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb255',
    opacity=1, depth=0.0, interpolate=True)
centre_cross4 = visual.ShapeStim(
    win=win, name='centre_cross4', vertices='cross',units='norm', 
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1.5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "response"
responseClock = core.Clock()
response1disk = visual.ImageStim(
    win=win,
    name='response1disk', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response1disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response2disk = visual.ImageStim(
    win=win,
    name='response2disk', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response2disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk = visual.ImageStim(
    win=win,
    name='response3disk', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response3disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response4disk = visual.ImageStim(
    win=win,
    name='response4disk', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response4disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk = visual.ImageStim(
    win=win,
    name='response5disk', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response5disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response6disk = visual.ImageStim(
    win=win,
    name='response6disk', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response6disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
response7disk = visual.ImageStim(
    win=win,
    name='response7disk', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response7disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
response8disk = visual.ImageStim(
    win=win,
    name='response8disk', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response8disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Circle_2 = visual.Polygon(
    win=win, name='Circle_2',
    edges=1000, size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb255',
    opacity=1, depth=-9.0, interpolate=True)
text_23 = visual.TextStim(win=win, name='text_23',
    text='Please choose the similarity level of the previously 2 cued circles\n0 => Most similar\n7 => Most different ',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "special_trial"
special_trialClock = core.Clock()
text_33 = visual.TextStim(win=win, name='text_33',
    text='SPECIAL TRIAL',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='RED', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "catch_1"
catch_1Clock = core.Clock()
response1disk_3 = visual.ImageStim(
    win=win,
    name='response1disk_3', 
    image='response1disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response2disk_3 = visual.ImageStim(
    win=win,
    name='response2disk_3', 
    image='response2disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_3 = visual.ImageStim(
    win=win,
    name='response3disk_3', 
    image='response3disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response4disk_3 = visual.ImageStim(
    win=win,
    name='response4disk_3', 
    image='response4disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk_3 = visual.ImageStim(
    win=win,
    name='response5disk_3', 
    image='response5disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response6disk_3 = visual.ImageStim(
    win=win,
    name='response6disk_3', 
    image='response6disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
response7disk_3 = visual.ImageStim(
    win=win,
    name='response7disk_3', 
    image='response7disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
response8disk_3 = visual.ImageStim(
    win=win,
    name='response8disk_3', 
    image='response8disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()
# Set up catch trials 

catchtrialorder = []
for i in range(0,10):
    n = rnd.randint(1,162)
    catchtrialorder.append(n)
print(catchtrialorder)

text_26 = visual.TextStim(win=win, name='text_26',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
rectangle_2 = visual.Rect(
    win=win, name='rectangle_2',
    width=(0.1, 0.08)[0], height=(0.1, 0.08)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)

# Initialize components for Routine "response_2"
response_2Clock = core.Clock()
response1disk_2 = visual.ImageStim(
    win=win,
    name='response1disk_2', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response1disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response2disk_2 = visual.ImageStim(
    win=win,
    name='response2disk_2', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response2disks.png', mask=None,
    ori=0, pos=(0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
response3disk_2 = visual.ImageStim(
    win=win,
    name='response3disk_2', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response3disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
response4disk_2 = visual.ImageStim(
    win=win,
    name='response4disk_2', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response4disks.png', mask=None,
    ori=0, pos=(0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
response5disk_2 = visual.ImageStim(
    win=win,
    name='response5disk_2', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response5disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
response6disk_2 = visual.ImageStim(
    win=win,
    name='response6disk_2', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response6disks.png', mask=None,
    ori=0, pos=(-0.09,-0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
response7disk_2 = visual.ImageStim(
    win=win,
    name='response7disk_2', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response7disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
response8disk_2 = visual.ImageStim(
    win=win,
    name='response8disk_2', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/response8disks.png', mask=None,
    ori=0, pos=(-0.09,0.09), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
rectangle = visual.Rect(
    win=win, name='rectangle',
    width=(0.1, 0.08)[0], height=(0.1, 0.08)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor='green', fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
trialnumber = 0;

text_25 = visual.TextStim(win=win, name='text_25',
    text='Please click on the green rectangle to continue',
    font='Arial',
    pos=(0, -0.27), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_24 = visual.TextStim(win=win, name='text_24',
    text='default text',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "welcome_instr"
welcome_instrClock = core.Clock()
welcome = visual.TextStim(win=win, name='welcome',
    text='Welcome to this experiment \n\nThis will take about 45 minutes ',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=2, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
space = visual.TextStim(win=win, name='space',
    text='Press SPACE to continue ',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instr_1"
instr_1Clock = core.Clock()
text_1 = visual.TextStim(win=win, name='text_1',
    text='Before starting the main experiment, we need to do some quick calibrations to ensure your screen is set up correctly.',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space_2 = visual.TextStim(win=win, name='space_2',
    text='Press SPACE to continue ',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Warning! It is critical that these calibrations are done correctly or you will be unable to do the experiment and we will be unable to approve your payment!',
    font='Arial',
    pos=(0,-0.3), height=0.04, wrapWidth=1.5, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "instr_3"
instr_3Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Next, we need to get you to keep your head a fixed distance from the screen.\nThis will ensure future images are the right size for your screen. On the next screen please:',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='1. Keeping your arm straight, please touch your thumb to the centre of the screen in the oval\n2. While keeping your head in the same position, lower your arm.\n3. Please keep your head in this position for the remainder of the experiment ',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
space_3 = visual.TextStim(win=win, name='space_3',
    text='Press SPACE to continue ',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "instr_4"
instr_4Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='1. While keeping your arm straight touch your thumb to the centre of the screen in the oval.\n2. Keep yourhead in the same position, but lower and relax your arm.\n3. Please keep your head in this position for the remainder of the experiment\n4. Press SPACE to continue ',
    font='Arial',
    pos=(0, 0.2), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
calibrationline = visual.ImageStim(
    win=win,
    name='calibrationline', 
    image='/Users/bethfisher/Documents/Simcolourproject_online/calibrationline.png', mask=None,
    ori=0, pos=(0, -0.2), size=(0.1, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr_5"
instr_5Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Lastly, we need to know how far your head is from the screen.\nPlease keep your head in the same position as before.\n\nOver the next few pages we will explain how we can work out how far you are sitting from the screen.\nPlease pay attention and follow all the instructions carefully.\n\nThese first few pages will be INSTRUCTIONS ONLY. You will be instructed when the calibrations start.\n\nWhen ready, press SPACE to continue and follow the instructions on the next page.\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=2, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()
space_4 = visual.TextStim(win=win, name='space_4',
    text='Press SPACE to continue ',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instr_6"
instr_6Clock = core.Clock()
key_resp_6 = keyboard.Keyboard()
space_5 = visual.TextStim(win=win, name='space_5',
    text='Press SPACE to continue ',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only = visual.TextStim(win=win, name='instr_only',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='1. Put a finger on <ENTER> on the keyboard.',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instr_8"
instr_8Clock = core.Clock()
key_resp_8 = keyboard.Keyboard()
space_7 = visual.TextStim(win=win, name='space_7',
    text='Press SPACE to continue ',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only_3 = visual.TextStim(win=win, name='instr_only_3',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='2. Close your right eye',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instr_7"
instr_7Clock = core.Clock()
key_resp_7 = keyboard.Keyboard()
space_6 = visual.TextStim(win=win, name='space_6',
    text='Press SPACE to continue ',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_only_2 = visual.TextStim(win=win, name='instr_only_2',
    text='INSTRUCTIONS ONLY',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='3. Stare at the middle of the screen, keeping your head in the same position as before.\nKeep your right eye closed.',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
center_cross = visual.ShapeStim(
    win=win, name='center_cross', vertices='cross',units='norm', 
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1.5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "colour_circle_instr"
colour_circle_instrClock = core.Clock()
import pandas as pd
from psychopy import tools
import random as rnd
rnd.seed()


key_resp_9 = keyboard.Keyboard()
intructioncircle_1 = visual.Polygon(
    win=win, name='intructioncircle_1',
    edges=1000, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[255, 0, 0], fillColorSpace='rgb255',
    opacity=1, depth=-2.0, interpolate=True)
instructioncircle_2 = visual.Polygon(
    win=win, name='instructioncircle_2',
    edges=1000, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[255, 170, 0], fillColorSpace='rgb255',
    opacity=1, depth=-3.0, interpolate=True)
instructioncircle_3 = visual.Polygon(
    win=win, name='instructioncircle_3',
    edges=1000, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[170, 255, 0], lineColorSpace='rgb',
    fillColor=[170, 255, 0], fillColorSpace='rgb255',
    opacity=1, depth=-4.0, interpolate=True)
instructioncircle_4 = visual.Polygon(
    win=win, name='instructioncircle_4',
    edges=1000, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[0, 255, 0], fillColorSpace='rgb255',
    opacity=1, depth=-5.0, interpolate=True)
instructioncircle_5 = visual.Polygon(
    win=win, name='instructioncircle_5',
    edges=1000, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[0, 255, 169], fillColorSpace='rgb255',
    opacity=1, depth=-6.0, interpolate=True)
insturctioncircle_6 = visual.Polygon(
    win=win, name='insturctioncircle_6',
    edges=1000, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[0, 169, 255], fillColorSpace='rgb255',
    opacity=1, depth=-7.0, interpolate=True)
instructioncircle_7 = visual.Polygon(
    win=win, name='instructioncircle_7',
    edges=1000, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[0, 0, 255], fillColorSpace='rgb255',
    opacity=1, depth=-8.0, interpolate=True)
instructioncircle_8 = visual.Polygon(
    win=win, name='instructioncircle_8',
    edges=1000, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[170, 0, 255], fillColorSpace='rgb255',
    opacity=1, depth=-9.0, interpolate=True)
instructioncircle_9 = visual.Polygon(
    win=win, name='instructioncircle_9',
    edges=1000, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=None, lineColorSpace='rgb',
    fillColor=[255, 0, 170], fillColorSpace='rgb255',
    opacity=1, depth=-10.0, interpolate=True)
space_9 = visual.TextStim(win=win, name='space_9',
    text='Press SPACE to continue ',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='During the test, you will see these 9 colors below',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "instr_10"
instr_10Clock = core.Clock()
space_10 = visual.TextStim(win=win, name='space_10',
    text='Press SPACE to continue ',
    font='Arial',
    pos=(0.4, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='You are going to do a few practice trials to make you be more familiar with the experiment.\nWhen you are ready, please press SPACE to start the practice trials',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_10 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "startup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
startupComponents = []
for thisComponent in startupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startup"-------
while continueRoutine:
    # get current time
    t = startupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startup"-------
for thisComponent in startupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "startup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "screen_scale"-------
continueRoutine = True
# update component parameters for each repeat
ccimage.setSize((x_size*x_scale, x_size*x_scale*0.62))
# keep track of which components have finished
screen_scaleComponents = [text_top, text_bottom, ccimage]
for thisComponent in screen_scaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
screen_scaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "screen_scale"-------
while continueRoutine:
    # get current time
    t = screen_scaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=screen_scaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    keys=event.getKeys()
    
    if len(keys):
        if t-oldt<.5:
            dscale=5*dbase
            oldt=t
        else:
            dscale=dbase
            oldt=t
        if 'space' in keys:
            continueRoutine=False
        elif 'left' in keys:
            x_scale=round((x_scale-dscale)*10000)/10000
        elif 'right' in keys:
            x_scale=round((x_scale+dscale)*10000)/10000
        screen_height=round(vsize*10/y_scale)/10
        ccimage.size=[x_size*x_scale, x_size*x_scale*0.62]
        
    
    # *text_top* updates
    if text_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_top.frameNStart = frameN  # exact frame index
        text_top.tStart = t  # local t and not account for scr refresh
        text_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_top, 'tStartRefresh')  # time at next scr refresh
        text_top.setAutoDraw(True)
    
    # *text_bottom* updates
    if text_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_bottom.frameNStart = frameN  # exact frame index
        text_bottom.tStart = t  # local t and not account for scr refresh
        text_bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_bottom, 'tStartRefresh')  # time at next scr refresh
        text_bottom.setAutoDraw(True)
    
    # *ccimage* updates
    if ccimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ccimage.frameNStart = frameN  # exact frame index
        ccimage.tStart = t  # local t and not account for scr refresh
        ccimage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ccimage, 'tStartRefresh')  # time at next scr refresh
        ccimage.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in screen_scaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "screen_scale"-------
for thisComponent in screen_scaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('X Scale',x_scale)
thisExp.addData('Y Scale',y_scale)

thisExp.addData('ccimage.started', ccimage.tStartRefresh)
thisExp.addData('ccimage.stopped', ccimage.tStopRefresh)
# the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practrials.xlsx', selection='0:7'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Stim1_display_prac"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # Circle position and size 
    
    x = 100
    y = 100
    
    radius_F = 1 
    radius_P = 1
    
    angle_1 = 0
    angle_2 = 0
    
    
    theta_1 = (angle_1)*(pi/180)
    theta_2 = (angle_2)*(pi/180)
    
    
    deltax_1 = radius_F*cos(theta_1)
    deltay_1 = radius_F*sin(theta_1)
    deltax_2 = radius_P*cos(theta_2)
    deltay_2 = radius_P*sin(theta_2)
    
    
    a_1 = x + deltax_1
    b_1 = y + deltay_1
    a_2 = x + deltax_2
    b_2 = y + deltay_2
    
    
    # Set circle position 
    if Ecc == 'FF':
        circle1posx = a_1;
        circle1posy = b_1;
    elif Ecc == 'PF':
            circle1posx = a_2;
            circle1posy = b_2;
    
    # Randomly select circle colour
    
    Colour_1 = rnd.randint(1,9);
    
    # Set circle colour
    if Colour_1 == 1:
        Circle1_col = (255, 0, 0);
    elif Colour_1 == 2:
        Circle1_col = (255, 170, 0);
    elif Colour_1 == 3:
        Circle1_col = (170, 255, 0);
    elif Colour_1 == 4:
        Circle1_col = (0, 255, 0);
    elif Colour_1 == 5:
        Circle1_col = (0, 255, 169);
    elif Colour_1 == 6:
        Circle1_col = (255, 0, 0);
    elif Colour_1 == 7:
        Circle1_col = (0, 0, 255);
    elif Colour_1 == 8:
        Circle1_col = (170, 0, 255);
    elif Colour_1 == 9:
        Circle1_col = (255, 0, 170);
    # keep track of which components have finished
    Stim1_display_pracComponents = [Circle, centre_cross4_2]
    for thisComponent in Stim1_display_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Stim1_display_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Stim1_display_prac"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Stim1_display_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Stim1_display_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Circle* updates
        if Circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Circle.frameNStart = frameN  # exact frame index
            Circle.tStart = t  # local t and not account for scr refresh
            Circle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Circle, 'tStartRefresh')  # time at next scr refresh
            Circle.setAutoDraw(True)
        if Circle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Circle.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Circle.tStop = t  # not accounting for scr refresh
                Circle.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Circle, 'tStopRefresh')  # time at next scr refresh
                Circle.setAutoDraw(False)
        if Circle.status == STARTED:  # only update if drawing
            Circle.setPos((circle1posx,circle1posy), log=False)
            Circle.setFillColor(Circle1_col, log=False)
        
        # *centre_cross4_2* updates
        if centre_cross4_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            centre_cross4_2.frameNStart = frameN  # exact frame index
            centre_cross4_2.tStart = t  # local t and not account for scr refresh
            centre_cross4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(centre_cross4_2, 'tStartRefresh')  # time at next scr refresh
            centre_cross4_2.setAutoDraw(True)
        if centre_cross4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > centre_cross4_2.tStartRefresh + 0.500-frameTolerance:
                # keep track of stop time/frame for later
                centre_cross4_2.tStop = t  # not accounting for scr refresh
                centre_cross4_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(centre_cross4_2, 'tStopRefresh')  # time at next scr refresh
                centre_cross4_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stim1_display_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Stim1_display_prac"-------
    for thisComponent in Stim1_display_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('Circle.started', Circle.tStartRefresh)
    trials_2.addData('Circle.stopped', Circle.tStopRefresh)
    trials_2.addData('centre_cross4_2.started', centre_cross4_2.tStartRefresh)
    trials_2.addData('centre_cross4_2.stopped', centre_cross4_2.tStopRefresh)
    
    # ------Prepare to start Routine "response_prac"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_5
    mouse_5.clicked_name = []
    gotValidClick = False  # until a click is received
    # Count trial numbers
    
    pracnumber =  pracnumber + 1;
    
    # Randomly select circle colour
    
    Colour_2 = rnd.randint(1,9);
    
    # Set circle colour
    if Colour_2 == 1:
        Circle2_col = (255, 0, 0);
    elif Colour_2 == 2:
        Circle2_col = (255, 170, 0);
    elif Colour_2 == 3:
        Circle2_col = (170, 255, 0);
    elif Colour_2 == 4:
        Circle2_col = (0, 255, 0);
    elif Colour_2 == 5:
        Circle2_col = (0, 255, 169);
    elif Colour_2 == 6:
        Circle2_col = (255, 0, 0);
    elif Colour_2 == 7:
        Circle2_col = (0, 0, 255);
    elif Colour_2 == 8:
        Circle2_col = (170, 0, 255);
    elif Colour_2 == 9:
        Circle2_col = (255, 0, 170);
    
    # keep track of which components have finished
    response_pracComponents = [response1disk_5, response2disk_5, response3disk_5, response4disk_5, response5disk_5, response6disk_5, response7disk_5, response8disk_5, mouse_5, Circle_3, text_29]
    for thisComponent in response_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    response_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response_prac"-------
    while continueRoutine:
        # get current time
        t = response_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response1disk_5* updates
        if response1disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_5.frameNStart = frameN  # exact frame index
            response1disk_5.tStart = t  # local t and not account for scr refresh
            response1disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_5, 'tStartRefresh')  # time at next scr refresh
            response1disk_5.setAutoDraw(True)
        
        # *response2disk_5* updates
        if response2disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response2disk_5.frameNStart = frameN  # exact frame index
            response2disk_5.tStart = t  # local t and not account for scr refresh
            response2disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2disk_5, 'tStartRefresh')  # time at next scr refresh
            response2disk_5.setAutoDraw(True)
        
        # *response3disk_5* updates
        if response3disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_5.frameNStart = frameN  # exact frame index
            response3disk_5.tStart = t  # local t and not account for scr refresh
            response3disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_5, 'tStartRefresh')  # time at next scr refresh
            response3disk_5.setAutoDraw(True)
        
        # *response4disk_5* updates
        if response4disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response4disk_5.frameNStart = frameN  # exact frame index
            response4disk_5.tStart = t  # local t and not account for scr refresh
            response4disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response4disk_5, 'tStartRefresh')  # time at next scr refresh
            response4disk_5.setAutoDraw(True)
        
        # *response5disk_5* updates
        if response5disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_5.frameNStart = frameN  # exact frame index
            response5disk_5.tStart = t  # local t and not account for scr refresh
            response5disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_5, 'tStartRefresh')  # time at next scr refresh
            response5disk_5.setAutoDraw(True)
        
        # *response6disk_5* updates
        if response6disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response6disk_5.frameNStart = frameN  # exact frame index
            response6disk_5.tStart = t  # local t and not account for scr refresh
            response6disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response6disk_5, 'tStartRefresh')  # time at next scr refresh
            response6disk_5.setAutoDraw(True)
        
        # *response7disk_5* updates
        if response7disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_5.frameNStart = frameN  # exact frame index
            response7disk_5.tStart = t  # local t and not account for scr refresh
            response7disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_5, 'tStartRefresh')  # time at next scr refresh
            response7disk_5.setAutoDraw(True)
        
        # *response8disk_5* updates
        if response8disk_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response8disk_5.frameNStart = frameN  # exact frame index
            response8disk_5.tStart = t  # local t and not account for scr refresh
            response8disk_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response8disk_5, 'tStartRefresh')  # time at next scr refresh
            response8disk_5.setAutoDraw(True)
        # *mouse_5* updates
        if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_5.frameNStart = frameN  # exact frame index
            mouse_5.tStart = t  # local t and not account for scr refresh
            mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
            mouse_5.status = STARTED
            mouse_5.mouseClock.reset()
            prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
        if mouse_5.status == STARTED:  # only update if started and not finished!
            buttons = mouse_5.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [response1disk,response2disk,response3disk,response4disk,response5disk,response6disk,response7disk,response8disk,]:
                        if obj.contains(mouse_5):
                            gotValidClick = True
                            mouse_5.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *Circle_3* updates
        if Circle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Circle_3.frameNStart = frameN  # exact frame index
            Circle_3.tStart = t  # local t and not account for scr refresh
            Circle_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Circle_3, 'tStartRefresh')  # time at next scr refresh
            Circle_3.setAutoDraw(True)
        if Circle_3.status == STARTED:  # only update if drawing
            Circle_3.setFillColor(Circle2_col, log=False)
        
        # *text_29* updates
        if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_29.frameNStart = frameN  # exact frame index
            text_29.tStart = t  # local t and not account for scr refresh
            text_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
            text_29.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response_prac"-------
    for thisComponent in response_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('response1disk_5.started', response1disk_5.tStartRefresh)
    trials_2.addData('response1disk_5.stopped', response1disk_5.tStopRefresh)
    trials_2.addData('response2disk_5.started', response2disk_5.tStartRefresh)
    trials_2.addData('response2disk_5.stopped', response2disk_5.tStopRefresh)
    trials_2.addData('response3disk_5.started', response3disk_5.tStartRefresh)
    trials_2.addData('response3disk_5.stopped', response3disk_5.tStopRefresh)
    trials_2.addData('response4disk_5.started', response4disk_5.tStartRefresh)
    trials_2.addData('response4disk_5.stopped', response4disk_5.tStopRefresh)
    trials_2.addData('response5disk_5.started', response5disk_5.tStartRefresh)
    trials_2.addData('response5disk_5.stopped', response5disk_5.tStopRefresh)
    trials_2.addData('response6disk_5.started', response6disk_5.tStartRefresh)
    trials_2.addData('response6disk_5.stopped', response6disk_5.tStopRefresh)
    trials_2.addData('response7disk_5.started', response7disk_5.tStartRefresh)
    trials_2.addData('response7disk_5.stopped', response7disk_5.tStopRefresh)
    trials_2.addData('response8disk_5.started', response8disk_5.tStartRefresh)
    trials_2.addData('response8disk_5.stopped', response8disk_5.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    x, y = mouse_5.getPos()
    buttons = mouse_5.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [response1disk,response2disk,response3disk,response4disk,response5disk,response6disk,response7disk,response8disk,]:
            if obj.contains(mouse_5):
                gotValidClick = True
                mouse_5.clicked_name.append(obj.name)
    trials_2.addData('mouse_5.x', x)
    trials_2.addData('mouse_5.y', y)
    trials_2.addData('mouse_5.leftButton', buttons[0])
    trials_2.addData('mouse_5.midButton', buttons[1])
    trials_2.addData('mouse_5.rightButton', buttons[2])
    if len(mouse_5.clicked_name):
        trials_2.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
    trials_2.addData('mouse_5.started', mouse_5.tStart)
    trials_2.addData('mouse_5.stopped', mouse_5.tStop)
    trials_2.addData('Circle_3.started', Circle_3.tStartRefresh)
    trials_2.addData('Circle_3.stopped', Circle_3.tStopRefresh)
    trials_2.addData('text_29.started', text_29.tStartRefresh)
    trials_2.addData('text_29.stopped', text_29.tStopRefresh)
    # the Routine "response_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "summary1_prac"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_8
    mouse_8.clicked_name = []
    gotValidClick = False  # until a click is received
    pracnumbertext = f'You have finished {pracnumber} of 7 practice questions';
    
    text_35.setText(pracnumbertext)
    # keep track of which components have finished
    summary1_pracComponents = [response1disk_8, response2disk_8, response3disk_8, response4disk_8, response5disk_8, response6disk_8, response7disk_8, response8disk_8, mouse_8, rectangle_6, text_34, text_35]
    for thisComponent in summary1_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    summary1_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "summary1_prac"-------
    while continueRoutine:
        # get current time
        t = summary1_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=summary1_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response1disk_8* updates
        if response1disk_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_8.frameNStart = frameN  # exact frame index
            response1disk_8.tStart = t  # local t and not account for scr refresh
            response1disk_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_8, 'tStartRefresh')  # time at next scr refresh
            response1disk_8.setAutoDraw(True)
        
        # *response2disk_8* updates
        if response2disk_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response2disk_8.frameNStart = frameN  # exact frame index
            response2disk_8.tStart = t  # local t and not account for scr refresh
            response2disk_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2disk_8, 'tStartRefresh')  # time at next scr refresh
            response2disk_8.setAutoDraw(True)
        
        # *response3disk_8* updates
        if response3disk_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_8.frameNStart = frameN  # exact frame index
            response3disk_8.tStart = t  # local t and not account for scr refresh
            response3disk_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_8, 'tStartRefresh')  # time at next scr refresh
            response3disk_8.setAutoDraw(True)
        
        # *response4disk_8* updates
        if response4disk_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response4disk_8.frameNStart = frameN  # exact frame index
            response4disk_8.tStart = t  # local t and not account for scr refresh
            response4disk_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response4disk_8, 'tStartRefresh')  # time at next scr refresh
            response4disk_8.setAutoDraw(True)
        
        # *response5disk_8* updates
        if response5disk_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_8.frameNStart = frameN  # exact frame index
            response5disk_8.tStart = t  # local t and not account for scr refresh
            response5disk_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_8, 'tStartRefresh')  # time at next scr refresh
            response5disk_8.setAutoDraw(True)
        
        # *response6disk_8* updates
        if response6disk_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response6disk_8.frameNStart = frameN  # exact frame index
            response6disk_8.tStart = t  # local t and not account for scr refresh
            response6disk_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response6disk_8, 'tStartRefresh')  # time at next scr refresh
            response6disk_8.setAutoDraw(True)
        
        # *response7disk_8* updates
        if response7disk_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_8.frameNStart = frameN  # exact frame index
            response7disk_8.tStart = t  # local t and not account for scr refresh
            response7disk_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_8, 'tStartRefresh')  # time at next scr refresh
            response7disk_8.setAutoDraw(True)
        
        # *response8disk_8* updates
        if response8disk_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response8disk_8.frameNStart = frameN  # exact frame index
            response8disk_8.tStart = t  # local t and not account for scr refresh
            response8disk_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response8disk_8, 'tStartRefresh')  # time at next scr refresh
            response8disk_8.setAutoDraw(True)
        # *mouse_8* updates
        if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_8.frameNStart = frameN  # exact frame index
            mouse_8.tStart = t  # local t and not account for scr refresh
            mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
            mouse_8.status = STARTED
            mouse_8.mouseClock.reset()
            prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
        if mouse_8.status == STARTED:  # only update if started and not finished!
            buttons = mouse_8.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [rectangle]:
                        if obj.contains(mouse_8):
                            gotValidClick = True
                            mouse_8.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *rectangle_6* updates
        if rectangle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rectangle_6.frameNStart = frameN  # exact frame index
            rectangle_6.tStart = t  # local t and not account for scr refresh
            rectangle_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rectangle_6, 'tStartRefresh')  # time at next scr refresh
            rectangle_6.setAutoDraw(True)
        
        # *text_34* updates
        if text_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_34.frameNStart = frameN  # exact frame index
            text_34.tStart = t  # local t and not account for scr refresh
            text_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_34, 'tStartRefresh')  # time at next scr refresh
            text_34.setAutoDraw(True)
        
        # *text_35* updates
        if text_35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_35.frameNStart = frameN  # exact frame index
            text_35.tStart = t  # local t and not account for scr refresh
            text_35.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_35, 'tStartRefresh')  # time at next scr refresh
            text_35.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in summary1_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "summary1_prac"-------
    for thisComponent in summary1_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('response1disk_8.started', response1disk_8.tStartRefresh)
    trials_2.addData('response1disk_8.stopped', response1disk_8.tStopRefresh)
    trials_2.addData('response2disk_8.started', response2disk_8.tStartRefresh)
    trials_2.addData('response2disk_8.stopped', response2disk_8.tStopRefresh)
    trials_2.addData('response3disk_8.started', response3disk_8.tStartRefresh)
    trials_2.addData('response3disk_8.stopped', response3disk_8.tStopRefresh)
    trials_2.addData('response4disk_8.started', response4disk_8.tStartRefresh)
    trials_2.addData('response4disk_8.stopped', response4disk_8.tStopRefresh)
    trials_2.addData('response5disk_8.started', response5disk_8.tStartRefresh)
    trials_2.addData('response5disk_8.stopped', response5disk_8.tStopRefresh)
    trials_2.addData('response6disk_8.started', response6disk_8.tStartRefresh)
    trials_2.addData('response6disk_8.stopped', response6disk_8.tStopRefresh)
    trials_2.addData('response7disk_8.started', response7disk_8.tStartRefresh)
    trials_2.addData('response7disk_8.stopped', response7disk_8.tStopRefresh)
    trials_2.addData('response8disk_8.started', response8disk_8.tStartRefresh)
    trials_2.addData('response8disk_8.stopped', response8disk_8.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    x, y = mouse_8.getPos()
    buttons = mouse_8.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [rectangle]:
            if obj.contains(mouse_8):
                gotValidClick = True
                mouse_8.clicked_name.append(obj.name)
    trials_2.addData('mouse_8.x', x)
    trials_2.addData('mouse_8.y', y)
    trials_2.addData('mouse_8.leftButton', buttons[0])
    trials_2.addData('mouse_8.midButton', buttons[1])
    trials_2.addData('mouse_8.rightButton', buttons[2])
    if len(mouse_8.clicked_name):
        trials_2.addData('mouse_8.clicked_name', mouse_8.clicked_name[0])
    trials_2.addData('mouse_8.started', mouse_8.tStart)
    trials_2.addData('mouse_8.stopped', mouse_8.tStop)
    trials_2.addData('rectangle_6.started', rectangle_6.tStartRefresh)
    trials_2.addData('rectangle_6.stopped', rectangle_6.tStopRefresh)
    trials_2.addData('text_34.started', text_34.tStartRefresh)
    trials_2.addData('text_34.stopped', text_34.tStopRefresh)
    trials_2.addData('text_35.started', text_35.tStartRefresh)
    trials_2.addData('text_35.stopped', text_35.tStopRefresh)
    # the Routine "summary1_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "special_trial_prac"-------
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    special_trial_pracComponents = [text_36]
    for thisComponent in special_trial_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    special_trial_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "special_trial_prac"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = special_trial_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=special_trial_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_36* updates
        if text_36.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_36.frameNStart = frameN  # exact frame index
            text_36.tStart = t  # local t and not account for scr refresh
            text_36.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_36, 'tStartRefresh')  # time at next scr refresh
            text_36.setAutoDraw(True)
        if text_36.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_36.tStartRefresh + .250-frameTolerance:
                # keep track of stop time/frame for later
                text_36.tStop = t  # not accounting for scr refresh
                text_36.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_36, 'tStopRefresh')  # time at next scr refresh
                text_36.setAutoDraw(False)
        # Run catch trials 
        if not ((pracnumber == catchtrialorderprac[0]) or (pracnumber == catchtrialorderprac[1])):
            continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in special_trial_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "special_trial_prac"-------
    for thisComponent in special_trial_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_36.started', text_36.tStartRefresh)
    trials_2.addData('text_36.stopped', text_36.tStopRefresh)
    
    # ------Prepare to start Routine "catch_prac"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_7
    mouse_7.clicked_name = []
    gotValidClick = False  # until a click is received
    # Select random number for catch trial
    
    catchnumberprac = rnd.randint(0,7);
    
    catchtext = f'SPECIAL TRIAL PLEASE JUST SELECT {catchnumberprac}'
    text_32.setText(catchtext)
    # keep track of which components have finished
    catch_pracComponents = [response1disk_7, response2disk_7, response3disk_7, response4disk_7, response5disk_7, response6disk_7, response7disk_7, response8disk_7, mouse_7, text_32, rectangle_5]
    for thisComponent in catch_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    catch_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "catch_prac"-------
    while continueRoutine:
        # get current time
        t = catch_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=catch_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response1disk_7* updates
        if response1disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_7.frameNStart = frameN  # exact frame index
            response1disk_7.tStart = t  # local t and not account for scr refresh
            response1disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_7, 'tStartRefresh')  # time at next scr refresh
            response1disk_7.setAutoDraw(True)
        
        # *response2disk_7* updates
        if response2disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response2disk_7.frameNStart = frameN  # exact frame index
            response2disk_7.tStart = t  # local t and not account for scr refresh
            response2disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2disk_7, 'tStartRefresh')  # time at next scr refresh
            response2disk_7.setAutoDraw(True)
        
        # *response3disk_7* updates
        if response3disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_7.frameNStart = frameN  # exact frame index
            response3disk_7.tStart = t  # local t and not account for scr refresh
            response3disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_7, 'tStartRefresh')  # time at next scr refresh
            response3disk_7.setAutoDraw(True)
        
        # *response4disk_7* updates
        if response4disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response4disk_7.frameNStart = frameN  # exact frame index
            response4disk_7.tStart = t  # local t and not account for scr refresh
            response4disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response4disk_7, 'tStartRefresh')  # time at next scr refresh
            response4disk_7.setAutoDraw(True)
        
        # *response5disk_7* updates
        if response5disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_7.frameNStart = frameN  # exact frame index
            response5disk_7.tStart = t  # local t and not account for scr refresh
            response5disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_7, 'tStartRefresh')  # time at next scr refresh
            response5disk_7.setAutoDraw(True)
        
        # *response6disk_7* updates
        if response6disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response6disk_7.frameNStart = frameN  # exact frame index
            response6disk_7.tStart = t  # local t and not account for scr refresh
            response6disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response6disk_7, 'tStartRefresh')  # time at next scr refresh
            response6disk_7.setAutoDraw(True)
        
        # *response7disk_7* updates
        if response7disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_7.frameNStart = frameN  # exact frame index
            response7disk_7.tStart = t  # local t and not account for scr refresh
            response7disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_7, 'tStartRefresh')  # time at next scr refresh
            response7disk_7.setAutoDraw(True)
        
        # *response8disk_7* updates
        if response8disk_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response8disk_7.frameNStart = frameN  # exact frame index
            response8disk_7.tStart = t  # local t and not account for scr refresh
            response8disk_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response8disk_7, 'tStartRefresh')  # time at next scr refresh
            response8disk_7.setAutoDraw(True)
        # *mouse_7* updates
        if mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_7.frameNStart = frameN  # exact frame index
            mouse_7.tStart = t  # local t and not account for scr refresh
            mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
            mouse_7.status = STARTED
            mouse_7.mouseClock.reset()
            prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
        if mouse_7.status == STARTED:  # only update if started and not finished!
            buttons = mouse_7.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [response1disk,response2disk,response3disk,response4disk,response5disk,response6disk,response7disk,response8disk,]:
                        if obj.contains(mouse_7):
                            gotValidClick = True
                            mouse_7.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        # Run catch trials 
        if not ((pracnumber == catchtrialorderprac[0]) or (pracnumber == catchtrialorderprac[1])):
            continueRoutine=False
        
        # *text_32* updates
        if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_32.frameNStart = frameN  # exact frame index
            text_32.tStart = t  # local t and not account for scr refresh
            text_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
            text_32.setAutoDraw(True)
        
        # *rectangle_5* updates
        if rectangle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rectangle_5.frameNStart = frameN  # exact frame index
            rectangle_5.tStart = t  # local t and not account for scr refresh
            rectangle_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rectangle_5, 'tStartRefresh')  # time at next scr refresh
            rectangle_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in catch_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "catch_prac"-------
    for thisComponent in catch_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('response1disk_7.started', response1disk_7.tStartRefresh)
    trials_2.addData('response1disk_7.stopped', response1disk_7.tStopRefresh)
    trials_2.addData('response2disk_7.started', response2disk_7.tStartRefresh)
    trials_2.addData('response2disk_7.stopped', response2disk_7.tStopRefresh)
    trials_2.addData('response3disk_7.started', response3disk_7.tStartRefresh)
    trials_2.addData('response3disk_7.stopped', response3disk_7.tStopRefresh)
    trials_2.addData('response4disk_7.started', response4disk_7.tStartRefresh)
    trials_2.addData('response4disk_7.stopped', response4disk_7.tStopRefresh)
    trials_2.addData('response5disk_7.started', response5disk_7.tStartRefresh)
    trials_2.addData('response5disk_7.stopped', response5disk_7.tStopRefresh)
    trials_2.addData('response6disk_7.started', response6disk_7.tStartRefresh)
    trials_2.addData('response6disk_7.stopped', response6disk_7.tStopRefresh)
    trials_2.addData('response7disk_7.started', response7disk_7.tStartRefresh)
    trials_2.addData('response7disk_7.stopped', response7disk_7.tStopRefresh)
    trials_2.addData('response8disk_7.started', response8disk_7.tStartRefresh)
    trials_2.addData('response8disk_7.stopped', response8disk_7.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    x, y = mouse_7.getPos()
    buttons = mouse_7.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [response1disk,response2disk,response3disk,response4disk,response5disk,response6disk,response7disk,response8disk,]:
            if obj.contains(mouse_7):
                gotValidClick = True
                mouse_7.clicked_name.append(obj.name)
    trials_2.addData('mouse_7.x', x)
    trials_2.addData('mouse_7.y', y)
    trials_2.addData('mouse_7.leftButton', buttons[0])
    trials_2.addData('mouse_7.midButton', buttons[1])
    trials_2.addData('mouse_7.rightButton', buttons[2])
    if len(mouse_7.clicked_name):
        trials_2.addData('mouse_7.clicked_name', mouse_7.clicked_name[0])
    trials_2.addData('mouse_7.started', mouse_7.tStart)
    trials_2.addData('mouse_7.stopped', mouse_7.tStop)
    trials_2.addData('text_32.started', text_32.tStartRefresh)
    trials_2.addData('text_32.stopped', text_32.tStopRefresh)
    trials_2.addData('rectangle_5.started', rectangle_5.tStartRefresh)
    trials_2.addData('rectangle_5.stopped', rectangle_5.tStopRefresh)
    # the Routine "catch_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "summary2_prac"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_6
    mouse_6.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run catch trials 
    if not ((pracnumber == catchtrialorderprac[0]) or (pracnumber == catchtrialorderprac[1])):
        continueRoutine=False
    
    pracnumbertext = f'You have finished {pracnumber} of 7 practice questions';
    
    
    text_31.setText(pracnumbertext)
    # keep track of which components have finished
    summary2_pracComponents = [response1disk_6, response2disk_6, response3disk_6, response4disk_6, response5disk_6, response6disk_6, response7disk_6, response8disk_6, mouse_6, rectangle_4, text_30, text_31]
    for thisComponent in summary2_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    summary2_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "summary2_prac"-------
    while continueRoutine:
        # get current time
        t = summary2_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=summary2_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response1disk_6* updates
        if response1disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_6.frameNStart = frameN  # exact frame index
            response1disk_6.tStart = t  # local t and not account for scr refresh
            response1disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_6, 'tStartRefresh')  # time at next scr refresh
            response1disk_6.setAutoDraw(True)
        
        # *response2disk_6* updates
        if response2disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response2disk_6.frameNStart = frameN  # exact frame index
            response2disk_6.tStart = t  # local t and not account for scr refresh
            response2disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2disk_6, 'tStartRefresh')  # time at next scr refresh
            response2disk_6.setAutoDraw(True)
        
        # *response3disk_6* updates
        if response3disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_6.frameNStart = frameN  # exact frame index
            response3disk_6.tStart = t  # local t and not account for scr refresh
            response3disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_6, 'tStartRefresh')  # time at next scr refresh
            response3disk_6.setAutoDraw(True)
        
        # *response4disk_6* updates
        if response4disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response4disk_6.frameNStart = frameN  # exact frame index
            response4disk_6.tStart = t  # local t and not account for scr refresh
            response4disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response4disk_6, 'tStartRefresh')  # time at next scr refresh
            response4disk_6.setAutoDraw(True)
        
        # *response5disk_6* updates
        if response5disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_6.frameNStart = frameN  # exact frame index
            response5disk_6.tStart = t  # local t and not account for scr refresh
            response5disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_6, 'tStartRefresh')  # time at next scr refresh
            response5disk_6.setAutoDraw(True)
        
        # *response6disk_6* updates
        if response6disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response6disk_6.frameNStart = frameN  # exact frame index
            response6disk_6.tStart = t  # local t and not account for scr refresh
            response6disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response6disk_6, 'tStartRefresh')  # time at next scr refresh
            response6disk_6.setAutoDraw(True)
        
        # *response7disk_6* updates
        if response7disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_6.frameNStart = frameN  # exact frame index
            response7disk_6.tStart = t  # local t and not account for scr refresh
            response7disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_6, 'tStartRefresh')  # time at next scr refresh
            response7disk_6.setAutoDraw(True)
        
        # *response8disk_6* updates
        if response8disk_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response8disk_6.frameNStart = frameN  # exact frame index
            response8disk_6.tStart = t  # local t and not account for scr refresh
            response8disk_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response8disk_6, 'tStartRefresh')  # time at next scr refresh
            response8disk_6.setAutoDraw(True)
        # *mouse_6* updates
        if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_6.frameNStart = frameN  # exact frame index
            mouse_6.tStart = t  # local t and not account for scr refresh
            mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
            mouse_6.status = STARTED
            mouse_6.mouseClock.reset()
            prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
        if mouse_6.status == STARTED:  # only update if started and not finished!
            buttons = mouse_6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [rectangle]:
                        if obj.contains(mouse_6):
                            gotValidClick = True
                            mouse_6.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *rectangle_4* updates
        if rectangle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rectangle_4.frameNStart = frameN  # exact frame index
            rectangle_4.tStart = t  # local t and not account for scr refresh
            rectangle_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rectangle_4, 'tStartRefresh')  # time at next scr refresh
            rectangle_4.setAutoDraw(True)
        
        # *text_30* updates
        if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_30.frameNStart = frameN  # exact frame index
            text_30.tStart = t  # local t and not account for scr refresh
            text_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
            text_30.setAutoDraw(True)
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in summary2_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "summary2_prac"-------
    for thisComponent in summary2_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('response1disk_6.started', response1disk_6.tStartRefresh)
    trials_2.addData('response1disk_6.stopped', response1disk_6.tStopRefresh)
    trials_2.addData('response2disk_6.started', response2disk_6.tStartRefresh)
    trials_2.addData('response2disk_6.stopped', response2disk_6.tStopRefresh)
    trials_2.addData('response3disk_6.started', response3disk_6.tStartRefresh)
    trials_2.addData('response3disk_6.stopped', response3disk_6.tStopRefresh)
    trials_2.addData('response4disk_6.started', response4disk_6.tStartRefresh)
    trials_2.addData('response4disk_6.stopped', response4disk_6.tStopRefresh)
    trials_2.addData('response5disk_6.started', response5disk_6.tStartRefresh)
    trials_2.addData('response5disk_6.stopped', response5disk_6.tStopRefresh)
    trials_2.addData('response6disk_6.started', response6disk_6.tStartRefresh)
    trials_2.addData('response6disk_6.stopped', response6disk_6.tStopRefresh)
    trials_2.addData('response7disk_6.started', response7disk_6.tStartRefresh)
    trials_2.addData('response7disk_6.stopped', response7disk_6.tStopRefresh)
    trials_2.addData('response8disk_6.started', response8disk_6.tStartRefresh)
    trials_2.addData('response8disk_6.stopped', response8disk_6.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    x, y = mouse_6.getPos()
    buttons = mouse_6.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [rectangle]:
            if obj.contains(mouse_6):
                gotValidClick = True
                mouse_6.clicked_name.append(obj.name)
    trials_2.addData('mouse_6.x', x)
    trials_2.addData('mouse_6.y', y)
    trials_2.addData('mouse_6.leftButton', buttons[0])
    trials_2.addData('mouse_6.midButton', buttons[1])
    trials_2.addData('mouse_6.rightButton', buttons[2])
    if len(mouse_6.clicked_name):
        trials_2.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])
    trials_2.addData('mouse_6.started', mouse_6.tStart)
    trials_2.addData('mouse_6.stopped', mouse_6.tStop)
    trials_2.addData('rectangle_4.started', rectangle_4.tStartRefresh)
    trials_2.addData('rectangle_4.stopped', rectangle_4.tStopRefresh)
    trials_2.addData('text_30.started', text_30.tStartRefresh)
    trials_2.addData('text_30.stopped', text_30.tStopRefresh)
    trials_2.addData('text_31.started', text_31.tStartRefresh)
    trials_2.addData('text_31.stopped', text_31.tStopRefresh)
    # the Routine "summary2_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimconditions.xlsx', selection='0:10'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Stim1_display"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # Circle position and size 
    
    x = 100
    y = 100
    
    radius_F = 1 
    radius_P = 1
    
    angle_1 = 0
    angle_2 = 0
    
    
    theta_1 = (angle_1)*(pi/180)
    theta_2 = (angle_2)*(pi/180)
    
    
    deltax_1 = radius_F*cos(theta_1)
    deltay_1 = radius_F*sin(theta_1)
    deltax_2 = radius_P*cos(theta_2)
    deltay_2 = radius_P*sin(theta_2)
    
    
    a_1 = x + deltax_1
    b_1 = y + deltay_1
    a_2 = x + deltax_2
    b_2 = y + deltay_2
    
    
    # Set circle position 
    if Ecc == 'FF':
        circle1posx = a_1;
        circle1posy = b_1;
    elif Ecc == 'PF':
            circle1posx = a_2;
            circle1posy = b_2;
    
    # Set circle colour
    if Colour_1 == 1:
        Circle1_col = (255, 0, 0);
    elif Colour_1 == 2:
        Circle1_col = (255, 170, 0);
    elif Colour_1 == 3:
        Circle1_col = (170, 255, 0);
    elif Colour_1 == 4:
        Circle1_col = (0, 255, 0);
    elif Colour_1 == 5:
        Circle1_col = (0, 255, 169);
    elif Colour_1 == 6:
        Circle1_col = (255, 0, 0);
    elif Colour_1 == 7:
        Circle1_col = (0, 0, 255);
    elif Colour_1 == 8:
        Circle1_col = (170, 0, 255);
    elif Colour_1 == 9:
        Circle1_col = (255, 0, 170);
    # keep track of which components have finished
    Stim1_displayComponents = [Circle_1, centre_cross4]
    for thisComponent in Stim1_displayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Stim1_displayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Stim1_display"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Stim1_displayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Stim1_displayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Circle_1* updates
        if Circle_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Circle_1.frameNStart = frameN  # exact frame index
            Circle_1.tStart = t  # local t and not account for scr refresh
            Circle_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Circle_1, 'tStartRefresh')  # time at next scr refresh
            Circle_1.setAutoDraw(True)
        if Circle_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Circle_1.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                Circle_1.tStop = t  # not accounting for scr refresh
                Circle_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Circle_1, 'tStopRefresh')  # time at next scr refresh
                Circle_1.setAutoDraw(False)
        if Circle_1.status == STARTED:  # only update if drawing
            Circle_1.setPos((circle1posx,circle1posy), log=False)
            Circle_1.setFillColor(Circle1_col, log=False)
        
        # *centre_cross4* updates
        if centre_cross4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            centre_cross4.frameNStart = frameN  # exact frame index
            centre_cross4.tStart = t  # local t and not account for scr refresh
            centre_cross4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(centre_cross4, 'tStartRefresh')  # time at next scr refresh
            centre_cross4.setAutoDraw(True)
        if centre_cross4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > centre_cross4.tStartRefresh + 0.500-frameTolerance:
                # keep track of stop time/frame for later
                centre_cross4.tStop = t  # not accounting for scr refresh
                centre_cross4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(centre_cross4, 'tStopRefresh')  # time at next scr refresh
                centre_cross4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stim1_displayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Stim1_display"-------
    for thisComponent in Stim1_displayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Circle_1.started', Circle_1.tStartRefresh)
    trials.addData('Circle_1.stopped', Circle_1.tStopRefresh)
    trials.addData('centre_cross4.started', centre_cross4.tStartRefresh)
    trials.addData('centre_cross4.stopped', centre_cross4.tStopRefresh)
    
    # ------Prepare to start Routine "response"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # Count trial numbers
    
    trialnumber =  trialnumber + 1;
    
    # Set circle colour
    if Colour_2 == 1:
        Circle2_col = (255, 0, 0);
    elif Colour_2 == 2:
        Circle2_col = (255, 170, 0);
    elif Colour_2 == 3:
        Circle2_col = (170, 255, 0);
    elif Colour_2 == 4:
        Circle2_col = (0, 255, 0);
    elif Colour_2 == 5:
        Circle2_col = (0, 255, 169);
    elif Colour_2 == 6:
        Circle2_col = (255, 0, 0);
    elif Colour_2 == 7:
        Circle2_col = (0, 0, 255);
    elif Colour_2 == 8:
        Circle2_col = (170, 0, 255);
    elif Colour_2 == 9:
        Circle2_col = (255, 0, 170);
    
    # keep track of which components have finished
    responseComponents = [response1disk, response2disk, response3disk, response4disk, response5disk, response6disk, response7disk, response8disk, mouse, Circle_2, text_23]
    for thisComponent in responseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response"-------
    while continueRoutine:
        # get current time
        t = responseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response1disk* updates
        if response1disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk.frameNStart = frameN  # exact frame index
            response1disk.tStart = t  # local t and not account for scr refresh
            response1disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk, 'tStartRefresh')  # time at next scr refresh
            response1disk.setAutoDraw(True)
        
        # *response2disk* updates
        if response2disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response2disk.frameNStart = frameN  # exact frame index
            response2disk.tStart = t  # local t and not account for scr refresh
            response2disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2disk, 'tStartRefresh')  # time at next scr refresh
            response2disk.setAutoDraw(True)
        
        # *response3disk* updates
        if response3disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk.frameNStart = frameN  # exact frame index
            response3disk.tStart = t  # local t and not account for scr refresh
            response3disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk, 'tStartRefresh')  # time at next scr refresh
            response3disk.setAutoDraw(True)
        
        # *response4disk* updates
        if response4disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response4disk.frameNStart = frameN  # exact frame index
            response4disk.tStart = t  # local t and not account for scr refresh
            response4disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response4disk, 'tStartRefresh')  # time at next scr refresh
            response4disk.setAutoDraw(True)
        
        # *response5disk* updates
        if response5disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk.frameNStart = frameN  # exact frame index
            response5disk.tStart = t  # local t and not account for scr refresh
            response5disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk, 'tStartRefresh')  # time at next scr refresh
            response5disk.setAutoDraw(True)
        
        # *response6disk* updates
        if response6disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response6disk.frameNStart = frameN  # exact frame index
            response6disk.tStart = t  # local t and not account for scr refresh
            response6disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response6disk, 'tStartRefresh')  # time at next scr refresh
            response6disk.setAutoDraw(True)
        
        # *response7disk* updates
        if response7disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk.frameNStart = frameN  # exact frame index
            response7disk.tStart = t  # local t and not account for scr refresh
            response7disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk, 'tStartRefresh')  # time at next scr refresh
            response7disk.setAutoDraw(True)
        
        # *response8disk* updates
        if response8disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response8disk.frameNStart = frameN  # exact frame index
            response8disk.tStart = t  # local t and not account for scr refresh
            response8disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response8disk, 'tStartRefresh')  # time at next scr refresh
            response8disk.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [response1disk,response2disk,response3disk,response4disk,response5disk,response6disk,response7disk,response8disk,]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *Circle_2* updates
        if Circle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Circle_2.frameNStart = frameN  # exact frame index
            Circle_2.tStart = t  # local t and not account for scr refresh
            Circle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Circle_2, 'tStartRefresh')  # time at next scr refresh
            Circle_2.setAutoDraw(True)
        if Circle_2.status == STARTED:  # only update if drawing
            Circle_2.setFillColor(Circle2_col, log=False)
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            text_23.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response"-------
    for thisComponent in responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('response1disk.started', response1disk.tStartRefresh)
    trials.addData('response1disk.stopped', response1disk.tStopRefresh)
    trials.addData('response2disk.started', response2disk.tStartRefresh)
    trials.addData('response2disk.stopped', response2disk.tStopRefresh)
    trials.addData('response3disk.started', response3disk.tStartRefresh)
    trials.addData('response3disk.stopped', response3disk.tStopRefresh)
    trials.addData('response4disk.started', response4disk.tStartRefresh)
    trials.addData('response4disk.stopped', response4disk.tStopRefresh)
    trials.addData('response5disk.started', response5disk.tStartRefresh)
    trials.addData('response5disk.stopped', response5disk.tStopRefresh)
    trials.addData('response6disk.started', response6disk.tStartRefresh)
    trials.addData('response6disk.stopped', response6disk.tStopRefresh)
    trials.addData('response7disk.started', response7disk.tStartRefresh)
    trials.addData('response7disk.stopped', response7disk.tStopRefresh)
    trials.addData('response8disk.started', response8disk.tStartRefresh)
    trials.addData('response8disk.stopped', response8disk.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [response1disk,response2disk,response3disk,response4disk,response5disk,response6disk,response7disk,response8disk,]:
            if obj.contains(mouse):
                gotValidClick = True
                mouse.clicked_name.append(obj.name)
    trials.addData('mouse.x', x)
    trials.addData('mouse.y', y)
    trials.addData('mouse.leftButton', buttons[0])
    trials.addData('mouse.midButton', buttons[1])
    trials.addData('mouse.rightButton', buttons[2])
    if len(mouse.clicked_name):
        trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    trials.addData('Circle_2.started', Circle_2.tStartRefresh)
    trials.addData('Circle_2.stopped', Circle_2.tStopRefresh)
    trials.addData('text_23.started', text_23.tStartRefresh)
    trials.addData('text_23.stopped', text_23.tStopRefresh)
    # the Routine "response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "special_trial"-------
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    special_trialComponents = [text_33]
    for thisComponent in special_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    special_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "special_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = special_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=special_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_33* updates
        if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_33.frameNStart = frameN  # exact frame index
            text_33.tStart = t  # local t and not account for scr refresh
            text_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
            text_33.setAutoDraw(True)
        if text_33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_33.tStartRefresh + .250-frameTolerance:
                # keep track of stop time/frame for later
                text_33.tStop = t  # not accounting for scr refresh
                text_33.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
                text_33.setAutoDraw(False)
        # Run catch trials 
        if not ((trialnumber == catchtrialorder[0]) or (trialnumber == catchtrialorder[1]) or (trialnumber == catchtrialorder[2]) or (trialnumber == catchtrialorder[3]) or (trialnumber == catchtrialorder[4]) or (trialnumber == catchtrialorder[5]) or (trialnumber == catchtrialorder[6]) or (trialnumber == catchtrialorder[7]) or (trialnumber == catchtrialorder[8]) or (trialnumber == catchtrialorder[9])):
            continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in special_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "special_trial"-------
    for thisComponent in special_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_33.started', text_33.tStartRefresh)
    trials.addData('text_33.stopped', text_33.tStopRefresh)
    
    # ------Prepare to start Routine "catch_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # Select random number for catch trial
    
    catchnumber = rnd.randint(0,7);
    
    catchtext = f'SPECIAL TRIAL PLEASE JUST SELECT {catchnumber}'
    text_26.setText(catchtext)
    # keep track of which components have finished
    catch_1Components = [response1disk_3, response2disk_3, response3disk_3, response4disk_3, response5disk_3, response6disk_3, response7disk_3, response8disk_3, mouse_3, text_26, rectangle_2]
    for thisComponent in catch_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    catch_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "catch_1"-------
    while continueRoutine:
        # get current time
        t = catch_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=catch_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response1disk_3* updates
        if response1disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_3.frameNStart = frameN  # exact frame index
            response1disk_3.tStart = t  # local t and not account for scr refresh
            response1disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_3, 'tStartRefresh')  # time at next scr refresh
            response1disk_3.setAutoDraw(True)
        
        # *response2disk_3* updates
        if response2disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response2disk_3.frameNStart = frameN  # exact frame index
            response2disk_3.tStart = t  # local t and not account for scr refresh
            response2disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2disk_3, 'tStartRefresh')  # time at next scr refresh
            response2disk_3.setAutoDraw(True)
        
        # *response3disk_3* updates
        if response3disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_3.frameNStart = frameN  # exact frame index
            response3disk_3.tStart = t  # local t and not account for scr refresh
            response3disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_3, 'tStartRefresh')  # time at next scr refresh
            response3disk_3.setAutoDraw(True)
        
        # *response4disk_3* updates
        if response4disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response4disk_3.frameNStart = frameN  # exact frame index
            response4disk_3.tStart = t  # local t and not account for scr refresh
            response4disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response4disk_3, 'tStartRefresh')  # time at next scr refresh
            response4disk_3.setAutoDraw(True)
        
        # *response5disk_3* updates
        if response5disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_3.frameNStart = frameN  # exact frame index
            response5disk_3.tStart = t  # local t and not account for scr refresh
            response5disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_3, 'tStartRefresh')  # time at next scr refresh
            response5disk_3.setAutoDraw(True)
        
        # *response6disk_3* updates
        if response6disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response6disk_3.frameNStart = frameN  # exact frame index
            response6disk_3.tStart = t  # local t and not account for scr refresh
            response6disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response6disk_3, 'tStartRefresh')  # time at next scr refresh
            response6disk_3.setAutoDraw(True)
        
        # *response7disk_3* updates
        if response7disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_3.frameNStart = frameN  # exact frame index
            response7disk_3.tStart = t  # local t and not account for scr refresh
            response7disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_3, 'tStartRefresh')  # time at next scr refresh
            response7disk_3.setAutoDraw(True)
        
        # *response8disk_3* updates
        if response8disk_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response8disk_3.frameNStart = frameN  # exact frame index
            response8disk_3.tStart = t  # local t and not account for scr refresh
            response8disk_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response8disk_3, 'tStartRefresh')  # time at next scr refresh
            response8disk_3.setAutoDraw(True)
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [response1disk,response2disk,response3disk,response4disk,response5disk,response6disk,response7disk,response8disk,]:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        # Run catch trials 
        if not ((trialnumber == catchtrialorder[0]) or (trialnumber == catchtrialorder[1]) or (trialnumber == catchtrialorder[2]) or (trialnumber == catchtrialorder[3]) or (trialnumber == catchtrialorder[4]) or (trialnumber == catchtrialorder[5]) or (trialnumber == catchtrialorder[6]) or (trialnumber == catchtrialorder[7]) or (trialnumber == catchtrialorder[8]) or (trialnumber == catchtrialorder[9])):
            continueRoutine=False
        
        # *text_26* updates
        if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_26.frameNStart = frameN  # exact frame index
            text_26.tStart = t  # local t and not account for scr refresh
            text_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
            text_26.setAutoDraw(True)
        
        # *rectangle_2* updates
        if rectangle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rectangle_2.frameNStart = frameN  # exact frame index
            rectangle_2.tStart = t  # local t and not account for scr refresh
            rectangle_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rectangle_2, 'tStartRefresh')  # time at next scr refresh
            rectangle_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in catch_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "catch_1"-------
    for thisComponent in catch_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('response1disk_3.started', response1disk_3.tStartRefresh)
    trials.addData('response1disk_3.stopped', response1disk_3.tStopRefresh)
    trials.addData('response2disk_3.started', response2disk_3.tStartRefresh)
    trials.addData('response2disk_3.stopped', response2disk_3.tStopRefresh)
    trials.addData('response3disk_3.started', response3disk_3.tStartRefresh)
    trials.addData('response3disk_3.stopped', response3disk_3.tStopRefresh)
    trials.addData('response4disk_3.started', response4disk_3.tStartRefresh)
    trials.addData('response4disk_3.stopped', response4disk_3.tStopRefresh)
    trials.addData('response5disk_3.started', response5disk_3.tStartRefresh)
    trials.addData('response5disk_3.stopped', response5disk_3.tStopRefresh)
    trials.addData('response6disk_3.started', response6disk_3.tStartRefresh)
    trials.addData('response6disk_3.stopped', response6disk_3.tStopRefresh)
    trials.addData('response7disk_3.started', response7disk_3.tStartRefresh)
    trials.addData('response7disk_3.stopped', response7disk_3.tStopRefresh)
    trials.addData('response8disk_3.started', response8disk_3.tStartRefresh)
    trials.addData('response8disk_3.stopped', response8disk_3.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [response1disk,response2disk,response3disk,response4disk,response5disk,response6disk,response7disk,response8disk,]:
            if obj.contains(mouse_3):
                gotValidClick = True
                mouse_3.clicked_name.append(obj.name)
    trials.addData('mouse_3.x', x)
    trials.addData('mouse_3.y', y)
    trials.addData('mouse_3.leftButton', buttons[0])
    trials.addData('mouse_3.midButton', buttons[1])
    trials.addData('mouse_3.rightButton', buttons[2])
    if len(mouse_3.clicked_name):
        trials.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
    trials.addData('mouse_3.started', mouse_3.tStart)
    trials.addData('mouse_3.stopped', mouse_3.tStop)
    trials.addData('text_26.started', text_26.tStartRefresh)
    trials.addData('text_26.stopped', text_26.tStopRefresh)
    trials.addData('rectangle_2.started', rectangle_2.tStartRefresh)
    trials.addData('rectangle_2.stopped', rectangle_2.tStopRefresh)
    # the Routine "catch_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "response_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    trialnumbertext = f'You have finished {trialnumber} of 324 questions';
    
    
    text_24.setText(trialnumbertext)
    # keep track of which components have finished
    response_2Components = [response1disk_2, response2disk_2, response3disk_2, response4disk_2, response5disk_2, response6disk_2, response7disk_2, response8disk_2, mouse_2, rectangle, text_25, text_24]
    for thisComponent in response_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    response_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "response_2"-------
    while continueRoutine:
        # get current time
        t = response_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=response_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response1disk_2* updates
        if response1disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response1disk_2.frameNStart = frameN  # exact frame index
            response1disk_2.tStart = t  # local t and not account for scr refresh
            response1disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response1disk_2, 'tStartRefresh')  # time at next scr refresh
            response1disk_2.setAutoDraw(True)
        
        # *response2disk_2* updates
        if response2disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response2disk_2.frameNStart = frameN  # exact frame index
            response2disk_2.tStart = t  # local t and not account for scr refresh
            response2disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response2disk_2, 'tStartRefresh')  # time at next scr refresh
            response2disk_2.setAutoDraw(True)
        
        # *response3disk_2* updates
        if response3disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response3disk_2.frameNStart = frameN  # exact frame index
            response3disk_2.tStart = t  # local t and not account for scr refresh
            response3disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response3disk_2, 'tStartRefresh')  # time at next scr refresh
            response3disk_2.setAutoDraw(True)
        
        # *response4disk_2* updates
        if response4disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response4disk_2.frameNStart = frameN  # exact frame index
            response4disk_2.tStart = t  # local t and not account for scr refresh
            response4disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response4disk_2, 'tStartRefresh')  # time at next scr refresh
            response4disk_2.setAutoDraw(True)
        
        # *response5disk_2* updates
        if response5disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response5disk_2.frameNStart = frameN  # exact frame index
            response5disk_2.tStart = t  # local t and not account for scr refresh
            response5disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response5disk_2, 'tStartRefresh')  # time at next scr refresh
            response5disk_2.setAutoDraw(True)
        
        # *response6disk_2* updates
        if response6disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response6disk_2.frameNStart = frameN  # exact frame index
            response6disk_2.tStart = t  # local t and not account for scr refresh
            response6disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response6disk_2, 'tStartRefresh')  # time at next scr refresh
            response6disk_2.setAutoDraw(True)
        
        # *response7disk_2* updates
        if response7disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response7disk_2.frameNStart = frameN  # exact frame index
            response7disk_2.tStart = t  # local t and not account for scr refresh
            response7disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response7disk_2, 'tStartRefresh')  # time at next scr refresh
            response7disk_2.setAutoDraw(True)
        
        # *response8disk_2* updates
        if response8disk_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response8disk_2.frameNStart = frameN  # exact frame index
            response8disk_2.tStart = t  # local t and not account for scr refresh
            response8disk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response8disk_2, 'tStartRefresh')  # time at next scr refresh
            response8disk_2.setAutoDraw(True)
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [rectangle]:
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *rectangle* updates
        if rectangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rectangle.frameNStart = frameN  # exact frame index
            rectangle.tStart = t  # local t and not account for scr refresh
            rectangle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rectangle, 'tStartRefresh')  # time at next scr refresh
            rectangle.setAutoDraw(True)
        
        # *text_25* updates
        if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_25.frameNStart = frameN  # exact frame index
            text_25.tStart = t  # local t and not account for scr refresh
            text_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
            text_25.setAutoDraw(True)
        
        # *text_24* updates
        if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            text_24.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in response_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response_2"-------
    for thisComponent in response_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('response1disk_2.started', response1disk_2.tStartRefresh)
    trials.addData('response1disk_2.stopped', response1disk_2.tStopRefresh)
    trials.addData('response2disk_2.started', response2disk_2.tStartRefresh)
    trials.addData('response2disk_2.stopped', response2disk_2.tStopRefresh)
    trials.addData('response3disk_2.started', response3disk_2.tStartRefresh)
    trials.addData('response3disk_2.stopped', response3disk_2.tStopRefresh)
    trials.addData('response4disk_2.started', response4disk_2.tStartRefresh)
    trials.addData('response4disk_2.stopped', response4disk_2.tStopRefresh)
    trials.addData('response5disk_2.started', response5disk_2.tStartRefresh)
    trials.addData('response5disk_2.stopped', response5disk_2.tStopRefresh)
    trials.addData('response6disk_2.started', response6disk_2.tStartRefresh)
    trials.addData('response6disk_2.stopped', response6disk_2.tStopRefresh)
    trials.addData('response7disk_2.started', response7disk_2.tStartRefresh)
    trials.addData('response7disk_2.stopped', response7disk_2.tStopRefresh)
    trials.addData('response8disk_2.started', response8disk_2.tStartRefresh)
    trials.addData('response8disk_2.stopped', response8disk_2.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [rectangle]:
            if obj.contains(mouse_2):
                gotValidClick = True
                mouse_2.clicked_name.append(obj.name)
    trials.addData('mouse_2.x', x)
    trials.addData('mouse_2.y', y)
    trials.addData('mouse_2.leftButton', buttons[0])
    trials.addData('mouse_2.midButton', buttons[1])
    trials.addData('mouse_2.rightButton', buttons[2])
    if len(mouse_2.clicked_name):
        trials.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
    trials.addData('mouse_2.started', mouse_2.tStart)
    trials.addData('mouse_2.stopped', mouse_2.tStop)
    trials.addData('rectangle.started', rectangle.tStartRefresh)
    trials.addData('rectangle.stopped', rectangle.tStopRefresh)
    trials.addData('text_25.started', text_25.tStartRefresh)
    trials.addData('text_25.stopped', text_25.tStopRefresh)
    trials.addData('text_24.started', text_24.tStartRefresh)
    trials.addData('text_24.stopped', text_24.tStopRefresh)
    # the Routine "response_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


# ------Prepare to start Routine "welcome_instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
welcome_instrComponents = [welcome, key_resp, space]
for thisComponent in welcome_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_instr"-------
while continueRoutine:
    # get current time
    t = welcome_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome* updates
    if welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        welcome.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space* updates
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space.frameNStart = frameN  # exact frame index
        space.tStart = t  # local t and not account for scr refresh
        space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
        space.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_instr"-------
for thisComponent in welcome_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space.started', space.tStartRefresh)
thisExp.addData('space.stopped', space.tStopRefresh)
# the Routine "welcome_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instr_1Components = [text_1, space_2, text_2, key_resp_2]
for thisComponent in instr_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_1"-------
while continueRoutine:
    # get current time
    t = instr_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_1* updates
    if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_1.frameNStart = frameN  # exact frame index
        text_1.tStart = t  # local t and not account for scr refresh
        text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
        text_1.setAutoDraw(True)
    
    # *space_2* updates
    if space_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_2.frameNStart = frameN  # exact frame index
        space_2.tStart = t  # local t and not account for scr refresh
        space_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_2, 'tStartRefresh')  # time at next scr refresh
        space_2.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_1"-------
for thisComponent in instr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_1.started', text_1.tStartRefresh)
thisExp.addData('text_1.stopped', text_1.tStopRefresh)
thisExp.addData('space_2.started', space_2.tStartRefresh)
thisExp.addData('space_2.stopped', space_2.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_3"-------
continueRoutine = True
# update component parameters for each repeat
movie = visual.MovieStim3(
    win=win, name='movie',units='pix', 
    noAudio = False,
    filename='/Users/bethfisher/Documents/Simcolourproject_online/calibrationinstructions_py.mov',
    ori=0, pos=(0, 100), opacity=1,
    loop=True,
    size=(380,410),
    depth=0.0,
    )
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instr_3Components = [movie, text, key_resp_3, text_3, space_3]
for thisComponent in instr_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_3"-------
while continueRoutine:
    # get current time
    t = instr_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    if movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie.frameNStart = frameN  # exact frame index
        movie.tStart = t  # local t and not account for scr refresh
        movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    if movie.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *space_3* updates
    if space_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_3.frameNStart = frameN  # exact frame index
        space_3.tStart = t  # local t and not account for scr refresh
        space_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_3, 'tStartRefresh')  # time at next scr refresh
        space_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_3"-------
for thisComponent in instr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie.started', movie.tStartRefresh)
thisExp.addData('movie.stopped', movie.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('space_3.started', space_3.tStartRefresh)
thisExp.addData('space_3.stopped', space_3.tStopRefresh)
# the Routine "instr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instr_4Components = [text_4, key_resp_4, calibrationline]
for thisComponent in instr_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_4"-------
while continueRoutine:
    # get current time
    t = instr_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *calibrationline* updates
    if calibrationline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calibrationline.frameNStart = frameN  # exact frame index
        calibrationline.tStart = t  # local t and not account for scr refresh
        calibrationline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calibrationline, 'tStartRefresh')  # time at next scr refresh
        calibrationline.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_4"-------
for thisComponent in instr_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('calibrationline.started', calibrationline.tStartRefresh)
thisExp.addData('calibrationline.stopped', calibrationline.tStopRefresh)
# the Routine "instr_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_5"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
instr_5Components = [text_5, key_resp_5, space_4]
for thisComponent in instr_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_5"-------
while continueRoutine:
    # get current time
    t = instr_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_4* updates
    if space_4.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_4.frameNStart = frameN  # exact frame index
        space_4.tStart = t  # local t and not account for scr refresh
        space_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_4, 'tStartRefresh')  # time at next scr refresh
        space_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_5"-------
for thisComponent in instr_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_4.started', space_4.tStartRefresh)
thisExp.addData('space_4.stopped', space_4.tStopRefresh)
# the Routine "instr_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_6"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
instr_6Components = [key_resp_6, space_5, instr_only, text_6]
for thisComponent in instr_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_6"-------
while continueRoutine:
    # get current time
    t = instr_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_5* updates
    if space_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_5.frameNStart = frameN  # exact frame index
        space_5.tStart = t  # local t and not account for scr refresh
        space_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_5, 'tStartRefresh')  # time at next scr refresh
        space_5.setAutoDraw(True)
    
    # *instr_only* updates
    if instr_only.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only.frameNStart = frameN  # exact frame index
        instr_only.tStart = t  # local t and not account for scr refresh
        instr_only.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only, 'tStartRefresh')  # time at next scr refresh
        instr_only.setAutoDraw(True)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_6"-------
for thisComponent in instr_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_5.started', space_5.tStartRefresh)
thisExp.addData('space_5.stopped', space_5.tStopRefresh)
thisExp.addData('instr_only.started', instr_only.tStartRefresh)
thisExp.addData('instr_only.stopped', instr_only.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "instr_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_8"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
instr_8Components = [key_resp_8, space_7, instr_only_3, text_8]
for thisComponent in instr_8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_8"-------
while continueRoutine:
    # get current time
    t = instr_8Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_8Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_7* updates
    if space_7.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_7.frameNStart = frameN  # exact frame index
        space_7.tStart = t  # local t and not account for scr refresh
        space_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_7, 'tStartRefresh')  # time at next scr refresh
        space_7.setAutoDraw(True)
    
    # *instr_only_3* updates
    if instr_only_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only_3.frameNStart = frameN  # exact frame index
        instr_only_3.tStart = t  # local t and not account for scr refresh
        instr_only_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only_3, 'tStartRefresh')  # time at next scr refresh
        instr_only_3.setAutoDraw(True)
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_8"-------
for thisComponent in instr_8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_7.started', space_7.tStartRefresh)
thisExp.addData('space_7.stopped', space_7.tStopRefresh)
thisExp.addData('instr_only_3.started', instr_only_3.tStartRefresh)
thisExp.addData('instr_only_3.stopped', instr_only_3.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "instr_8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_7"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
instr_7Components = [key_resp_7, space_6, instr_only_2, text_7, center_cross]
for thisComponent in instr_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_7"-------
while continueRoutine:
    # get current time
    t = instr_7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *space_6* updates
    if space_6.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_6.frameNStart = frameN  # exact frame index
        space_6.tStart = t  # local t and not account for scr refresh
        space_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_6, 'tStartRefresh')  # time at next scr refresh
        space_6.setAutoDraw(True)
    
    # *instr_only_2* updates
    if instr_only_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_only_2.frameNStart = frameN  # exact frame index
        instr_only_2.tStart = t  # local t and not account for scr refresh
        instr_only_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_only_2, 'tStartRefresh')  # time at next scr refresh
        instr_only_2.setAutoDraw(True)
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *center_cross* updates
    if center_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        center_cross.frameNStart = frameN  # exact frame index
        center_cross.tStart = t  # local t and not account for scr refresh
        center_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(center_cross, 'tStartRefresh')  # time at next scr refresh
        center_cross.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_7"-------
for thisComponent in instr_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('space_6.started', space_6.tStartRefresh)
thisExp.addData('space_6.stopped', space_6.tStopRefresh)
thisExp.addData('instr_only_2.started', instr_only_2.tStartRefresh)
thisExp.addData('instr_only_2.stopped', instr_only_2.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
thisExp.addData('center_cross.started', center_cross.tStartRefresh)
thisExp.addData('center_cross.stopped', center_cross.tStopRefresh)
# the Routine "instr_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "colour_circle_instr"-------
continueRoutine = True
# update component parameters for each repeat
# Randomly place instruction circles 
circle_position = [(-0.25,0.25),(0,0.25),(0.25,0.25),(-0.25,0),(0,0),(0.25,0),(0.25,-0.25),(0,-0.25),(-0.25,-0.25)]
rnd.shuffle(circle_position)
print(circle_position)


key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
colour_circle_instrComponents = [key_resp_9, intructioncircle_1, instructioncircle_2, instructioncircle_3, instructioncircle_4, instructioncircle_5, insturctioncircle_6, instructioncircle_7, instructioncircle_8, instructioncircle_9, space_9, text_9]
for thisComponent in colour_circle_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
colour_circle_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "colour_circle_instr"-------
while continueRoutine:
    # get current time
    t = colour_circle_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=colour_circle_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    #for jj in range(len(instruction_3_color)):
    #    circle[jj].draw()
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *intructioncircle_1* updates
    if intructioncircle_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intructioncircle_1.frameNStart = frameN  # exact frame index
        intructioncircle_1.tStart = t  # local t and not account for scr refresh
        intructioncircle_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intructioncircle_1, 'tStartRefresh')  # time at next scr refresh
        intructioncircle_1.setAutoDraw(True)
    if intructioncircle_1.status == STARTED:  # only update if drawing
        intructioncircle_1.setPos(circle_position[1], log=False)
    
    # *instructioncircle_2* updates
    if instructioncircle_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_2.frameNStart = frameN  # exact frame index
        instructioncircle_2.tStart = t  # local t and not account for scr refresh
        instructioncircle_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_2, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_2.setAutoDraw(True)
    if instructioncircle_2.status == STARTED:  # only update if drawing
        instructioncircle_2.setPos(circle_position[2], log=False)
    
    # *instructioncircle_3* updates
    if instructioncircle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_3.frameNStart = frameN  # exact frame index
        instructioncircle_3.tStart = t  # local t and not account for scr refresh
        instructioncircle_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_3, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_3.setAutoDraw(True)
    if instructioncircle_3.status == STARTED:  # only update if drawing
        instructioncircle_3.setPos(circle_position[3], log=False)
    
    # *instructioncircle_4* updates
    if instructioncircle_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_4.frameNStart = frameN  # exact frame index
        instructioncircle_4.tStart = t  # local t and not account for scr refresh
        instructioncircle_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_4, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_4.setAutoDraw(True)
    if instructioncircle_4.status == STARTED:  # only update if drawing
        instructioncircle_4.setPos(circle_position[4], log=False)
    
    # *instructioncircle_5* updates
    if instructioncircle_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_5.frameNStart = frameN  # exact frame index
        instructioncircle_5.tStart = t  # local t and not account for scr refresh
        instructioncircle_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_5, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_5.setAutoDraw(True)
    if instructioncircle_5.status == STARTED:  # only update if drawing
        instructioncircle_5.setPos(circle_position[5], log=False)
    
    # *insturctioncircle_6* updates
    if insturctioncircle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insturctioncircle_6.frameNStart = frameN  # exact frame index
        insturctioncircle_6.tStart = t  # local t and not account for scr refresh
        insturctioncircle_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insturctioncircle_6, 'tStartRefresh')  # time at next scr refresh
        insturctioncircle_6.setAutoDraw(True)
    if insturctioncircle_6.status == STARTED:  # only update if drawing
        insturctioncircle_6.setPos(circle_position[6], log=False)
    
    # *instructioncircle_7* updates
    if instructioncircle_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_7.frameNStart = frameN  # exact frame index
        instructioncircle_7.tStart = t  # local t and not account for scr refresh
        instructioncircle_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_7, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_7.setAutoDraw(True)
    if instructioncircle_7.status == STARTED:  # only update if drawing
        instructioncircle_7.setPos(circle_position[7], log=False)
    
    # *instructioncircle_8* updates
    if instructioncircle_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_8.frameNStart = frameN  # exact frame index
        instructioncircle_8.tStart = t  # local t and not account for scr refresh
        instructioncircle_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_8, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_8.setAutoDraw(True)
    if instructioncircle_8.status == STARTED:  # only update if drawing
        instructioncircle_8.setPos(circle_position[8], log=False)
    
    # *instructioncircle_9* updates
    if instructioncircle_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructioncircle_9.frameNStart = frameN  # exact frame index
        instructioncircle_9.tStart = t  # local t and not account for scr refresh
        instructioncircle_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructioncircle_9, 'tStartRefresh')  # time at next scr refresh
        instructioncircle_9.setAutoDraw(True)
    if instructioncircle_9.status == STARTED:  # only update if drawing
        instructioncircle_9.setPos(circle_position[0], log=False)
    
    # *space_9* updates
    if space_9.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_9.frameNStart = frameN  # exact frame index
        space_9.tStart = t  # local t and not account for scr refresh
        space_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_9, 'tStartRefresh')  # time at next scr refresh
        space_9.setAutoDraw(True)
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in colour_circle_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "colour_circle_instr"-------
for thisComponent in colour_circle_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('intructioncircle_1.started', intructioncircle_1.tStartRefresh)
thisExp.addData('intructioncircle_1.stopped', intructioncircle_1.tStopRefresh)
thisExp.addData('instructioncircle_2.started', instructioncircle_2.tStartRefresh)
thisExp.addData('instructioncircle_2.stopped', instructioncircle_2.tStopRefresh)
thisExp.addData('instructioncircle_3.started', instructioncircle_3.tStartRefresh)
thisExp.addData('instructioncircle_3.stopped', instructioncircle_3.tStopRefresh)
thisExp.addData('instructioncircle_4.started', instructioncircle_4.tStartRefresh)
thisExp.addData('instructioncircle_4.stopped', instructioncircle_4.tStopRefresh)
thisExp.addData('instructioncircle_5.started', instructioncircle_5.tStartRefresh)
thisExp.addData('instructioncircle_5.stopped', instructioncircle_5.tStopRefresh)
thisExp.addData('insturctioncircle_6.started', insturctioncircle_6.tStartRefresh)
thisExp.addData('insturctioncircle_6.stopped', insturctioncircle_6.tStopRefresh)
thisExp.addData('instructioncircle_7.started', instructioncircle_7.tStartRefresh)
thisExp.addData('instructioncircle_7.stopped', instructioncircle_7.tStopRefresh)
thisExp.addData('instructioncircle_8.started', instructioncircle_8.tStartRefresh)
thisExp.addData('instructioncircle_8.stopped', instructioncircle_8.tStopRefresh)
thisExp.addData('instructioncircle_9.started', instructioncircle_9.tStartRefresh)
thisExp.addData('instructioncircle_9.stopped', instructioncircle_9.tStopRefresh)
thisExp.addData('space_9.started', space_9.tStartRefresh)
thisExp.addData('space_9.stopped', space_9.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# the Routine "colour_circle_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_10"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
instr_10Components = [space_10, text_10, key_resp_10]
for thisComponent in instr_10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_10"-------
while continueRoutine:
    # get current time
    t = instr_10Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_10Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *space_10* updates
    if space_10.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        space_10.frameNStart = frameN  # exact frame index
        space_10.tStart = t  # local t and not account for scr refresh
        space_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_10, 'tStartRefresh')  # time at next scr refresh
        space_10.setAutoDraw(True)
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_10"-------
for thisComponent in instr_10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('space_10.started', space_10.tStartRefresh)
thisExp.addData('space_10.stopped', space_10.tStopRefresh)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr_10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

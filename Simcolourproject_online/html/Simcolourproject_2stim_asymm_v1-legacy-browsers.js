/**************************************** 
 * Simcolourproject_2Stim_Asymm_V1 Test *
 ****************************************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Simcolourproject_2stim_asymm_v1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcome_instrRoutineBegin());
flowScheduler.add(welcome_instrRoutineEachFrame());
flowScheduler.add(welcome_instrRoutineEnd());
flowScheduler.add(colour_circle_instrRoutineBegin());
flowScheduler.add(colour_circle_instrRoutineEachFrame());
flowScheduler.add(colour_circle_instrRoutineEnd());
flowScheduler.add(instr_1RoutineBegin());
flowScheduler.add(instr_1RoutineEachFrame());
flowScheduler.add(instr_1RoutineEnd());
flowScheduler.add(instr_3RoutineBegin());
flowScheduler.add(instr_3RoutineEachFrame());
flowScheduler.add(instr_3RoutineEnd());
flowScheduler.add(instr_4RoutineBegin());
flowScheduler.add(instr_4RoutineEachFrame());
flowScheduler.add(instr_4RoutineEnd());
flowScheduler.add(instr_5RoutineBegin());
flowScheduler.add(instr_5RoutineEachFrame());
flowScheduler.add(instr_5RoutineEnd());
flowScheduler.add(instr_6RoutineBegin());
flowScheduler.add(instr_6RoutineEachFrame());
flowScheduler.add(instr_6RoutineEnd());
flowScheduler.add(instr_8RoutineBegin());
flowScheduler.add(instr_8RoutineEachFrame());
flowScheduler.add(instr_8RoutineEnd());
flowScheduler.add(instr_7RoutineBegin());
flowScheduler.add(instr_7RoutineEachFrame());
flowScheduler.add(instr_7RoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var welcome_instrClock;
var welcome;
var key_resp;
var space;
var colour_circle_instrClock;
var key_resp_9;
var space_8;
var intructioncircle_1;
var instructioncircle_2;
var instructioncircle_3;
var instructioncircle_4;
var instructioncircle_5;
var insturctioncircle_6;
var instructioncircle_7;
var instructioncircle_8;
var instructioncircle_9;
var space_9;
var text_9;
var instr_1Clock;
var text_1;
var space_2;
var text_2;
var key_resp_2;
var instr_3Clock;
var text;
var key_resp_3;
var text_3;
var space_3;
var instr_4Clock;
var text_4;
var key_resp_4;
var calibrationline;
var instr_5Clock;
var text_5;
var key_resp_5;
var space_4;
var instr_6Clock;
var key_resp_6;
var space_5;
var instr_only;
var text_6;
var instr_8Clock;
var key_resp_8;
var space_7;
var instr_only_3;
var text_8;
var instr_7Clock;
var key_resp_7;
var space_6;
var instr_only_2;
var text_7;
var center_cross;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "welcome_instr"
  welcome_instrClock = new util.Clock();
  welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome',
    text: 'Welcome to this experiment \n\nThis will take about 45 minutes ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: 2, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space = new visual.TextStim({
    win: psychoJS.window,
    name: 'space',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "colour_circle_instr"
  colour_circle_instrClock = new util.Clock();
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_8',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  intructioncircle_1 = new visual.Polygon ({
    win: psychoJS.window, name: 'intructioncircle_1', 
    edges: 1000, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(undefined),
    fillColor: new util.Color([255, 0, 0]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  instructioncircle_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_2', 
    edges: 1000, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(undefined),
    fillColor: new util.Color([255, 170, 0]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  instructioncircle_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_3', 
    edges: 1000, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([170, 255, 0]),
    fillColor: new util.Color([170, 255, 0]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  instructioncircle_4 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_4', 
    edges: 1000, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(undefined),
    fillColor: new util.Color([0, 255, 0]),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  instructioncircle_5 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_5', 
    edges: 1000, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(undefined),
    fillColor: new util.Color([0, 255, 169]),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  insturctioncircle_6 = new visual.Polygon ({
    win: psychoJS.window, name: 'insturctioncircle_6', 
    edges: 1000, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(undefined),
    fillColor: new util.Color([0, 169, 255]),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  instructioncircle_7 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_7', 
    edges: 1000, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(undefined),
    fillColor: new util.Color([0, 0, 255]),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  instructioncircle_8 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_8', 
    edges: 1000, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(undefined),
    fillColor: new util.Color([170, 0, 255]),
    opacity: 1, depth: -10, interpolate: true,
  });
  
  instructioncircle_9 = new visual.Polygon ({
    win: psychoJS.window, name: 'instructioncircle_9', 
    edges: 1000, size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color(undefined),
    fillColor: new util.Color([255, 0, 170]),
    opacity: 1, depth: -11, interpolate: true,
  });
  
  space_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_9',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'During the test, you will see these 9 colors below',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.5], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -13.0 
  });
  
  // Initialize components for Routine "instr_1"
  instr_1Clock = new util.Clock();
  text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_1',
    text: 'Before starting the main experiment, we need to do some quick calibrations to ensure your screen is set up correctly.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  space_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_2',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Warning! It is critical that these calibrations are done correctly or you will be unable to do the experiment and we will be unable to approve your payment!',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('red'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr_3"
  instr_3Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Next, we need to get you to keep your head a fixed distance from the screen.\nThis will ensure future images are the right size for your screen. On the next screen please:',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.03,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '1. Keeping your arm straight, please touch your thumb to the centre of the screen in the oval\n2. While keeping your head in the same position, lower your arm.\n3. Please keep your head in this position for the remainder of the experiment ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  space_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_3',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "instr_4"
  instr_4Clock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '1. While keeping your arm straight touch your thumb to the centre of the screen in the oval.\n2. Keep yourhead in the same position, but lower and relax your arm.\n3. Please keep your head in this position for the remainder of the experiment\n4. Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  calibrationline = new visual.ImageStim({
    win : psychoJS.window,
    name : 'calibrationline', units : undefined, 
    image : '/Users/bethfisher/Documents/Simcolourproject_online/calibrationline.png', mask : undefined,
    ori : 0, pos : [0, (- 0.2)], size : [0.1, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "instr_5"
  instr_5Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Lastly, we need to know how far your head is from the screen.\nPlease keep your head in the same position as before.\n\nOver the next few pages we will explain how we can work out how far you are sitting from the screen.\nPlease pay attention and follow all the instructions carefully.\n\nThese first few pages will be INSTRUCTIONS ONLY. You will be instructed when the calibrations start.\n\nWhen ready, press SPACE to continue and follow the instructions on the next page.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: 2, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_4',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "instr_6"
  instr_6Clock = new util.Clock();
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_5',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '1. Put a finger on <ENTER> on the keyboard.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "instr_8"
  instr_8Clock = new util.Clock();
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_7',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only_3',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '2. Close your right eye',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "instr_7"
  instr_7Clock = new util.Clock();
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  space_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_6',
    text: 'Press SPACE to continue ',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_only_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_only_2',
    text: 'INSTRUCTIONS ONLY',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -2.0 
  });
  
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: '3. Stare at the middle of the screen, keeping your head in the same position as before.\nKeep your right eye closed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.03,  wrapWidth: 1.5, ori: 0,
    color: new util.Color('yellow'),  opacity: 1,
    depth: -3.0 
  });
  
  center_cross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'center_cross', units : 'norm', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 1.5, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_resp_allKeys;
var welcome_instrComponents;
function welcome_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'welcome_instr'-------
    t = 0;
    welcome_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    welcome_instrComponents = [];
    welcome_instrComponents.push(welcome);
    welcome_instrComponents.push(key_resp);
    welcome_instrComponents.push(space);
    
    welcome_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function welcome_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'welcome_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = welcome_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome* updates
    if (t >= 0.0 && welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome.tStart = t;  // (not accounting for frame time here)
      welcome.frameNStart = frameN;  // exact frame index
      
      welcome.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space* updates
    if (t >= 0.0 && space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space.tStart = t;  // (not accounting for frame time here)
      space.frameNStart = frameN;  // exact frame index
      
      space.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    welcome_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcome_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'welcome_instr'-------
    welcome_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "welcome_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var circle_position;
var _key_resp_9_allKeys;
var colour_circle_instrComponents;
function colour_circle_instrRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'colour_circle_instr'-------
    t = 0;
    colour_circle_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    circle_position = [[(- 0.25), 0.25], [0, 0.25], [0.25, 0.25], [(- 0.25), 0], [0, 0], [0.25, 0], [0.25, (- 0.25)], [0, (- 0.25)], [(- 0.25), (- 0.25)]];
    rnd.shuffle(circle_position);
    
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    // keep track of which components have finished
    colour_circle_instrComponents = [];
    colour_circle_instrComponents.push(key_resp_9);
    colour_circle_instrComponents.push(space_8);
    colour_circle_instrComponents.push(intructioncircle_1);
    colour_circle_instrComponents.push(instructioncircle_2);
    colour_circle_instrComponents.push(instructioncircle_3);
    colour_circle_instrComponents.push(instructioncircle_4);
    colour_circle_instrComponents.push(instructioncircle_5);
    colour_circle_instrComponents.push(insturctioncircle_6);
    colour_circle_instrComponents.push(instructioncircle_7);
    colour_circle_instrComponents.push(instructioncircle_8);
    colour_circle_instrComponents.push(instructioncircle_9);
    colour_circle_instrComponents.push(space_9);
    colour_circle_instrComponents.push(text_9);
    
    colour_circle_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function colour_circle_instrRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'colour_circle_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = colour_circle_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    /* Syntax Error: Fix Python code */
    
    // *key_resp_9* updates
    if (t >= 2 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_8* updates
    if (t >= 0.0 && space_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_8.tStart = t;  // (not accounting for frame time here)
      space_8.frameNStart = frameN;  // exact frame index
      
      space_8.setAutoDraw(true);
    }

    
    // *intructioncircle_1* updates
    if (t >= 0.0 && intructioncircle_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intructioncircle_1.tStart = t;  // (not accounting for frame time here)
      intructioncircle_1.frameNStart = frameN;  // exact frame index
      
      intructioncircle_1.setAutoDraw(true);
    }

    
    if (intructioncircle_1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      intructioncircle_1.setPos(circle_position[1]);
    }
    
    // *instructioncircle_2* updates
    if (t >= 0.0 && instructioncircle_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_2.tStart = t;  // (not accounting for frame time here)
      instructioncircle_2.frameNStart = frameN;  // exact frame index
      
      instructioncircle_2.setAutoDraw(true);
    }

    
    if (instructioncircle_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      instructioncircle_2.setPos(circle_position[2]);
    }
    
    // *instructioncircle_3* updates
    if (t >= 0.0 && instructioncircle_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_3.tStart = t;  // (not accounting for frame time here)
      instructioncircle_3.frameNStart = frameN;  // exact frame index
      
      instructioncircle_3.setAutoDraw(true);
    }

    
    if (instructioncircle_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      instructioncircle_3.setPos(circle_position[3]);
    }
    
    // *instructioncircle_4* updates
    if (t >= 0.0 && instructioncircle_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_4.tStart = t;  // (not accounting for frame time here)
      instructioncircle_4.frameNStart = frameN;  // exact frame index
      
      instructioncircle_4.setAutoDraw(true);
    }

    
    if (instructioncircle_4.status === PsychoJS.Status.STARTED){ // only update if being drawn
      instructioncircle_4.setPos(circle_position[4]);
    }
    
    // *instructioncircle_5* updates
    if (t >= 0.0 && instructioncircle_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_5.tStart = t;  // (not accounting for frame time here)
      instructioncircle_5.frameNStart = frameN;  // exact frame index
      
      instructioncircle_5.setAutoDraw(true);
    }

    
    if (instructioncircle_5.status === PsychoJS.Status.STARTED){ // only update if being drawn
      instructioncircle_5.setPos(circle_position[5]);
    }
    
    // *insturctioncircle_6* updates
    if (t >= 0.0 && insturctioncircle_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      insturctioncircle_6.tStart = t;  // (not accounting for frame time here)
      insturctioncircle_6.frameNStart = frameN;  // exact frame index
      
      insturctioncircle_6.setAutoDraw(true);
    }

    
    if (insturctioncircle_6.status === PsychoJS.Status.STARTED){ // only update if being drawn
      insturctioncircle_6.setPos(circle_position[6]);
    }
    
    // *instructioncircle_7* updates
    if (t >= 0.0 && instructioncircle_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_7.tStart = t;  // (not accounting for frame time here)
      instructioncircle_7.frameNStart = frameN;  // exact frame index
      
      instructioncircle_7.setAutoDraw(true);
    }

    
    if (instructioncircle_7.status === PsychoJS.Status.STARTED){ // only update if being drawn
      instructioncircle_7.setPos(circle_position[7]);
    }
    
    // *instructioncircle_8* updates
    if (t >= 0.0 && instructioncircle_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_8.tStart = t;  // (not accounting for frame time here)
      instructioncircle_8.frameNStart = frameN;  // exact frame index
      
      instructioncircle_8.setAutoDraw(true);
    }

    
    if (instructioncircle_8.status === PsychoJS.Status.STARTED){ // only update if being drawn
      instructioncircle_8.setPos(circle_position[8]);
    }
    
    // *instructioncircle_9* updates
    if (t >= 0.0 && instructioncircle_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructioncircle_9.tStart = t;  // (not accounting for frame time here)
      instructioncircle_9.frameNStart = frameN;  // exact frame index
      
      instructioncircle_9.setAutoDraw(true);
    }

    
    if (instructioncircle_9.status === PsychoJS.Status.STARTED){ // only update if being drawn
      instructioncircle_9.setPos(circle_position[0]);
    }
    
    // *space_9* updates
    if (t >= 2 && space_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_9.tStart = t;  // (not accounting for frame time here)
      space_9.frameNStart = frameN;  // exact frame index
      
      space_9.setAutoDraw(true);
    }

    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_9.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    colour_circle_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function colour_circle_instrRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'colour_circle_instr'-------
    colour_circle_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "colour_circle_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var instr_1Components;
function instr_1RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_1'-------
    t = 0;
    instr_1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    instr_1Components = [];
    instr_1Components.push(text_1);
    instr_1Components.push(space_2);
    instr_1Components.push(text_2);
    instr_1Components.push(key_resp_2);
    
    instr_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_1RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_1* updates
    if (t >= 0.0 && text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_1.tStart = t;  // (not accounting for frame time here)
      text_1.frameNStart = frameN;  // exact frame index
      
      text_1.setAutoDraw(true);
    }

    
    // *space_2* updates
    if (t >= 0.0 && space_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_2.tStart = t;  // (not accounting for frame time here)
      space_2.frameNStart = frameN;  // exact frame index
      
      space_2.setAutoDraw(true);
    }

    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_1RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_1'-------
    instr_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "instr_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var movieClock;
var movie;
var _key_resp_3_allKeys;
var instr_3Components;
function instr_3RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_3'-------
    t = 0;
    instr_3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    movieClock = new util.Clock();
    movie = new visual.MovieStim({
      win: psychoJS.window,
      name: 'movie',
      units: 'pix',
      movie: '/Users/bethfisher/Documents/Simcolourproject_online/calibrationinstructions_py.mov',
      pos: [0, 100],
      size: [380, 410],
      ori: 0,
      opacity: 1,
      loop: true,
      noAudio: false,
      });
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    instr_3Components = [];
    instr_3Components.push(movie);
    instr_3Components.push(text);
    instr_3Components.push(key_resp_3);
    instr_3Components.push(text_3);
    instr_3Components.push(space_3);
    
    instr_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_3RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *movie* updates
    if (t >= 0.0 && movie.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      movie.tStart = t;  // (not accounting for frame time here)
      movie.frameNStart = frameN;  // exact frame index
      
      movie.setAutoDraw(true);
    }

    frameRemains = 0.0 + undefined - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (movie.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      movie.setAutoDraw(false);
    }

    if (movie.status === PsychoJS.Status.FINISHED) {  // force-end the routine
        continueRoutine = false;
    }
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *space_3* updates
    if (t >= 0.0 && space_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_3.tStart = t;  // (not accounting for frame time here)
      space_3.frameNStart = frameN;  // exact frame index
      
      space_3.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_3RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_3'-------
    instr_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "instr_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var instr_4Components;
function instr_4RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_4'-------
    t = 0;
    instr_4Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    instr_4Components = [];
    instr_4Components.push(text_4);
    instr_4Components.push(key_resp_4);
    instr_4Components.push(calibrationline);
    
    instr_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_4RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_4'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *calibrationline* updates
    if (t >= 0.0 && calibrationline.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      calibrationline.tStart = t;  // (not accounting for frame time here)
      calibrationline.frameNStart = frameN;  // exact frame index
      
      calibrationline.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_4RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_4'-------
    instr_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "instr_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var instr_5Components;
function instr_5RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_5'-------
    t = 0;
    instr_5Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    instr_5Components = [];
    instr_5Components.push(text_5);
    instr_5Components.push(key_resp_5);
    instr_5Components.push(space_4);
    
    instr_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_5RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_5'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 2 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_4* updates
    if (t >= 2 && space_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_4.tStart = t;  // (not accounting for frame time here)
      space_4.frameNStart = frameN;  // exact frame index
      
      space_4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_5RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_5'-------
    instr_5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "instr_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var instr_6Components;
function instr_6RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_6'-------
    t = 0;
    instr_6Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    instr_6Components = [];
    instr_6Components.push(key_resp_6);
    instr_6Components.push(space_5);
    instr_6Components.push(instr_only);
    instr_6Components.push(text_6);
    
    instr_6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_6RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_6'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_6* updates
    if (t >= 2 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_5* updates
    if (t >= 2 && space_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_5.tStart = t;  // (not accounting for frame time here)
      space_5.frameNStart = frameN;  // exact frame index
      
      space_5.setAutoDraw(true);
    }

    
    // *instr_only* updates
    if (t >= 0.0 && instr_only.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only.tStart = t;  // (not accounting for frame time here)
      instr_only.frameNStart = frameN;  // exact frame index
      
      instr_only.setAutoDraw(true);
    }

    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_6RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_6'-------
    instr_6Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "instr_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_8_allKeys;
var instr_8Components;
function instr_8RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_8'-------
    t = 0;
    instr_8Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    instr_8Components = [];
    instr_8Components.push(key_resp_8);
    instr_8Components.push(space_7);
    instr_8Components.push(instr_only_3);
    instr_8Components.push(text_8);
    
    instr_8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_8RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_8'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_8Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_8* updates
    if (t >= 2 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_7* updates
    if (t >= 2 && space_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_7.tStart = t;  // (not accounting for frame time here)
      space_7.frameNStart = frameN;  // exact frame index
      
      space_7.setAutoDraw(true);
    }

    
    // *instr_only_3* updates
    if (t >= 0.0 && instr_only_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only_3.tStart = t;  // (not accounting for frame time here)
      instr_only_3.frameNStart = frameN;  // exact frame index
      
      instr_only_3.setAutoDraw(true);
    }

    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_8Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_8RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_8'-------
    instr_8Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "instr_8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var instr_7Components;
function instr_7RoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instr_7'-------
    t = 0;
    instr_7Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    instr_7Components = [];
    instr_7Components.push(key_resp_7);
    instr_7Components.push(space_6);
    instr_7Components.push(instr_only_2);
    instr_7Components.push(text_7);
    instr_7Components.push(center_cross);
    
    instr_7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function instr_7RoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instr_7'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instr_7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_7* updates
    if (t >= 2 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *space_6* updates
    if (t >= 2 && space_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_6.tStart = t;  // (not accounting for frame time here)
      space_6.frameNStart = frameN;  // exact frame index
      
      space_6.setAutoDraw(true);
    }

    
    // *instr_only_2* updates
    if (t >= 0.0 && instr_only_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_only_2.tStart = t;  // (not accounting for frame time here)
      instr_only_2.frameNStart = frameN;  // exact frame index
      
      instr_only_2.setAutoDraw(true);
    }

    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    
    // *center_cross* updates
    if (t >= 0.0 && center_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      center_cross.tStart = t;  // (not accounting for frame time here)
      center_cross.frameNStart = frameN;  // exact frame index
      
      center_cross.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr_7Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_7RoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instr_7'-------
    instr_7Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // the Routine "instr_7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

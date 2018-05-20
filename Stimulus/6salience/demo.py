from psychopy import visual, core, event #import some libraries from PsychoPy

#create a window
mywin = visual.Window([800,600], monitor="testMonitor", units="cm")
#controller = visual.Window([800, 600], monitor="controller", units="deg")

#create some stimuli
background_grating = visual.GratingStim(win=mywin, mask=None, size=200, pos=(0,0), sf=1)
grating = visual.GratingStim(win=mywin, mask='circle', size=3, pos=[-3,3], ori=30, sf=1)
color_circle = visual.Circle(win=mywin, size=3, pos=[-3, 3], fillColor=(0, 1, 0), fillColorSpace='rgb')
contour = visual.Circle(win=mywin, size=3, pos=[-3,3], lineColor=(1,0,0), lineColorSpace='rgb')
fixation = visual.GratingStim(win=mywin, size=0.2, pos=[0,0], sf=0, rgb=-1)

high_time = 1
low_time = 2
seq = [ ("grating", grating, high_time),
        ("circle",  color_circle, high_time),
        ("contour", contour, high_time)]
idx = 0

t = core.Clock()

current_stim = None
is_grating = False

#draw the stimuli and update the window
while True: #this creates a never-ending loop
    t.add(low_time)
    while t.getTime() < 0:
        background_grating.setPhase(0.05, '+')
        background_grating.draw()
        mywin.flip()
        event.clearEvents()

    current_stim = seq[idx%3][1]
    t.add(seq[idx%3][2])
    idx += 1

    while t.getTime() < 0:
        background_grating.setPhase(0.05, '+')
        background_grating.draw()

        if seq[(idx-1)%3][0] == 'grating':
            current_stim.setPhase(0.05, '-')
        current_stim.draw()
        fixation.draw()
        mywin.flip()

        event.clearEvents()

#cleanup
mywin.close()
core.quit()

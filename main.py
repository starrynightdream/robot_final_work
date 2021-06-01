from toBerry import gogo, back, stop, rockL, rockR, getIR, speed, pwmEnd
import time

stepTime = 0.01
testTime = 0.1
turnAroundTime = 1.4
Ending = False

def mainTurnRight():
    rockR()

def mainTurnLeft():
    rockL()

def turnAround():
    goTime = 1
    checkStep = 0.1

    pasBy = False
    gogo()
    time.sleep(goTime)
    rockR()
    l, r = getIR()

    while not l:
        time.sleep(checkStep)
        l, r = getIR()
    
    while l:
        time.sleep(checkStep)
        l, r = getIR()
    
    while not l:
        time.sleep(checkStep)
        l, r = getIR()

    # rockR()
    # time.sleep(turnAroundTime)
    # stop()

def mainGoGo():
    gogo()

if __name__ == "__main__":
    time.sleep(0.1)
    speed(50)

    try:
        while not Ending:
            l, r = getIR()

            if l and r:
                turnAround()
            elif l:
                mainTurnLeft()
            elif r:
                mainTurnRight()
            else:
                mainGoGo()

            time.sleep( stepTime)
            # stop()
            # time.sleep( 0.001)
            # time.sleep( testTime)
    finally:
        stop()
        pwmEnd()
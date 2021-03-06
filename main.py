from toBerry import gogo, back, stop, rockL, rockR, getIR, speed, pwmEnd
import time

stepTime = 0.001
testTime = 0.1
turnAroundTime = 1.4
Ending = False

def mainTurnRight():
    rockR()

def mainTurnLeft():
    rockL()

def turnAround():
    goTime = 0.1
    checkStep = 0.01

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
    
    while not (l or r):
        time.sleep(checkStep)
        l, r = getIR()

    back()
    time.sleep(checkStep)
    stop()
    # rockR()
    # time.sleep(turnAroundTime)
    # stop()

def mainGoGo():
    gogo()

if __name__ == "__main__":
    time.sleep(0.1)
    speed(10)
    count = True

    try:
        while not Ending:
            l, r = getIR()

            if l and r:
                if count:
                    count = False
                    turnAround()
                else:
                    stop()
                    break
            elif l:
                mainTurnLeft()
            elif r:
                mainTurnRight()
            else:
                mainGoGo()

            time.sleep( stepTime)
            stop()
            time.sleep( stepTime / 10)
            # time.sleep( testTime)
    finally:
        stop()
        pwmEnd()
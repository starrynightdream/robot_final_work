from toBerry import gogo, back, stop, rockL, rockR, getIR, speed, pwmEnd, get_Dis_Sound
import time

stepTime = 0.001
testTime = 0.1
turnAroundTime = 1.4
Ending = False

def turnLeft():
    goTime = 0.1
    checkStep = 0.01

    gogo()
    time.sleep(goTime)
    rockL()
    l, r = getIR()

    while not l:
        time.sleep(checkStep)
        l, r = getIR()
    
    while l:
        time.sleep(checkStep)
        l, r = getIR()
    
    stop()

if __name__ == "__main__":
    time.sleep(0.1)
    speed(10)
    # 添加超声判断
    count = 3
    k = 0.1
    fast = True
    while count != 0 and fast:
        dis = get_Dis_Sound()
        if dis < k and fast:
            fast = False
            count -=1
        else:
            fase = True

    count = 3
    try:
        while count != 0:
            l, r = getIR()

            if l and r:
                if count !=0:
                    count -= 1
                    turnLeft()
                else:
                    stop()
                    break

            elif l:
                rockL()
            elif r:
                rockR()
            else:
                gogo()

            time.sleep( stepTime)
            stop()
            time.sleep( stepTime / 10)
            # time.sleep( testTime)
    finally:
        stop()
        pwmEnd()
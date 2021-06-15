from toBerry import gogo, back, stop, rockL, rockR, getIR, speed, pwmEnd, get_Dis_Sound, LGogo
import time

stepTime = 0.01
testTime = 0.1
turnAroundTime = 1.4
Ending = False

def turnLeft():
    goTime = 0.1
    checkStep = 0.01

    gogo()
    # time.sleep(goTime)
    l, r = getIR()
    while l or r:
        time.sleep(checkStep)
        l, r = getIR()
    
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
    k = 6
    fast = True
    while count != 0:
        dis = get_Dis_Sound()
        print(dis < k, fast, count)
        if dis < k:
            if fast:
                fast = False
                count -=1
        else:
            fast = True
    
    count = 4
    try:
        while count != 0:
            l, r = getIR()

            if l and r:
                if count !=0:
                    '''
                    遇到过弯处
                    '''
                    count -= 1
                    turnLeft()
                else:
                    '''
                    退出循环
                    '''
                    stop()
                    pwmEnd()
                    break

            elif l:
                rockL()
            elif r:
                rockR()
                time.sleep(0.005)
            else:
                # LGogo()
                gogo()
                time.sleep(0.055)

            time.sleep( stepTime)
            stop()
            time.sleep( stepTime / 10)
            # time.sleep( testTime)
    finally:
        stop()
        pwmEnd()
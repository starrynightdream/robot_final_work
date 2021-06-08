# design

本仓库是一个带有控制脚本与网络后台的小车控制代码。

因为是为了作业某些脚本不具有通用性。

## feat
- <del> 添加自动根据脚本数生成按钮 </del>
- ws实现双向通信检测脚本运行情况。

## main2 design
- 只有左转弯，且转弯时两边都有黑线
- 如何区分到最后与在路途中偏移位置。

    def main:
        waitForSound
        count = 3
        fast = true
        while count != 0:
            dis = getD
            if dis < k and fast:
                count-=1
                fast = false
            else:
                fase = true

        // 紧接寻路算法。
        count = 3
        while True:
            l,r = get lr
            if l and r:
                if count != 0:
                    count -= 1
                    turn_left
            if l:
                rr 
            if r:
                rl
            else
                gogo
            
            sleep


    def turn_left:
        前进一段
        gogo()
        sleep()
        rl
        l,r = get lr
        while not l:
            sleep()
            l,r = get lr

        while l:
            sleep()
            l,r = get lr

import math, Manu


# 设定温度20度
def VK(t, td, e1, e2):
    Dp = 0.05
    Di = 0.1
    Dd = 0.1
    e = td - t  # td设定温度，t当前温
    result = Dp * (e - e1) + Di * e + Dd * (e - 2 * e1 + e2)
    return result


def Test(arg, exp):
    global e1 # 上一次的温差
    global e2 # 上上次的温差
    global v1
    print 'Hello world'
    seekresult = CH_232_加热棒.Clear()
    seekresult = CH_232_温度传感器.Clear()
    Protocol_温度传感器.温度值.Value = arg[2]  # 读取当前温度
    print Protocol_温度传感器.温度值.Value
    bool = Protocol_温度传感器.Write()
    API.Common.Timer.Normal.Sleep(1000)
    # 第一次
    if arg[0] == 1:
        e2 = arg[1] - arg[2]
    # 第二次
    if arg[0] == 2:
        e1 = arg[1] - arg[2]
        Protocol_加热棒.BlockRead()
        v1 = Protocol_加热棒.加热棒输出电压.Value
        print '上一次电压'
        print v1
    # 两次以上
    if arg[0] > 2:
        V = VK(arg[2], arg[1], e1, e2) + v1
        print VK(arg[2], arg[1], e1, e2)
        print '本次电压'
        print V
        if V < 0:
            V = 0
        print
        VK(arg[2], arg[1], e1, e2)
        print v1
        show = []
        str = '设定温度为:%d,室温为：%f' % (arg[1], arg[2])
        show.append(str)
        str = '预期电压为:%f' % (V)
        show.append(str)
        show.append('界面室温显示是否正确?')
        passed = Manu.Check(show)
        e2 = e1
        e1 = arg[1] - arg[2]
        # 协议读，获取通道数据
        Protocol_加热棒.BlockRead()
        # 获取字段，当前电压，作为下一次的v(k-1)
        v1 = Protocol_加热棒.加热棒输出电压.Value


Standard_Test(Test)
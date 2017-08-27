def outer():
    print('out() first line')

    def iner():
        print('int() first line')

        def ininer():
            print('ininer() first line')

        print('ininer: ' + str(ininer))
        return ininer

    print('iner: ' + str(iner))
    return iner


iam = outer()  # 现在iam就是iner了

heis = iam()  # 现在heis就是ininer了

# 现在间接得到了嵌套函数
heis()
heis()
heis()




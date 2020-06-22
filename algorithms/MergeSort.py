def merge(arr):
    leng = len(arr)
    if leng <= 1:
        return arr
    else:
        c = merge(arr[0: leng // 2])
        d = merge(arr[leng // 2:])
        ci = 0
        di = 0
        cmax = len(c)
        dmax = len(d)
        b = []
        for i in range(leng):
            if ci < cmax and di < dmax:
                if c[ci] < d[di]:
                    b.append(c[ci])
                    ci += 1
                else:
                    b.append(d[di])
                    di += 1
        for i in range(ci, cmax):
            b.append(c[i])
        for i in range(di, dmax):
            b.append(d[i])
        return b

print(merge(['5', '4', '0', '3']))
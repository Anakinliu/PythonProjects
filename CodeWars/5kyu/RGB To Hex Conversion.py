"""
test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")
"""

def trans(color):
    res = ""
    if color > 255:
        res = "FF"
    elif color < 0:
        res = "00"
    else:
        res = str(hex(color)).upper()
        if len(res) == 3:
            res = "0" + res[-1]
        else:
            res = res[-2:]
    return res

def rgb(r, g, b):
    return trans(r) + trans(g) + trans(b)


# =======大神解法

def rgb2(r, g, b):
    round = lambda x: min(255, max(x, 0))
    #
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
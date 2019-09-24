def add(a, b):
    return a + b

def t():
    for r in range(4):
        yield r
        pass
    pass

g = t()

for n in [666, 666, 666, 100]:
    print(n)
    g = (add(n, i) for i in g)
    pass

print(list(g))

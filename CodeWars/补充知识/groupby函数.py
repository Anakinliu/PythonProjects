
#
# functools.reduce(function, iterable[, initializer])¶
# iterable: 可以看作更新几次值
# for element in it:
#     initializer = function(initializer, element)
# if initializer is given,
# for element in it:
#     initializer = function(initializer, element)
print(reduce(lambda s, _: "".join(f'{len(list(g))}{n}' for n, g in groupby(s)), range(2-1), "222"))
# BEGIN 相当于
def lam(s, _):
    return "".join(f'{len(list(g))}{n} 'for n, g in groupby(s))
s = "222"
for i in range(0):
    s = lam(s, i)
print(s)
# END

# groupby
for n, g in groupby("22245677889"):
    print(n)
    # print(type(g))
    print(list(g))
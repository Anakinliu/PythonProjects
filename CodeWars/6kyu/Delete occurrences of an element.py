# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
def delete_nth(order, max_e):
    # code here
    dict_count = dict()
    len_order = len(order)
    result = []
    for i in range(len_order):
        e = order[i]
        if dict_count.get(e) is None:
            dict_count[e] = 1
            result.append(e)
        else:
            dict_count[e] += 1
            if dict_count[e] <= max_e:
                result.append(e)
    # print(result)
    return result
    pass


# 逆向思维， 从结果list判断是否数量超过max_e
# list.count(e) 数一下e在list里出现了几次
def delete_nth2(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e:
            ans.append(o)
    return ans

# delete_nth([20,37,20,21], 1)
delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3)

# e = [1,2,3,4,5]
# for i in e:
#     if i == 2:
#         e.pop(1)
#     if i == 4:
#         e.pop(3)
#         e.co
# print(e)
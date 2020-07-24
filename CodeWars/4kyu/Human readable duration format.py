"""
以人类友好的方式格式化持续时间（以秒为单位）。
该函数必须接受一个非负整数。
如果为零，则仅返回“ now”。
否则，持续时间表示为years, days, hours, minutes and seconds的组合。

例子：
format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

一年是365天，一天是24小时。
注意空格符
结果表达式由4秒钟，1年等组成。通常，一个正整数和一个有效的时间单位之一，以空格分隔。
如果整数大于1，则使用多个时间单位。组件之间用逗号和空格（“，”）分隔，除了最后一个用“and”分隔的部分，就像用英语书写一样。
比最不重要的时间单位要早得多的时间单位: 因此，1 second and 1 year 是不正确的，但 1 year and 1 second 是。
不同的组件具有不同的时间单位。
因此，没有像 5 seconds and 1 second 这样的重复单元。
如果组件的值恰好为零，则根本不会出现。
因此，1 minute 0 second 无效，应该是 1 minute。

必须“尽可能”使用一个时间单位。
这意味着该函数不应返回61 seconds，而应返回1 minute and 1 second。
正式地，组件指定的持续时间不得大于任何有效的更重要的时间单位。
1 min = 60 seconds
1 hour = 60 minutes
1 day = 24 hours
1 year = 365 days

"""

def solution(seconds):
    """
    :param seconds: >=0 整数
    :return: 人类友好的读数
    """
    if seconds == 0:
        return 'now'
    units = ['year', 'day', 'hour', 'minute', 'second']
    times = [1, 60, 60 * 60, 60 * 60 * 24, 60 * 60 * 24 * 365]
    # print(times)
    count = []
    n = seconds
    for i in times[::-1]:
        count.append(n // i)
        n = n % i
    # print(count)
    res = []
    for idx, e in enumerate(count):
        # print(e, idx)
        if e != 0:
            if e == 1:
                res.append(f'1 {units[idx]}')
            else:
                res.append(f'{e} {units[idx]}s')
            # if i + 2 < len(count) and count[i+1] != 0 and :
    # print(res)
    # if 判断写进 return 里
    return ', '.join(res[:-1]) + ' and ' + res[-1] if len(res) > 1 else res[0]
    # res_len = len(res)
    # if res_len == 1:
    #     print(res[0])
    #     return res[0]
    # elif res_len == 2:
    #     # print(' and '.join(res))
    #     return ' and '.join(res)
    # else:
    #     print(', '.join(res[:-1]) + ' and ' + res[-1])
    #     return ', '.join(res[:-1]) + ' and ' + res[-1]


"""
daddepledge, Cod3r, capsheafer, jdifjdf, Ocelotl_Fer, Decimo (plus 28 more warriors)

"""
times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    # 这种混杂的结构命名使用 chunks 数据块
    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:  # 非 0
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

solution(1)
solution(62)
solution(120)
solution(3600)
solution(3662)
solution(31539662)
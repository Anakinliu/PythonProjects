"""
完美代价：
给定字符串，返回变换为回文字符串的最小步骤
"""
def to_solve(s, n):
    j = n - 1
    cnt = 0
    flag = 0
    i = 0
    while i < j:
        for k in range(j, i - 1, -1):
            if k == i:
                # 字符串长度为偶数并且存在一个单独的字符时，Impossible
                # 字符串长度为奇数时，flag为1又出现一次，两种字符出现1次，Impossible
                if n % 2 == 0 or flag == 1:
                    return "Impossible"
                flag = 1
                cnt += n // 2 - i  # 将来要放在中间的字符
                # s.insert(n // 2, s.pop(k))
            elif s[k] == s[i]:
                cnt += j - k
                s.insert(j, s.pop(k))
                j -= 1
                break
        i += 1
    print(cnt)
    return cnt


s = list("twsstaa")
n = 7
to_solve(s, n)

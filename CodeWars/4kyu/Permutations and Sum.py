"""
Given a number N less than 10000, calculate total number of permutations of it and also the sum of all permutations including that number itself.
For example, let us take N to be 12. There exists 2 permutations of that number '12' and '21'. Sum of these two permutations is 33. So output will be 2 33.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
The first line of each Test case contains a positive number N.

Output:
Output in a single line the number of distinct permutations of that number and the  sum of all permutations of that number including that number separated by space .

Constraints:
1 <= T <= 1000
1 < N <= 10000

Example:
Input:
2
5
12
Output:
1 5
2 33
"""

"""
输入n，输出n的全排列个数和他们的和
"""

def d(n, left, right):
    if left == right:
        print(n)
    else:
        for i in range(left, right):
            n[left], n[i] = n[i], n[left]
            d(n, left+1, right)
            n[left], n[i] = n[i], n[left]

def solution(n):
    n = str(n)
    length = len(n)
    count = 1
    for i in range(length, 0, -1):
        count *= i
    print(count)
    d(n, 0, length)
    pass

# solution(404)
d(['a', 'b', 'c'], 0, 3)
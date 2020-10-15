"""
总共有 numCourses 个课程需要选，标签从 0 到 numCourses-1
某些课程可能具有先决条件，
例如，要学习课程0，您必须首先学习课程1，该课程以一对表示：[0,1]
给定课程总数和先决条件对列表，您是否可以完成所有课程？
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

约束：
输入的先决条件是由边组成的列表而不是邻接矩阵表示的图。
阅读有关图表示方式的更多信息。
您可以假设输入的先决条件中没有重复的边。
1 <= numCourses <= 10 ^ 5, 0 <= 课程lebel < 10 ^ 5
"""


def solution(numCourses, prerequisites):
    labels = [0] * (10 ** 5)
    for idx in prerequisites:
        labels[idx[0]] += 1
        labels[idx[1]] += 1
    # print(labels)
    if max(labels) <= 1 and labels.count(1) <= numCourses:
        return True
    else:
        return False

print(solution(1, []))


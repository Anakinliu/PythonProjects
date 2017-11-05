# 宽度优先

__author__ = 'ysc'
import numpy as np


class State:
    def __init__(self, state, direction_flag=None, parent=None):
        self.state = state
        # state 是一个含有三个元素的numpy.array类型, 每个元素是一个列表, 列表代表一行三个元素
        self.direction = ['up', 'down', 'right', 'left']  # 可以移动的位置标志
        # 如果当前表是由 symbol move left 得到, 那么就删除right
        if direction_flag:
            # 保留可用的方向
            self.direction.remove(direction_flag)
        self.parent = parent
        self.symbol = ' '

    # def get_direction(self):
    #     return self.direction

    def show_info(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i, j], end='  ')
            print("\n")
        print('\->')
        return

    # 得到空白格的位置
    def get_empty_pos(self):
        position = np.where(self.state == self.symbol)
        return position

    # 生产当前状态的可用子状态
    def generate_substates(self):
        if not self.direction:
            return []
        sub_states = []
        boarder = len(self.state) - 1  # boarder = 2
        row, col = self.get_empty_pos()
        # print("the symbol index : " + "row: " + str(row) + ", " + "col: " + str(col))
        if 'left' in self.direction and col > 0:
            # thw symbol can move to left
            s = self.state.copy()
            s[row, col] = s[row, col - 1]
            s[row, col - 1] = self.symbol
            # news保存一位后方向状态, 避免再移回去的情况
            news = State(s, direction_flag='right', parent=self)
            sub_states.append(news)
        if 'up' in self.direction and row > 0:
            # thw symbol can move to upper place
            s = self.state.copy()
            s[row, col] = s[row - 1, col]
            s[row - 1, col] = self.symbol
            news = State(s, direction_flag='down', parent=self)
            sub_states.append(news)
        if 'down' in self.direction and row < boarder:
            # thw symbol can move to down place
            s = self.state.copy()
            s[row, col] = s[row + 1, col]
            s[row + 1, col] = self.symbol
            news = State(s, direction_flag='up', parent=self)
            sub_states.append(news)
        if self.direction.count('right') and col < boarder:
            # the symbol can move to right place
            s = self.state.copy()
            s[row, col] = s[row, col + 1]
            s[row, col + 1] = self.symbol
            news = State(s, direction_flag='left', parent=self)
            sub_states.append(news)
        return sub_states

    def solve(self):
        # 空的open table
        open_table = []
        # 空的close table
        close_table = []
        # 将初始节点加入open table
        open_table.append(self)
        steps = 0
        # start the loop
        print("-----start search------")
        while len(open_table) > 0:
            n = open_table.pop(0)  # 从openTable弹出第一个并删除， 弹出放到closeTable, 下次搜索使用
            print(n.state, end='\n==' + str(steps) + '==\n')

            # 如果n已经在close table 中, 跳过, 利用close table, 不能让close table废了
            if self.check_close_table(close_table, n):
                continue
            else:
                print("")  # 提示信息中也有换行, 保持格式一致

            close_table.append(n)
            # if not sub_states:
            #     break

            # 迭代生产的子表, 检查是否是目标答案, 因为子状态中的任何一个都可视为下一次搜索目标
            # for s in sub_states:
            #     steps += 1  # 当前搜索总的步数 +1
            #     print(s.state, end='\n==' + str(steps) + '==\n')
            #     if (s.state == s.answer).all():
            #         # print("how many times? ")
            #         # 循环到原始节点，更新路径，直到s的父节点是初始节点，
            #         while s and s != originState:
            #             path.append(s.parent)
            #             s = s.parent
            #         path.reverse()  # 反转路径
            #         return [path, steps + 1]
            path = []  #
            steps += 1  # 当前搜索总的步数 +1
            if (n.state == n.answer).all():
                # print("how many times? ")
                # 循环到原始节点，更新路径，直到s的父节点是初始节点，
                while n and n != originState:
                    path.append(n.parent)
                    n = n.parent
                path.reverse()  # 反转路径
                return [path, steps]

            sub_states = n.generate_substates()  # 生成子状态
            open_table.extend(sub_states)  # 保存这些子节点, extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
            # steps += 1  # 当前搜索总的步数
        else:
            return [None, None]

    @staticmethod
    def check_close_table(close_table, n):
        """
        查找n是否在close table 中, 在, 返回True
        """
        # 如果n已经在close table 中, 跳过
        n_in_close = False
        for m in close_table:
            if (m.state == n.state).all():
                print("!!!!!!!!!!当前状态已在close table 中, 跳过!!!!!!!!!!!!!!\n\n")
                n_in_close = True
        return n_in_close


# 从其他模块运行则会跳过的代码
if __name__ == '__main__':
    # 设置空位置的字符
    symbolOfEmpty = ' '
    State.symbol = symbolOfEmpty

    # 问题的初始状态
    originState = State(np.array([[2, 8, 3], [1, symbolOfEmpty, 4], [7, 6, 5]]))  # numpy模块的array方法使数组运算更灵活
    # 一个可解的目标答案
    State.answer = np.array([[7, 8, 4], [2, 3, 1], [symbolOfEmpty, 6, 5]])

    # s1 = State(state=originState.state)
    path, steps = originState.solve()

    print("-----end search------")
    if path:  # if find the solution
        print("the path is :")
        for node in path:
            # print the path from the origin to final state
            node.show_info()
        print(State.answer)
        print("Total steps is %d" % steps)

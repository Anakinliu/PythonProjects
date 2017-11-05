__author__ = 'ysc'
import numpy as np


class State:
    def __init__(self, state, direction_flag=None, parent=None, depth=1):
        self.state = state
        # state is a numpy.array with a shape(3,3) to storage the state
        self.direction = ['up', 'down', 'right', 'left']
        if direction_flag:
            self.direction.remove(direction_flag)
            # record the possible directions to generate the sub-states
        self.parent = parent
        self.symbol = ' '
        self.answer = np.array([[1, 2, 3], [8, State.symbol, 4], [7, 6, 5]])
        self.depth = depth
        # calculate the num of elements which are not in the proper position
        num = 0
        for i in range(len(state)):
            for j in range(len(state)):
                if self.state[i, j] != ' ' and self.state[i, j] != self.answer[i, j]:
                    num += 1
        self.cost = num + self.depth

    def get_direction(self):
        return self.direction

    def show_info(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i, j], end='  ')
            print("\n")
        print('->')
        return

    def get_empty_pos(self):
        postion = np.where(self.state == self.symbol)
        return postion

    def generate_sub_states(self):
        if not self.direction:
            return []
        sub_states = []
        boarder = len(self.state) - 1  # boarder = 2
        # the maximum of the x,y
        row, col = self.get_empty_pos()
        if 'left' in self.direction and col > 0:
            # it can move to left place
            s = self.state.copy()
            s[row, col] = s[row, col - 1]
            s[row, col - 1] = self.symbol
            news = State(s, direction_flag='right', parent=self, depth=self.depth + 1)
            sub_states.append(news)
        if 'up' in self.direction and row > 0:
            # it can move to upper place
            s = self.state.copy()
            s[row, col] = s[row - 1, col]
            s[row - 1, col] = self.symbol
            news = State(s, direction_flag='down', parent=self, depth=self.depth + 1)
            sub_states.append(news)
        if 'down' in self.direction and row < boarder:
            # it can move to down place
            s = self.state.copy()
            s[row, col] = s[row + 1, col]
            s[row + 1, col] = self.symbol
            news = State(s, direction_flag='up', parent=self, depth=self.depth + 1)
            sub_states.append(news)
        if self.direction.count('right') and col < boarder:
            # it can move to right place
            s = self.state.copy()
            s[row, col] = s[row, col + 1]
            s[row, col + 1] = self.symbol
            news = State(s, direction_flag='left', parent=self, depth=self.depth + 1)
            sub_states.append(news)
        return sub_states

    def solve(self):
        # generate a empty open_table
        open_table = []
        # generate a empty close_table
        close_table = []
        # append the origin state to the open_table
        open_table.append(self)
        # denote the steps it travels
        steps = 0
        while len(open_table) > 0:  # start the loop
            n = open_table.pop(0)
            print(n.state, end='\ncost: ' + str(n.cost) + '\n\n')
            close_table.append(n)
            sub_states = n.generate_sub_states()
            path = []
            steps += 1  # 当前搜索总的步数 +1
            if (n.state == n.answer).all():
                # print("how many times? ")
                # 循环到原始节点，更新路径，直到s的父节点是初始节点，
                while n and n.parent and n != originState:
                    path.append(n.parent)
                    n = n.parent
                path.reverse()  # 反转路径
                return [path, steps]

            open_table.extend(sub_states)
            # 按照cost值升序排序openTable中的元素
            open_table.sort(key=lambda x: x.cost)
        # steps += 1
        else:
            return None, None


if __name__ == '__main__':
    # the symbol representing the empty place
    symbolOfEmpty = ' '
    # you can change the symbol at here
    State.symbol = symbolOfEmpty
    # set the origin state of the puzzle
    originState = State(np.array([[2, 8, 3], [1, 6, 4], [7, symbolOfEmpty, 5]]))
    State.answer = np.array([[1, 2, 3], [8, State.symbol, 4], [7, 6, 5]])
    s1 = State(state=originState.state)
    path, steps = s1.solve()
    if path:
        print("the path is :")  # if find the solution
        for node in path:
            # print the path from the origin to final state
            node.show_info()
        print(State.answer)
        print("Total steps is %d" % steps)
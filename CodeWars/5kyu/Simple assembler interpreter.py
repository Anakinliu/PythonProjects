"""
https://www.codewars.com/kata/58e24788e24ddee28e000053
"""
"""
mov x y 赋值y到x中其中y可以是常量或者寄存器
inc x 使得寄存器x加1
dec x 与inc x相反
jnz x y 跳转到一条指令y位置（正数表示正向，负数表示向后），但仅当x（常数或寄存器）不为零时

寄存器名只包含字母，常量只包含整数
jnz是相对位置

该函数将获取带有程序指令序列的输入列表，并将返回包含寄存器内容的字典。
同样，寄存器上的每个inc / dec / jnz都将始终先在其上移动，因此您不必担心未初始化的寄存器。
"""

"""
simple_assembler(['mov a 5','inc a','dec a','dec a','jnz a -1','inc a'])

''' visualized:
mov a 5
inc a
dec a
dec a
jnz a -1
inc a
'''

The above code will:

set register a to 5,
increase its value by 1,
decrease its value by 2,
then decrease its value until it is zero (jnz a -1 jumps to the previous instruction if a is not zero)
and then increase its value by 1, leaving register a at 1
So, the function should return

{'a': 1}
"""


def simple_assembler2(program):
    # return a dictionary with the registers
    print(program)
    registers = dict()

    ins_index = 0
    while ins_index < len(program):
        state = program[ins_index]
        state_list = state.split()
        if state_list[0] == 'mov':
            if state_list[2].isalpha():
                registers[state_list[1]] = registers[state_list[2]]
            else:
                registers[state_list[1]] = int(state_list[2])
        if state_list[0] == 'inc':
            registers[state_list[1]] += 1
        if state_list[0] == 'dec':
            registers[state_list[1]] -= 1

        if state_list[0] == 'jnz' and (
                (not state_list[1].isalpha() and state_list[1] != 0) or registers[state_list[1]] != 0):
            # print('ook')
            ins_index = ins_index + int(state_list[2])
        else:
            ins_index += 1
        # ins_index += 1
    return registers


# code = '''\
# mov a 5
# inc a
# dec a
# dec a
# jnz a -1
# inc a'''
code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
print(simple_assembler2(['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2']))


# {'a': 1}
# {'a': 409600, 'c': 409600, 'b': 409600}
# print('a'.isalpha())

def simple_assembler(program):
    d, i = {}, 0
    while i < len(program):
        # r: register
        cmd, r, v = (program[i] + ' 0').split()[:3]  # 加的这个 0 很厉害
        if cmd == 'inc':
            d[r] += 1
        if cmd == 'dec':
            d[r] -= 1
        if cmd == 'mov':
            d[r] = d[v] if v in d else int(v)
        if cmd == 'jnz' and (d[r] if r in d else int(r)):
            i += int(v) - 1
        i += 1
    return d

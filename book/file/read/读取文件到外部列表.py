file_list = []
with open(r'..\text_files\pi_digits.txt') as file_obj:
    file_list2 = file_obj.readlines()

with open(r'..\text_files\pi_digits.txt') as file_obj:
    for a_line in file_obj:
        file_list.append(a_line)

pi_str = ''
with open(r'..\text_files\pi_million_digits.txt') as file_obj:
    for a_str in file_obj:
        pi_str += a_str.strip()

print(file_list)
print(file_list2)
pi_str = pi_str.replace('1', '\ A /', )
# print(pi_str)

birthday = input("input your birthday: ")
if birthday in pi_str:
    print("IN!")
else:
    print("Not IN!")

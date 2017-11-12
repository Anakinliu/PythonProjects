with open(r'text_files\pi_digits.txt') as file_obj:
    for line in file_obj:
        print(line.rstrip())
        print(line, end='')
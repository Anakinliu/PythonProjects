file_path = r'..\text_files\pi_digits.txt'
try:
    with open(file_path) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    msg = "sorry, file " + file_path + "does not exist!"
    print(msg)
else:
    print(contents, end='')
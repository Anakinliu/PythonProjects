file_name = r'..\text_files\s_empty.txt'
with open(file_name, 'w') as file_obj:
    file_obj.write("I LOVE programming!\n")
    file_obj.write(str(233))

with open(file_name, 'a') as file_obj:
    file_obj.write("\nappend......\n")

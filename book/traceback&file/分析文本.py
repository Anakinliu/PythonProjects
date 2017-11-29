def count_about_words(file_path):
    # split分割字符串

    try:
        with open(file_path) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        msg = "sorry, the " + file_path + " doesn't exist"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("this file " + file_path + " has about " + str(num_words) + " words.")


file_path = r"..\file\text_files\from_gutenbreg.txt"
count_about_words(file_path)
"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""
def pig_it(text):
    text = str(text)
    text_lst = text.split()
    res_lst = []
    for word in text_lst:
        if word.isalpha():
            res_lst.append(word[1:] + word[0] + 'ay')
        else:
            res_lst.append(word)
    result = ' '.join(res_lst)
    print(result)
    pass

pig_it('Hello world !')
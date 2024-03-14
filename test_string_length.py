def compare_word(word):
    """Test if length of word is equal to 5"""
    word_len = len(word)
    if word_len == 5:
        print("word length is 5 characters")
    elif word_len < 5:
        print("word length is less than 5 characters")
    else:
        print("Word length is more than 5 characters")



word = input("Please enter a word: ")
compare_word(word)

print("Hello World")

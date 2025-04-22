def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def counting_characters(text):
    char_count={}
    uncap_text = text.lower()
    for letter in uncap_text:
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count           
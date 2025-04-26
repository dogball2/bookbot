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

def chars_dict_to_sorted_list(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char":char, "count":count})
    def sort_on(dict):
        return dict["count"]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
import sys
def check_book():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words
from stats import counting_characters
from stats import chars_dict_to_sorted_list

def main():
    check_book()
    text = get_book_text(sys.argv[1])
    word_count = get_num_words(text)
    count = counting_characters(text)
    sorted_list = chars_dict_to_sorted_list(count)
    sorted_alpha = []
    for item in sorted_list:
        if item["char"].isalpha():
            sorted_alpha.append(item)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print(f"--------- Character Count -------")
    for item in sorted_alpha:
        print(f"{item['char']}: {item['count']}")
        
    print("============= END ===============")

main()
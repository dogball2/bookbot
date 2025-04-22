def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words
from stats import counting_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(text)
    count = counting_characters(text)
    print(f"{word_count} words found in the document")
    print(count)

main()
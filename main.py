import sys
from stats import get_num_words, get_num_chars, get_sorted_dics

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    book = sys.argv[1]
    file_content = get_book_text(book)
    num_words = get_num_words(file_content)
    print("============ BOOKBOT ============\n"
        f"Analyzing book found at {book}...\n"
        "----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    dic_chars = get_num_chars(file_content)
    #print(dic_chars)

    unsorted = get_sorted_dics(dic_chars)

    for e in unsorted:
        print(f"{e["char"]}: {e["num"]}")


main()
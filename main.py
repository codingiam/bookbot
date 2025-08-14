import sys

from stats import characters_list, get_num_words, count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    print("----------- Word Count ----------")
    nws = get_num_words(text)
    print(f"Found {nws} total words")

    print("--------- Character Count -------")
    ccs = count_characters(text)
    lst = characters_list(ccs)
    for li in lst:
        c = li["char"]
        if c.isalpha():
            print(f"{c}: {li['num']}")

main()

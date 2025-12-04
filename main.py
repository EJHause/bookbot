import sys
from stats import count_words, char_count, sort_char_counts

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    #Check for command-line argument

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    #Word count
    num_words = count_words(book_text)

    # Character count
    char_counts = char_count(book_text)

    #Sorted character counts
    sorted_counts = sort_char_counts(char_counts)

    #Report output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath} ...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")

    for item in sorted_counts:
          print(f"{item['char']}: {item['num']}")

    print("============= END =============")

if __name__ == "__main__":
	main()


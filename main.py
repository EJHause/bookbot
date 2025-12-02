def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

from stats import count_words

from stats import char_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    # Character count
    char_counts = char_count(book_text)
    print(char_counts)

if __name__ == "__main__":
	main()


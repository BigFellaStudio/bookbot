from stats import count_words, count_characters
import sys

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    number_of_characters = count_characters(text)
    
    # # Generate Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    generate_report(text)
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def generate_report(text):
    char_dict = count_characters(text)

    for c in char_dict:
        if c.isalpha():
            print(f"{c}: {char_dict[c]}")

main()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    number_of_characters = count_characters(text)
    
    # Generate Report
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print()
    generate_report(text)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(string):
    number = len(string.split())
    return number

def count_characters(string):
    characters = {}
    lowered_string = string.lower()
    
    for c in lowered_string:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    
    return characters

def generate_report(text):
    char_dict = count_characters(text)

    for c in char_dict:
        if c.isalpha():
            print(f"The '{c}' character was found {char_dict[c]} times")

main()
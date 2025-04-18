from stats import get_num_words

file_path = "books/frankenstein.txt"

def main():
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    print (f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        book = f.read()
    return book


    
main()
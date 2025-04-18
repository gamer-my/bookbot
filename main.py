file_path = "books/frankenstein.txt"

def main():
    text = get_book_text(file_path)
    num_words = words_count(text)
    print (f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        book = f.read()
    return book

def words_count(book):
    words_array = book.split()
    count = len(words_array)
    return count
    
main()
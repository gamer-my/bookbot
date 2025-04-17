file_path = "books/frankenstein.txt"

def main():
    get_book_text(file_path)

def get_book_text(path):
    with open(path) as f:
        book = f.read()
    print(book)
    
    
main()
from stats import get_num_words
from stats import char_count

file_path = "books/frankenstein.txt"

def main():
    #print word count
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    #print letter count
    lt_count = char_count(text)
    print(lt_count)
    

def get_book_text(path):
    with open(path) as f:
        book = f.read()
    return book


    
main()
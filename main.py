from stats import get_num_words
from stats import char_count
from stats import dic_sort

file_path = "books/frankenstein.txt"

def main():
    #print top line
    print("============ BOOKBOT ============")
    #print book file
    print(f"Analyzing book found at {file_path}")
    #print word count line
    print("----------- Word Count ----------")
    
    #print word count
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    #print Character  count line
    print("--------- Character Count -------")
    
    #print character count + sort
    lt_count = char_count(text)
    sort_lt_count = dic_sort(lt_count)
    for key, value in sort_lt_count.items():
        print(f"{key}: {value}")
        
        
def get_book_text(path):
    with open(path) as f:
        book = f.read()
    return book


    
main()
import sys
from stats import get_num_words, char_count, dic_sort

#file_path = "books/frankenstein.txt"

def main():
    #Wrong input exit
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    
    #print top line
    print("============ BOOKBOT ============")
    #print book file
    print(f"Analyzing book found at {file_path}")
    #print word count line
    print("----------- Word Count ----------")
    
    #print word count
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    
    #print Character  count line
    print("--------- Character Count -------")
    
    #print character count + sort
    lt_count = char_count(text)
    sort_lt_count = dic_sort(lt_count)
    for key, value in sort_lt_count.items():
        print(f"{key}: {value}")
        
    #print end line
    print("============= END ===============")

     
def get_book_text(path):
    with open(path) as f:
        book = f.read()
    return book


    
main()
def main():
    text = "hAllo piet qwwet"
    test = char_count(text)
    print (test)

def get_num_words(book):
    words_array = book.split()
    count = len(words_array)
    return count
    
def char_count(book):
    lower_text = book.lower()
    a = list(lower_text)
    counts = dict()
    for i in a:
        counts[i] = counts.get(i, 0) + 1
    return counts
    
def dic_sort(char_count):
    sort_dic = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    return sort_dic
    
#main()
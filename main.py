from stats import count_words, symbol_counter, listify
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_text = get_book_text(book)
    words_count = count_words(book_text)
    symbol_dict = symbol_counter(book_text)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------\nFound {words_count} total words")
    #for symbol in symbol_dict:
    #    print(f"'{symbol}': {symbol_dict[symbol]}")
    
    main_list = listify(symbol_dict)
    print("--------- Character Count -------")
    for dictionary in main_list:
        x, y = dictionary.items()
        print (f"{x[1]}: {y[1]}")



def get_book_text(book):
    with open(book) as b:
        return b.read()
    
main()
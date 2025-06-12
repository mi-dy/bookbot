from stats import count_words, symbol_counter

def main():
    book = "./books/frankenstein.txt"
    book_text = get_book_text(book)
    words_count = count_words(book_text)
    symbol_dict = symbol_counter(book_text)
    print(f"{words_count} words found in the document")
    for symbol in symbol_dict:
        print(f"'{symbol}': {symbol_dict[symbol]}")

def get_book_text(book):
    with open(book) as b:
        return b.read()
    
main()
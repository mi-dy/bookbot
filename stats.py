def count_words(book_text):
    words_list = book_text.split()
    i = 0
    for word in words_list:
        i += 1
    return i

def symbol_counter(book_text):
    main_dict = {}
    for symbol in book_text.lower():
        if symbol not in main_dict:
            main_dict[symbol] = 1
        elif symbol in main_dict:
            main_dict[symbol] += 1
    return main_dict

def listify(symbol_dict):
    main_list = []
    for symbol in symbol_dict:
        if symbol.isalpha():
            new_dict = {}
            new_dict["char"] = symbol
            new_dict["num"] = symbol_dict[symbol]
            main_list.append(new_dict)
    main_list.sort(reverse=True, key=sort_key)
    return main_list

def sort_key(dict):
    return dict["num"]
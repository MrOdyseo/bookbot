def word_count(get_book_text):
    count = 0
    words = get_book_text("books/frankenstein.txt").split()

    for word in words:
        count += 1
    
    return count

def chartacter_count(get_book_text):
    char_count = {}

    for char in get_book_text("books/frankenstein.txt").lower():
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

def sort_char(chars):
    sorted_chars = list(chars.items())
    sorted_chars.sort(key=lambda item: item[1], reverse=True)

    return sorted_chars


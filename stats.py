def get_book_text (file_path): 
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(book_path):
    count = 0
    words = get_book_text(book_path).split()

    for word in words:
        count += 1
    
    return count

def chartacter_count(book_path):
    char_count = {}

    for char in get_book_text(book_path).lower():
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

def sort_char(chars):
    sorted_chars = list(chars.items())
    sorted_chars.sort(key=lambda item: item[1], reverse=True)

    return sorted_chars


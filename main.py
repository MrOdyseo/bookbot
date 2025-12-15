from stats import word_count, chartacter_count, sort_char

def get_book_text (file_path): 
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():

    chars = chartacter_count(get_book_text)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text)} total words")
    print("--------- Character Count -------")

    for char, count in sort_char(chars):
        if char.isalpha():
            print(f"{char}: {count}")
        else:
            continue
        
    print("============= END ===============")

    
main()
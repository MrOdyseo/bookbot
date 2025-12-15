from stats import word_count, chartacter_count, sort_char, get_book_text
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_path)} total words")
    print("--------- Character Count -------")
    chars = chartacter_count(book_path)
    for char, count in sort_char(chars):
        if char.isalpha():
            print(f"{char}: {count}")
        else:
            continue
        
    print("============= END ===============")

main()
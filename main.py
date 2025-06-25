import sys

from stats import count_characters, count_words


def get_book_text(filepath: str) -> str:
    """Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(filepath, 'r') as f:
        return f.read()

def sort_characters(characters: dict[str, int]) -> list[tuple[str, int]]:
    """Sorts characters by their count in descending order.
    
    Args:
        characters (dict[str, int]): A dictionary with characters as keys and their counts as values.
        
    Returns:
        list[tuple[str, int]]: A sorted list of tuples containing characters and their counts.
    """
    return sorted(characters.items(), key=lambda item: item[1], reverse=True)

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = args[0]
    book = get_book_text(book_filepath)
    words_count = count_words(book)
    characters_count = count_characters(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for char, count in sort_characters(characters_count):
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

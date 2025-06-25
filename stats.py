def count_words(text: str) -> int:
    """Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    """Counts the occurrences of each character in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        dict[str, int]: A dictionary with characters as keys and their counts as values.
    """
    chars: dict[str, int] = {}
    for char in text:
        char = char.lower()
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars

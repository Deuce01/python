def is_palindrome(word):
    """
    Check if a given word is a palindrome.

    Parameters:
    - word (str): The word to be checked.

    Returns:
    - bool: True if the word is a palindrome, False otherwise.
    """
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

# Example usage:
if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")
    
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome!")
    else:
        print(f"{user_input} is not a palindrome.")

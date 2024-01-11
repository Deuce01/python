import random

def generate_random_mapping():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mapping = {char: random.randint(1, 100) for char in alphabet}
    mapping[' '] = 0  # Add space mapping
    return mapping

def text_to_numbers(text, mapping):
    number_text = ' '.join(str(mapping.get(char.lower(), ord(char))) for char in text)
    return number_text

def numbers_to_text(number_text, mapping):
    reversed_mapping = {v: k for k, v in mapping.items()}
    text = ''.join(reversed_mapping.get(int(num), chr(int(num))) for num in number_text.split())
    return text

if __name__ == "__main__":
    number_mapping = generate_random_mapping()

    while True:
        choice = input("Choose an option (e for encrypt, d for decrypt, q to quit): ").lower()

        if choice == 'e':
            input_text = input("Enter the text to encrypt: ")
            encrypted_text = text_to_numbers(input_text, number_mapping)
            print("\nEncrypted Text:")
            print(encrypted_text)

        elif choice == 'd':
            input_text = input("Enter the text to decrypt: ")
            decrypted_text = numbers_to_text(input_text, number_mapping)
            print("\nDecrypted Text:")
            print(decrypted_text)

        elif choice == 'q':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")

import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

word = random.choice(words)
guessed_letters = []
tries_left = 6

while tries_left > 0:
    display_word = ""
    
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(display_word)
    
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break
    
    guess = input("Guess a letter: ").lower()
    
    if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            tries_left -= 1
            print("Wrong guess! Tries left:", tries_left)
            if tries_left == 0:
                print("Game over! The word was:", word)
                break
            continue
    else:
        print("Invalid input! Please enter one letter.")
    
print("\nThanks for playing Hangman!")
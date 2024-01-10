import random

def fortune_teller():
    print("Welcome to the Fortune Teller!")
    user_name = input("What's your name? ")
    
    # List of humorous predictions
    predictions = [
        f"{user_name}, beware of falling coconuts tomorrow!",
        f"Good news, {user_name}! You'll find a hidden treasure soon.",
        f"{user_name}, avoid eating purple mushrooms today.",
        f"Expect the unexpected, {user_name}. Your pet rock might come to life!",
        f"Today is a great day to wear mismatched socks, {user_name}.",
        f"{user_name}, a talking parrot will give you valuable advice.",
        f"Beware of ninja squirrels, {user_name}!",
        f"{user_name}, your lucky number for today is {random.randint(1, 100)}.",
        f"{user_name}, you'll discover a new talent in interpretive dance.",
        f"Watch out for flying spaghetti monsters, {user_name}!",
    ]

    # Get a random prediction
    random_prediction = random.choice(predictions)

    print("\nHere's your fortune:")
    print(random_prediction)

if __name__ == "__main__":
    fortune_teller()


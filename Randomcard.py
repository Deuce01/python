# Import random module using the import keyword.
import random
# Give the first list of card values as static input say and store it in a variable.
card_points = ['A', 'K', 'Q', 'J', '2',
               '3', '4', '5', '6', '7', '8', '9', '10']
# Give the second list of card signs as static input and store it in another variable.
card_signs = ['Heart', 'CLUB', 'DIAMOND', 'SPADE']
# Apply random. choice() method for the first list to get the random item and
# store it in another variable.
randm_card = random.choice(card_points)
# Apply random. choice() method for the second list to get the random item and
# store it in another variable.
randm_sign = random.choice(card_signs)
# Get the random card by assigning both obtained random cards and store it in
# another variable.
rndm_crd = randm_card, randm_sign
# Print the random card from the deck of cards.
print("The random card from a deck of cards = ", rndm_crd)

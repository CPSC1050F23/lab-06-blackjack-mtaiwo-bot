"""
Author:         Folu Taiwo
Date:           10/5/23
Assignment:     Lab 06
Course:         CPSC1051
Lab Section:    003

CODE DESCRIPTION: 

"""

deck = [
    "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
    "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"
]
import random
#ask player for a seed
print("Give me a seed:")
seed = int(input())
random.seed(seed)

#ask for number of players
print("How many players would you like to play with?")
num_players = int(input())
if num_players < 0:
    print("Please enter a value greater than 0: ")
    num_players = int(input()) 

#function that creates the hands for each player and stores those hands
def create_and_store_hands():
    """
    Create hands for each player and store them.

    Parameters:
        deck (list): A list representing the deck of cards.
        num_players (int): The number of players.

    Returns:
        list: A list of lists, where each inner list represents a player's hand.
    """

  # Initialize hands for each player
    hand = []
    
    for i in range(2):
        index = random.randint(0, len(deck) - 1)
        hand.append(deck[index])
        del deck[index]
    
    return hand

hand = create_and_store_hands()

#function that gets card value
def card_value(card):
    """
    Get the value of a card.

    Parameters:
        card (str): The card's rank as a string.

    Returns:
        int: The value of the card.
    """
    rank = card[0]
    values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
        '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }
    return values[card['rank']]
card_value = card_value(card)
#Function that gets the sum of the cards in the user’s hand
def calculate_hand_sum(hand):
    hand_sum = 0
    num_aces = 0

    for card in hand:
        hand_sum = sum(get_card_value(card) for card in hand)
        num_aces = sum(1 for card in hand if card['rank'] == 'A')

    while num_aces > 0 and hand_sum > 21:
        hand_sum -= 10  # Convert Ace from 11 to 1
        num_aces -= 1

    return hand_sum


hand_value = calculate_hand_sum(hand)

#A function that checks if the user has busted or not.
def is_busted(player_hand):
    """
    Check if the player has busted.

    Parameters:
        hand_value (int): The total value of the player's hand.
        bust_limit (int): The maximum allowed hand value before busting.

    Returns:
        bool: True if the player has busted, False otherwise.
    """
    hand_sum = calculate_hand_sum(hand)
    return hand_sum > 21

#A function that deals two cards to the user from the deck given the current random seed.
def deal_two_cards(deck):
    """
    Deal two cards to the user from a deck using a random seed.

    Parameters:
        deck (list): A list representing the deck of cards.
        random_seed (int): An optional random seed for reproducibility.

    Returns:
        list: A list containing two cards drawn from the deck.
    """
    user_hand = [deck.pop(), deck.pop()]

    return user_hand

#A function that deals a card to a player when they decide to hit.
def deal_card_to_player(player_hand, deck):
    if len(deck) > 0:
        card = deck.pop()
        player_hand.append(card)
        return card

def display_player_hands(players_hands):
    """
    Display the cards in each player's hand.

    Parameters:
        players_hands (list): A list of lists, where each inner list represents a player's hand.

    Returns:
        None
    """
    for i, hand in enumerate(players_hands):
        print(f"Player {(i+1)}'s cards:")
        for card in hand:
            print(card)

def player_turn(deck, player_hand):
    for i in range(num_players):
        player_hand = player_hands[i]
        print(f"Player {i+1} would you like to hit or stick?")
        input = str(input()).strip().lower()
        if choice == "hit":
            deal_card_to_player(player_hand, deck)
        if is_busted(player_hand):
            print(f"Player {i+1} you have busted. Enter any key to acknowlege this.")
            key = input()
            break
        elif choice == "stick":
            break
        else:
            print("Invalid input. Please enter either hit or stick: ")


#print player x's cards
display_player_hands(players_hands)

for i in range(num_players):
    print(f"Acknowledge that you have seen your cards player {(i+1)}'s by entering any key.")
    user_input = input()

print("Now that everyone knows their cards, let's play!")

#ask player if they want to hit or stick
player_turn(deck, player_hand)

max_score = -1
winning_player = None
for i, player_hand in enumerate(player_hands):
    hand_sum = calculate_hand_sum(player_hand)
    if hand_sum <= 21 and hand_sum > max_score:
        max_score = hand_sum
        winning_player = i

print(f"Players X and Y tied for the highest score of N")

print(f"Player {winning_player+1} got the highest score of {max_score}.")

print("Nobody won.")


    

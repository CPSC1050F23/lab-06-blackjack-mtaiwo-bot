"""
Author:         Folu Taiwo
Date:           10/5/23
Assignment:     Lab 06
Course:         CPSC1051
Lab Section:    003

CODE DESCRIPTION: 

"""
def deal(deck):
    hand = []
    for i in range(2):
        index = random.randint(0, len(deck) - 1)
        hand.append(deck[index])
        del deck[index]
    return hand

def hit(deck, hand):
    index = random.randint(0, len(deck) - 1)
    hand.append(deck[index])
    del deck[index]
    return hand

def calculate_score(hand):
    score = 0
    num_aces = hand.count("A")
    
    for card in hand:
        if card[0].isdigit():
            if card[0] == "1":
                score += 10
            else:
                score += int(card[0])
        elif card[0] in ["J", "Q", "K"]:
            score += 10
        elif card[0] == "A":
            score += 11
        
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    
    return score

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
while num_players < 0:
    print("Please enter a value greater than 0: ")
    num_players = int(input()) 


player_hands = [deal(deck) for i in range(num_players)]

for i in range(num_players):
    print(f"Player {i + 1}'s cards: \n{player_hands[i]}")
    print(f"Acknowledge that you have seen your cards player {i + 1} by entering any key.")
    input().strip()
print("Now that everyone knows their cards, let's play!")

while True:
    for i in range(num_players): 
        print(f"Player {i + 1}'s cards: \n{player_hands[i]}")
        print(f"Player {i+1} would you like to hit or stick?")
        action = input().strip()

        if action.lower() == "hit":
            player_hands[i] = hit(deck, player_hands[i])
            print(f"Player {i + 1}'s cards: {player_hands[i]}")
            if calculate_score(player_hands[i]) > 21:
                print(f"Player {i + 1}'s cards: {player_hands[i]}")
                print(f"Player {i+1} you have busted. Enter any key to acknowlege this.")
                busted = input().strip()
                break
        elif action.lower() == "stick":
            break
        else:
            print("Invalid input. Please enter either hit or stick: ")
            action = input().strip()
    break
# Scores are stored in player_hands
max_score = 0
max_players = []
# Find out who busted
for i in range(len(player_hands)):
    if calculate_score(player_hands[i]) > max_score and calculate_score(player_hands[i]) > 2 and calculate_score(player_hands[i]) <= 21:
        max_score = calculate_score(player_hands[i])
    if calculate_score(player_hands[i]) > 21:
        print(f"Player {i + 1} has busted.")
    if calculate_score(player_hands[i]) == max_score:
        max_players.append(i)


if len(max_players) == 1:
    print(f"Player {max_players[0]} got the highest score of {max_score}.")
if len(max_players) > 1:
    print(f"Players {i} and {i+1} tied for the highest score of {max_score}")   
if len(max_players) == 0:
    print("Nobody won.")
    

#ask player if they want to hit or stick
#print(f"Player {i+1} would you like to hit or stick?")
#print("Invalid input. Please enter either hit or stick: ")


#print(f"Player {i+1} you have busted. Enter any key to acknowlege this.")

#print(f"Player {} has busted")
#print(f"Players X and Y tied for the highest score of N")

#print(f"Player {winner[0]} got the highest score of {max_score}.")

#print("Nobody won.")


    

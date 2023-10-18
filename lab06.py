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
        if card[-1] in ["J", "Q", "K"]:
            score += 10
        elif card[-1] == "A":
            score += 11
        else:
            score += int(card[:-1])
        
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
    print(f"Player {i + 1} hand: {player_hands[i]}")

for i in range(num_players):  
    while True:
        print(f"Player {i + 1} hand: {player_hands[i]}")
        print(f"Player {i+1} would you like to hit or stick?")
        action = input().strip()

        if action.lower() == "hit":
            card = hit(deck, hand)
            player_hands[i].append(card)  
            if calculate_score(player_hands[i]) > 21:
                print(f"Player {i+1} you have busted. Enter any key to acknowlege this.")
                busted = input(0).strip()
                break
        elif action.lower() == "stick":
            break
        else:
            print("Invalid input. Please enter either hit or stick: ")
    
    busted_players = []
    max_score = 0
    winners = []

    for i in range(num_players):
        score = calculate_score(player_hands[i])
        
        if score <= 21:
            if score > max_score:
                max_score = score
                winners = [i + 1]
            elif score == max_score:
                winners.append(i + 1)
        else:
            busted_players.append(i + 1)
        
    if busted_players:
        print(f"Player {', '.join(map(str, busted_players))} has busted")
    
    if winners:
        if len(winners) == 1:
            print(f"Player {winner[0]} got the highest score of {max_score}.")
        else:
            print(f"Players {' and '.join(map(str, winners))} tied for the highest score of {max_score}")
    
    if not winners and not busted_players:
        print("Nobody won.")

#print player x's cards
for i in range(num_players):
    print(f"Player {(i+1)}'s cards: {player_hands[i]}")
    print(f"Acknowledge that you have seen your cards player {(i+1)}'s by entering any key.")
    user_input = input()

print("Now that everyone knows their cards, let's play!")

#ask player if they want to hit or stick
#print(f"Player {i+1} would you like to hit or stick?")
#print("Invalid input. Please enter either hit or stick: ")


#print(f"Player {i+1} you have busted. Enter any key to acknowlege this.")

#print(f"Player {', '.join(map(str, busted_players))} has busted")
#print(f"Players X and Y tied for the highest score of N")

#print(f"Player {winner[0]} got the highest score of {max_score}.")

#print("Nobody won.")


    

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
    num_aces = 0
    # num_aces = hand.count("A")
    # print("num aces: ", num_aces)
    
    for card in hand:
        # print("card val: ", card[:-1])
        if card[:-1].isdigit():
            score += int(card[:-1])
        elif card[:-1] in "JQK":
            # print("foundJQK")
            score += 10
        elif card[:-1] == "A":
            # print("found A")
            score += 11
            num_aces += 1
        
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    
    #print("hand: ", hand)
    #print("score: ", score)
    return score

deck = [
    "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
    "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"
]

deck_values = {
    "AH":10, "2H":2, "3H": 3, "4H": 4, "5H":5, "6H":6, "7H":7, "8H":8, "9H":9, "10H":10, "JH":10, "QH":10, "KH":10,
    "AD":11, "2D":2, "3D":3, "4D":4, "5D":5, "6D":6, "7D":7, "8D":8, "9D":9, "10D":10, "JD":10, "QD":10, "KD":10,
    "AC":11, "2C":2, "3C":3, "4C":4, "5C":5, "6C":6, "7C":7, "8C":8, "9C":9, "10C":10, "JC":10, "QC":10, "KC":10,
    "AS":11, "2S":2, "3S":3, "4S":4, "5S":5, "6S":6, "7S":7, "8S":8, "9S":9, "10S":10, "JS":10, "QS":10, "KS":10
}
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

for i in range(num_players): 
    while True: 
        print(f"Player {i + 1}'s cards: \n{player_hands[i]}")
        print(f"Player {i+1} would you like to hit or stick?")
        action = input().strip()

        while action != "hit" and action != "Hit" and action != "stick" and action != "Stick":
            print("Invalid input. Please enter either hit or stick: ")
            action = input().strip()

        if action == "hit" or action == "Hit":
            player_hands[i] = hit(deck, player_hands[i])
            if calculate_score(player_hands[i]) > 21:
                print(f"Player {i + 1}'s cards: {player_hands[i]}")
                print(f"Player {i+1} you have busted. Enter any key to acknowledge this.")
                busted = input().strip()
                break 
        elif action == "stick" or action == "Stick":
            break

# Scores are stored in player_hands
max_score = 0
max_players = []
# Find out who busted
for i in range(len(player_hands)):
    players_score = calculate_score(player_hands[i])
    #print(f"Player {i + 1}'s score: {players_score}.")
    if players_score > max_score and players_score > 2 and players_score <= 21:
        max_score = players_score
        # max_players.append(i)
    if players_score > 21:
        print(f"Player {i + 1} has busted.")
    # if players_score == max_score:
        # max_players.append(i)

for i in range(len(player_hands)):
    players_score = calculate_score(player_hands[i])
    if players_score == max_score:
        max_players.append(i+1)

if len(max_players) == 1:
    print(f"Player {max_players[0]} got the highest score of {max_score}.")
elif len(max_players) > 1:
    print(f"Players {max_players[0]} and {max_players[1]} tied for the highest score of {max_score}")   
elif len(max_players) == 0:
    print("Nobody won.")


#ask player if they want to hit or stick
#print(f"Player {i+1} would you like to hit or stick?")
#print("Invalid input. Please enter either hit or stick: ")


#print(f"Player {i+1} you have busted. Enter any key to acknowlege this.")

#print(f"Player {} has busted")
#print(f"Players X and Y tied for the highest score of N")

#print(f"Player {winner[0]} got the highest score of {max_score}.")

#print("Nobody won.")


    

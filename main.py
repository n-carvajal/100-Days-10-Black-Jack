# Imports
from random import choice
from cards import deck


# Functions
def deal_card():
    """
    Issues a random card to a player X.
    """
    card = choice(list(deck))
    value = deck[card]
    return card, value


def score_check(x_hand, x_score, x_ace_reductions):
    """
    Checks a hand for presence of As.
    If present and over 21 subtracts 10 from score.
    """
    if "A" in x_hand:
        for card in range(0, x_hand.count("A")):
            if x_score > 21 and x_ace_reductions < x_hand.count("A"):
                x_score -= 10
                x_ace_reductions += 1
    return x_hand, x_score, x_ace_reductions


# Welcome
print("Welcome to 21 Black Jack\n")
# Get username:
player = input("What is your name: ")
print(f"{player}, would you like to play some 21 Black Jack?")
game_replay = True
while game_replay:
    replay = input("\nType 'Yes' or 'No': ").lower()
    if replay == "yes":
        print("\n" * 20)
        player_hand = []
        house_hand = []
        player_score = 0
        house_score = 0
        player_ace_reductions = 0
        house_ace_reductions = 0
        game_over = False
        # Issue first two cards to player 1 show both:
        for i in range(2):
            random_card, random_value = deal_card()
            player_hand.append(random_card)
            player_score += random_value
        player_hand, player_score, player_ace_reductions = score_check(player_hand, player_score, player_ace_reductions)
        print(f"\n{player} your hand is {player_hand}")
        print(f"Your hand score is {player_score}")
        # Issue first two cards to house show only first:
        for i in range(2):
            random_card, random_value = deal_card()
            house_hand.append(random_card)
            house_score += random_value
        house_hand, house_score, house_ace_reductions = score_check(house_hand, house_score, house_ace_reductions)
        print(f"\nThe house has {house_hand[0]}")
        # print(f"\nThe house has {house_hand}") --------- Testing
        # print(f"The house hand score is {house_score}") --------- Testing
        # While loop for game over:
        game_over = False
        while not game_over:
            if len(player_hand) == 2 and player_score == 21:
                print("Black Jack")
                print("You win.")
                game_over = True
            # Ask player if another card and issue if yes.
            else:
                new_card = input("\nWould you like another card: ").lower()
                if new_card == 'yes':
                    random_card, random_value = deal_card()
                    player_hand.append(random_card)
                    player_score += random_value
                    player_hand, player_score, player_ace_reductions = score_check(player_hand, player_score,
                                                                                   player_ace_reductions)
                    print(f"\n{player} your hand is now {player_hand}")
                    print(f"Your hand score is {player_score}")
                    print(f"\nThe house has {house_hand[0]}")
                    # print(f"The house hand score is {house_score}") --------- Testing
                    # If player score less than 22:
                    if player_score < 22:
                        continue
                    # If player score 22 or over.
                    else:
                        print("\nSorry you are bust.")
                        game_over = True
                # If player does not want additional cards:
                elif new_card == "no":
                    print("\nYou are sticking.")
                    print(f"\n{player} your hand is now {player_hand}")
                    print(f"Your hand score is {player_score}")
                    print(f"\nThe house has {house_hand}")
                    print(f"The house hand score is {house_score}")
                    # If house score is less than 17:
                    if house_score < 17:
                        # House issued extra card
                        random_card, random_value = deal_card()
                        house_hand.append(random_card)
                        house_score += random_value
                        house_hand, house_score, house_ace_reductions = score_check(house_hand, house_score,
                                                                                    house_ace_reductions)
                        print("\nThe house has less than 17 another card will be issued.")
                        print(f"\nThe house has {house_hand}")
                        print(f"\nThe house hand score is {house_score}")
                    # If house score 22 or over.
                    if house_score > 21:
                        print("\nHouse is BUST. You Win.")
                        game_over = True
                    # Else if player and house tied.
                    elif house_score == player_score:
                        print("\nIt's a tie.")
                        game_over = True
                    elif 21 - player_score < 21 - house_score:
                        print("\nYou win.")
                        game_over = True
                    # Else house wins.
                    else:
                        print("\nHouse wins.")
                        game_over = True
                else:
                    print("You did not type 'Yes' or 'No'.")
                    continue
        print("\nWould you like to play again?")
        continue
    elif replay == "no":
        game_replay = False
    else:
        print("Invalid input.")
print("\n" * 20)
print("\nGame Over")

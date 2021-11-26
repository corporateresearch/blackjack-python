from random import randint
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return cards[randint(0, 12)]

def calculate_score(cards):

    if cards == [11, 10] or cards == [10, 11]:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
    
def compare_scores(user_score, computer_score):
    if computer_score == user_score:
        return "THIS IS A DRAW"
    elif computer_score == 0:
        return "Dealer wins!"
    elif user_score == 0:
        return "You win!"
    elif user_score > 21:
        return "You lose"
    elif computer_score > 21:
        return "You win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"



def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(user_cards)

    while game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Current score: {user_score}")
        print(f"Dealer's card is {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_another_card = input("Press \"y\" to draw another and \"n\" to end the game.")
            if draw_another_card == "y":
                user_cards.append(deal_card())
                print(user_cards)
            else:
                game_over = True


    while computer_score != 0 and computer_score == 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Computer's score is {computer_score}")

    print(compare_scores(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type \"y\" or \"n\"") == 'y':
    clear()
    play_game()



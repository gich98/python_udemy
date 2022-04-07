import art
import random


def draw_user_card(cards_symbol, cards_value):
    first_card = random.choice(cards_symbol)
    second_card = random.choice(cards_symbol)
    first_card_value = cards_value[first_card]
    second_card_value = cards_value[second_card]
    return [first_card_value, second_card_value]


def draw_dealer_card(cards_symbol, cards_value):
    first_card = random.choice(cards_symbol)
    second_card = random.choice(cards_symbol)
    first_card_value = cards_value[first_card]
    second_card_value = cards_value[second_card]
    return [first_card_value, second_card_value]


def draw_card(cards_symbol, cards_value):
    another_card = random.choice(cards_symbol)
    return cards_value[another_card]


def sum_cards_value(cards_drawn):
    sum_cards = 0
    ace = 0
    for card in cards_drawn:
        if type(card) != list:
            sum_cards += card
        else:
            ace += 1
    for i in range(ace):
        temp_sum = sum_cards + 11
        if temp_sum > 21:
            sum_cards += 1
        else:
            sum_cards = temp_sum
    return sum_cards


cards_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_dict = {
    "1": [1, 11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
status_game = ""

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while play == "y":
    print(art.logo)
    user_cards = draw_user_card(cards_list, cards_dict)
    dealer_cards = draw_dealer_card(cards_list, cards_dict)

    user_score = sum_cards_value(user_cards)
    dealer_score = sum_cards_value(dealer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
    while draw_again == "y" and status_game != "Lose":
        user_cards.append(draw_card(cards_list, cards_dict))
        user_score = sum_cards_value(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if user_score > 21:
            status_game = "Lose"
        else:
            draw_again = input("Type 'y' to get another card, type 'n' to pass: ")

    if status_game != "Lose":
        if dealer_score < 17:
            dealer_cards.append(draw_card(cards_list, cards_dict))
            dealer_score = sum_cards_value(dealer_cards)

        print(f"Your final cards are {user_cards}, with a score of {user_score}")
        print(f"Computer's final cards are {dealer_cards}, with a score of {dealer_score}")
        if dealer_score > 21 or user_score > dealer_score:
            print("W")
        elif user_score == dealer_score:
            print("D")
        else:
            print("L")
    else:
        dealer_cards.append(draw_card(cards_list, cards_dict))
        dealer_score = sum_cards_value(dealer_cards)
        print("L")

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        user_cards = []
        user_score = 0
        dealer_cards = []
        dealer_score = 0


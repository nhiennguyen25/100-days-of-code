import random
import art

def deal_cards(deal_user_cards, deal_computer_cards):
    for card in range(deal_user_cards):
        player_cards.append(random.choice(cards))
    for card in range(deal_computer_cards):
        computer_cards.append(random.choice(cards))

def calculate_score(list_of_cards):
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    elif sum(list_of_cards) > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        return sum(list_of_cards)
    else:
        return sum(list_of_cards)

def print_cards():
    print(f"    Your cards: {player_cards}, current score: {calculate_score(player_cards)}\n"
          f"    Computer's first card: {computer_cards[0]}")

def compare():
    user_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    if user_score > 21:
        final_cards()
        print("You went over! You lose 😭")
    elif user_score == computer_score:
        final_cards()
        print("It's a draw 😜")
    elif user_score > computer_score or user_score == 21:
        final_cards()
        print("You win 🏆")
    elif computer_score > 21:
        final_cards()
        print("Opponent went over. You win! 😁")
    elif computer_score > user_score or computer_score == 21:
        final_cards()
        print("You lose 😔")

def final_cards():
    print(f"    Your final hand: {player_cards}, final score: {calculate_score(player_cards)}\n"
          f"    Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")

def play_Blackjack():
    player_cards.clear()
    computer_cards.clear()
    start_game = input("Do you wanna play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == "y":
        print("\n" * 20)
        print(art.logo)
        deal_cards(2,2)
        calculate_score(player_cards)
        calculate_score(computer_cards)
        print_cards()
        if calculate_score(player_cards) == 0:
            final_cards()
            print("You won with a Blackjack 😎")
            play_Blackjack()
        elif calculate_score(computer_cards) == 0:
            final_cards()
            print("You lose. Opponent won with a Blackjack 😭")
            play_Blackjack()
    elif start_game == "n":
        return

    draw_new_card = True
    while draw_new_card:
        next_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if next_card == "y":
            deal_cards(1,0)
            calculate_score(player_cards)
            calculate_score(computer_cards)
            print_cards()
            if calculate_score(player_cards) > 21:
                final_cards()
                print("You went over! You lose 😭")
                draw_new_card = False
                play_Blackjack()
        elif next_card == "n":
            draw_new_card = False
            give_computer_cards = True
            while give_computer_cards:
                if calculate_score(computer_cards) < 17:
                    deal_cards(0,1)
                else:
                    give_computer_cards = False
            compare()
            play_Blackjack()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

play_Blackjack()


# use recursion to reset the game. didn't work kept adding cards. do i need to put the lists in the function???


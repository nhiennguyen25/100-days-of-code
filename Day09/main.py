import art
print(art.logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidder = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}.")

bidders = {}
# highest_bidder = 0
# name_of_highest_bidder = ""
next_bidder = True

while next_bidder:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bidders[name] = price

    ask_more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n   ").lower()
    if ask_more_bidders == "no":
        next_bidder = False
        find_highest_bidder(bidding_dictionary = bidders)

        # for winner in bidders:
        #     if bidders[winner] > highest_bidder:
        #         highest_bidder = bidders[winner]
        #         name_of_highest_bidder = winner
        # print(f"The winner is {name_of_highest_bidder} with a bid of ${highest_bidder}.")

    elif ask_more_bidders == "yes":
        print("\n" * 20)


# my version of Todo-4
#     for winner in bidders:
#         if bidders[winner] > highest_bidder:
#             highest_bidder = bidders[winner]
#             name_of_highest_bidder = winner
#     print(f"The winner is {name_of_highest_bidder} with a bid of ${highest_bidder}.")

import random

deck = {
    "A♥": 11, "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7, "8♥": 8, "9♥": 9, "10♥": 10, "J♥": 10, "Q♥": 10, "K♥": 10,
    "A♦": 11, "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7, "8♦": 8, "9♦": 9, "10♦": 10, "J♦": 10, "Q♦": 10, "K♦": 10,
    "A♣": 11, "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7, "8♣": 8, "9♣": 9, "10♣": 10, "J♣": 10, "Q♣": 10, "K♣": 10,
    "A♠": 11, "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7, "8♠": 8, "9♠": 9, "10♠": 10, "J♠": 10, "Q♠": 10, "K♠": 10
}

game_over = False

def player_hit_me(hand, deck):
    
    # Draws a new card and adds it to the players hand.
    new_card = random.choice(list(deck.items()))
    player_hand.append((new_card))

    return print("Your card is: ", new_card)

def dealer_hit_me(hand, deck):
    
    # Draws a new card and adds it to the dealer hand.
    new_card = random.choice(list(deck.items()))
    dealer_hand.append((new_card))

    return print("Your card is: ", new_card)

def player_new_value(hand):

    player_hand_total = [] 

    # Loop through each tuple in the hand
    for card, value in hand:
        # Check if the value is an integer
        if isinstance(value, int):  
            # Add the value to the list
            player_hand_total.append(value)  

    player_hand_total = sum(player_hand_total) 

    return player_hand_total 

def dealer_new_value(hand):

    dealer_hand_total = []
    for card, value in hand:
        # Check if the value is an integer
        if isinstance(value, int):  
            # Add the value to the list
            dealer_hand_total.append(value)

    dealer_hand_total = sum(dealer_hand_total)

    return dealer_hand_total 

# Game loop
while game_over == False:
   
    print("---------------- Welcome to BlackJack ----------------\n")
    print("In this game you and the dealer will draw cards to hit the goal value of 21. \n")
    print("Whoever is closer to 21 without exceeding the value of 21 is the winner. \n")
    print("Let's start with your name and two cards drawn for you and two for the dealer. \n")

    player_name = input("Enter your name: \n")
    print("Welcome", player_name, "Here are your cards.")

    # Initialize player and dealer hands
    player_hand = []
    player_hand_total = []

    dealer_hand = []
    dealer_hand_total = []

    # Deal two cards to the player
    for card in range(2):
        player_card = random.choice(list(deck.items()))
        player_hand.append(player_card)

    for card, value in player_hand:
        # Check if the value is an integer if it is then add to player_hand_total
        if isinstance(value, int):
            player_hand_total.append(value) 

    print("Player hand: ", player_hand, "\n")
    print("Your hand value: ", sum(player_hand_total), "\n")

    # Deal two cards to the dealer
    for card in range(2):
        dealer_card = random.choice(list(deck.items()))
        dealer_hand.append(dealer_card)

    for card, value in dealer_hand:
        # Check if the value is a integer if it is then add to dealer_hand_total
        if isinstance(value, int):
            dealer_hand_total.append(value) 

    print("Dealer has two cards, one face up one face down. \n")
    print("Dealer faceup card: ", dealer_hand[1], "\n")
    print("Dealer faceup value: ", dealer_hand_total[1], "\n")

    player_choice = input("Hit or Stand? \n")

    # Player's Turn
    if player_choice.lower() == "hit":
        # Player hits
        player_hit_me(player_hand, deck)
        player_hand_total = player_new_value(player_hand)
        print("Player hand total: ", player_hand_total, "\n")

        # Check if the player busts
        if player_hand_total > 21:
            print("Player busts! Dealer wins.")
            game_over = True
    else:
        print("Player stands. Dealer's turn.")

    # Dealer's Turn (only if the player hasn't busted)

    # Dealer's Turn (only if the player hasn't busted)
if game_over == False:

    dealer_hand_total = sum(dealer_hand_total)

    while dealer_hand_total < 17:  # Dealer hits until total is at least 17
        dealer_hit_me(dealer_hand, deck)
        dealer_hand_total = dealer_new_value(dealer_hand)  # Update the total

        print("Dealer hand total: ", dealer_hand_total, "\n")

        # Check if the dealer busts
        if dealer_hand_total > 21:
            print("Dealer busts! Player wins.")
            game_over = True
            break

    # Compare totals if the dealer hasn't busted
    if game_over == False:
        print("Final Dealer hand total:", dealer_hand_total)
        print("Final Player hand total:", player_hand_total)

        if dealer_hand_total > player_hand_total:
            print("Dealer wins!")
        elif dealer_hand_total < player_hand_total:
            print("You win!")
        else:
            print("It's a tie!")

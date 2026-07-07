import random
import time


cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
deck = cards * 4
starting_chips = 500

# play welcome message and give the player their chips
def start_game():
    print("Welcome to blackjack!")
    player_chips = starting_chips
    return player_chips


# get score of a hand of cards, accounting for the value of face cards
def get_score(cards):
    
    score = 0
    aces = 0
    for c in cards: 
        if type(c) == int:
            score += c
        else:
            if c == 'K' or c == "Q" or c == "J":
                score += 10
            elif c == 'A':
                score += 11
                aces += 1
            else:
                score += int(c)
            # reduce the value of aces if the total score is over 21
        while score > 21 and aces:
            score -= 10
            aces -=1
    return score


# give the player a card and update their score, checking for bust or 21
def hit(player_cards):
    player_cards.append(random.choice(deck))
    print("You drew a " + str(player_cards[-1]))
    player_score = get_score(player_cards)

    if player_score > 21:
        print("You busted!")
    elif player_score == 21:
        print("21! You stand with a score of 21.")
    else:
        print("Your new score: " + str(player_score))

    return player_score


# reveal the dealer's hand, dealer draws until they have 17, decide winner.
def stand(player_score, dealer_cards, dealer_score, chips_used, player_chips):
    print("You stand with a score of " + str(player_score))
    print("The dealer's cards: " + str(dealer_cards))

    while dealer_score < 17:
        time.sleep(1)
        dealer_cards.append(random.choice(deck))
        dealer_score = get_score(dealer_cards)
        print("The dealer draws a " + str(dealer_cards[-1]))
        print("The dealer's score: " + str(dealer_score))

    if dealer_score > 21:
        print("The dealer busts! You win!")
        player_chips += chips_used * 2
    elif dealer_score == player_score:
        print("It's a tie!")
        player_chips += chips_used
    elif dealer_score > player_score:
        print("The dealer wins!")
    else:
        print("You win!")
        player_chips += chips_used * 2

    return player_chips



# main game loop, handles betting and player choices
def game_loop(player_chips):
    while True:
        print("You have " + str(player_chips) + " chips.")
        try:
            chips_used = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Please enter a number.")
            continue
        if chips_used <= 0:
            print("Please bet at least 1 chip.")
            continue
        if chips_used > player_chips:
            print("Sorry, that's too many chips.")
            continue
        else:
            player_chips -= chips_used
            break

    player_cards = random.sample(deck, 2)
    player_score = get_score(player_cards)
    dealer_cards = random.sample(deck, 2)
    dealer_score = get_score(dealer_cards)
    print("Your cards: " + str(player_cards))
    print("Your score: " + str(player_score))
    if player_score == 21:
        print("Blackjack!")
        player_chips += chips_used + int(chips_used * (3/2))
        return player_chips
    print("The dealer is showing " + str(dealer_cards[1]))
    while True:
        user_choice = input("Would you like to hit or stand? ")
        if user_choice == 'hit':
            player_score = hit(player_cards)
            if player_score > 21:
                break
            elif player_score == 21:
                player_chips = stand(player_score, dealer_cards, dealer_score, chips_used, player_chips)
                break
            else:
                continue
        elif user_choice == 'stand' or user_choice == 's':
            player_chips = stand(player_score, dealer_cards, dealer_score, chips_used, player_chips)
            break
        else:
            print("Please enter 'hit' or 'stand'.")
            continue
    return player_chips

# main, handle replay.
def main():
    player_chips = int(start_game())
    while True:
        player_chips = game_loop(player_chips)
        play_again = input("Would you like to play again? (y/n) ")
        if play_again != 'y':
            print("Thanks for playing!")
            break

main()

import random
print("\x1bc")
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return "Black Jack"
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You Lose! You called and went over 21"
    elif user_score == computer_score:
        return "It's a Draw!"
    elif user_score == 21 or user_score == 0:
        return "BLACK JACK! You win!"
    elif computer_score == 21 or computer_score == 0:
        return "You Lose! Dealer gets BLACK JACK!"
    elif user_score > 21:
        return "You Lose! You went over 21"
    elif computer_score > 21:
        return "You Win! Dealer's went over 21"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You Lose!"
def title():
    print("\x1bc")
    print(65*"=")
    print("\t   Welcome to Python's Simple Black Jack Game")
    print(65*"=")
    print("\t\t\t\t\t\t\tby: Mochi\n")
    return title
def play():
    title()
    user_cards = []
    computer_cards = []
    end_game = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not end_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        deal_var = f"\nDealer's cards\t: [ ]{computer_cards[1:6]}\n\n"
        print (deal_var)
        print(f"Your cards\t: {user_cards}\t\t Your score: {user_score}")
        if user_score >= 21 or computer_score >= 21:
            print("\n\t\t" + compare(user_score, computer_score))
            end_game = True
        else:
            should_deal = input("\nType [+] for more card, just press Enter to pass: ")
            if should_deal=="+":
                title()
                user_cards.append(deal_card())
                deal_var = computer_cards.append(deal_card())
                print (deal_var)
            else:
                end_game=True
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    title()
    #print("\n")
    
    print(f"\nDealer's cards\t: {computer_cards}\n\t\t\t\tDealer's score\t: {computer_score}\n")
    print(f"Your cards\t: {user_cards}\n\t\t\t\tYour score: {user_score}")
    print("\n\t" + compare(user_score, computer_score))
    

while input("\nEnter[007] as your password to play, or just press Enter to exit: ") == "007":
    play()

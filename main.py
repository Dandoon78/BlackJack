print("WELCOME TO BLACKJACK!")

import random

money = 1000
counter = 0

while counter == 0:
    blackjack1 = False
    print("------------------")
    print("You have $", money)
    
    bet = int(input("How much do you want to bet? "))
    print("------------------")

    while bet > money:
        print("You cannot bet more than what you have!")
        bet = int(input("How much do you want to bet? "))
        print("------------------")

    money = money - bet
    p1c1 = random.randint(2,11)
    p1c2 = random.randint(2,11)
    pcc1 = random.randint(2,11)
    pcc2 = random.randint(2,11)

    p1total = p1c1 + p1c2
    pctotal = pcc1 + pcc2

    print("You drew", p1c1, "and", p1c2)
    print("Your total is", p1total)
    print("------------------")

    print("The dealer has", pcc1, "and a hidden number")
    print("The total is hidden too")
    print("------------------")

    if p1total > 21:
        print("You Bust! The Dealer Wins!")
        print("You currently have $", money)
        
    elif p1total == 21 and (p1c1 == 10 or p1c1 == 11) and (p1c2 == 10 or p1c2 == 11):
        print("YOU GOT BLACKJACK!")
        blackjack1 = True

    else:
        hitstay = int(input("Hit or stay? (1 to hit or any other number to stay): "))

        while hitstay == 1: 
            hit = random.randint(2,11)
            p1total = p1total + hit
            print("You got", hit)
            print("Your new total is", p1total)
            print("------------------")

            if p1total > 21:
                print("You Bust! The Dealer Wins!")
                print("You currently have $", money)
                break
            else:
                hitstay = int(input("Hit or stay? (1 to hit or any other number to stay): "))

        else:
            while pctotal <= 16:
                print("------------------")
                print("The Dealer has a total of", pctotal)
                print("The Dealer chooses to hit!")
                hit = random.randint(2,11)
                pctotal = pctotal + hit
                print("The Dealer drew a", hit)
                
            else:

                if pctotal > 21:
                    print("The Dealer has a total of", pctotal)
                    print("The Dealer Busts! You Win!")
                    money = money + (bet * 1.5)
                    print("You currently have $", money)
                    
                    
                else:
                    if p1total > pctotal:
                        print("------------------")
                        print("The Dealer has a total of", pctotal)
                        print("CONGRATS YOU WON!")
                        money = money + (bet * 1.5)
                        print("You currently have $", money)

                        
                    elif p1total < pctotal:
                        print("------------------")
                        print("The Dealer has a total of", pctotal)
                        print("You Lost! The Dealer Wins")
                        print("You currently have $", money)
                        
                    else:
                        print("------------------")
                        print("The Dealer has a total of", pctotal)
                        print("ITS A TIE! The Dealer Wins")
                        print("You currently have $", money)
                        
    if pctotal == 21 and (pcc1 == 10 or pcc1 == 11) and (pcc2 == 10 or pcc2 == 11):
        print("The Dealer GOT BLACKJACK!")

        if blackjack1 == True:
            print("No money was gained or lost!")
            print("You currently have $", money)

        else:
            print("You lost!")
            print("You currently have $", money)

    elif blackjack1 == True:
        print("YOU WIN!")
        money = money + (bet * 1.5)
        print("You currently have $", money)

    else:
        pass
    
    if money != 0:
        print("------------------")
        again = input("Do you want to play again? (Press Q to quit) ")

        if again == "Q":
            print("------------------")
            print("THANKS FOR PLAYING!")
            counter = 1
        
        else:
            pass
    else:
        print("YOU RAN OUT OF MONEY!")
        print("------------------")
        print("THANKS FOR PLAYING!")
        counter = 1

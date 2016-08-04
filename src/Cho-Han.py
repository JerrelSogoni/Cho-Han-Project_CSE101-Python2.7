# CSE 101 Final Project Cho-Han - Jerrel Sogoni (109619783)
import random
def dieRange1(guess1):
    while(guess1 < 1 or guess1 > 6):
        print "Enter valid die number"
        guess1 = int(raw_input("Guess whats the die number of one of them (1-6) integer:\n"))
    return guess1
def dieRange2(guess2):
    while(guess2 < 1 or guess2 > 6):
        print "Enter valid die number"
        guess2 = int(raw_input("Guess whats the die number of one of them (1-6) integer:\n"))
    return guess2
def getbet(bet):
    while(bet <= 0):
        print "Please Enter Positive number(Not Zero you already commited in Gambling!)\nand must be less than the Bankroll Amount"
        bet = float(raw_input("Enter Your Bet:\n$"))
    return bet
def getMoney(money):
    while(money <= 0):
        print "Please Enter Positive number or greater than 0"
        money = float(raw_input("Please Enter Your Desired Bankroll Amount( must be greater than 0): \n$"))
    return money
def check():
    again = int(raw_input("Do you want to play again?\nPress 1 to play again.\nPress 2 to stop.\n"))
    while(again < 1 or again > 2):
        print "Please Enter valid response"
        again = int(raw_input("Do you want to play again?\nPress 1 to play again.\nPress 2 to stop.\n"))
    if(again == 1):
        print "Ok lets play again!"
        return False
    else:
        return True
def choice():
    choice = int(raw_input("Do you want to gamble?\nPress 1 to Gamble\nPress 2 to NOT Gamble\nPress 3 to Cash Out\n"))
    while(choice < 1 or choice > 3):
        print "Please Enter valid response"
        choice = int(raw_input("Do you want to gamble?\nPress 1 to Gamble\nPress 2 to NOT Gamble\nPress 3 to Cash Out\n"))
    return choice
def dice1():
    die1 = random.randrange(1,7)
    return die1
def dice2():
    die2 = random.randrange(1,7)
    return die2
def reveal():
    answer = []
    die1 = dice1()
    die2 = dice2()
    print "--\t" , "--"
    print "|%d|\t" % die1 , "|%d|" % die2
    print "--\t", "--"
    answer.append(die1)
    answer.append(die2)
    return answer
def diceAction():
    print "shaking can with dice in it"
    print "---"
    print "| |"
    print "---"
    print "  ---"
    print " / / "
    print "---"
    print "---"
    print "| |"
    print "---"
    print "---"
    print " \\ \\"
    print "  ---"
    print "---"
    print "| |"
    print "---"
def decisions(start,gamble):
    if(gamble == 3):
            print "You opted to Cash Out you have this much money $ %.2f" % start
    while(gamble == 2):
        if(start == 0):
            print "Looks like you have no money :( and can't gamble\nYou need to start a new game"
        print "Not gambling :( here is what the dices would be"
        diceAction()
        reveal()
        print "Your total balance is still $%.2f" % start
        gamble = choice()
        if(gamble == 3):
            print "You opted to Cash Out you have this much money $ %.2f" % start
    if(start == 0):
        print "Looks like you have no money :( and can't gamble\nYou need to start a new game"
    while( start > 0 and gamble == 1):
        bet1 = float(raw_input("Enter Your Bet:\n$"))
        bet = getbet(bet1)
        while( bet > start):
            print "Your bet must be less than your Bankroll amount and NOT negative"
            bet1 = float(raw_input("Enter Your Bet:\n$"))
            bet = getbet(bet1)
        diceAction()
        guess = []
        guess1 = int(raw_input("Guess whats the die number of the dice (1-6) integer:\n"))
        guess1 = dieRange1(guess1)
        print "Guess 1 is: %d" % guess1
        guess2 = int(raw_input("Again Guess whats the die number of dice (1-6) integer:\n"))
        guess2 = dieRange2(guess2)
        print "Guess 2 is: %d" % guess2
        guess.append(guess1)
        guess.append(guess2)
        true = reveal()
        true.sort()
        guess.sort()
        if((guess[0] == true[0]) and (guess[1] == true[1]) ):
            start += (2*bet)
            print "You win!!!"
            print "Your total is $ %.2f" % start
            gamble = choice()
            if(gamble == 3):
                print "You opted to Cash Out you have this much money $ %.2f" % start
            while(gamble == 2):
                print "Not gambling :( here is what the dices would be"
                diceAction()
                reveal()
                print "Your total balance is still $%.2f" % start
                gamble = choice()
                if(gamble == 3):
                    print "You opted to Cash Out you have this much money $ %.2f" % start
        else:
            start -=  bet
            print "You Lose!!!"
            print "Your total is $ %.2f" % start
            gamble = choice()
            if(gamble == 3):
                print "You opted to Cash Out you have this much money $ %.2f" % start
            while(gamble == 2):
                print "Not gambling :( here is what the dices would be"
                diceAction()
                reveal()
                print "Your total balance is still $%.2f" % start
                gamble = choice()
                if(gamble == 3):
                    print "You opted to Cash Out you have this much money $ %.2f" % start
            if(start == 0):
                print "Looks like you have no money :( and can't gamble\nYou need to start a new game"
                break
            if(start < 0):
                print "Looks like your broke and in debt :( i suggest you play again"
                break
def cred():
    print
    for i in range(5):
        print "****************************************************************************"
        for p in range(1):
            print "***********Credits to Jerrel Sogoni for intense python coding!!!************"
def intro():
    print "---------(Jerrel Sogoni Version)------ CHO-HAN ---------(Jerrel Sogoni Version)------"
    print "You must enter a Bankroll Amount to begin the game."
    print "Then you have an option of gambling your Bankroll or not.\nIf you guess the two dice numbers in any order you get double \nyour bid added to your balance."
    print "If you do not guess them correctly you will be deducted the amount you typed for your bid"
    print "If you reach 0 you will be asked if you want to play again since you cannot gamble anymore"
    cred()
    print
def main():
    final = False
    while not final:
        intro()
        money = float(raw_input("Please Enter Your Desired Bankroll Amount( must be greater than 0): \n$"))
        start = getMoney(money)
        print "Starting Bankroll is $ %.2f" % (start)
        gamble = choice()
        decisions(start, gamble)
        final = check()
    print "Thanks For playing!!!"
main()

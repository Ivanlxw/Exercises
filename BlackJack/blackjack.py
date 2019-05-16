import random

#Createing deck class
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 
        'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace':11}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        return f"{self.deck}"
    def __len__(self):
        return len(self.deck)       #should be 52
    def shuffle(self):
        return random.shuffle(self.deck)
    def deal(self):
        player_cards = self.deck[0:3:2]
        dealer_cards = self.deck[1:4:2]
        return player_cards, dealer_cards

class Player:
    def __init__(self, balance, cards=[]):
        self.balance = balance
        self.cards = cards
    def hit(self, card):
        self.cards.append(card)
    def __str__(self):
        str = ""
        for i in self.cards:
            str += "\n" + i.rank + ' of ' + i.suit
        return "Player1 has: " + str
    def value(self):
        total = 0
        for i in self.cards:
            total += values[i.rank]
        if ('Ace' in self.cards and len(self.cards) >= 4) or total > 21:
            total -= 10
        return total

class Dealer:
    def __init__(self, cards):
        self.cards = cards
    def __str__(self):
        str = ""
        for i in self.cards[1:]:
            str += "\n" + i.rank + ' of ' + i.suit
        return "Dealer has: " + str
    def value(self):
        total = 0
        for i in self.cards:
            total += values[i.rank]
        if ('Ace' in self.cards and len(self.cards) >= 4) or total > 21:
            total -= 10
        return total
    def hit(self,card):
        self.cards.append(card)

def take_bet(balance):
    while True:
        try: 
            bet = int(input("How much would you like to bet?"))
        except:
            print("Please enter an integer")
            continue
        else:
            if bet < balance:
                return bet
            else:
                print("You can't bet more than what you have")
                continue

def check_results(player1_value, dealer_value):
    """
    True means player1 win, False means player2 win
    """
    if player1_value > 21:
        print("Player has BUSTED!")
        return False
    elif dealer_value > 21:
        print("Dealer has BUSTED")
        return True
    elif player1_value > dealer_value:
        print("Your beat the dealer")
        return True
    elif dealer_value > player1_value:
        print("Dealer beats you")
        return False


def replay(balance):
    if balance <= 0:
        print("You're out of funds.")
        return False
    while True:
        play = input("Would you like to continue? (Yes/No)")
        if play.lower() == 'yes':
            return True
        elif play.lower() == 'no':
            return False
        else: 
            print("Please choose properly! ")



if __name__ == '__main__':
    #initiate game
        while True:
            game = input("Do you want to play the game? (Yes/No)\n")
            if game.lower() == 'yes':
                start = int(input("Choose starting balance: "))
                playing = True
                break
            elif game.lower() == 'no':
                playing = False
                break
            else: 
                print("Please choose Yes/No")

    #the game
        while playing:
            playingdeck = Deck()
            playingdeck.shuffle()
            #print(playingdeck)
            player_card, dealer_card = playingdeck.deal()
            dealer = Dealer(dealer_card)
            player1 = Player(start,player_card)
            bet = take_bet(player1.balance)

            i=4
            while True:
                #Player
                print("{}".format(player1))
                print("{}".format(dealer))
                print("Player1 card total is {}".format(player1.value()))
                choice = input("Hit or Stand?")
                if choice.lower() == 'hit':
                    player1.hit(playingdeck.deck[i])
                    i += 1
                    if player1.value() > 21:
                        break       #end the loop (game)
                    else:
                        continue
                elif choice.lower() == 'stand':
                    break
                else: 
                    print("There is no such thing, please choose to hit/stand")
                    continue
            
            while True:
                #Dealer
                if player1.value() > 21:
                    break       #no point having dealer to play
                else:
                    print("Dealer cards are {}".format(dealer))
                    print("Dealer card total is {}".format(dealer.value()))
                    if dealer.value() < 21 and dealer.value() <= player1.value():      #actual code 
                        dealer.hit(playingdeck.deck[i])
                        i+=1
                    elif dealer.value() > 21:
                        break
                    elif dealer.value() > player1.value():
                        break          
        
            #Time to see results!
            if check_results(player1.value(), dealer.value()):
                start += bet
                player1.balance += bet
                print("Player 1's balance is {}".format(player1.balance))
            else:
                start -= bet
                player1.balance -= bet
                print("Player 1's balance is {}".format(player1.balance))

            #play again
            playing = replay(player1.balance)

        print("Thanks for playing!")
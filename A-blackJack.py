#You need to create a simple text-based BlackJack game
#The game needs to have one player versus an automated dealer.
#The player can stand or hit.
#The player must be able to pick their betting amount.
#You need to keep track of the player's total money.
#You need to alert the player of wins, losses, or busts, etc...
#2version:
#Feel free to expand this game. Try including multiple players. 
#Try adding in Double-Down and card splits! 


import random

#Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') #tuple for immutability
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
 #translating string to integer using a dictionary
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,'Seven':7, 'Eight':8,
          'Nine':9,'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1  11} #!!!!!!!

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self): #print output for the class
        return f"{self.rank} of {self.suit}"

class Baralho:    
    def __init__(self):
        self.all_cards = []

        for suit in suits: #populating all_cards
            for rank in ranks:
                new_card = Card(suit,rank) 
                self.all_cards.append(new_card)

    def shuffle(self): #hide implementation(encapsulation)
        random.shuffle(self.all_cards) 
    
    def deal_one(self):
        return self.all_cards.pop() #.pop(default) = all_cards[-1]  (removes and returns it)
    

class Player:
    def __init__(self):
        self.bank = 1000
        self.player_cards = []

    def add_cards(self,new_card_s):
        self.player_cards_cards.append(new_card_s) #explicit: new_card_s[-1]

    def hit(self):

    
    def stand(self):

    def bet(self):
        print(f"How much u wanna bet? Your balance:{self.bank}")

    def __str__(self):
     return f"You have {self.cards} and ${self.bank}"




#LOGIG------------------------------------------------------------------------------------------------------------------------------------------
#setup
player = Player()
computer = Player()
new_deck = Baralho()
new_deck.shuffle() 

print("Welcome to BlackJack 21")

#shuffle

#while gameOn{

#place Bet

#deal 2 cards for player
#deal 1 for computer

#Hit and stand functions (by request)

#COMPUTERS TURN
#deal +1 for computer(if stand)

#computer automated hit:
#if player.score > computer {computer.hit()}
#check if computer.score > 21 {bust}

#Check result
#if player.score == 21 {win}
#if player.score > 21  {bust}
#if player.score > computer {lost}

#new game





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

        for suit in suits: #instanciating card's and populating all_cards
            for rank in ranks:
                new_card = Card(suit,rank) 
                self.all_cards.append(new_card)

    def shuffle(self): #hide implementation(encapsulation)
        random.shuffle(self.all_cards) 
    
    def deal_one(self):
        return self.all_cards.pop() #.pop(default) = all_cards[-1]  (removes and returns it)
    
    def game_still_on():
        choice = 'default'                      #so it goes through the while on the first time
        while choice not in ['Y','N']:          #keep asking
            choice = input("Wanna play, mate?  Y/N ")
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False

class Player:
    def __init__(self):
        self.bank = 1000
        self.player_cards = []
        self.bet = 0
        self.sum = 0

    def hit(self,new_card):
        self.player_cards.append(new_card) #explicit: new_card[-1] rightmost

    def clear_old_cards(self):
        for cards in self.player_cards:
          self.player_cards.pop() #.pop(default) = [-1]  (removes and returns it)

    def hit_or_stand():
        choice = 'default'                      
        while choice not in ['hit','stand']:          
           choice = input("type hit or stand:  (please, type exactly as it's written) ")
         
         while choice == 'hit':
           player.hit(new_deck.deal_one())
           print(player)
           continue
   
        elif choice == 'stand':




    def checkbust_or_21(self):
        #if self.sum == 21 or self.sum > 21 
       
    def __str__(self):
     return f" Cards: {self.player_cards} sum:{self.sum}"



#LOGIG------------------------------------------------------------------------------------------------------------------------------------------
#setup
player = Player()
computer = Player()
new_deck = Baralho()
gameOn = new_deck.game_still_on() #ask's if wants to play
new_deck.shuffle()


while gameOn:
 #new round
    player.clear_old_cards()

 #place Bet
    player.bet = input(f"How much u wanna bet?    Your balance:{player.bank}")

 #deal 2 (hit 2x) cards for player
    for i in range(2):
      player.hit(new_deck.deal_one())
      print(player)

 #deal 1 for computer
    player.hit(new_deck.deal_one())
    print(f"Dealer has {player} and XX")

 #Hit and stand
    player.hit_or_stand()
    player.checkbust_or_21()

 #COMPUTERS TURN(after stand)
    #deal +1 for computer(if stand)
    player.hit(new_deck.deal_one())
    print(f"Dealer has {player}")
    #computer automated hit:
    #if player.score > computer {computer.hit()}
    #check if computer.score > 21 {bust}

    #Check result
    #if player.score == 21 {win}
    #if player.score > 21  {bust}
    #if player.score > computer {lost}

    #check game
    gameChoise = input("Press 0 to KEEP PLAYING or 1 to LEAVE ")
    if gameChoise == 1:
       gameOn = False
    #play1more or leave
    #if play1more keep the balance





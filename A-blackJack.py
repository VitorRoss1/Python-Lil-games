#You need to create a simple text-based BlackJack game
#The game needs to have one player versus an automated dealer.
#The player can stand or hit.
#The player must be able to pick their betting amount.
#You need to keep track of the player's total money.
#You need to alert the player of wins, losses, or busts, etc...
#Feel free to expand this game. Try including multiple players. 
#Try adding in Double-Down and card splits! 


import random 
from abc import ABC, abstractmethod

#Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') #tuple for immutability
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
 #translating string to integer using a dictionary
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,'Seven':7, 'Eight':8,
          'Nine':9,'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11} # if sum>21 and ace: sum-10!!!!!!!

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  #value[key]

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

class Game:
    def __init__(self):
        #self.playerXComputer_cards = []
        self.sum = 0

    def hit(self,new_card):
        self.player_cards.append(new_card) #explicit: new_card[-1] rightmost

    def clear_old_cards(self):
        for cards in self.player_cards:
          self.player_cards.pop() #.pop(default) = [-1]  (removes and returns it)

    @abstractmethod
    def add_and_check(self):
        pass


class Player(Game):
    def __init__(self):
        self.bank = 1000
        self.player_cards = []
        self.bet = 0


    def hit_or_stand():                      
        while True:          
          choice = input("Type hit or stand:  (please, type exactly as it's written).")
         
          if choice == 'hit':
           player.hit(new_deck.deal_one())
           print(player)
           #checkbust21
   
          elif choice == 'stand':
            print("Player stands. Dealer's turn.")
            break
          
          else:
            print("Invalid option, try again.")
    
    def add_and_check(self):
       aces = 0
       for cards in self.player_cards:
         self.sum += cards.value    #cards is one of the card objects in player_cards list;   cards.value = values[card.rank]
         
         #ace counter
         if cards.rank == "Ace":
            aces+=1

         #changes aces values if bigger than 21 
         while self.sum > 21 and aces > 0: 
           print("Changing Ace value(11 -> 1)")
           self.sum -= 10
           aces -= 1

         #bj & bust check
         if self.sum == 21:
           self.bank += self.bet
           print(f"{player} BLACKJACK")
           return False #gameOn = false

         elif self.sum > 21: 
            self.bank -= self.bet
            print(f"{player} BUST")
            return False #gameOn = false
         return True

    def __str__(self):
     return f" Your Cards: {self.player_cards} sum:{self.sum}"


class Computer(Game):
   def __init__(self):
      self.computer_cards = []

   def add_and_check(self):
       aces = 0
       for cards in self.computer_cards:
         self.sum += cards.value   
         
         #ace counter
         if cards.rank == "Ace":
            aces+=1

         #changes aces values if bigger than 21 
         while self.sum > 21 and aces > 0: 
           print("Changing Ace value(11 -> 1)")
           self.sum -= 10
           aces -= 1


         #Game check
         if self.sum > player.sum:
           self.bank += self.bet
           print(f"{player} Dealer has Won")
           return False #gameOn = false

         elif self.sum > 21: 
            self.bank -= self.bet
            print(f"computer {co} BUST")
            return False #gameOn = false
         
         elif self.sum == player.sum:

       return True
    #override add_check with computer implementation

   def __str__(self):
     return f" Computer Cards: {self.computer_cards} sum:{self.sum}"
   



#LOGIG------------------------------------------------------------------------------------------------------------------------------------------
#setup
player = Player()
computer = Computer()
new_deck = Baralho()
gameOn = new_deck.game_still_on() #ask's if wants to play
new_deck.shuffle()


if gameOn:

 #new round
    player.clear_old_cards()

 # while not victory and bank > 0:

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
    gameOn = player.add_and_check()
     
 #COMPUTERS TURN(after stand)
    #deal +1 for computer(if stand)
    computer.hit(new_deck.deal_one())
    print(f"Dealer has {player}")

    #computer automated hit:
    if player.sum > computer.sum:
       computer.hit()
       if computer.sum >
    #check if computer.score > 21 {bust}
       #computer.checkbust_or_21()
    

    #Check result
    #if player.score == 21 {win}
    #if player.score > 21  {bust}
    #if player.score > computer {lost}

    #check game
        #play1more or leave
        #if play1more keep the balance





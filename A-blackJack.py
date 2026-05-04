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

# ---------------------------------------------------------------------------
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  #value[key]

    def __str__(self): #print output for the class
        return f"{self.rank} of {self.suit}"

# ---------------------------------------------------------------------------
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
    
    @staticmethod                                   # @staticmethod:
    def ask_play():
        choice = 'default'                      #so it goes through the while on the first time
        while choice not in ['Y','N']:          #keep asking
            choice = input("Wanna play, mate?  Y/N ")
            return choice == 'Y' #true if =='Y', false if not('N')

# ---------------------------------------------------------------------------
class Game(ABC): #inheritence from ABC
    def __init__(self):
        self.cards = []
        self.sum = 0

    def hit(self,new_card):
        self.cards.append(new_card) #explicit: new_card[-1] rightmost

    def clear_old_cards(self):
        self.cards = [] #empty list instead of .pop() returns leave the loop???/??
        self.sum = 0

#calculate sum ?????
    def calculate_sum(self):
     #reset bf re-adding
     self.sum = 0 
     aces = 0

     #adder and ace counter 
     for card in self.cards:  #cards is one of the card objects in cards list;  
        if card.rank == 'Ace': 
           self.sum += card.value # card.value = values[card.rank]; dict[key]
           aces += 1

     while self.sum > 21 and aces > 0:
        print("[Ace adjusted: 11 -> 1]")
        self.sum -= 10
        aces -= 1

    @abstractmethod #classes with abstract methods CANT be instanciated.
    def add_and_check(self): #subclasses do the implementation,like an interface contract with the child classes
        pass 

    @staticmethod     #belongs to the class itself can be called withoud instanciating                             
    def result_check(): 
         print(f"--- RESULTS ---")
         print(f"Player: {player.sum}  |  Dealer: {computer.sum}")

         if computer.sum > 21:
           player.bank += player.bet
           print(f"Dealer BUST! You win! Winnings: +{player.bet}")

         elif computer.sum > player.sum:
           player.bank -= player.bet
           print(f"You lose! Your losses: -{player.bet}")
         
         elif computer.sum == player.sum:
            print(f"TIE! Bet returned")
         
         elif computer.sum < player.sum:
            player.bank += player.bet
            print(f"You have Won! Your winnings: +{player.bet}")

# ---------------------------------------------------------------------------
class Player(Game):
    def __init__(self):
        super().__init__() #inherit variables from parent class
        self.bank = 1000
        self.bet = 0

    def place_bet(self): #place Bet(with error handling)
     while True:
      try:
          player.bet = int(input(f"How much u wanna bet? balance:{player.bank}"))
          if 0 < player.bet <= player.bank: #if valid break
             break
          print(f"Bet must be between 1 and {player.bank}.") #will be printed if bet bigger than balance or smaller than zero('if' didnt catch it) and it will iterate
      except ValueError: #error catcher
          print("Type a valid number.")

    def add_and_check(self):
         #sum
         self.calculate_sum()  #parent class encapsulation and reusability

         if self.sum == 21:
           self.bank += self.bet
           print(f"{player} BLACKJACK")
           return False #gameOn = false

         elif self.sum > 21: 
            self.bank -= self.bet
            print(f"{player} BUST")
            return False #gameOn = false
         return True
    
    @staticmethod                                   
    def hit_or_stand():
        #gameOn = return                       
        while True:          
          choice = input("Type hit or stand:  (please, type exactly as it's written).")
         
          if choice == 'hit':
           player.hit(new_deck.deal_one())
           print(player)
           if not player.add_and_check() #stop the loop if bust/blackjack (false)
              return False  #if addandcheck = false = bj or bust then hitorstand returns false
            
          elif choice == 'stand':
            print("Player stands. Dealer's turn.")
            return True  #to leave while loop; 
          
          else:
            print("Invalid option, try again.")

    def __str__(self):
     
     return f" Your Cards: {self.player_cards} sum:{self.sum}"

# ---------------------------------------------------------------------------
class Computer(Game):
   def __init__(self):
      super().__init__()                         

   def add_and_check(self):
       aces = 0
       self.sum = 0 # reset bf readd

       for cards in self.computer_cards:
         self.calculate_sum()
         
         if self.sum > 21: 
            print(f"{self} Dealer BUST") #X {computer} X instead {self}
            return False #gameOn = false

       return True
    #override add_check with computer implementation

   def __str__(self):
     return f" Dealer Cards: {self.computer_cards} sum:{self.sum}"
   

 
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#LOGIG
player = Player()
computer = Computer()
new_deck = Baralho()
new_deck.shuffle()

gameOn = Baralho.ask_play() #ask's if wants to play  static method dont need instanciate to call can call directly through class

while gameOn and player.bank > 0:

 #reset round
    player.clear_old_cards()
    computer.clear_old_cards()

 #place bet
    player.place_bet()

 #deal 2 (hit 2x) cards for player
    for i in range(2):
       player.hit(new_deck.deal_one())

    player.add_and_check() #check for bj
    print(player)

 #deal 1 for dealer
    computer.hit(new_deck.deal_one())
    print(f"Dealer shows: {computer} and [hidden]")

 #Hit or stand
    gameOn = Player.hit_or_stand() #false if

    player.hit_or_stand()
    gameOn = player.add_and_check()
     
 #computer's turn(after stand)
    if gameOn: #addandcheck will return true if stand and false if hit on the input asked(true = stand)
        computer.hit(new_deck.deal_one()) #deal +1 for computer
        computer.add_and_check() #check for bust
        print({computer})

    #computer automated hit (rule: hit on <=17 stand on >17):
        while player.sum > computer.sum or computer.sum < 17 :
          print("Dealer hits...")
          computer.hit(new_deck.deal_one())
          computer.add_and_check() #busted?
          print(computer)

 #Check result
    Game.result_check()

 #Check balance
    print(f"Your balance: {player.bank}")

    if player.bank <= 0:
     print("You're out of money! Game over.")
     break
    
print("Thanks for playing!")





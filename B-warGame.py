# War card game simulation
# 10/4/26
#
import random

#Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') #tuple for immutability
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
 #translating string to integer using a dictionary
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,'Seven':7, 'Eight':8,'Nine':9,'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14} #obs: uppercased first letter


#CLASSES--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Card:
    def __init__(self,suitP,rankP): #'P' as parameter
        self.suit = suitP
        self.rank = rankP
        self.value = values[rankP]

    def __str__(self): #str method defines print output for the class
        return f"{self.rank} of {self.suit}"
    


class Deck:     #"baralho" create 52 cards, hold them as a list of card objects,shuffle,pop dealed cards
    def __init__(self):
        self.all_cards = []
        #populating all_cards
        for suit in suits: 
            for rank in ranks:
                new_card = Card(suit,rank) #instanciating
                self.all_cards.append(new_card)

    def shuffle(self): # just to hide implementation details (encapsulation)
        random.shuffle(self.all_cards) #random.method doesnt return anything, just shuffles the attribute(list) 
    
    def deal_one(self):
        return self.all_cards.pop() #.pop(default) = all_cards[-1]  (removes and returns it)
    


class Playaa:    #hold current list of cards, remove/add cards, add 1 or +1 cards to their personal list
                 #play from the top pop([0]) first card(leftmost); add to the bottom append([-1])

    def __init__(self,name):
        self.name = name
        self.your_cards = [] 

    def remove_one(self):
        return self.your_cards.pop(0) #pops first(leftmost) card 

    def add_card_s(self,new_card_s):
        #adding +1 cards
        if type(new_card_s) == type([]):
            self.your_cards.extend(new_card_s)
        #adding 1 card
        else:
            self.your_cards.append(new_card_s) #explicit new_card_s[-1]

    def __str__(self):
        return f"{self.name} has {len(self.your_cards)} cards."
    


#Game-Logic--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 #setup
player1 = Playaa("P1")
player2 = Playaa("P2")
new_deck = Deck()
new_deck.shuffle() # random.shuffle(new_deck.all_cards) encapsulated

 #26 cards each
for i in range(26):
    player1.add_card_s(new_deck.deal_one())
    player2.add_card_s(new_deck.deal_one())

 #check
round_counter = 0
gameOn = True

while gameOn:
    round_counter+=1

 #checking for an empty list of cards
    if len(player1.your_cards)==0:
        gameOn = False
        print("player 2 wins")
        break

    if len(player2.your_cards)==0:
        gameOn = False
        print("player 1 wins")
        break
        
 #printing number of cards(__str__ returning) BEFORE drawing    
    print(f"(Round {round_counter}) |  {player1}  |  {player2}  |") 
    
 #draw this round cards
    playerOne_roundCards = []
    playerOne_roundCards.append(player1.remove_one()) #draws 1 card from the starter 26, to the table (player1.your_cards.pop(0))
    playerTwo_roundCards = []
    playerTwo_roundCards.append(player2.remove_one())

 #info displayed every round(part2)
    print(f"{playerOne_roundCards[-1]} vs {playerTwo_roundCards[-1]} , FIGHT!")

    #draw 5 cards, last one used for comparision over the war result
    war_mode = True
    while war_mode:   
        if playerOne_roundCards[-1].value > playerTwo_roundCards[-1].value: #[-1] to not pick the first card(avoid repeting the same card in case of war). [-1] doesnt matter if there is only one(no war scenario)
            war_mode = False
            player1.add_card_s(playerTwo_roundCards) # add single or list of cards to the bottom of player1.your_cards
            player1.add_card_s(playerOne_roundCards) #returning from battle
            random.shuffle(player1.your_cards) #shuffling won cards!

        elif playerOne_roundCards[-1].value < playerTwo_roundCards[-1].value:
            war_mode = False
            player2.add_card_s(playerOne_roundCards)
            player2.add_card_s(playerTwo_roundCards)
            random.shuffle(player2.your_cards)

        else: #WAR
            #check (able to play war) 
            if len(player1.your_cards) < 5:
                print("Player One unable to play war! Game Over at War\nPlayer Two Wins!")
                gameOn = False
                break   

            elif len(player2.your_cards) < 5:
                print("Player Two unable to play war! Game Over at War\nPlayer One Wins!")
                gameOn = False
                break

            for i in range(5):  #each player puts down 5 more cards
                playerOne_roundCards.append(player1.remove_one())
                playerTwo_roundCards.append(player2.remove_one())

            print(f"WAR\n(WAR ROUND) {playerOne_roundCards[-1]} vs {playerTwo_roundCards[-1]}")









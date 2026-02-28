#TIC TAC TOE 
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

#global variables
table = [['','',''],['','',''],['','','']]
acceptable_inputs = range(1,10)


#1F
play = True
def game_still_on():
   choice = 'default'
   while choice not in ['Y','N']:          #keep asking
      choice = input("Wanna play mate?")

   if choice == 'Y':
    return True
   elif choice == 'N':
    return False

#2F
acceptable_inputs = range(1, 10)
def user_position_input():
    position_index = 'DEFAULT'        #by default a 0 so it goes through the while on the first time

    while not position_index.isdigit() or int(position_index) not in acceptable_inputs:
         print("Make sure to type a number from 1 to 9!")
         position_index = input("select a position: ")
    return int(position_index)

#3F
def display_table(table):
    for row in table:
        print(row)


#4F
xorball = 0
position = user_position_input()

def update_table(position):
 global xorball   #scope

 #Conversion algorithm
 row = (position - 1) // 3           #floor division = int output
 col = (position - 1) % 3

 while game_still_on:
     if xorball%2 == 0:
       table[row][col]= 'X'
     else:
       table[row][col]= 'O'

     xorball += 1


#5F CHECKING


#6F Message
def initial_message():
    print("Welcome to tic tac toe!")
    positions_table = [[1,2,3],[4,5,6],[7,8,9]]
    for row in positions_table:
        print(row)




#call order
game_still_on()
initial_message()
display_table()

while play:
  user_position_input()
  update_table()
  display_table()







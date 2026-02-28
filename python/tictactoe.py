#TIC TAC TOE 
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

#global variable
table = [['','',''],['','',''],['','','']]
acceptable_inputs = range(1,10)


#1F input handling
def user_position_input():
    position_index = 0        #by default a 0 so it goes through the while on the first time

    while not position_index.isdigit() or position_index not in acceptable_inputs:
         position_index = input("select a position: ")
         print("Make sure to type a number from 1 to 9!")
    return int(position_index)

#CONVERSIONS
position = user_position_input()
if position == 1:
   converted_table = table[0][0]
elif position == 1:
   converted_table = table[0][1]   
elif position == 3:
   converted_table = table[0][1] 



#2F
game_still_on = True
def update_table():
    xorball = 0

    while game_still_on:
     if xorball%2 == 0:
      table[position_index][] = 'X'
      xorball += 1
     else:
      table[position_index][] = 'O'
      xorball += 1


#3F
def display_table(table):
    for row in table:
        print(row)



#initial message
print("Welcome to tic tac toe!")
positions_table = [[1,2,3],[4,5,6],[7,8,9]]
for row in positions_table:
    print(row)












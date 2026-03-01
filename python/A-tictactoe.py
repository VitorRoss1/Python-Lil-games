#TIC TAC TOE 
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
#D:\vscode\python

#00------------------------------------------------------------------------
table = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

#1F------------------------------------------------------------------------

def game_still_on():
   choice = 'default'                      #so it goes through the while on the first time
   while choice not in ['Y','N']:          #keep asking
      choice = input("Wanna play mate?  Y/N")
   if choice == 'Y':
    return True
   elif choice == 'N':
    return False

#2F------------------------------------------------------------------------
acceptable_inputs = range(0, 9)
def user_position_input():
    position_index = 'DEFAULT'        

    while not position_index.isdigit() or int(position_index) not in acceptable_inputs:
         print("Welcome to tic tac toe!")
         print("[0 1 2]")
         print("[3 4 5]")
         print("[6 7 8]")
         print("type a number from 0 to 8!")
         position_index = input("select a position: ")
         if position[position_index] != ' ':
            position_index = input("select a position not occupied: ")

    return int(position_index)

#3F------------------------------------------------------------------------
def display_table(table):
    for item in table:
        print(item)

#4F------------------------------------------------------------------------
xorball = 0

def update_table(position):
 global xorball                  #scope

 #Conversion algorithm
 row = (position) // 3           #'//'floor division = integer output
 col = (position) % 3

 if xorball%2 == 0:
    table[row][col]= 'X'
 else:
    table[row][col]= 'O'
 xorball += 1

#5F------------------------------------------------------------------------ CHECKING
def check_victory(table):
   global isGameOn
 #checking rows and columns
   for col in range(0,3):
      if table[0][col] == table[1][col] == table[2][col] and table[0][col] != ' ' : #checks if not empty too
        print("Win :)")
        isGameOn = False
   for row in range(0,3):
      if table[row][0] == table[row][1] == table[row][2] and table[row][0] != ' ':
        print("Win :)")
        isGameOn = False
 #Diagonals
   if table[0][0] == table[1][1] == table[2][2] and table[0][0] != ' ':
        print("Win :)")
        isGameOn = False
   elif table[0][2] == table[1][1] == table[2][0] and table[0][2] != ' ':
        print("Win :)")
        return True
   print("Not a Win")
   isGameOn = True
   

#66------------------------------------------------------------------------
#Call order
isGameOn = game_still_on() #ask's if he/she wants to play

while not isGameOn:
  position = user_position_input() #ask's for the position to be marked
  update_table(position)          
  display_table(table)                  
  victory = check_victory(table)   #Checks for victory







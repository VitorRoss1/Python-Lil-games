#TIC TAC TOE 
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
#D:\vscode\python

#00------------------------------------------------------------------------
table = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
plays = 0

#1F------------------------------------------------------------------------

def game_still_on():
   choice = 'default'                      #so it goes through the while on the first time
   while choice not in ['Y','N']:          #keep asking
      choice = input("Wanna play, mate?  Y/N ")
   if choice == 'Y':
    return True
   elif choice == 'N':
    return False

#2F------------------------------------------------------------------------
acceptable_inputs = range(0, 9)

def user_position_input():
    while True:
         print("[0 1 2]")
         print("[3 4 5]")
         print("[6 7 8]")
         print("Select a position from 0 to 8!")
         print("And make sure it isn't already occupied.")
         raw_position = input("select a position: ") 

    #CheckPoints
         if not raw_position.isdigit():
            print("Invalid input. Not a digit")              
            continue                   
            
         position = int(raw_position) #using raw_position first bc the input could be something other than a number. so if i tried to typecast it, an error would occour AND .isdigit() only works for strings
                                      
         if position not in acceptable_inputs:     #knowing position is a number and converted to integer
            print("Invalid input (Not in range(0-8))")
            continue 
         
         #Conversion algorithm
         row = (position) // 3      
         col = (position) % 3

         if not table[row][col] == ' ':
            print("Invalid input (Position occupied)")
            continue 
         
         return position #passed the checkpoints the return ends the function with the ''infinite'' while true loop

#3F------------------------------------------------------------------------
def display_table(table):
    for item in table:
        print(item)

#4F------------------------------------------------------------------------
xorball = 0

def update_table(position):
 global xorball                  #scope

 row = (position) // 3         #'//'floor division = integer output  
 col = (position) % 3

 if xorball%2 == 0:
    table[row][col]= 'X'
 else:
    table[row][col]= 'O'
 xorball += 1

#5F------------------------------------------------------------------------ CHECKING
victory = False
def check_victory(table):
 #checking rows and columns
   for col in range(0,3):
      if table[0][col] == table[1][col] == table[2][col] and table[0][col] != ' ' : #checks if not empty too
        winner = table[0][col]                  #Catches if the winner is X or O             
        print(f"{winner} won :P ")              #custom message
        return True
   for row in range(0,3):
      if table[row][0] == table[row][1] == table[row][2] and table[row][0] != ' ':
        winner = table[row][0]                             
        print(f"{winner} won :P ")   
        return True
 #Diagonals
   if table[0][0] == table[1][1] == table[2][2] and table[0][0] != ' ':
        winner = table[0][0]                             
        print(f"{winner} won :P ")   
        return True
   elif table[0][2] == table[1][1] == table[2][0] and table[0][2] != ' ':
        winner = table[0][2]                             
        print(f"{winner} won :P ")   
        return True
   return False
   

#66------------------------------------------------------------------------
#Call order
isGameOn = game_still_on() #ask's if he/she wants to play

if isGameOn:
   print("Welcome to tic tac toe!")
   while not victory and plays < 9:
     display_table(table) 
     position = user_position_input() #ask's for the position to be marked
     update_table(position)                        
     victory = check_victory(table)   #Checks for victory
     plays +=1
   if not victory:  # if after 8 plays no victory was achieved(scaped the not victory loop bc plays == 9)
        print("TIE :| ") 







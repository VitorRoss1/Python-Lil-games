from random import randint
num = randint(0,100)

print("Guess the number!")
print(" xx rules xx")
print("if you guessed it in a margin of 10 numbers = 'warm' ")
print("if didn't = 'cold' ")
print("I'll tell you if you're getting closer or not :p")

#list to store guesses
guesses = []
guessesDistances = []

while True:
    guess = int(input("Guess the number between 1 and 100"))
    distance = abs(guess-num)

    
#first check if its inbetween
    if guess > 100 or guess < 1:
        print ('OUT OF BOUNDS')
        continue

#append the guess
    guesses.append(guess)

#Secondly check if you got it
    if guess == num:
           print(f"You got it! number of tries:{len(guesses)}.")
           break

#response for first try 
    if len(guesses)==1:
        if distance > 10:
            print('Cold')
        else:
             print('Warm')
        guessesDistances.append(distance)
#response for other tries
    else:
            if distance < guessesDistances[-1]: #-1 BEING THE LAST ADDED element INDEX
               print('Warmer')
            else: 
                print('colder')
            guessesDistances.append(distance)
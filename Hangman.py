playername1 = input("What's your name?...You will give the word:")
playername2 = input("What's your name?...You will be guessing:")
space = " "
greetings = input("Hi" + space+ playername1 +space+ "are you ready to play?...Yes or No:")
wordsentence = "Enter a word:"
word = ""
if greetings == "Yes" or "yes":
    word += input(wordsentence)
    print("Now pass the game on to"+space + playername2)
else:
    print ("Thank You for your time, see you next time =)")
    while greetings == No:
        print("Game Ended")
if len(word) > 8:
    print("ERROR! no more than 8 letters allowed...Exit and try again.")
print(space)
print('REMEMBER YOU ONLY HAVE 11 TRIES!!!')
print("With that out of the way, lets start guessing:")
guess = input('Enter a letter')
points = 11
if word.find(guess) > -1:
    print("HOORAY!! You got one.")
    word.replace(guess," ")
else:
    print("WRONG")
    points = points - 1
    print("POINTS LEFT:")
    print(points)

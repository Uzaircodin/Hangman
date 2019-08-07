_input = True

playername1 = input("What's your name?...You will give the word:")
playername2 = input("What's your name?...You will be guessing:")
space = " "
greetings = input("Hi" + space+ playername1 +space+ "are you ready to play?...Yes or No:")
wordsentence = "Enter a word:"
word = ""

if greetings == "Yes":
    word += input(wordsentence)
    print("REMEMBER YOU ONLY HAVE 11 TRIES!!!")
    print("With that out of the way thats get started with guessing:")
    print("Now pass the game on to"+space + playername2)
    _input = False
else:
    print ("Thank You for your time, see you next time =)")
    _input = True

def mainprog():
    if len(word) > 8:
        print("ERROR! no more than 8 letters allowed...Exit and try again.")
        _input = True
    points = 11
    guess = input('Enter a letter')

    if word.find(guess) > -1:
        word.replace(guess," ")
        print("HOORAY!! You got one.")
        _input = False
    else:
        print("WRONG")
        points = points - 1
        print("POINTS LEFT:")
        _input = False
    print(points)
while _input == True:
    mainprog()

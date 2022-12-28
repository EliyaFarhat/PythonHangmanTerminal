import random

# Terminal Version:

words = ['python', 'java', 'coding', 'animal', 'hi', 'zebudderyninja69',
         "walk","act","worry","why","straight","sail",
         "meal","verb","till","fight","copper","share",
         "sink","solar","bee","article","nobody","those",
         "hearing","take","none","feet","continued","proud",
         "writer","barn","everybody","happen","former","soldier",
         "wagon","way","led","star","grade","attached",
         "younger","broken","once","actual","doctor","trunk"]

# randrange is inclusive :/
# this will select the word to guess from our words list

while True:

    print('\n\nSelect from the following options:')
    choice = int(input('1. Play. 2. Exit.'))

    if choice == 2:
        print("GAME CLOSED")
        break
    elif choice == 1:
        # Game loop
        # Will store and compare guesses
        # Creates array with each letter of the word at diff index
        wordArr = []
        theWord = words[random.randrange(0, len(words))]
        guesses = ['_'] * len(theWord)
        incorrect = 0
        stopper = 0
        used = []
        for x in theWord:
            wordArr.append(x)
        while stopper == 0:

            print('------HANGMAN------')
            print('      ----------   ')
            print('      |        |   ')
            print('      |            ')
            print('      |            ')
            print('      |            ')
            print('      |            ')
            print('     ___           ')
            print("")
            print('Guesses: ', end=" ")
            for y in guesses:
                print(y, end=" ")

            guess = input("\nGuess: ")
            guess1 = guess.lower()

            if wordArr.count(guess1) >= 1:
                index = 0
                for x in range(0, len(wordArr)):
                    if wordArr[x] == guess1:
                        guesses[x] = guess1
            else:
                used.append(guess1)
                incorrect += 1

            if guesses == wordArr:
                print("\nYOU HAVE WON!")
                stopper = 1
                break
            if incorrect == 1:
                while stopper == 0:
                    print('------HANGMAN------')
                    print('      ----------   ')
                    print('      |        |   ')
                    print('      |        O   ')
                    print('      |            ')
                    print('      |            ')
                    print('      |            ')
                    print('     ___           ')
                    print("")
                    print('Guesses: ', end=" ")
                    for y in guesses:
                        print(y, end=" ")
                    print('\nIncorrect: ', end=" ")
                    for z in used:
                        print(z, end=", ")

                    guess = input("\nGuess: ")
                    guess1 = guess.lower()

                    if wordArr.count(guess1) >= 1:
                        index = 0
                        for x in range(0, len(wordArr)):
                            if wordArr[x] == guess1:
                                guesses[x] = guess1
                    else:
                        used.append(guess1)
                        incorrect += 1

                    if guesses == wordArr:
                        print("\nYOU HAVE WON!")
                        stopper = 1
                        break

                    if incorrect == 2:
                        while stopper == 0:
                            print('------HANGMAN------')
                            print('      ----------   ')
                            print('      |        |   ')
                            print('      |        O   ')
                            print('      |       |||  ')
                            print('      |            ')
                            print('      |            ')
                            print('     ___           ')
                            print("")
                            print('Guesses: ', end=" ")
                            for y in guesses:
                                print(y, end=" ")
                            print('\nIncorrect: ', end=" ")
                            for z in used:
                                print(z, end=", ")
                            guess = input("\nGuess: ")
                            guess1 = guess.lower()

                            if wordArr.count(guess1) >= 1:
                                index = 0
                                for x in range(0, len(wordArr)):
                                    if wordArr[x] == guess1:
                                        guesses[x] = guess1
                            else:
                                used.append(guess1)
                                incorrect += 1

                            if guesses == wordArr:
                                print("\nYOU HAVE WON!")
                                stopper = 1
                                break
                            if incorrect == 3:
                                while stopper == 0:
                                    print('------HANGMAN------')
                                    print('      ----------   ')
                                    print('      |        |   ')
                                    print('      |        O   ')
                                    print('      |       /|\  ')
                                    print('      |       /    ')
                                    print('      |            ')
                                    print('     ___           ')
                                    print("")
                                    print('Guesses: ', end=" ")
                                    for y in guesses:
                                        print(y, end=" ")
                                    print('\nIncorrect: ', end=" ")
                                    for z in used:
                                        print(z, end=", ")

                                    guess = input("\nGuess: ")
                                    guess1 = guess.lower()

                                    if wordArr.count(guess1) >= 1:
                                        index = 0
                                        for x in range(0, len(wordArr)):
                                            if wordArr[x] == guess1:
                                                guesses[x] = guess1
                                    else:
                                        used.append(guess1)
                                        incorrect += 1

                                    if guesses == wordArr:
                                        stopper = 1
                                        print("\nYOU HAVE WON!")
                                        break

                                    if incorrect == 4:
                                        print('------HANGMAN------')
                                        print('      ----------   ')
                                        print('      |        |   ')
                                        print('      |        O   ')
                                        print('      |       /|\  ')
                                        print('      |       / \  ')
                                        print('      |            ')
                                        print('     ___           ')
                                        print("")
                                        print("GAME OVER, YOU LOST.")
                                        print('Guesses: ', end=" ")
                                        for y in guesses:
                                            print(y, end=" ")
                                        print('\nIncorrect: ', end=" ")
                                        for z in used:
                                            print(z, end=", ")
                                        stopper = 1
                                        break

        print("\nTHE WORD WAS:", theWord)
        print("-----------END-----------")

# Python-Hangman in the Terminal
A simple hangman game to be played and displayed in the terminal.
## The Game
This section of the README will discuss the thought process behind constructing the game.

The first thing we need to know is how hangman is played. Now, I know you may be familiar with this already, but it is necessary to discuss.

The goal of hangman is to guess a word correctly without exceeding a maximum amount of incorrect guesses, one letter at a time. In the event an incorrect letter is guessed (which is a letter that the word does not contain) a body part will be added to the board. The game ends when, the word is correctly guessed or the player exceeds the maximum amount of incorrect guesses allowed. Breaking up the game into smaller sub-problems is crucial to crafting this game in Python.

## The Code
### Setting Up the Foundation
The first thing we must think about is how exactly we are going to obtain words for the player to guess, and how we wil be able to randomly select them.

We can implement this using an **list of words** and the **random** module.

```python
import random

words = ['python', 'java', 'coding', 'animal', 'hi', 'zebudderyninja69',
         "walk","act","worry","why","straight","sail",
         "meal","verb","till","fight","copper","share",
         "sink","solar","bee","article","nobody","those",
         "hearing","take","none","feet","continued","proud",
         "writer","barn","everybody","happen","former","soldier",
         "wagon","way","led","star","grade","attached",
         "younger","broken","once","actual","doctor","trunk"]
```

This list will store all of the available words for the game to choose from. You may add or remove words as you please.

Now, let's implement a way for the game to randomly select a word from the list. We can do this by assigning a variable to hold a random index of the list of words using the randrange() function. This is what it will look like in python.

```python
  theWord = words[random.randrange(0, len(words))]
```

Now that we have a way to randomly select a word, we must implement a loop to keep the game running until certain inputs or values are met. We can do this using a while True loop. This loop will break if and only if a 'break' is called. We will also ask the user for their decesion on whether or not they would like to play the game. If the user selects the option to play the game we will begin the game using conditional statements, we will break the loop if the user decides to. If however, the user decides to play, me must draw out the game's UI and initialize some variables:
1. **wordArr**
  - Stores each letter of the word separately in a list
2. **guesses**
  - Stores an "_" for each letter in the word, this will be used to display the known letters
3. **incorrect**
  - Stores the number of incorrect guesses
4. **stopper**
  - This is the variable that will be used later to break each while loop once the max-value of **incorrect** is reached
5. **used**
  - Stores the letters of the incorrect guesses

```python
while True:

    print('\n\nSelect from the following options:')
    choice = int(input('1. Play. 2. Exit.'))

    if choice == 2:
        print("GAME CLOSED")
        break
    elif choice == 1:
        wordArr = []
        theWord = words[random.randrange(0, len(words))]
        guesses = ['_'] * len(theWord)
        incorrect = 0
        stopper = 0
        used = []
        
        # Append each letter of the word to wordArr
        for x in theWord:
            wordArr.append(x)
        
        # First instance of the game, 0 incorrect guesses
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
```            
If you ran the code, you may have noticed that it loops forever... oops.

Anyway, to fix this we need to have the game ask the player for their guess, we will also need to display **guesses** as underlines on the screen. This will give the user information on the length of the word and the correct guesses they have made. We can add the below code under the previous code.

```python
print('Guesses: ', end=" ")
            for y in guesses:
                print(y, end=" ")

            guess = input("\nGuess: ")
            guessFinal = guess.lower()
```            
We will also need to begin thinking of the event in which the player guesses correctly and incorrectly.

### CORRECT GUESS:
We must figure out if the guess is correct. To do this, we will check if the guess is contained in the list using the .count() method. If it is, we will replace the "_" in the guesses list with the correct letter at the respective index it is contained at in the word. We can implement this the following way.

```python
if wordArr.count(guess1) >= 1:
  for x in range(0, len(wordArr)):
    if wordArr[x] == guess1:
      guesses[x] = guess1
```

It is however, possible to beat the game without making incorrect guesses. We must add a conditional statement that handles this.

```python
if guesses == wordArr:
  print("\nYOU HAVE WON!")
  stopper = 1
  break
```

### INCORRECT GUESS:
To figure out if a guess is incorrect, we can simply add an else statement to the 2nd to last if statement. Here, we can append the incorrect guess to the **used** list and we can move on to drawing the first body part.

```python
else:
  used.append(guess1)
  incorrect += 1
```  

### The Heart of the Game
So far, your code should look like this:

```python
import random

words = ['python', 'java', 'coding', 'animal', 'hi', 'zebudderyninja69',
         "walk","act","worry","why","straight","sail",
         "meal","verb","till","fight","copper","share",
         "sink","solar","bee","article","nobody","those",
         "hearing","take","none","feet","continued","proud",
         "writer","barn","everybody","happen","former","soldier",
         "wagon","way","led","star","grade","attached",
         "younger","broken","once","actual","doctor","trunk"]

while True:
    # randrange is inclusive
    # this will select the word to guess from our words list
    print('\n\nSelect from the following options:')
    choice = int(input('1. Play. 2. Exit.'))

    if choice == 2:
        print("GAME CLOSED")
        break
    elif choice == 1:
        wordArr = []
        theWord = words[random.randrange(0, len(words))]
        guesses = ['_'] * len(theWord)
        incorrect = 0
        stopper = 0
        used = []

        # Append each letter of the word to wordArr
        for x in theWord:
            wordArr.append(x)

        # First instance of the game, 0 incorrect guesses
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
```

We must now handle each instance where an incorrect guess is made and draw the respective body part based on how many incorrect guesses have been made. Recall how we added a conditional statement to increment the **incorrect** variable by 1 if the letter guesses is not contained in the word. This is how we will decide which body part is to be drawn next, and how close the player is to losing the game. Now, if a player makes an incorrect guess, and follows up with a correct one. We still want the body part to be drawn for the incorrect guess that was previously made. We can do this by implementing another while loop.

The first body part to be drawn is the head, this is what the next while loop will look like:
```python
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
```

You may have noticed some differences, the first being that the while loop exists within a conditional statement. This is true because we only want to activate this while loop if 1 incorrect guess has been made, and keep the player here if that is still the case. The second difference is that we are now printing incorrect guesses. The final differrence is that we drew a head on the display. Other than that, the code is nearly identical. We can use that to our advantage by simply copy pasting this segment of code, changing only the first conditional statement (adding 1 to it) and adding new body parts. In this game, I decided to give the player 4 pardons on their incorrect guesses before the body is fully drawn. 
If you follow this is exactly as I am, your code should look like this:
```python
import random

words = ['python', 'java', 'coding', 'animal', 'hi', 'zebudderyninja69',
         "walk","act","worry","why","straight","sail",
         "meal","verb","till","fight","copper","share",
         "sink","solar","bee","article","nobody","those",
         "hearing","take","none","feet","continued","proud",
         "writer","barn","everybody","happen","former","soldier",
         "wagon","way","led","star","grade","attached",
         "younger","broken","once","actual","doctor","trunk"]


while True:
    
    # randrange is inclusive
    # this will select the word to guess from our words list
    print('\n\nSelect from the following options:')
    choice = int(input('1. Play. 2. Exit.'))

    if choice == 2:
        print("GAME CLOSED")
        break
    elif choice == 1:
        wordArr = []
        theWord = words[random.randrange(0, len(words))]
        guesses = ['_'] * len(theWord)
        incorrect = 0
        stopper = 0
        used = []

        # Append each letter of the word to wordArr
        for x in theWord:
            wordArr.append(x)

        # First instance of the game, 0 incorrec guesses
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
``` 

You may have noticed that their exists a conditional statement using the **incorrect** variable that does not contain a while loop. The reason for this is that if the 4th incorrect guess is made, the entire body is drawn. Thus, the game is over and the player has lost. We can now exit the game by setting the stopper variable to 1. This will break each while loop as the condition for them to run is for the stopper to be equal to 0.

When the game ends, the player will be greeted with the option to play the game or exit the game, the reason for this is that the while loop that handles this initial choice is always true and is not affected by the stopper.

### The End
Congratualtions on building hangman in the terminal! The next tutorial/repo will be on building hangman using the pygame module, making it more appealing to look at and play.

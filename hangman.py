import random

def start_game():
    x = ""
    while x != "exit" or x != "play":
        choose = input('Type "play" to play the game, "exit" to quit: ')
        if choose == "play":
            x = "play"
            return True
        elif choose == "exit":
            x = "exit"
            return False

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

print("H A N G M A N")
print()
condition2 = True
condition = True
while condition2:
    if start_game() == False:
        condition2 = False
        condition = False
    else:
        condition2 = True
        condition = True
        print()
    lol = "----------------------------------------------------------"
    remeber = []
    tries = 8
    key = random_line("Slownik")
    hidden = lol[0:len(key)]
    hidden = list(hidden)
    while condition:
        print("".join(hidden))
        if "-" not in hidden:
            print("You guessed the word!")
            print("You survived!")
            condition = False
            print()
        else:
            x = input("Input a letter: ")

            if x in remeber:
                print("You already typed this letter")
                print()

            elif len(x) > 1 or len(x) < 1:
                print("You should print a single letter")
                print()

            elif x not in 'abcdefghijklmnopqrstuvwxyz':
                print("It is not an ASCII lowercase letter")
                print()

            elif x in key:
                for i in range(len(key)):
                    if key[i] == x:
                        hidden[i] = x
                        remeber.append(x)
                        print()

            else:
                if x not in remeber:
                    print("No such letter in the word")
                    tries = tries - 1
                    remeber.append(x)
                    if tries == 0:
                        print("You are hanged!")
                        condition = False
                    print()
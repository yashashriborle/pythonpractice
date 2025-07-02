import random
playing = True
while playing:
    choice = input("Press Enter to roll the dice... (y/n):").lower()
    if choice == 'y' or choice == 'Y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
    print(f"You rolled a {die1} and {die2}.")
    if die1 == die2:
        print("You rolled a double! You get to roll again.")
        playing = False
    elif choice == 'n' or choice == 'N':
        print("You choose not to roll the dice.")
        break
else:
    print("Invalid input.")
    
            

# Imports
import random

# global variables
current_player = "p1"
game_is_running = True
was_caught = False

class Player:

    def __init__(self, name, attack, health, catchRate):
        self.name = name
        self.attack = attack
        self.health = health
        self.catchRate = catchRate

    def attacking(self, enemy_player):
        # Get current player attack
        currAtk = self.attack

        # Subtract current player attack from p2 health
        print("You dealt " + str(currAtk) + " damage to " + enemy_player.name)
        enemy_player.health = enemy_player.health - currAtk

        # Print new p2 health
        print(enemy_player.name + " now has " + str(enemy_player.health) + " health.\n")

    def catch(self, enemy_player):
        global was_caught
        # Get current player health
        currHealth = enemy_player.health

        # Calculate catch rate
        newCR = enemy_player.catchRate + (100 - currHealth)

        # Execute catch
        random_num = random.randint(0, 100)
        if random_num < newCR:
            print("You successfully caught " + enemy_player.name)
            was_caught = True
        else:
            print(enemy_player.name + " could not be caught.")


# Function that allows player 1 to choose their starter
def choose_starter(ice, fire, shadow):

    # While loop stops invalid inputs
    while True:
        choice = input("Player 1, would you like to play as Ice, Fire, Shadow, or Earth: ")

        # Player selected Ice
        if choice == "Ice":
            starter = "Ice"
            return starter

        # Player selected Fire
        elif choice == "Fire":
            starter = "Fire"
            return starter

        elif choice == "Shadow":
            starter = "Shadow"
            return starter

        elif choice == "Earth":
            starter = "Earth"
            return starter

        else:
            print("Invalid selection. Please type your choice exactly as they appear.")


# Function that allows p2 to choose their starter
def choose_starter_p2(ice, fire, shadow):
    # While loop stops invalid inputs
    while True:
        choice = input("Player 2, would you like to play as Ice, Fire, Shadow, or Earth: ")

        # Player selected Ice
        if choice == "Ice":
            starter = "Ice"
            return starter

        # Player selected Fire
        elif choice == "Fire":
            starter = "Fire"
            return starter

        elif choice == "Shadow":
            starter = "Shadow"
            return starter

        elif choice == "Earth":
            starter = "Earth"
            return starter

        else:
            print("Invalid selection. Please type your choice exactly as they appear.")


# Displays starting information before the battle begins
def display_starting_info(p1, p2):
    print("\nWelcome to the battlefield! You have chosen " + p1.name + "!")

    if p1.name == "Ice":
        print("Player 1 " + "(" + p1.name + ")" + " has " + str(p1.attack) + " attack and " + str(p1.health) + " health.")
        print("Player 2 " + "(" + p2.name + ")" + " has " + str(p2.attack) + " attack and " + str(p2.health) + " health." + "\n")
        print("May you envelop " + p2.name + " in your blizzard!\n")

    elif p1.name == "Fire":
        print("Player 1 " + "(" + p1.name + ")" + " has " + str(p1.attack) + " attack and " + str(p1.health) + " health.")
        print("Player 2 " + "(" + p2.name + ")" + " has " + str(p2.attack) + " attack and " + str(p2.health) + " health." + "\n")
        print("May the fires of vengeance scorch " + p2.name + "!\n")

    elif p1.name == "Shadow":
        print("Player 1 " + "(" + p1.name + ")" + " has " + str(p1.attack) + " attack and " + str(p1.health) + " health.")
        print("Player 2 " + "(" + p2.name + ")" + " has " + str(p2.attack) + " attack and " + str(p2.health) + " health." + "\n")
        print("May you be as elusive as the shadows \n")

    elif p1.name == "Earth":
        print("Player 1 " + "(" + p1.name + ")" + " has " + str(p1.attack) + " attack and " + str(p1.health) + " health.")
        print("Player 2 " + "(" + p2.name + ")" + " has " + str(p2.attack) + " attack and " + str(p2.health) + " health." + "\n")
        print("May you crush your enemy under the weight of your boulder \n")

# Function that handles each turn
def handle_turn(current_player, p1, p2):
    print(current_player + "'s turn." )

    if current_player == "p1":
        current_player = p1
        enemy_player = p2

    elif current_player == "p2":
        current_player = p2
        enemy_player = p1

    while True:
        action = input("Enter 'A' to attack or 'C' to attempt to catch them: ")
        if action == "A":
            print("Attacking...\n")
            current_player.attacking(enemy_player)
            break
        elif action == "C":
            print("Attempting to catch...\n")
            current_player.catch(enemy_player)
            break
        else:
            print("Invalid Action.")

def check_win(p1, p2):
    global current_player, game_is_running, was_caught

    if was_caught and current_player == "p1":
        print("p1 won by catching " + p2.name)
        game_is_running = False

    elif was_caught and current_player == "p2":
        print("p2 won by catching " + p1.name)
        game_is_running = False

    elif p1.health <= 0:
        print("p2 won with " + p2.name)
        game_is_running = False

    elif p2.health <= 0:
        print("p1 won with " + p1.name)
        game_is_running = False

    return

def change_player():
    global current_player
    # if the current player was p1, then switch to p2
    if current_player == "p1":
        current_player = "p2"

    # if current player was p2, then switch to p1
    elif current_player == "p2":
        current_player = "p1"
    return


def main_loop():
    global game_is_running

    # initialize players
    ice = Player("Ice", 25, 100, 5)
    fire = Player("Fire", 33, 100, 20)
    shadow = Player("Shadow", 20, 100, 1)
    earth = Player("Earth", 40, 100, 50)

    # Choose starting player
    starterP1 = choose_starter(ice, fire, shadow)

    # Assigns p1 to your choice
    if starterP1 == "Ice":
        p1 = ice

    elif starterP1 == "Fire":
        p1 = fire

    elif starterP1 == "Shadow":
        p1 = shadow

    elif starterP1 == "Earth":
        p1 = earth

    starterP2 = choose_starter_p2(ice, fire, shadow)

    # Assigns p1 to your choice
    if starterP2 == "Ice":
        p2 = ice

    elif starterP2 == "Fire":
        p2 = fire

    elif starterP2 == "Shadow":
        p2 = shadow

    elif starterP2 == "Earth":
        p2 = earth

    # Display Information
    display_starting_info(p1, p2)


    # Main Game Loop

    while game_is_running == True:

        # Handle player turn
        handle_turn(current_player, p1, p2)

        # Check if game is over
        check_win(p1, p2)

        # Change current player
        change_player()

# Call main loop
main_loop()
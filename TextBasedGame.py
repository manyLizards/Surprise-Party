# Jordan Nichole Barringer

# Function showing the goal of the game and move commands
def show_instructions():
    # print a main menu
    print("Roommate's Surprise Party")
    print("Collect the party supplies without getting caught by the birthday girl.")


# Function for winning the game
def beat_game():
    # show game won
    print("You've successfully surprised the birthday girl!")
    print("Click play at the top of PyCharm to play again or 'exit' to exit the game.")

# Function for losing the game
def game_over():
    print("You blew the surprise! The birthday girl happily helps you finish setting up her birthday party.")
    print("Try again?")
    print("Click play at the top of PyCharm to try again or 'exit' to exit the game.")


# The main function for overall gameplay functionality
def main():
    # A dictionary linking a room to other rooms
    # and linking one item for each room except the Start room (Living Room)
    # and the room containing the birthday girl
    rooms = {
        'Your Room': {'north': 'Bathroom', 'west': 'Hallway', 'item': 'streamers'},
        'Bathroom': {'south': 'Your Room', 'item': 'speakers'},
        'Hallway': {'north': "Roommate 1's Room", 'south': "Roommate 2's Room", 'west': 'Living Room',
                    'east': 'Your Room', 'item': 'activities'},
        "Roommate 1's Room": {'south': 'Hallway', 'item': 'Birthday Girl'},  # villain
        "Roommate 2's Room": {'north': 'Hallway', 'item': 'music'},
        "Living Room": {'south': 'Laundry Room', 'west': 'Kitchen', 'east': 'Hallway'},  # Start - no item
        "Laundry Room": {"north": "Living Room", 'item': 'costumes'},
        "Kitchen": {"east": "Living Room", 'item': 'food and drinks'}
    }

    # Establish inventory and current room variables
    inventory = []
    current_room = "Living Room"

    show_instructions()

    def show_status():
        print("Currently in the {}".format(current_room))
        print("Inventory: {}".format(", ".join(inventory)))
        if 'item' in rooms[current_room]:
            print('You see {}'.format(rooms[current_room]['item']))

    while True:
        show_status()

        # Get the player's move command
        command = input(
            'Enter a direction ("North", "South", "East", "West"), "get (item)", or "exit" to quit: ').strip().lower()

        # Handle the exit command
        if command == 'exit':
            print('Thanks for playing!')
            break

        # Check if there is an item in the current room and the command matches
        elif 'item' in rooms[current_room] and command == 'get {}'.format(rooms[current_room]['item']):
            item = rooms[current_room]['item']
            if item not in inventory:
                inventory.append(item)
                print('Added {} to your inventory'.format(item))
            else:
                print('You already have this item.')

        # Check if the command is a valid direction in the current room
        elif command in rooms[current_room]:
            # Move to the new room
            current_room = rooms[current_room][command]

            # Check for the birthday girl and whether the game is won or lost
            if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Birthday Girl':
                if len(inventory) == 6:  # 6 items needed to win the game
                    beat_game()
                    break
                else:
                    game_over()
                    break
        else:
            # Invalid move or command
            print('Invalid move! Please enter a valid command.')


# Run main
main()

import random

class ZombieDice:
    def __init__(self):
        # Dice colors and faces
        self.dice_colors = ["Green", "Green", "Green", "Yellow", "Yellow", "Red"]
        self.dice_faces = {
            "Green": ["Brain", "Brain", "Brain", "Footsteps", "Footsteps", "Shotgun"],
            "Yellow": ["Brain", "Brain", "Footsteps", "Footsteps", "Shotgun", "Shotgun"],
            "Red": ["Brain", "Footsteps", "Footsteps", "Shotgun", "Shotgun", "Shotgun"]
        }
    
    def roll_die(self, die_color):
        return random.choice(self.dice_faces[die_color])

    def play_turn(self):
        brains = 0
        shotguns = 0

        print("\nStarting a new turn!")
        while True:
            print(f"Brains: {brains}, Shotguns: {shotguns}")
            
            # End turn if player is shot 3 times
            if shotguns >= 3:
                print("You got shot 3 times! Your turn ends.")
                return 0
            
            # Draw dice
            dice_to_roll = random.sample(self.dice_colors, 3)
            print(f"Rolling: {dice_to_roll}")
            
            # Roll each die
            for die in dice_to_roll:
                result = self.roll_die(die)
                print(f"{die} die result: {result}")
                if result == "Brain":
                    brains += 1
                elif result == "Shotgun":
                    shotguns += 1

            # Ask if the player wants to continue
            choice = input("Do you want to roll again? (y/n): ").lower()
            if choice != 'y':
                print("Ending turn.")
                break

        return brains

    def play_game(self):
        print("Welcome to Zombie Dice!")
        total_brains = 0

        while True:
            total_brains += self.play_turn()
            print(f"Total brains: {total_brains}")
            play_again = input("Do you want to play another turn? (y/n): ").lower()
            if play_again != 'y':
                print(f"Game over! Total brains collected: {total_brains}")
                break


if __name__ == "__main__":
    game = ZombieDice()
    game.play_game()

from location import Location
from player import Player
from station_item import DiagnosticTool, EnergyCrystal
from damaged_maintenance_droid import DamagedMaintenanceDroid

class GameController:
    """
    Controls the main game loop and manages the game state.
    """
    def __init__(self):
        """Initialize the game world and player."""
        self.setup_game()
        self.player = Player(self.maintenance_tunnels)
        self.game_over = False
    
    def setup_game(self) -> None:
        """Set up the game world with locations and items."""
        # Create locations
        self.maintenance_tunnels = Location(
            "Maintenance Tunnels",
            "You are in the dimly lit maintenance tunnels of the space station. "
            "The walls are lined with pipes and conduits. To the east is the Docking Bay."
        )
        
        self.docking_bay = Location(
            "Docking Bay",
            "You are in the spacious Docking Bay. Ships come and go from here. "
            "To the west are the Maintenance Tunnels."
        )
        
        # Connect locations
        self.maintenance_tunnels.add_exit("east", self.docking_bay)
        self.docking_bay.add_exit("west", self.maintenance_tunnels)
        
        # Add items to locations
        self.maintenance_tunnels.add_item(DiagnosticTool())
        self.docking_bay.add_item(EnergyCrystal())
        
        # Add the droid to block the path
        self.maintenance_tunnels.droid_present = True
    
    def start(self) -> None:
        """Start the game."""
        print("Welcome to Space Station Maintenance!")
        print("Type 'help' for a list of commands.\n")
        print(self.player.current_location.describe())
        
        while not self.game_over:
            self.process_command()
    
    def process_command(self) -> None:
        """Get and process a command from the player."""
        command = input("\n> ").strip().lower()
        
        if command in ["north", "south", "east", "west"]:
            print(self.player.move(command))
        elif command == "look":
            print(self.player.current_location.describe())
        elif command == "take":
            print(self.player.take_item())
        elif command == "use":
            print(self.player.use_tool())
        elif command == "inventory" or command == "i":
            print(self.player.get_inventory())
        elif command == "score":
            print(self.player.get_status())
        elif command == "win":
            if self.player.current_location == self.docking_bay:
                self.player.score += 30  # Bonus for winning
                print(f"Congratulations! You've completed your mission!\nFinal Score: {self.player.score} | Hazards: {self.player.hazards}")
                self.game_over = True
            else:
                print("You can't win from here. You need to be in the Docking Bay.")
        elif command in ["help", "?"]:
            self.show_help()
        elif command in ["quit", "exit"]:
            print("Thanks for playing!")
            self.game_over = True
        else:
            print("I don't understand that command. Type 'help' for a list of commands.")
    
    def show_help(self) -> None:
        """Display the help text."""
        help_text = """
Available Commands:
  north/south/east/west - Move in that direction
  look - Look around the current location
  take - Pick up an item
  use - Use the diagnostic tool on the droid
  inventory (or i) - Check your inventory
  score - Check your score and hazards
  win - Complete the mission (only in Docking Bay)
  help - Show this help message
  quit - Exit the game
"""
        print(help_text)


def main():
    """Entry point for the game."""
    game = GameController()
    game.start()

if __name__ == "__main__":
    main()

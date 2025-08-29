from typing import List, Optional
from station_item import StationItem

class Player:
    """
    Represents the player in the game, tracking inventory and score.
    """
    def __init__(self, starting_location):
        """
        Initialize a new player.
        
        Args:
            starting_location: The initial location of the player
        """
        self.current_location = starting_location
        self.inventory: List[StationItem] = []
        self.score = 0
        self.hazards = 0
    
    def move(self, direction: str) -> str:
        """
        Attempt to move the player in the given direction.
        
        Args:
            direction (str): The direction to move
            
        Returns:
            str: A message describing the result of the movement attempt
        """
        new_location = self.current_location.get_exit(direction)
        if new_location is None:
            return "You can't go that way."
        
        # Check if trying to enter the Docking Bay with the droid still blocking
        if new_location.name == "Docking Bay" and self.current_location.droid_present:
            self.hazards += 1
            return "The maintenance droid is blocking the way to the Docking Bay! You'll need to repair it first."
            
        # Check if the path is blocked by the droid
        if new_location.droid_present:
            self.hazards += 1
            return "A maintenance droid blocks your path! You'll need to repair it first."
        
        self.current_location = new_location
        return f"You move {direction} to {new_location.name}.\n\n{new_location.describe()}"
    
    def take_item(self) -> str:
        """
        Take an item from the current location.
        
        Returns:
            str: A message describing the result of the attempt
        """
        if not self.current_location.has_item:
            return "There's nothing here to take."
        
        item = self.current_location.remove_item()
        if item is None:
            return "You can't take that."
        
        self.inventory.append(item)
        
        # Update score based on item taken
        if item.name == "diagnostic tool":
            self.score += 10
            return "You take the diagnostic tool. (+10 points)"
        elif item.name == "energy crystal":
            self.score += 50
            return "You take the energy crystal. (+50 points)"
        
        return f"You take the {item.name}."
    
    def use_tool(self) -> str:
        """
        Use the diagnostic tool on the droid.
        
        Returns:
            str: A message describing the result of the action
        """
        # Check if player has the diagnostic tool
        tool = next((item for item in self.inventory if item.name == "diagnostic tool"), None)
        if tool is None:
            return "You don't have a diagnostic tool to use."
        
        # Check if there's a droid in the current location
        if not self.current_location.droid_present:
            return "There's nothing here to use the diagnostic tool on."
        
        # If we get here, we're using the tool on the droid
        self.score += 20
        self.current_location.droid_present = False
        return "You use the diagnostic tool on the droid. It beeps and moves aside! (+20 points)"
    
    def get_inventory(self) -> str:
        """
        Get a description of the player's inventory.
        
        Returns:
            str: A formatted list of items in the inventory
        """
        if not self.inventory:
            return "You're not carrying anything."
        
        items = "\n".join(f"- {item.name}" for item in self.inventory)
        return f"You are carrying:\n{items}"
    
    def get_status(self) -> str:
        """
        Get the player's current status.
        
        Returns:
            str: A formatted status message
        """
        return f"Score: {self.score} | Hazards: {self.hazards}"

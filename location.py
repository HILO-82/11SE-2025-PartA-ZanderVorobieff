from typing import Dict, Optional, Tuple
from station_item import StationItem, DiagnosticTool, EnergyCrystal

class Location:
    """
    Represents a place in the game world.
    """
    def __init__(self, name: str, description: str):
        """
        Initialize a new location.
        
        Args:
            name (str): The name of the location
            description (str): A description of the location
        """
        self.name = name
        self.description = description
        self.exits: Dict[str, 'Location'] = {}
        self._item: Optional[StationItem] = None
        self._droid_present: bool = False
    
    def add_exit(self, direction: str, location: 'Location') -> None:
        """
        Add an exit to another location.
        
        Args:
            direction (str): The direction of the exit (e.g., 'north', 'east')
            location (Location): The location this exit leads to
        """
        self.exits[direction.lower()] = location
    
    def get_exit(self, direction: str) -> Optional['Location']:
        """
        Get the location in the given direction, if it exists.
        
        Args:
            direction (str): The direction to check
            
        Returns:
            Optional[Location]: The location in that direction, or None if no exit exists
        """
        return self.exits.get(direction.lower())
    
    def add_item(self, item: StationItem) -> bool:
        """
        Add an item to this location.
        
        Args:
            item (StationItem): The item to add
            
        Returns:
            bool: True if the item was added, False if the location already has an item
        """
        if self._item is None:
            self._item = item
            return True
        return False
    
    def remove_item(self) -> Optional[StationItem]:
        """
        Remove and return the item from this location.
        
        Returns:
            Optional[StationItem]: The removed item, or None if there was no item
        """
        item = self._item
        self._item = None
        return item
    
    @property
    def has_item(self) -> bool:
        """Check if this location has an item."""
        return self._item is not None
    
    @property
    def item(self) -> Optional[StationItem]:
        """Get the item at this location, if any."""
        return self._item
    
    @property
    def droid_present(self) -> bool:
        """Check if the droid is present at this location."""
        return self._droid_present
    
    @droid_present.setter
    def droid_present(self, value: bool) -> None:
        """Set whether the droid is present at this location."""
        self._droid_present = value
    
    def describe(self) -> str:
        """
        Generate a description of this location.
        
        Returns:
            str: A formatted description of the location and its contents
        """
        description = f"{self.name}\n{'-' * 20}\n{self.description}\n"
        
        # Add item description if present
        if self._item:
            description += f"\nYou see a {self._item.name} here."
        
        # Add droid description if present
        if self._droid_present:
            description += "\nA maintenance droid blocks the way!"
        
        # Add exit information
        if self.exits:
            exits = ", ".join(self.exits.keys())
            description += f"\n\nExits: {exits}"
        
        return description

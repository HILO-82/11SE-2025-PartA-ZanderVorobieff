class StationItem:
    """
    Base class for all items in the game.
    """
    def __init__(self, name: str, description: str):
        """
        Initialize a new station item.
        
        Args:
            name (str): The name of the item
            description (str): A description of the item
        """
        self._name = name
        self._description = description
    
    @property
    def name(self) -> str:
        """Get the item's name."""
        return self._name
    
    @property
    def description(self) -> str:
        """Get the item's description."""
        return self._description
    
    def examine(self) -> str:
        """
        Returns a text description specific to the item.
        
        Returns:
            str: A description of the item
        """
        return self._description


class DiagnosticTool(StationItem):
    """
    The tool used to repair the droid.
    """
    def __init__(self):
        super().__init__(
            name="diagnostic tool",
            description="A handheld device for repairing electronic systems."
        )
    
    def examine(self) -> str:
        """Return a description of the diagnostic tool."""
        return "This diagnostic tool seems designed to interface with maintenance droids."


class EnergyCrystal(StationItem):
    """
    The volatile crystal that the player must collect.
    """
    def __init__(self):
        super().__init__(
            name="energy crystal",
            description="A glowing crystal pulsing with unstable energy."
        )
    
    def examine(self) -> str:
        """Return a description of the energy crystal."""
        return "The crystal pulses with an unstable, vibrant energy."

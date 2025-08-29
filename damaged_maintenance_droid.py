class DamagedMaintenanceDroid:
    """
    A damaged maintenance droid that blocks the player's path until repaired.
    """
    def __init__(self):
        """Initialize the droid as blocking by default."""
        self._blocking = True
    
    @property
    def is_blocking(self) -> bool:
        """Check if the droid is currently blocking the path."""
        return self._blocking
    
    def repair(self) -> bool:
        """
        Attempt to repair the droid.
        
        Returns:
            bool: True if the droid was repaired (previously blocking), 
                  False if it was already repaired
        """
        was_blocking = self._blocking
        self._blocking = False
        return was_blocking
    
    def examine(self) -> str:
        """
        Get a description of the droid's current state.
        
        Returns:
            str: A description of the droid
        """
        if self._blocking:
            return "A damaged maintenance droid blocks your path. It appears to be in standby mode."
        return "The maintenance droid is now functioning normally and has moved aside."

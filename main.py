from game_controller import GameController

def main():
    """
    Main entry point for the Space Station Maintenance game.
    """
    try:
        game = GameController()
        game.start()
    except KeyboardInterrupt:
        print("\n\nGame ended by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please report this issue to the game developer.")

if __name__ == "__main__":
    main()

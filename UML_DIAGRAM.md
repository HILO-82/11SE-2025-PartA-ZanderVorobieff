# Space Station Maintenance - UML Class Diagram

```mermaid
classDiagram
    %% Main Game Controller
    class GameController {
        +maintenance_tunnels: Location
        +docking_bay: Location
        +player: Player
        +game_over: bool
        +__init__()
        +setup_game()
        +start()
        +process_command(command: str)
        +show_help()
    }

    %% Player Class
    class Player {
        -current_location: Location
        -inventory: StationItem[*]
        -score: int
        -hazards: int
        +move(direction: str) str
        +take_item() str
        +use_tool() str
        +get_inventory() str
        +get_status() str
    }

    %% Location Class
    class Location {
        -name: str
        -description: str
        -exits: Map~String, Location~
        -_item: StationItem
        -_droid_present: bool
        +add_exit(direction: str, location: Location)
        +get_exit(direction: str) Location
        +add_item(item: StationItem) bool
        +remove_item() StationItem
        +describe() str
    }

    %% Base Item Class
    <<interface>> StationItem
    class StationItem {
        <<abstract>>
        +name: str
        +description: str
        +use() str
    }

    %% Item Implementations
    class DiagnosticTool {
        +use() str
    }

    class EnergyCrystal {
        +use() str
    }

    %% Droid Class
    class DamagedMaintenanceDroid {
        -is_repaired: bool
        +repair() str
    }

    %% Relationships
    GameController "1" *-- "1" Player : contains >
    GameController "1" *-- "*" Location : contains >
    Player "1" -- "0..1" Location : current location
    Player "*" -- "*" StationItem : inventory
    Location "1" -- "0..1" StationItem : contains
    StationItem <|-- DiagnosticTool
    StationItem <|-- EnergyCrystal
    Location "1" -- "0..1" DamagedMaintenanceDroid : contains
```

## Diagram Notes

1. **Composition** (filled diamond):
   - GameController owns Player and Locations
   - Locations own Items

2. **Association** (solid line):
   - Player interacts with Locations and Items

3. **Inheritance** (hollow triangle):
   - StationItem is the parent class of specific items

4. **Multiplicity**:
   - `*` means "many"
   - `0..1` means "zero or one"
   - `1` means exactly one

## How to Use
1. Copy the Mermaid code to any Mermaid-compatible editor
2. Most modern IDEs support Mermaid with plugins
3. You can also use the [Mermaid Live Editor](https://mermaid.live/) to view/edit the diagram

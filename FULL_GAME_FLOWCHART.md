# Full Game Flowchart - Space Station Maintenance

This flowchart represents the complete functionality of the Space Station Maintenance game, including all commands, win conditions, and game states.

```mermaid
flowchart TD
    %% ========== GAME INITIALIZATION ==========
    A([Start]) --> B[Initialize Game]
    B --> C[Create Game World]
    C --> D[Create Player]
    D --> E[Display Welcome Message]
    
    %% ========== MAIN GAME LOOP ==========
    E --> F[Display Location Info]
    F --> G[Get Player Input]
    
    %% ========== COMMAND PROCESSING ==========
    G --> H{Parse Command}
    
    %% ----- Movement Command -----
    H -->|"north", "south", "east", "west"| I[Check Direction]
    I --> J{Valid Direction?}
    J -->|No| K[Show "You can't go that way"]
    J -->|Yes| L[Check Droid Blocking]
    L -->|Blocked| M[Show "Droid blocks your path!"]
    L -->|Clear| N[Move Player]
    N --> O[Check Location for Items]
    O --> P[Increment Hazard Counter]
    
    %% ----- Take Item Command -----
    H -->|"take"| Q[Check Item Present]
    Q -->|No Item| R[Show "No item here"]
    Q -->|Item Exists| S[Add to Inventory]
    S --> T[Update Score]
    T --> U[Remove Item from Location]
    U --> V[Show "You took the item"]
    
    %% ----- Use Command -----
    H -->|"use"| W[Check Holding Tool]
    W -->|No Tool| X[Show "You're not holding anything"]
    W -->|Has Tool| Y[Check Droid Present]
    Y -->|No Droid| Z[Show "Nothing to use it on"]
    Y -->|Droid Present| AA[Repair Droid]
    AA --> AB[Update Score]
    AB --> AC[Clear Blockage]
    AC --> AD[Show "Droid repaired!"]
    
    %% ----- Inventory Command -----
    H -->|"inventory"| AE[Show Inventory]
    
    %% ----- Score Command -----
    H -->|"score"| AF[Show Score]
    
    %% ----- Help Command -----
    H -->|"help"| AG[Show Help Text]
    
    %% ----- Quit Command -----
    H -->|"quit"| AH[End Game]
    
    %% ========== WIN/LOSE CONDITIONS ==========
    %% Win Condition
    O --> AI{In Docking Bay?}
    AI -->|Yes| AJ{Has Energy Crystal
    AND Droid Repaired?}
    AJ -->|Yes| AK[Add Bonus Points]
    AK --> AL[Show Win Message]
    AL --> AM([End Game - Win!])
    
    %% Partial Win Condition (Docking Bay but missing requirements)
    AJ -->|No| AN[Show What's Missing]
    AN --> F
    
    %% Hazard Check
    P --> AO{Hazards > 3?}
    AO -->|Yes| AP[Show Game Over Message]
    AP --> AQ([End Game - Lose])
    AO -->|No| F
    
    %% ========== ERROR HANDLING ==========
    %% Return to Main Loop
    K --> F
    M --> F
    R --> F
    X --> F
    Z --> F
    AE --> F
    AF --> F
    AG --> F
    
    %% ========== STYLING ==========
    classDef startEnd fill:#f9f,stroke:#333,stroke-width:2px,color:#fff;
    classDef process fill:#bbf,stroke:#333,stroke-width:2px;
    classDef decision fill:#f96,stroke:#333,stroke-width:2px;
    classDef success fill:#9f9,stroke:#333,stroke-width:2px;
    classDef error fill:#f99,stroke:#333,stroke-width:2px;
    
    %% Apply Styles
    class A,AM,AQ startEnd;
    class B,C,D,E,F,G,I,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AF,AG,AH,AI,AK,AL,AN,AO,AP process;
    class H,J,AJ decision;
    class AK,AL success;
    class K,M,R,X,Z,AN,AP error;
```

## Game Flow Explanation

### 1. Game Initialization
- Creates the game world with all locations
- Sets up the player character
- Displays welcome message and instructions

### 2. Main Game Loop
- Continuously displays current location and available actions
- Processes player input
- Updates game state
- Checks win/lose conditions

### 3. Command Processing
- **Movement**: Handles player navigation between locations
- **Take Item**: Manages item collection and inventory
- **Use Item**: Handles tool usage (specifically for droid repair)
- **Game State**: Shows inventory, score, and help
- **Game Control**: Allows quitting the game

### 4. Win Conditions
To win the game, the player must:
1. Collect the Energy Crystal
2. Repair the droid using the Diagnostic Tool
3. Reach the Docking Bay

### 5. Lose Condition
- The game ends if the player encounters more than 3 hazards

## How to Use This Flowchart
1. The flowchart is written in Mermaid.js syntax
2. Copy the code into any Mermaid-compatible editor
3. The chart will render automatically
4. Follow the arrows to trace different game paths

## Key Features
- Clear visualization of all game states
- Shows all possible player actions
- Details win/lose conditions
- Includes error handling and feedback messages
- Color-coded for better readability

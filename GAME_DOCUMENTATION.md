# Space Station Maintenance - Game Documentation

## Overview
Space Station Maintenance is a text-based adventure game where the player navigates through a space station, collects items, and completes objectives to win the game.

## Core Gameplay

### Objective
- Navigate to the Docking Bay to win the game
- Collect items to increase your score
- Avoid hazards to minimize penalties

### Game World
- **Maintenance Tunnels**: Starting location with dim lighting and pipes
- **Docking Bay**: Destination to win the game

## Game Components

### 1. Player
- **Attributes**:
  - `current_location`: Tracks player's position
  - `inventory`: List of collected items
  - `score`: Player's current score
  - `hazards`: Number of hazards encountered

### 2. Locations
- **Properties**:
  - Name and description
  - Connected exits (north, south, east, west)
  - Items available in the location
  - Droid presence indicator

### 3. Items
- **Diagnostic Tool**:
  - Found in Maintenance Tunnels
  - Used to repair the maintenance droid
  - Adds 10 points when collected

- **Energy Crystal**:
  - Found in Docking Bay
  - Valuable item worth 50 points

### 4. Damaged Maintenance Droid
- Blocks access to the Docking Bay
- Must be repaired using the diagnostic tool
- Awards 20 points when repaired

## Game Commands

| Command       | Description                                      |
|---------------|--------------------------------------------------|
| north/south/east/west | Move in the specified direction          |
| look          | View current location description                |
| take          | Pick up an item from the current location        |
| use           | Use the diagnostic tool on the droid             |
| inventory (i) | View items in your inventory                     |
| score         | Check current score and hazards                  |
| win           | Complete the mission (only in Docking Bay)       |
| help          | Show list of available commands                  |
| quit/exit     | Exit the game                                    |

## Scoring System
- Collect Diagnostic Tool: +10 points
- Collect Energy Crystal: +50 points
- Repair Droid: +20 points
- Reach Docking Bay: +30 points (win condition)
- Hazard Penalty: -1 point per hazard (when blocked by droid)

## Game Flow
1. Game starts in Maintenance Tunnels
2. Player must collect the diagnostic tool
3. Use the tool on the droid blocking the Docking Bay
4. Navigate to the Docking Bay to win

## Technical Implementation
- **Main Loop**: Handles user input and game state
- **Command Processing**: Parses and executes player commands
- **World State**: Tracks locations, items, and game progress
- **Scoring System**: Manages points and hazards

## Classes and Their Responsibilities

### GameController
- Manages game state and flow
- Processes player commands
- Handles game initialization

### Player
- Tracks player's inventory and score
- Handles movement between locations
- Manages item interactions

### Location
- Represents game locations
- Manages exits and items
- Handles droid presence

### StationItem (Base Class)
- Base class for all in-game items
- Extended by specific item types

### DiagnosticTool & EnergyCrystal
- Specific item implementations
- Define item properties and behaviors

Year 11 Software Engineering - Blended mechatronics / OOP project 
___________________________________________________________________________________________________________________________________________________________________

  Syllabus Outcomes Addressed:

This project will allow you to demonstrate your understanding and application of the following NESA Software Engineering Stage 6 Syllabus Outcomes:

SE-11-01: describes methods used to plan, develop and engineer software solutions

SE-11-02: explains how structural elements are used to develop programming code

SE-11-03: describes how current hardware, software and emerging technologies influence the development of software engineering solutions

SE-11-06: applies tools and resources to design, develop, manage and evaluate software

SE-11-07: implements safe and secure programming solutions

SE-11-08: applies language structures to refine code

SE-11-09: manages and documents the development of a software project

Overall Weighting: This entire assessment (Parts A, B, C, and D combined) contributes [40%] to your final course grade.
___________________________________________________________________________________________________________________________________________________________________
  
  Overview:

Welcome, Engineer, to Project Orbital Operations Platform! This mission challenges you to develop your Object-Oriented Programming (OOP) skills and then apply them in a collaborative Mechatronics context, all within an engaging Science Fiction RPG.

  This project is divided into several parts:

Part A (Individual): You will individually design and build a text-based Sci-Fi Role-Playing Game (RPG) in Python, showcasing strong OOP principles. (SE-11-01, SE-11-02, SE-11-06, SE-11-08, SE-11-09)

Part B (Team-Based - Details Forthcoming): You will then, as part of a team, design, construct, and program a physical piece of Sci-Fi hardware (using a Raspberry Pi 5 and provided kit) that is thematically linked to the RPG concept. This part will emphasise collaborative development, hardware integration, and OOP control. (Details for Part B, including team formation and specific GitHub requirements for teams, will be provided separately. (SE-11-01, SE-11-02, SE-11-03, SE-11-06, SE-11-07, SE-11-08, SE-11-09)

Part C (Individual Submission, incorporating elements from Part A & B): You will produce an integrated documentation report covering your individual work on Part A and your contributions to the team-based Part B. (SE-11-01, SE-11-09, and incorporates documentation of SE-11-02, SE-11-03, SE-11-06, SE-11-08).

Part D (Individual Online Examination - Details Forthcoming): An individual online examination will assess your comprehension of concepts applied throughout the project. (Details for Part D will be provided separately. It will assess understanding across all relevant outcomes.)
___________________________________________________________________________________________________________________________________________________________________
  
  This project assesses your ability to:

Analyse system requirements using the COIPEA framework. (SE-11-01, SE-11-09)

Design complex software using OOP principles. (SE-11-01, SE-11-02)

Effectively use tools like an IDE and potentially version control (e.g., personal GitHub repository for Part A, mandatory shared repository for Part B). (SE-11-06, SE-11-09)

(In Part B) Interface software (Python) with hardware (Raspberry Pi and components). (SE-11-03, SE-11-06)

Apply systematic documentation practices. (SE-11-01, SE-11-09)

Reflect critically on the design and development process. (SE-11-01, SE-11-09)

You will leverage skills developed during the Hangman project, adapting state management, modularity, and logical control flow to the OOP paradigm. (SE-11-02, SE-11-08)
___________________________________________________________________________________________________________________________________________________________________

  Assessment Components & Weightings:

Part A: OOP Sci-Fi Text-Based RPG (Software Focus) - Individual Project - Weighting: 25%

Part B: Mechatronics Sci-Fi Physical Interface (Hardware & OOP Control Focus) - Team Project (Details Forthcoming) - Weighting: 25%

Part C: Integrated Documentation & Project Management - Individual Submission - Weighting: 25%

Part D: Code & Concept Comprehension Online Exam - Individual Assessment (Details Forthcoming) - Weighting: 25%
___________________________________________________________________________________________________________________________________________________________________

  Part A: OOP Sci-Fi Text-Based RPG (Software Focus) - Individual Project - Weighting: 25%
  (Primarily addresses: SE-11-01, SE-11-02, SE-11-06, SE-11-08, SE-11-09)

Vibe Coding is NOT ALLOWED. If you use any AI assistance, you must transparently document it in your logbook—include the original generated code and explain any edits you made. Treat AI as your intern: you will be tested on your code. If you do not fully understand any AI‐generated snippet, explicitly ask AI to explain and teach it to you; if you still cannot replicate or explain it, do not use that code.

  1. Game Overview
Your task is to build a minimal text-based RPG in Python. The player must follow a fixed “golden path” and earn points exactly as described below. If the player tries to move past the droid before it is repaired, a hazard counter increases. At the end, the game displays total score and hazards.

Golden Path Steps (in order):

Maintenance Tunnels: Player begins here.

Pick up the Diagnostic Tool (awards +10 points).

Use the Diagnostic Tool on the Damaged Maintenance Droid (awards +20 points) to clear it.

Move to Docking Bay.

Pick up the Energy Crystal (awards +50 points).

Type “win” (from Docking Bay) to complete the mission (awards +30 points).

Hazard Rule:

If the player tries to move east (toward Docking Bay) while the droid is still blocking, increment the hazard counter by 1 and display a “droid blocking” message.

  2. Classes, Attributes & Methods
Below are the exact classes you must create. Each class lists its attributes (names only—no data types) and its method names. You decide how to implement them internally, but do not rename any class, attribute, or method.

  1. StationItem (parent of both tool classes)
Purpose: Serves as a common parent for any item the player can pick up.

Attributes:

_name

_description

Methods:

examine()

Returns a text description specific to the item. Both subclasses override this.

  2. DiagnosticTool (inherits from StationItem)
Purpose: The tool used to repair the droid.

Parent: StationItem

Attributes:

(inherits _name and _description)

Methods:

examine()

Returns a hint such as “This diagnostic tool seems designed to interface with maintenance droids.”

  3. EnergyCrystal (inherits from StationItem)
Purpose: The volatile crystal that the player must collect.

Parent: StationItem

Attributes:

(inherits _name and _description)

Methods:

examine()

Returns a description like “The crystal pulses with an unstable, vibrant energy.”

  4. Location
Purpose: Represents a place in the game world. Each location can hold exactly one tool, one crystal, and/or the droid.

Attributes:

name

description

exits

has_tool

has_crystal

droid_present

Methods:

__init__

Initialise the location’s name, description, and default flags (no tool, no crystal, no droid).

add_exit(direction, other_location)

Record that a given direction (e.g. “east”) leads to another Location.

describe()

Return a formatted string that includes:

The location’s name and description.

“You see a diagnostic tool here.” if has_tool is True.

“You see an energy crystal here.” if has_crystal is True.

“A maintenance droid blocks the way!” if droid_present is True.

“Exits: <list of directions>.”

remove_tool()

If has_tool is True, clear that flag and indicate success; otherwise indicate failure.

remove_crystal()

If has_crystal is True, clear that flag and indicate success; otherwise indicate failure.

set_droid_present(flag)

Set the droid_present flag to True or False.

  5. DamagedMaintenanceDroid
Purpose: Blocks passage in Maintenance Tunnels until “repaired.”

Attributes:

blocking

Methods (purpose only):

__init__

Set blocking to True initially.

repair()

Change blocking to False.

is_blocking()

Return whether blocking is still True.

  6. Player
Purpose: Tracks the player’s current location, which items they hold, and their score/hazard counts.

Attributes:

current_location

has_tool

has_crystal

score

hazard_count

Methods:

__init__(starting_location)

Set current_location to the given Location; set has_tool and has_crystal to False, and score and hazard_count to zero.

move(direction)

Attempt to change current_location in the given direction:
• If no such exit exists, return failure.
• If the droid is still blocking, increment hazard_count, return failure.
• Otherwise update current_location and return success.

pick_up_tool()

If current_location.has_tool is True, clear that flag, set has_tool to True, add 10 to score, and return success; otherwise return failure.

use_tool_on_droid()

If has_tool is True and current_location.droid_present is True, call the droid’s repair method, clear droid_present, add 20 to score, return success; otherwise return failure.

pick_up_crystal()

If current_location.has_crystal is True, clear that flag, set has_crystal to True, add 50 to score, return success; otherwise return failure.

get_status()

Return the current score and hazard count (students decide how to format).

  7. GameController
Purpose: Creates and links all objects, runs the main input loop, and checks if the player wins.

Attributes:

maintenance_tunnels

docking_bay

droid

player

diagnostic_tool

energy_crystal

Methods:

__init__

Build the world (all locations, the droid, the two items, and the player).

setup_world()

Create two Location instances: one for “Maintenance Tunnels,” one for “Docking Bay.”

Indicate that Maintenance Tunnels starts with has_tool = True and droid_present = True.

Indicate that Docking Bay starts with has_crystal = True.

Link the two locations so that “east” from Maintenance Tunnels goes to Docking Bay, and “west” from Docking Bay goes back.

Instantiate a DamagedMaintenanceDroid and store it.

Instantiate one DiagnosticTool and one EnergyCrystal (students decide how these are held).

Instantiate a Player whose starting_location is Maintenance Tunnels.

start_game()

Print a welcome message. Then repeat:

Show current_location.describe().

Read a single line of input (allowed commands below).

Call process_input(command).

Call check_win_condition(). If True, break and end.

process_input(command)

Recognise exactly these commands (case-insensitive):

“move <direction>” → call player.move(direction) and print an appropriate message for success or failure (blocked by droid or no exit).

“pick up tool” → call player.pick_up_tool() and print success or “no tool here.”

“use tool” → call player.use_tool_on_droid() and print success or “nothing happens.”

“pick up crystal” → call player.pick_up_crystal() and print success or “no crystal here.”

“status” → call player.get_status() and print “Score: <score> Hazards: <hazard_count>”.

“win” → do nothing here (the check happens next).

Anything else → print “Invalid command.”

check_win_condition()

If all of these are true:

player.current_location is Docking Bay

player.has_crystal is True

the last command was “win”

Then add 30 to player.score, print:

Mission complete! Final Score: <score> Total Hazards: <hazard_count>
and return True; otherwise return False.

You may add any extra storyline around this, as long as the minimum requirements are met and demonstrable.  
___________________________________________________________________________________________________________________________________________________________________

  3. UML Class Diagram (Mermaid)
Below is a Mermaid‐format UML diagram showing how the current classes relate. You must modify this if you create other classes beyond those shown in this diagram.

image.png

  4. How to Use This Spec
Create a Storyboard First

Draw 8-10 boxes showing what the player sees and types at each golden-path step. Each box should include:

The output of player.current_location.describe().

The player’s typed command (e.g. “pick up tool”).

The game’s printed response (e.g. “You pick up the diagnostic tool. (+10)”).

Any score or hazard count updates shown.

The sequential flow between each frame.
Ensure you cover these moments:

Maintenance Tunnels (show description, tool present, droid present).

“pick up tool” → tool removed, score +10.

“move east” before repair → droid blocks, hazard +1.

“use tool” → droid repaired, score +20, droid gone.

“move east” again → arrive at Docking Bay.

“pick up crystal” → crystal removed, score +50.

“status” → show “Score: 80 Hazards: 1.”

“win” → show final summary with bonus +30.

Refer to the UML Diagram Above

Note how each class relates:

Inheritance: StationItem → DiagnosticTool and EnergyCrystal.

Aggregation (open diamond o--):

Location “contains” a DamagedMaintenanceDroid.

Player “uses” a Location as its current_location.

Composition (filled diamond *--):

GameController “owns” two Location instances, one DamagedMaintenanceDroid, one Player, one DiagnosticTool, and one EnergyCrystal.

Dependency (dashed arrow ..>):

Player methods call DamagedMaintenanceDroid’s repair() or is_blocking() without permanently owning a droid.

Implement Exactly These Classes & Methods

In your code, create each class with its listed attributes and methods.

Decide your own internal data structures (for example, how exits is stored).

In GameController.process_input(), recognise only the commands shown (move, pick up tool, use tool, pick up crystal, status, win).

Ensure that scoring and hazards adhere to the exact rules.

Optional Enhancements

After the minimal flow is established, you can add a “help” command or more detailed descriptions using AI or a random storyline.

Do not change any class names, method names, or scoring/hazard logic.

Deliverables

Storyboard (6–8 frames) capturing the UI/UX flow.

UML Diagram with your additions.

Flowcharts x 3

Movement (checks exits, handles blocking droid, updates location or hazard)

Use Tool (verifies tool possession, then checks and repairs the droid)

Win (validates both location and crystal before awarding bonus and ending

Structure Chart
Create a structure chart with start game loop at the top, branching into process player input and check win condition. Under process player input, include modules labeled move player, collect item, repair droid, show status, and attempt win, and draw arrows from each of those to the corresponding method calls.
___________________________________________________________________________________________________________________________________________________________________ 
  3-Week Plan
  
  Week 1: Planning & Design
Read the Spec & Sketch Ideas

Review the simplified RPG requirements (golden path, scoring, hazards).

In your logbook, note initial thoughts and any questions.

Git Commit #1: Create repository, add README with project overview and Part A goals.

Draft the Storyboard (6–8 Frames)

Sketch each key screen include the flow between each frame

Create UML Class Diagram

Recreate the mermaid code class diagram

Show relationships: inheritance, aggregation, composition, dependency.

  Week 2: Flowcharts & Initial Coding
Draw Three Flowcharts

Movement: Start “move <direction>,” check exit, handle blocking droid (hazard increment), or update location.

Use Tool: Start “use tool,” verify possession, check/repair droid.

Win: Start “win,” confirm location + crystal, award bonus or block.

Begin Core Class stubs

Create empty class files for each:

StationItem.py, DiagnosticTool.py, EnergyCrystal.py

Location.py, DamagedMaintenanceDroid.py, Player.py, GameController.py

In each file, define class name with empty methods.

Create markdown files (minimum CHANGELOG.md, PRD.md, TODO,md)
Git Commit: Push markdown files and class stubs with TODO comments for each method.

Implement Location & Droid Logic

In Location.py, implement __init__, add_exit(), describe(), remove_tool(), remove_crystal(), set_droid_present().

In DamagedMaintenanceDroid.py, implement __init__, repair(), is_blocking().

Git Commit: Commit completed Location and Droid classes, with initial unit tests in a separate tests/ folder.

  Week 3: Finalise Coding, Testing & Documentation
Complete Player & GameController Logic

In Player.py, implement __init__, move(), pick_up_tool(), use_tool_on_droid(), pick_up_crystal(), get_status().

In GameController.py, implement __init__, start_game(), process_input(), check_win_condition().

Git Commit: Push Player and GameController implementations with inline comments.

Testing & Evidence Collection

Write a test plan with at least five scenarios:

Move while blocked

Pick up tool

Use tool on droid

Pick up crystal

Win sequence

Capture screenshots or console transcripts for each scenario.

Git Commit #8: Add test scripts and sample run logs under tests/.

Embed Final Deliverables in Report

Insert the polished UML diagram, flowcharts, and storyboard into your report.

Include the final, well‐commented Python code.

Git Commit: Commit the final code in repo.

Logbook & Reflection

Ensure your logbook covers every session, including any AI help (include original vs edited code).

Write a one‐page reflection on challenges (OOP concepts, debugging) and what you learned from AI usage.

Git Commit #10: Add the completed logbook file and reflection section to repo.

Final Review & Submission Preparation

Proofread the report: Australian spelling, clear labels, consistent formatting.

Git Commit: Tag final commit as PartA_Final.

  2. Submission Instructions
Private GitHub Repo:

Ensure you have made at least 10 substantial commits (as above).

Repository should be shared only with the instructor.

Canvas Upload by 30 June 2025:

Export all .py files and related folders (e.g., tests/) into a ZIP file named YourName_PartA.zip.

Upload that ZIP to Canvas under the Part A assignment by midnight (AEST) 30 June 2025.
___________________________________________________________________________________________________________________________________________________________________

Part B: Mechatronics Sci-Fi Physical Interface (Hardware & OOP Control Focus) - Team Project (Details Forthcoming) - Weighting: 25%
(Primarily addresses: SE-11-01, SE-11-02, SE-11-03, SE-11-06, SE-11-07, SE-11-08, SE-11-09)
As part of Project Orbital Operations Platform, you will extend your Object-Oriented Programming (OOP) knowledge from the text-based RPG into a collaborative Mechatronics interface. In Part B of the assessment, your team will design, construct, and program a Sci-Fi inspired physical device using the Raspberry Pi 5, thematically linked to your "Mission C.O.I.P.E.A." scenario.

To complete this task, you are required to select and implement at least one (1) mechatronic component from each of the sections below. Each chosen component must be:

Purposefully integrated into your hardware concept (aligned with your RPG narrative or mission flow),

Controlled using Python in an OOP structure, with appropriate class definitions, encapsulation, and behavioural methods,

Documented clearly as part of your Part C submission (UML, flowcharts, etc.).

This glossary serves as a simplified technical reference for the types of components available in your provided hardware kit. It is designed to support your understanding of core mechatronic elements, and how these may interface with software systems using clean, object-oriented design.

⚠️ Tip: Think about how your mechatronic elements can enhance gameplay immersion. For example:

A servo motor might simulate a robotic arm retrieving the crystal.

A proximity sensor might detect player movement or act as a "security field".

LEDs or buzzers could reflect in-game health, hazards, or mission status.

You are encouraged to work creatively but within scope: focus on functionality, thematic consistency, and OOP clarity—not complexity. Support is available for wiring, coding, and class design.

Proceed below to review the categorised glossary, which includes concise definitions and examples suitable for your level. These are foundational to successfully completing Part B and understanding SE-11-03, SE-11-06, SE-11-07, and SE-11-08.

Mechatronic Components
___________________________________________________________________________________________________________________________________________________________________ 

  Part C: Integrated Documentation & Project Management - Individual Submission - Weighting: 25%
  (This entire part heavily focuses on SE-11-01, SE-11-06, and SE-11-09. Elements within also touch on SE-11-02 and SE-11-03 as you document your designs related    to those outcomes.)

Goal:
You will individually produce a single, comprehensive, and professionally presented report. This report will document your analysis, planning, design, development, and reflection for your individual Part A RPG ("Mission C.O.I.P.E.A"), and detail your specific roles, contributions, learning, and the outcomes of the team-based Part B Mechatronics project. The report must explicitly incorporate COIPEA where relevant and utilise the specified design tools and documentation practices. Use Australian spelling conventions throughout. (SE-11-01, SE-11-09)

Requirements:

Single Report (Individual Submission): Submit one integrated document (e.g., PDF). All diagrams should be embedded directly within the report and be clear, legible, and appropriately labelled. (SE-11-09)

Project Statement (Introduction Section):

Overall Project Overview: Briefly introduce the entire multi-part "Project [Your Chosen Project Name, e.g., OOP: Genesis Engine]" and its overarching Sci-Fi theme. State its aim to develop OOP skills and integrate software with hardware.

Part A Project Aim & Scope: Clearly state the specific aim of your individual Part A RPG ("Mission C.O.I.P.E.A."). Define its scope, outlining the key features and functionalities you implemented based on the provided scenario. Mention the core OOP principles (Class, Object, Inheritance, Polymorphism, Encapsulation, Abstraction) that your Part A project aimed to demonstrate.

Part B Project Aim & Scope (Brief): Briefly state the aim and scope of your team's Part B Mechatronics project (you will elaborate on your contributions later). Mention the thematic link to the RPG concept.

This section sets the stage for your entire report. (SE-11-01, SE-11-09)

COIPEA Analysis:

  Part A - RPG Concept: Provide a COIPEA (Class, Objects, Inheritance, Polymorphism, Encapsulation, Abstraction) analysis for your individual Part A RPG scenario. Explain how this analysis informed your design choices for the RPG. (SE-11-01)

  (Part B - Mechatronics Concept): (You will reference the team's COIPEA analysis for the Part B device, which will be part of the team's planning for Part B. Briefly summarise its key aspects here and how it linked to the RPG).

  Part A: RPG ("Mission C.O.I.P.E.A.") - Design & Development Documentation (Individual):

Pre-planning Evidence: Include scans/photos of your initial sketches, brainstorming notes, or draft diagrams for your Part A RPG. This demonstrates your iterative design process before final implementation. (SE-11-01, SE-11-09)

UML Class Diagram: A final, clear, correct, and fully labelled UML Class Diagram for your entire Part A RPG codebase. This must clearly show:

All classes you implemented (e.g., Player, Location, GameController, abstract StationItem, concrete item subclasses like DiagnosticTool, DamagedMaintenanceDroid or Droid class).

Attributes (with visibility markers if taught, e.g., private __attribute).

Methods (with parameters and return types if applicable).

Relationships: Inheritance (e.g., items from StationItem), Composition/Aggregation (e.g., Player has an inventory of Items; Location contains Items or NPCs), and any other significant associations.

Clear indication of abstract classes (e.g., StationItem italicised or marked {abstract}) and overridden methods.
(SE-11-01, SE-11-02, SE-11-09)

Data Flow Diagram (DFD - Context Level or Level 0): Create a DFD for a key process within your Part A RPG. For example:

"Player Uses Item on Target": Show the flow of data when the player inputs a "use [item] on [target]" command, how the GameController processes this, how it might interact with Player (inventory), Item (usability), and Target (NPC or environment object) objects, and the resulting feedback/state change.

Alternatively, "Player Movement" or "NPC Interaction" could be chosen.

Clearly label processes, data stores (if any implied by object states), external entities (Player via input), and data flows.
(SE-11-01, SE-11-09)

Structure Chart: Create a Structure Chart for one significant, complex function or method within your Part A RPG. For example:

The main method within your GameController that handles player input and dispatches actions.

The method responsible for resolving the use DiagnosticTool on DamagedMaintenanceDroid interaction, showing calls to other methods for checking conditions, updating states, and player scores.

Illustrate modules/methods, call hierarchy, and key parameters/data passed.
(SE-11-01, SE-11-02, SE-11-09)

Storyboard (Minimum 6-8 Frames): Create a storyboard illustrating the "Golden Path" (successful win sequence) of your Part A RPG. Each frame should depict:

A key screen/state in the game.

The player's input/action.

The game's textual output/response, including any score or hazard encounter changes.

Start from the game beginning and progress through all key steps of "Mission C.O.I.P.E.A." to the winning condition.
(SE-11-01, SE-11-09)

Source Code: Include your final, well-commented Python source code for Part A. This can be embedded as text or (if very long) provided as clearly labelled appendices or a link to your personal GitHub repository (if used and public).

Testing Evidence: Your detailed testing evidence for Part A (test plan, screenshots/descriptions of test runs) as specified in the Part A deliverables. (SE-11-01, SE-11-06)

  Part B: Mechatronics Project - Documentation of Individual Contribution to Team Project:

(Details for this section will be expanded when Part B is fully defined. It will include):

Brief overview of the team's final Part B device, its functionality, and thematic link.

Your Specific Role & Responsibilities: Clearly define what your role was within the team (e.g., lead programmer for a specific module, primary hardware assembler, documentation coordinator for specific diagrams).

Your Contributions: Detail your specific contributions to the team's design, fabrication, coding (e.g., specific classes or functions you wrote/co-wrote for the OOP control software, with reference to the team's GitHub), and documentation.

Team Diagrams You Contributed To: If your team divided the creation of diagrams for Part B (e.g., UML for control code, Wiring Diagram, Flowchart for device logic), specify which ones you had a significant hand in creating or were primarily responsible for, and include them here (or reference their location in a team submission if Part B has one).

Reference to the team's shared GitHub repository for Part B code.

Summary of team testing and your involvement.
(SE-11-01, SE-11-03, SE-11-06, SE-11-09)
___________________________________________________________________________________________________________________________________________________________________
  
  Logbook (Individual):

Submit your detailed, timestamped individual logbook covering both Part A development and your contributions to Part B.

For Part A: Record tasks undertaken, challenges faced, solutions found, design decisions made, specific OOP concepts applied, resources used (including any AI assistance with prompts and how output was used/adapted).

For Part B: Record your specific tasks within the team, individual challenges and solutions, contributions to team discussions and decisions, use of shared tools (like GitHub for the team), and any AI assistance.

This is a critical component for assessing your individual process and effort. (SE-11-09)

Reflection (Individual):

Part A Reflection:

Discuss your design process for the Part A RPG, including how COIPEA and planning tools (UML, DFD, Storyboard, Structure Chart) guided your development.

Reflect on the challenges you faced implementing the OOP principles (Class, Object, Inheritance, Polymorphism, Abstraction, Encapsulation) and how you overcame them.

Discuss what you learned about OOP from developing Part A.

Part B Reflection (Individual Perspective on Team Project):

Discuss your experience working in a team for the Mechatronics project.

Reflect on the challenges of integrating software with hardware.

Discuss the application of OOP principles to control physical hardware.

Comment on the team's use of collaborative tools (e.g., GitHub).

What did you learn from the Part B experience, both technically and in terms of teamwork?

Overall Learning:

How did this entire project (Parts A & B) enhance your understanding of software engineering?

How did skills from the Hangman project transfer or evolve?

If you used AI, critically evaluate its usefulness and limitations in this project.

What would you do differently or what further improvements could be made if you had more time?
(SE-11-01, SE-11-09, and reflects on application of all other relevant outcomes)

Presentation: The report must be professionally presented, well-organised, with all sections clearly labelled. Diagrams must be embedded directly, be of sufficient size and clarity (clear lines, legible text). Use Australian spelling conventions. (SE-11-09)

Key Additions/Clarifications in this Part C Revision:

Project Statement: Clearly defined with specific sub-points for overall, Part A, and Part B aims/scope.

Diagram Specificity:

UML Class Diagram (Part A): For the entire RPG codebase, with specific elements to include (abstract classes, overriding).

Data Flow Diagram (Part A): Specified choice (e.g., "Player Uses Item") and level (Context or Level 0).

Structure Chart (Part A): For one significant, complex function/method.

Storyboard (Part A): Minimum 6-8 frames, illustrating the "Golden Path."

Logbook: Emphasised as individual, covering both parts.

Reflection: Broken down for Part A, Part B (individual perspective on team), and Overall Learning.

Part B Section: Framed to capture individual contributions to the forthcoming team project.

Part D: Code & Concept Comprehension Online Exam - Individual Assessment (Details Forthcoming) - Weighting: 25%
(This part assesses individual understanding of concepts applied throughout the project, covering all relevant outcomes.)
Note: Full details for the Part D online examination, including format, scope, and specific topics covered from both your individual Part A and the team-based Part B, will be provided later in the course. It will require you to reference and explain aspects of your own submitted code (Part A), your team's code (Part B), diagrams, and analyses.

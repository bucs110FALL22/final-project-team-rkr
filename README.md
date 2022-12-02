# CS110 Project Proposal

# Arkanoid

## CS 110 Final Project

### Fall, 2022

### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

[repl](https://replit.com/join/udspqfxicu-romanpanchmia)

[slides](https://docs.google.com/presentation/d/1VBqLj7K3Fp3bzePjnTa2nCsM4RtaFZeKUjmoy5pQx8g/edit?usp=sharing)

### Team Name: RKR

#### Roman Panchmia and Kevin Cao

---

## Project Description

A simple recreation of Arkanoid, a block breaker arcade game. Controlling a paddle, the player is tasked with clearing blocks by deflecting a ball towards it without letting the ball hit the bottom edge of the playfield. Some blocks contain power-ups that have various effects, such as increasing the length of the paddle, creating additional balls, or turning the paddle into a laser cannon. Other blocks may be indestructible or require multiple hits to break.

---

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
- **Final GUI**
- **Level 1**

![Level 1](/etc/level_1.png)
- **Level 2**

![Level 2](/etc/level_2.png)
- **Level 3**

![Level 3](/etc/level_3.png)
- **Level 4**

![Level 4](/etc/level_4.png)
- **Game in Progress**

![Gaming](/etc/gaming.png)
- **Game Over**

![Game Over](/etc/game_over.png)
- **Win**

![Win](/etc/win.png)

---

## Program Design

- Non-Standard libraries
  - << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python.
    For each additional module you should include
    - url for the module documentation
    - a short description of the module >>
- Class Interface Design
  - << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
    - ![class diagram](assets/class_diagram.jpg)
- Classes

```
class Ball:
    attributes:
        speed
        angle
        changex
        changey
        damage
        x
        y
        image
        rect
    methods:
        follow_mouse
        update
        hit_vaus
        bounce
        hit_walls
        damages
```

```
class Vaus:
    attributes:
        width
        image
        rect
        rect.x
        rect.y
    methods:
        change_size
        update
```

```
class Brick:
    attributes:
        type
        hp
        image
        rect
        rect.x
        rect.y
    methods:
        take_damage
        get_hp
        get_type
```

## Project Structure and File List

The Project is broken down into the following file structure:

- main.py
- src
  - ball.py
  - brick.py
  - controller.py
  - vaus.py
- assets
  - background.png
  - ball.png
  - brick1.png
  - brick2.png
  - brick3.png
  - brick4.png
  - brick5.png
  - brick6.png
  - vaus.png
- etc
  - Misc

---

## Tasks and Responsibilities

- Roman: Worked as the creative designer by helping give ideas for various designs for the visual aspects of the game. Also filled out the ReadMe and Proposal for the project.
- Kevin: Front-end worked on the code for each class and tested to make sure it functioned. Used design information given by the design specialist to implement each class and the various code.

## Testing

- Everytime we implemented a new feature, such as the brick, or the paddle, we tested it.

## ATP

| Step | Procedure                                                      | Expected Results                                                                                                                                         |
| :--- | :------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01   | Open terminal, navigate to folder, and type, “python3 main.py” | Program starts                                                                                                                                           |
| 02   | Mouse Movement                                                 | Paddle will follow mouse x                                                                                                                               |
| 04   | Left Click                                                     | Launches the ball off the paddle into the bricks                                                                                                         |
| 05   | General Playtesting                                            |                                                                                                                                                          |
| 06   | Lose Life                                                      | If the ball doesn't make contact with the paddle, and hits the space under the paddle, the game resets and the player loses a life                       |
| 07   | Next Level                                                     | After all the bricks have been cleared on one level, the bricks reset with the level number going up and the addition of more bricks in different places |
| 08   | Win                                                            |                                                                                                                                                          |
| 09   | Lose                                                           | If all 3 lives are used up, the "game over" screen appears and the game is over                                                                          |
| 10   | Click Q key                                                    | Quits Game                                                                                                                                               |
| 11   | Click R key                                                    | Restarts Game                                                                                                                                            |
| 12   | Reopen Game to test High Score                                 |                                                                                                                                                          |

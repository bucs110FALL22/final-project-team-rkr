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

A simple recreation of Arkanoid, a block breaker arcade game. Controlling a paddle, the player is tasked with clearing blocks by deflecting a ball towards it without letting the ball hit the bottom edge of the playfield. As the bricks are broken, your score will go up with some blocks being worth more than others. The player has 3 lives and the goal is to break all the bricks to beat all levels before your lives run out.

---

## User Interface Design

- **Initial Concept**

  - **Start**
    ![Start](/etc/concept_start.png)
  - **Lose**
    ![Lose](/etc/concept_lose.png)
  - **Win**
    ![Win](/etc/concept_win.png)

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
  - Pygame
    - [Documentation](https://www.pygame.org/docs/)
    - A module designed for writing video games and includes computer graphics and sound libraries.
- Class Interface Design
  - ![class diagram](/etc/mvc.png)
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

```
class GUI:
    attributes:
        screen
        bg
        font
        big_font
        small_font
    methods:
        instructions
        keybinds
        draw_vauses
        draw_balls
        draw_bricks
        draw_level
        draw_score
        draw_lives
        draw_background
        win_screen
        lose_screen
        get_dimensions
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
  - concept_start.png
  - concept_lost.png
  - concept_win.png
  - level_1.png
  - level_2.png
  - level_3.png
  - level_4.png
  - gaming.png
  - game_over.png
  - win.png

---

## Tasks and Responsibilities

- Roman: Worked as the creative designer by helping give ideas for various designs for the visual aspects of the game and tested the game. Provided sprites and also filled out the README.
- Kevin: Project lead and back-end specialist; worked on the code for each class. Used design information given by the design specialist to implement each class and the various code. Also helped fill out the README.

## Testing

Main testing strategy included playing the game from start to finish.
- Everytime we implemented a new feature, such as the brick, or the paddle, we tested it to make sure everything had normal behavior.
- Made sure ball physics were proper and within bounds.
- Tried moving vaus off screen.
- Restarted game randomly to make sure sequence of events was proper.
- Intentionally lost to ensure game over screen displayed properly.
- Made test levels to make going to the next level and winning easier.


## ATP

| Step | Procedure                      | Expected Results                                                                                                                                                                                                                   |
| :--- | :----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01   | Run Controller()               | 1) Game opens with bricks, vaus, and ball initialized <br> 2) Level, score and lives display on the top <br> 3) Keybinds to quit and restart the game show on the bottom <br> 4) Instuctions on how to start display in the middle |
| 02   | Mouse Movement                 | 1) Paddle will follow mouse x <br> 2) Ball will follow mouse x                                                                                                                                                                     |
| 04   | Left Click                     | 1) Remove instruction on how to start game <br> 2) Ball will no longer follow mouse x <br> 3) Ball will start moving towards bricks                                                                                                |
| 05   | General Playtesting            | 1) Ball bounces off walls <br> 2) Ball bounces off bricks if hit from top or bottom (if hit from left or right keep breaking blocks) <br> 3) Ball bounces off paddle <br> 4) Score increase as blocks break                        |
| 06   | Lose Life                      | If the ball doesn't make contact with the paddle, and hits the space under the paddle, the game resets (keeps bricks, scores, lives) and the player loses a life                                                                   |
| 07   | Next Level                     | After all the bricks have been cleared on one level, the bricks reset with the level number going up and the addition of more bricks in different places. The ball's speed is also increased.                                      |
| 08   | Win                            | If all bricks on the last level are broken, the "you win" screen shows with your current score                                                                                                                                     |
| 09   | Lose                           | If all 3 lives are used up, the "game over" screen appears and the game is over. Your score and high score will display.                                                                                                           |
| 10   | Click Q key                    | Quits Game                                                                                                                                                                                                                         |
| 11   | Click R key                    | Restarts Game                                                                                                                                                                                                                      |
| 12   | Reopen Game to test High Score | Losing with a lower score should display the old high score.                                                                                                                                                                       |

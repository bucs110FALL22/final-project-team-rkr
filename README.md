:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Arkanoid
## CS 110 Final Project
### Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

[repl](https://replit.com/join/udspqfxicu-romanpanchmia)

<< [link to demo presentation slides](#) >>

### Team: RKR 
#### Roman P, Kevin C

***

## Project Description

A simple recreation of Arkanoid, a block breaker arcade game. Controlling a paddle, the player is tasked with clearing blocks by deflecting a ball towards it without letting the ball hit the bottom edge of the playfield. Some blocks contain power-ups that have various effects, such as increasing the length of the paddle, creating additional balls, or turning the paddle into a laser cannon. Other blocks may be indestructible or require multiple hits to break.

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
```
class Ball:
    attributes:
        x
        y
        angle
        damage
    methods:
        bounce()
        move_foward()
```
```
class Paddle:
    attributes:
        x
        y
        width
    methods:
        change_size()
        move_right()
        move_left()
```
```
class Brick:
    attributes:
        x
        y
        type
        hp
    methods:
        drop_item()
        take_damage()
```

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...

import pygame
from src.controller import Controller


def main():
    pygame.init()
    control = Controller()  # Create an instance on your controller object
    control.main_loop()  # Call your mainloop

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######


# https://codefather.tech/blog/if-name-main-python/
if __name__ == "__main__":
    main()

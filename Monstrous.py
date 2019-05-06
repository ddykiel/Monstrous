import pygame
import f
import t
import runpy

#Set up PyGame screen and icons
width = 600
height = 600
screen = pygame.display.set_mode((600, 600))

pygame.init()
icon = pygame.image.load('Art/icon.png')
pygame.display.set_icon(icon)

#Set up necessary variables
game_quit = False
menu_options = ['NEW', 'LOAD', 'ABOUT', 'CREDITS']
menu_choice = ''

new_menu = True

#Main loop. Effective until the user quits the game. Displays the start menu until the user clicks one of the buttons.
#Then, it will start a new game, load a saved game, display the about screen, or display credits, based on the user's choice
while not game_quit:

    #Plays music if the user is opening the menu for this first time. Doesn't re-start the music if the user clicks on
    #credits or about and then returns to menu
    if new_menu:
        pygame.mixer.music.load('Music/Evening of Chaos.mp3')
        pygame.mixer.music.play(-1)
        new_menu = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            game_quit = True

        while menu_choice not in menu_options:
            menu_choice = f.start_menu()

        if menu_choice in menu_options:

            if menu_choice == 'NEW':
                pygame.mixer.music.stop()
                runpy.run_module(mod_name='playGame')
                pygame.mixer.music.stop()
                new_menu = True
            elif menu_choice == 'LOAD':
                pygame.mixer.music.stop()
                #Load a saved game, unless no saved game exists. In that case, start a new game.
                try:
                    fh = open("Save file", "r")
                    runpy.run_module(mod_name='playGameSaved')
                except FileNotFoundError:
                    f.display_quote_start_game("Save file not found. New game will be started.", italic=False, modern=True)
                    runpy.run_module(mod_name='playGame')
                new_menu = True
            elif menu_choice == 'ABOUT':
                screen.fill(f.yellow_ochre)
                #Checks the saved game file to see if the user has finished the game. If so, it will show a more detailed
                #about screen. If not, it will show a less detailed about screen.
                try:
                    fh = open("Save file", "r")
                    game_list = f.load()
                    if game_list[7] == True:
                        f.display_about_later()
                    else:
                        f.display_about_initial()
                except FileNotFoundError:
                    f.display_about_initial()
            elif menu_choice == 'CREDITS':
                screen.fill(f.yellow_ochre)
                f.display_credits()
            menu_choice = ''



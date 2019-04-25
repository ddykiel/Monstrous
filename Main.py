import pygame
import f

width = 600
height = 600
screen = pygame.display.set_mode((600, 600))
#screen.fill(255, 239, 188)

pygame.init()
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

game_quit = False
menu_options = ['New Game', 'Load Game', 'About', 'Credits']
menu_choice = ''

while not game_quit:

    f.menu_choice = 'none'

    for event in pygame.event.get():

        pygame.mixer.music.load('Evening of Chaos.mp3')
        pygame.mixer.music.play(-1)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            game_quit = True

        while menu_choice not in menu_options:
            menu_choice = f.start_menu()

        if menu_choice == 'New Game':
            pygame.mixer.music.stop()
            import playGame
            pygame.mixer.music.stop()
        elif menu_choice == 'Load Game':
            pygame.mixer.music.stop()
            import playGameSaved

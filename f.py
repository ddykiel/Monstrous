#Set up board
import pygame
import textwrap

display_width = 600
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
gray = (105, 105, 105)

yellow_ochre = (255, 239, 188)
yellow_ochre_dark = (96, 90, 71)
yellow_ochre_button_text = (255, 253, 247)
yellow_ochre_hover = (155, 144, 110)

gray_green = (68, 88, 76)
gray_green_dark = (38, 49, 42)
gray_green_light = (138, 151, 143)
gray_green_very_light = (232, 234, 233)
gray_green_hover = (208, 213, 210)

purple = (39, 0, 45)
purple_button = (207, 191, 209)
purple_button_text = (62, 0, 72)
purple_hover = (245, 243, 245)

blue_bg = (18, 19, 66)
blue_button = (86, 87, 104)
blue_button_text = (11, 12, 41)
blue_button_hover = (119, 121, 152)

text_color = black
background_color = yellow_ochre
button_color = yellow_ochre_dark
button_text_color = yellow_ochre_button_text
button_hover = yellow_ochre_button_text

screen = pygame.display.set_mode((display_width, display_height))
screen.fill(background_color)

file_name = "blank file"

from pygame import font
pygame.font.init()

game_font = pygame.font.SysFont('couriernew',14)

def display(message, color = text_color, file = file_name, text = game_font):
    "Display text elements of the game"

    pos_y = 5

    file = open(file_name, 'a')
    #Wraps message by adding a new space approximately every 50 characters

    split_message = message.split('\n')
    for token in split_message:
       wrapped_token = textwrap.fill(token, 70)
       split_wrapped_token = wrapped_token.split('\n')
       pos_y += 20
       for token in split_wrapped_token:
           rendered_text = text.render(token, True, text_color)
           screen.blit(rendered_text, (20, pos_y))
           pos_y += 20
           pygame.display.update()

def display_choice(message, color = text_color, bg_color = background_color, text = game_font, short_message = True):
    """Displays choices from the game (in a different location from the text)"""
    if short_message:
        pos_y = 450
    else:
        pos_y = 430
    # Splits and wraps message so it doesn't print on one line
    split_message = message.split('\n')
    for token in split_message:
        rendered_text = text.render(token, True, text_color)
        screen.blit(rendered_text, (20, pos_y))
        pos_y += 20
        pygame.display.update()

def turn(text_to_display, choice_to_display, bg_color = background_color, font = game_font, num_choices = 2, short_message = True):
    """This function runs for every choice the user makes, i.e. every 'turn'. First it creates an updated board with the
    most recent background color. Then it displays the game text and subsequent user choice. Then, when the user clicks,
    it determines if the user clicked on button 1 or button 2. It returns clicking on button 1 or clicking on button 2
    as user choice."""

    screen.fill(background_color)

    button_font = pygame.font.SysFont('couriernew', 25)

    choice = 0

    pygame.init()

    turn_over = False

    display(text_to_display)

    if short_message:
        display_choice(choice_to_display)
    else:
        display_choice(choice_to_display, short_message = False)

    if num_choices == 0:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                turn_over = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                turn_over = True

    if num_choices == 2:

        while not turn_over:

            for event in pygame.event.get():

                button_1_rect = pygame.draw.rect(screen, button_color, (235, 500, 60, 60))
                button_2_rect = pygame.draw.rect(screen, button_color, (325, 500, 60, 60))

                mouse = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    turn_over = True

                elif button_1_rect.collidepoint(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        choice = 1
                        turn_over = True
                    else:
                        button_1_rect = pygame.draw.rect(screen, button_hover, (235, 500, 60, 60))

                elif button_2_rect.collidepoint(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        choice = 2
                        turn_over = True
                    else:
                        button_2_rect = pygame.draw.rect(screen, button_hover, (325, 500, 60, 60))

                pos_x_button = 257
                pos_y_button = 515

                button_text = ['1', '2']

                for text in button_text:
                    button_1_rendered = button_font.render(text, True, button_text_color)
                    screen.blit(button_1_rendered, (pos_x_button, pos_y_button))
                    pos_x_button += 90

                pygame.display.update()

    if num_choices == 3:

        while not turn_over:

            for event in pygame.event.get():

                button_1_rect = pygame.draw.rect(screen, button_color, (180, 500, 60, 60))
                button_2_rect = pygame.draw.rect(screen, button_color, (270, 500, 60, 60))
                button_3_rect = pygame.draw.rect(screen, button_color, (360, 500, 60, 60))

                mouse = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    turn_over = True

                elif button_1_rect.collidepoint(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        choice = 1
                        turn_over = True
                    else:
                        button_1_rect = pygame.draw.rect(screen, button_hover, (180, 500, 60, 60))

                elif button_2_rect.collidepoint(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        choice = 2
                        turn_over = True
                    else:
                        button_2_rect = pygame.draw.rect(screen, button_hover, (270, 500, 60, 60))

                elif button_3_rect.collidepoint(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        choice = 3
                        turn_over = True
                    else:
                        button_3_rect = pygame.draw.rect(screen, button_hover, (360, 500, 60, 60))

                pos_x_button = 202
                pos_y_button = 515

                button_text = ['1', '2', '3']

                for text in button_text:
                    button_1_rendered = button_font.render(text, True, button_text_color)
                    screen.blit(button_1_rendered, (pos_x_button, pos_y_button))
                    pos_x_button += 90

                pygame.display.update()

    if num_choices == 4:

        while not turn_over:

            for event in pygame.event.get():

                button_1_rect = pygame.draw.rect(screen, button_color, (145, 500, 60, 60))
                button_2_rect = pygame.draw.rect(screen, button_color, (235, 500, 60, 60))
                button_3_rect = pygame.draw.rect(screen, button_color, (325, 500, 60, 60))
                button_4_rect = pygame.draw.rect(screen, button_color, (415, 500, 60, 60))

                mouse = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    turn_over = True

                elif button_1_rect.collidepoint(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        choice = 1
                        turn_over = True
                    else:
                        button_1_rect = pygame.draw.rect(screen, button_hover, (145, 500, 60, 60))

                elif button_2_rect.collidepoint(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        choice = 2
                        turn_over = True
                    else:
                        button_2_rect = pygame.draw.rect(screen, button_hover, (235, 500, 60, 60))

                elif button_3_rect.collidepoint(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        choice = 3
                        turn_over = True
                    else:
                        button_3_rect = pygame.draw.rect(screen, button_hover, (325, 500, 60, 60))

                elif button_4_rect.collidepoint(mouse):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        choice = 4
                        turn_over = True
                    else:
                        button_4_rect = pygame.draw.rect(screen, button_hover, (415, 500, 60, 60))

                pos_x_button = 167
                pos_y_button = 515

                button_text = ['1', '2', '3', '4']

                # Writes '1' and '2' on buttons
                for text in button_text:
                    button_1_rendered = button_font.render(text, True, button_text_color)
                    screen.blit(button_1_rendered, (pos_x_button, pos_y_button))
                    pos_x_button += 90

                pygame.display.update()

    screen.fill(background_color)
    return choice


def display_image(name):
    """Displays the appropriate image at the end of the chapter; returns to menu when user clicks"""

    screen.fill(background_color)

    image = pygame.image.load(name)
    screen.blit(image, (0,100))
    pygame.display.update()

    turn_over = False

    while not turn_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                turn_over = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                turn_over = True

def display_quote(reflection_name, start_or_end, quote, italic = False):

    screen.fill(background_color)

    rendered_intro = game_font.render(reflection_name, True, text_color)
    screen.blit(rendered_intro, (20, 20))
    rendered_start = game_font.render(start_or_end, True, text_color)
    screen.blit(rendered_start, (20, 40))

    pos_y = 100

    if italic:
        quote_font = pygame.font.SysFont('couriernew', 15, italic = True)
    else:
        quote_font = pygame.font.SysFont('couriernew', 15)


    split_message = quote.split('\n')
    for token in split_message:
        wrapped_token = textwrap.fill(token, 62)
        split_wrapped_token = wrapped_token.split('\n')
        #pos_y += 20
        for token in split_wrapped_token:
            rendered_text = quote_font.render(token, True, text_color)
            screen.blit(rendered_text, (20, pos_y))
            pos_y += 20
            pygame.display.update()

    rendered_click = game_font.render("(Click anywhere to continue)", True, text_color)
    screen.blit(rendered_click, (20, 560))
    pygame.display.update()

    turn_over = False

    while not turn_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                turn_over = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                turn_over = True

def display_quote_start_game(quote):

    temp_background = black
    temp_text_color = white

    screen.fill(temp_background)

    quote_font = pygame.font.SysFont('couriernew', 15, italic=True)

    pos_y = 100

    wrapped_quote = textwrap.fill(quote, 60)
    split_wrapped_quote = wrapped_quote.split('\n')
    pos_y += 20
    for token in split_wrapped_quote:
        rendered_text = quote_font.render(token, True, temp_text_color)
        screen.blit(rendered_text, (20, pos_y))
        pos_y += 30
        pygame.display.update()

    rendered_click = game_font.render("(Click anywhere to continue)", True, temp_text_color)
    screen.blit(rendered_click, (20, 560))
    pygame.display.update()

    turn_over = False

    while not turn_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                turn_over = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                turn_over = True

def display_monster_screen(monster):
    monster_info = "Your monster is: "
    monster_info += monster
    display_quote_start_game(monster_info)









#Functions for game
import pygame
import textwrap
import pickle
import t

#Relevant variables (such as colors)
display_width = 600
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
gray = (105, 105, 105)
light_gray = (200, 200, 200)

yellow_ochre = (255, 239, 188)
yellow_ochre_dark = (96, 90, 71)
yellow_ochre_button_text = (255, 253, 247)
yellow_ochre_hover = (155, 144, 110)

dark_brown = (50, 47, 39)
off_white = (255, 255, 249)
white_hover = (155, 140, 107)

purple = (27, 0, 45)
purple_button = (200, 191, 209)
purple_button_text = (62, 0, 72)
purple_hover = (245, 243, 245)


text_color = black
background_color = yellow_ochre
button_color = yellow_ochre_dark
button_text_color = yellow_ochre_button_text
button_hover = yellow_ochre_button_text

file_name = "Past playthroughs.txt"


screen = pygame.display.set_mode((display_width, display_height))
screen.fill(background_color)

from pygame import font
pygame.font.init()
game_font = pygame.font.SysFont('couriernew',14)

def save(x_axis, y_axis, played_hunger, played_coldness, played_wrath, played_intro, played_middle, played_end, monster = '', monster_desc = '', display=True):
    """Stores a list of important objects in a save file on the user's computer so that they can later load the game"""

    pygame.mixer.music.stop()

    if display:
        display_save()

    game_list = [x_axis, y_axis, played_hunger, played_coldness, played_wrath, played_intro, played_middle, played_end, monster, monster_desc]
    with open("Save file", "wb") as f:
        pickle.dump(game_list , f)

def load():
    """Returns a list of important objects in the user's save file that impact what happens in the playGameSaved script"""
    with open("Save file", "rb") as f:
        game_list = pickle.load(f)
    return game_list

def get_bg_color(x, y, modern=False):
    """"Gets a background color based on the user's x-axis and y-axis values. If the turn takes place in modern-day,
    the background color is always the same shade of yellow"""
    if (modern == True):
        background_color = yellow_ochre

    else:
        #Tint red if x < 0. Tint dark if y < 0 and light if y > 0.
        if x < 0:
            blue_val = min(45 + 4 * x, 255)
            if (blue_val < 0):
                blue_val = 0
            red_val = min(39 + -4 * x + 4 * y, 255)
            if (red_val < 0):
                red_val = 0
            background_color = (red_val, 0, blue_val)
        #Tint blue if x < 0. Tint dark if y < 0 and light if y > 0.
        else:
            red_val = min(45 + 4 * x + 4 * y, 255)
            if (red_val < 0):
                red_val = 0
            blue_val = min(39 + 4 * x, 255)
            if (blue_val < 0):
                blue_val = 0
            background_color = (red_val, 0, blue_val)

    return background_color

def turn(text_to_display, choice_to_display, x, y, font = game_font, num_choices = 2, short_message = True, modern = False):
    """This function runs for every choice the user makes, i.e. every 'turn'. First it creates an updated screen with the
    most recent background color. Then it displays the game text and subsequent user choice. Then, when the user clicks,
    it determines what button the user clicks, and returns the number of the button (it can support 0, 2, 3, or 4 buttons)."""

    bg_color = get_bg_color(x, y, modern)
    screen.fill(bg_color)

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

        while not turn_over:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    turn_over = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    turn_over = True
                pygame.display.update()

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

                for text in button_text:
                    button_1_rendered = button_font.render(text, True, button_text_color)
                    screen.blit(button_1_rendered, (pos_x_button, pos_y_button))
                    pos_x_button += 90

                pygame.display.update()

    screen.fill(background_color)

    #Appends text to a file so that users can read through their past playthroughs
    file = open(file_name, 'a')
    to_write = "Choice: " + str(choice) + '\n' + '\n'
    file.write(to_write)
    file.close()

    return choice

def start_menu():
    """"Displays the Start menu. Returns what button in the menu the user clicks on."""

    menu_choice = 'none'

    display_menu = True

    pygame.display.set_caption('Monstrous')

    monstrous_menu = pygame.image.load('Art/MonstrousTitleScreen.png')
    screen.blit(monstrous_menu, (0, 0))

    buttons = [1, 2, 3, 4, 5]
    button_text = ['NEW', 'LOAD', 'CREDITS', 'ABOUT']

    x_text = 430
    y_text = 170

    button_font = pygame.font.SysFont('courier', 18, bold=False)

    pygame.display.update()

    while display_menu:

        for event in pygame.event.get():

            button_1 = pygame.draw.rect(screen, dark_brown, (245, 40, 100, 40))
            button_2 = pygame.draw.rect(screen, dark_brown, (460, 270, 100, 40))
            button_3 = pygame.draw.rect(screen, dark_brown, (245, 530, 100, 40))
            button_4 = pygame.draw.rect(screen, dark_brown, (40, 275, 100, 40))

            mouse = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                display_menu = False
                menu_choice = 'none'

            elif button_1.collidepoint(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_choice = 'NEW'
                    display_menu = False
                else:
                    button_1 = pygame.draw.rect(screen, white_hover, (245, 40, 100, 40))

            elif button_2.collidepoint(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_choice = 'LOAD'
                    display_menu = False
                else:
                    button_2 = pygame.draw.rect(screen, white_hover, (460, 270, 100, 40))

            elif button_3.collidepoint(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_choice = 'CREDITS'
                    display_menu = False
                else:
                    button_3 = pygame.draw.rect(screen, white_hover, (245, 530, 100, 40))

            elif button_4.collidepoint(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_choice = 'ABOUT'
                    display_menu = False
                else:
                    button_4 = pygame.draw.rect(screen, white_hover, (40, 275, 100, 40))

            else:
                menu_choice = 'none'

            button_1_text = button_font.render('NEW', True, off_white)
            screen.blit(button_1_text, (275, 45))

            button_2_text = button_font.render('LOAD', True, off_white)
            screen.blit(button_2_text, (485, 275))

            button_3_text = button_font.render('CREDITS', True, off_white)
            screen.blit(button_3_text, (255, 535))

            button_4_text = button_font.render('ABOUT', True, off_white)
            screen.blit(button_4_text, (60, 280))

        pygame.display.update()

    return menu_choice

def append_monster_choice(monster, monster_desc):
    file = open(file_name, 'a')
    to_write = "Monster: " + monster + '\n' + monster_desc + '\n' + '\n'
    file.write(to_write)
    file.close()

def display(message, color = text_color, text = game_font):
    """Display text in the game for the reflections and modern-day scenes"""

    pos_y = 5

    # Appends text to a file so that users can read through their past playthroughs
    file = open(file_name, 'a')
    file.write(message)
    file.write('\n')
    file.close()

    split_message = message.split('\n')
    for token in split_message:
        # Wraps message by adding a new space approximately every 70 characters
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

    # Appends text to a file so that users can read through their past playthroughs
    file = open(file_name, 'a')
    file.write(message)
    file.write('\n')
    file.close()

    split_message = message.split('\n')
    for token in split_message:
        rendered_text = text.render(token, True, text_color)
        screen.blit(rendered_text, (20, pos_y))
        pos_y += 20
        pygame.display.update()

def display_quote(reflection_name, start_or_end, quote, x, y, italic = False, para_breaks = False):
    """Used to display quotes at the start and end of every reflection. Includes options such as italics or paragraph breaks."""

    bg = get_bg_color(x, y)
    screen.fill(bg)

    rendered_intro = game_font.render(reflection_name, True, white)
    screen.blit(rendered_intro, (20, 20))
    rendered_start = game_font.render(start_or_end, True, white)
    screen.blit(rendered_start, (20, 40))

    pos_y = 100

    # Appends text to a file so that users can read through their past playthroughs
    file = open(file_name, 'a')
    to_write = reflection_name + '\n' + start_or_end + '\n' + '\n' + quote
    file.write(to_write)
    file.write('\n')
    file.write('\n')
    file.close()

    if italic:
        quote_font = pygame.font.SysFont('couriernew', 15, italic = True)
    else:
        quote_font = pygame.font.SysFont('couriernew', 15)


    split_message = quote.split('\n')
    for token in split_message:
        wrapped_token = textwrap.fill(token, 62)
        split_wrapped_token = wrapped_token.split('\n')
        if (para_breaks == True):
            pos_y += 20

        for token in split_wrapped_token:
            rendered_text = quote_font.render(token, True, white)
            screen.blit(rendered_text, (20, pos_y))
            pos_y += 20
            pygame.display.update()

    rendered_click = game_font.render("(Click anywhere to continue)", True, white)
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

def display_quote_start_game(quote, italic = True, modern = False):
    """Used to display quotes at the start of the game. Either displays yellow background/black text or black background/white text."""

    if modern:
        temp_background = yellow_ochre
        temp_text_color = black
    else:
        temp_background = black
        temp_text_color = white
        # Appends text to a file so that users can read through their past playthroughs
        # Only appends the epigraph at the beginning of the game: not the trigger warning or dedication
        file = open(file_name, 'a')
        file.write(quote)
        file.write('\n')
        file.write('\n')
        file.close()

    screen.fill(temp_background)

    if italic == True:
        quote_font = pygame.font.SysFont('couriernew', 15, italic=True)
    else:
        quote_font = pygame.font.SysFont('couriernew', 15)

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


def display_save():
    """"Displays a Game Saved screen. User clicks to exit."""

    temp_background = yellow_ochre
    temp_text_color = black

    screen.fill(temp_background)

    quote_font = pygame.font.SysFont('couriernew', 15)

    pos_y = 100

    rendered_game_saved = game_font.render("Game saved", True, temp_text_color)
    rendered_click = game_font.render("(Click anywhere to continue)", True, temp_text_color)

    screen.blit(rendered_game_saved, (20, 40))
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


def display_monster_screen(monster, monster_desc):
    """Displays the monster title/description and image at the end of the game"""

    screen.fill(black)

    quote_font_large = pygame.font.SysFont('couriernew', 17, italic=True)
    quote_font = pygame.font.SysFont('couriernew', 15)

    monster_is = "Your monster is: " + monster
    rendered_text_monster_is = quote_font_large.render(monster_is, True, white)

    monster_file_name = 'Art/' + monster + '.png'

    display_screen = True
    turn_over = False
    already_displayed = False

    button_1_rect = pygame.draw.rect(screen, white, (235, 570, 60, 20))
    button_2_rect = pygame.draw.rect(screen, white, (325, 570, 60, 20))

    #Different monsters have different dimensions, so they have different display positions
    if monster == 'Hand Monster' or monster == 'Throat Monster':
        blit_pos = (0, 0)

    elif monster == 'Teeth Monster':
        blit_pos = (110, 10)

    else: # monster == 'Throat Monster'
        blit_pos = (5, -20)

    #When the user presses button 1, they switch between the monster description and image.
    #If they press button 2, the function exits, and the user returns to the menu
    while not turn_over:

        #Displays monster description
        if display_screen:

            #Ensures PyGame only displays the screen once. Otherwise, the text looks strange.
            if not already_displayed:
                screen.blit(rendered_text_monster_is, (20, 50))

                pos_y = 80
                wrapped_quote = textwrap.fill(monster_desc, 60)
                split_wrapped_quote = wrapped_quote.split('\n')
                pos_y += 20
                for token in split_wrapped_quote:
                    rendered_text = quote_font.render(token, True, white)
                    screen.blit(rendered_text, (20, pos_y))
                    pos_y += 30

                rendered_choice = game_font.render("View monster image (1) | Return to menu (2)", True, white)
                screen.blit(rendered_choice, (115, 540))
                pygame.display.update()
                already_displayed = True

        #Displays monster image
        if not display_screen:

            #Ensures PyGame only displays the screen once. Otherwise, the text looks strange.
            if not already_displayed:
                monster_image = pygame.image.load(monster_file_name)
                monster_image = monster_image.convert_alpha()
                screen.blit(monster_image, blit_pos)

                rendered_choice = game_font.render("View monster description (1) | Return to menu (2)", True, white)
                screen.blit(rendered_choice, (100, 540))
                pygame.display.update()
                already_displayed = True

        for event in pygame.event.get():

            button_1_rect = pygame.draw.rect(screen, white, (235, 565, 60, 25))
            button_2_rect = pygame.draw.rect(screen, white, (325, 565, 60, 25))

            num_1 = game_font.render("1", True, black)
            screen.blit(num_1, (259, 568))
            num_2 = game_font.render("2", True, black)
            screen.blit(num_2, (350, 568))


            mouse = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                turn_over = True

            elif button_1_rect.collidepoint(mouse):

                if event.type == pygame.MOUSEBUTTONDOWN:
                    display_screen = not display_screen
                    already_displayed = False
                    screen.fill(black)
                else:
                    button_1_rect = pygame.draw.rect(screen, light_gray, (235, 565, 60, 25))
                    num_1 = game_font.render("1", True, black)
                    screen.blit(num_1, (259, 568))

            elif button_2_rect.collidepoint(mouse):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    turn_over = True
                else:
                    button_2_rect = pygame.draw.rect(screen, light_gray, (325, 565, 60, 25))
                    num_2 = game_font.render("2", True, black)
                    screen.blit(num_2, (350, 568))
            pygame.display.update()

def display_header_text(header, text, color = text_color, font = game_font, y_initial = 10):
    "Displays a header and text for the About and Credits section"

    quote_font_large = pygame.font.SysFont('couriernew', 17, italic=True)

    pos_y = y_initial

    rendered_header = quote_font_large.render(header, True, black)
    screen.blit(rendered_header, (20, pos_y))

    pos_y += 20

    split_message = text.split('\n')
    for token in split_message:
       wrapped_token = textwrap.fill(token, 70)
       split_wrapped_token = wrapped_token.split('\n')
       pos_y += 20
       for token in split_wrapped_token:
           rendered_text = font.render(token, True, black)
           screen.blit(rendered_text, (20, pos_y))
           pos_y += 20

    rendered_click = game_font.render("(Click anywhere to return to menu)", True, black)
    screen.blit(rendered_click, (20, 560))

    pygame.display.update()


def display_about_initial():
    """Displays the game's About section if the user hasn't yet played through the game. Exits when the user clicks."""
    turn_over = False

    display_header_text(t.about_header, t.about_text)
    display_header_text(t.about_creator_header, t.about_creator, y_initial=170)
    display_header_text("", t.about_playthroughs, y_initial=400)
    display_header_text("", t.about_return, y_initial=450)

    while not turn_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                turn_over = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                turn_over = True

def display_about_later():
    """Displays the game's About section if the user has played through the game. Exits when the user clicks."""
    turn_over = False

    #display_header_text(t.about_header, t.about_text)
    display_header_text(t.about_monsters_header, t.about_monsters)
    display_header_text("", t.about_playthroughs, y_initial=450)

    while not turn_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                turn_over = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                turn_over = True

def display_credits():
    "Displays the game's Credit section. Exits when the user clicks."
    turn_over = False

    display_header_text("Credits", t.credits)

    while not turn_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                turn_over = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                turn_over = True


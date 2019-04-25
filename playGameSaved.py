import pygame
import f
import t

game_list = f.load()

x_axis = game_list[0]
y_axis = game_list[1]

played_hunger = game_list[2]
played_coldness = game_list[3]
played_wrath = game_list[4]
played_intro = game_list[5]
played_middle = game_list[6]
played_end = game_list[7]
monster = game_list[8]
monster_desc = game_list[9]

def setup_modern():
    pygame.display.set_caption("Monstrous")
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Sovereign Quarter.mp3')
    pygame.mixer.music.play(-1)
    f.text_color = f.black
    f.button_color = f.yellow_ochre_dark
    f.button_text_color = f.yellow_ochre_button_text
    f.button_hover = f.yellow_ochre_hover

def play_hunger(played_hunger = played_hunger):
    pygame.display.set_caption("Reflection: Hunger")
    f.text_color = f.white
    f.button_color = f.purple_button
    f.button_text_color = f.purple_button_text
    f.button_hover = f.purple_hover
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Morgana Rides.mp3")
    pygame.mixer.music.play(-1)
    f.display_quote("Reflection: Hunger", "Start", t.hbeginningquote)

def play_coldness(played_coldness = played_coldness):
    pygame.display.set_caption("Reflection: Coldness")
    f.text_color = f.white
    f.button_color = f.gray_green_light
    f.button_text_color = f.gray_green
    f.button_hover = f.gray_green_hover
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Anamalie.mp3")
    pygame.mixer.music.play(-1)
    f.display_quote("Reflection: Coldness", "Start", t.cquote, italic=True)

def play_wrath(played_wrath = played_wrath):
    pygame.display.set_caption("Reflection: Wrath")
    f.text_color = f.white
    f.button_color = f.blue_button
    f.button_text_color = f.blue_button_text
    f.button_hover = f.blue_button_hover
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Lone Harvest.mp3")
    pygame.mixer.music.play(-1)
    f.display_quote("Reflection: Wrath", "Start", t.wbeginningquote, italic = True)

#Play Reflection: Coldness
def coldness(x_axis = x_axis, y_axis = y_axis):
    c1 = f.turn(t.ctext1, t.cchoice1, x=x_axis, y=y_axis)
    if c1 == 1:
        x_axis += 1
    else:
        x_axis += -1
    c2 = f.turn(t.ctext2, t.cchoice2, x=x_axis, y=y_axis)
    if c2 == 1:
        x_axis += 1
    else:
        x_axis += -1
    c3 = f.turn(t.ctext3, t.cchoice3, x=x_axis, y=y_axis)
    if c3 == 1:
        y_axis += -1
    else:
        y_axis += 1
    c4 = f.turn(t.ctext4, t.cchoice4, x=x_axis, y=y_axis)
    if c4 == 1:
        y_axis += 1
    else:
        y_axis += -1
    c5 = f.turn(t.ctext5, t.cchoice5, x=x_axis, y=y_axis)
    if c5 == 1:
        y_axis += 1
    else:
        y_axis += -1

    c6 = f.turn(t.ctext6, t.cchoice6, num_choices = 0, x=x_axis, y=y_axis)

    c7 = f.turn(t.ctext7, t.cchoice7, x=x_axis, y=y_axis)
    if c7 == 1:
        y_axis += -1
    else:
        y_axis += 1

    c8 = f.turn(t.ctext8, t.cchoice8, x=x_axis, y=y_axis)
    if c8 == 1:
        x_axis += -1
        y_axis += 1
    else:
        x_axis += 1
        y_axis += -1

    c9 = f.turn(t.ctext9, t.cchoice9, x=x_axis, y=y_axis)
    if c9 == 1:
        x_axis += -1
    else:
        x_axis += 1

    c10 = f.turn(t.ctext10, t.cchoice10, num_choices = 0, x=x_axis, y=y_axis)

    c11 = f.turn(t.ctext11, t.cchoice11, x=x_axis, y=y_axis)
    if c11 == 1:
        y_axis += -1
    else:
        y_axis += 1

    c12 = f.turn(t.ctext12, t.cchoice12, x=x_axis, y=y_axis)
    if c12 == 1:
        y_axis += -1
    else:
        y_axis += 1

    c13 = f.turn(t.ctext13, t.cchoice13, num_choices = 0, x=x_axis, y=y_axis)

    return x_axis, y_axis

def hunger_coffee_shop(x_axis = x_axis, y_axis = y_axis):
    hcoffee = f.turn(t.hcoffeetext, t.hcoffeechoice, x=x_axis, y=y_axis)
    if hcoffee == 1:
        x_axis += 1
    else:
        x_axis += -1

def hunger_arboretum(x_axis = x_axis, y_axis = y_axis):
    harb = f.turn(t.harbtext, t.harbchoice, x=x_axis, y=y_axis)
    if harb == 1:
        y_axis += -1
    else:
        y_axis += 1

def hunger_stars(x_axis = x_axis, y_axis = y_axis):
    hstars = f.turn(t.hstarstext, t.hstarschoice, x=x_axis, y=y_axis)
    if hstars == 1:
        y_axis += -1
    else:
        y_axis += 1

#Play Reflection: Hunger
def hunger(x_axis = x_axis, y_axis = y_axis):
    h1 = f.turn(t.htext1, t.hchoice1, x=x_axis, y=y_axis)
    if h1 == 1:
        x_axis += 1
        y_axis += -1
    else:
        x_axis += -1
        y_axis += 1

    h2 = f.turn(t.htext2, t.hchoice2, num_choices = 0, x=x_axis, y=y_axis)
    h3 = f.turn(t.htext3, t.hchoice3, num_choices = 0, x=x_axis, y=y_axis)

    h4 = f.turn(t.htext4, t.hchoice4, x=x_axis, y=y_axis)
    if h4 == 1:
        y_axis += -1
    else:
        y_axis += 1

    h5 = f.turn(t.htext5, t.hchoice5, x=x_axis, y=y_axis)
    if h5 == 1:
        y_axis += -1
    else:
        y_axis += 1

    h6 = f.turn(t.htext6, t.hchoice6, x=x_axis, y=y_axis)
    if h6 == 1:
        y_axis += -1
        x_axis += 1
    else:
        y_axis += 1
        x_axis += -1 #Should I keep this? Treating it as consideration of other ppl rather than blame

    h7 = f.turn(t.htext7, t.hchoice7, x=x_axis, y=y_axis)
    if h7 == 1:
        y_axis += -1
    else:
        y_axis += 1
        x_axis += -1

    h8 = f.turn(t.htext8, t.hchoice8, x=x_axis, y=y_axis)
    if h8 == 1:
        y_axis += -1
    else:
        y_axis += 1

    h9 = f.turn(t.htext9, t.hchoice9, num_choices = 0, x=x_axis, y=y_axis)
    h10 = f.turn(t.htext10, t.hchoice10, num_choices = 0, x=x_axis, y=y_axis)
    h11 = f.turn(t.htext11, t.hchoice11, num_choices = 0, x=x_axis, y=y_axis)
    h12 = f.turn(t.htext12, t.hchoice12, num_choices = 0, x=x_axis, y=y_axis)
    #h13 = f.turn(t.htext13, t.hchoice13)
    h14 = f.turn(t.htext14, t.hchoice14, num_choices = 3, x=x_axis, y=y_axis)
    if h14 == 1:
        hunger_coffee_shop()
        h14_ct = f.turn(t.hplacetext, t.hplacechoice, x=x_axis, y=y_axis)
        if h14_ct == 1:
            h14_1 = f.turn("", "Which place?" + '\n' + "The Arboretum (1) | The Field (2)", x=x_axis, y=y_axis)
            if h14_1 == 1:
                hunger_arboretum()
                h14_ct = f.turn(t.hplacetext, t.hlastplacechoice, x=x_axis, y=y_axis)
                if h14_ct == 1:
                    hunger_stars()
                else:
                    x_axis += -2
            else:
                hunger_stars()
                h14_ct = f.turn(t.hplacetext, t.hlastplacechoice, x=x_axis, y=y_axis)
                if h14_ct == 1:
                    hunger_arboretum()
                else:
                    x_axis += -2
        else:
            x_axis += -3
    elif h14 == 2:
        hunger_arboretum()
        h14_ct = f.turn(t.hplacetext, t.hplacechoice, x=x_axis, y=y_axis)
        if h14_ct == 1:
            h14_1 = f.turn("", "Which place?" + '\n' + "The Coffee Shop (1) | The Field (2)", x=x_axis, y=y_axis)
            if h14_1 == 1:
                hunger_coffee_shop()
                h14_ct = f.turn(t.hplacetext, t.hlastplacechoice, x=x_axis, y=y_axis)
                if h14_ct == 1:
                    hunger_stars()
                else:
                    x_axis += -2
            else:
                hunger_stars()
                h14_ct = f.turn(t.hplacetext, t.hlastplacechoice, x=x_axis, y=y_axis)
                if h14_ct == 1:
                    hunger_coffee_shop()
                else:
                    x_axis += -2
        else:
            x_axis += -3
    elif h14 == 3:
        hunger_stars()
        h14_ct = f.turn(t.hplacetext, t.hplacechoice, x=x_axis, y=y_axis)
        if h14_ct == 1:
            h14_1 = f.turn("", "Which place?" + '\n' + "The Coffee Shop (1) | The Arboretum (2)", x=x_axis, y=y_axis)
            if h14_1 == 1:
                hunger_coffee_shop()
                h14_ct = f.turn(t.hplacetext, t.hlastplacechoice, x=x_axis, y=y_axis)
                if h14_ct == 1:
                    hunger_arboretum()
                else:
                    x_axis += -2
            else:
                hunger_arboretum()
                h14_ct = f.turn(t.hplacetext, t.hlastplacechoice, x=x_axis, y=y_axis)
                if h14_ct == 1:
                    hunger_coffee_shop()
                else:
                    x_axis += -2
        else:
            x_axis += -3
    h15 = f.turn(t.htext15, t.hchoice15, num_choices = 0, x=x_axis, y=y_axis)

    return x_axis, y_axis

#Play Reflection: Wrath
def wrath (x_axis = x_axis, y_axis = y_axis):
    w1 = f.turn(t.wtext1, t.wchoice1, num_choices = 3, x=x_axis, y=y_axis)
    if w1 == 1:
        y_axis += -1
    elif w1 == 2:
        y_axis += 1
    elif w1 == 3:
        y_axis += 1

    w2=f.turn(t.wtext2, t.wchoice2, x=x_axis, y=y_axis)
    if w2 == 1:
        x_axis += 1
    else:
        x_axis += -1

    w3 =f.turn(t.wtext3, t.wchoice3, x=x_axis, y=y_axis)
    if w3== 1:
        x_axis += 1
        y_axis += 1
    else:
        x_axis += -1
        y_axis += -1

    w4 = f.turn(t.wtext4, t.wchoice4, x=x_axis, y=y_axis)
    if w4 == 1:
        y_axis += 1
    else:
        y_axis += -1

    w5 = f.turn(t.wtext5, t.wchoice5, x=x_axis, y=y_axis)
    if w5 == 1:
        y_axis += 1
    else:
        y_axis += -1

    w6 = f.turn(t.wtext6, t.wchoice6, x=x_axis, y=y_axis)
    if w6 == 1:
       y_axis += 2
    else:
        y_axis += -2

    w7 = f.turn(t.wtext7, t.wchoice7, num_choices = 0, x=x_axis, y=y_axis)

    w8 = f.turn(t.wtext8, t.wchoice8, short_message = False, x=x_axis, y=y_axis) #Revisit
    if w8 == 1:
        x_axis += -1
    else:
        y_axis += 1
        x_axis += 1

    w9 = f.turn(t.wtext9, t.wchoice9, short_message = False, x=x_axis, y=y_axis) #Revisit
    if w9 == 1:
        y_axis += 1
        x_axis += 1
    else:
        x_axis += -1

    w10 = f.turn(t.wtext10, t.wchoice10, x=x_axis, y=y_axis)
    if w10 == 1:
        y_axis += -1
    else:
        y_axis += 1

    w11 = f.turn(t.wtext11, t.wchoice11, x=x_axis, y=y_axis)
    if w11 == 1:
        y_axis += -1
        x_axis += 1
    else:
        y_axis += 1
        x_axis += -1

    w12 = f.turn(t.wtext12, t.wchoice12, x=x_axis, y=y_axis)
    if w12 == 1:
        x_axis += 1
    else:
        x_axis += -1

    w13 = f.turn(t.wtext13, t.wchoice13, num_choices = 0, x=x_axis, y=y_axis)

    w14 = f.turn(t.wtext14, t.wchoice14, x=x_axis, y=y_axis)
    if w14 == 1:
        y_axis += -1
    else:
        y_axis += 1

    w15 = f.turn(t.wtext15, t.wchoice15, num_choices=0, x=x_axis, y=y_axis)

    w16 = f.turn(t.wtext16, t.wchoice16, x=x_axis, y=y_axis)
    if w16 == 1:
        y_axis += 1
        x_axis += -1
    else:
        y_axis += -1
        x_axis += 1

    w17 = f.turn(t.wtext17, t.wchoice17, x=x_axis, y=y_axis)
    if w17 == 1:
        x_axis += -2
    else:
        x_axis += 2

    w18 = f.turn(t.wtext18, t.wchoice18, short_message = False, x=x_axis, y=y_axis)
    if w18 == 1:
        y_axis +=2
    else:
        y_axis += -2

    return x_axis, y_axis

#Setup
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

pygame.init()
pygame.display.set_caption("Monstrous")


#Play intro
if (played_intro == False):

    f.display_quote_start_game("Content warning for themes of suicide and emotional abuse")
    f.display_quote_start_game(t.quote)
    setup_modern()
    intro_1 = f.turn(t.wake_up, t.wake_up_choice, num_choices = 4, x=x_axis, y=y_axis, modern = True)
    if intro_1 == 1:
        x_axis += -1
        y_axis += 1
    elif intro_1 == 2:
        x_axis += -1
        y_axis += -1
    elif intro_1 == 3:
        x_axis += 1
        y_axis += 1
    elif intro_1 == 4:
        x_axis += 1
        y_axis += -1

    intro_2 = f.turn(t.dreams_linger, t.dreams_linger_choice, num_choices = 3, x=x_axis, y=y_axis, modern = True)

    if intro_2 == 1:
        wrath_intro = f.turn(t.dream_wrath, t.choice_wrath, x=x_axis, y=y_axis, modern = True)
        if wrath_intro == 1:
            x_axis += 1
        else:
            x_axis += -1

        play_wrath()
        x_axis, y_axis = wrath()
        f.display_quote("Reflection: Wrath", "End", t.wendingquote)
        played_wrath = True
        setup_modern()

    elif intro_2 == 2:
        coldness_intro = f.turn(t.dream_coldness, t.choice_coldness, x=x_axis, y=y_axis, modern = True)
        if coldness_intro == 1:
            x_axis += 1
        else:
            x_axis += -1

        play_coldness()
        x_axis, y_axis = coldness()
        f.display_quote("Reflection: Coldness", "End", t.cendingquote)
        played_coldness = True
        setup_modern()

    elif intro_2 == 3:
        hunger_intro = f.turn(t.dream_hunger, t.choice_hunger, x=x_axis, y=y_axis, modern = True)
        if hunger_intro == 1:
            y_axis += 1
        else:
            y_axis += -1

        play_hunger()
        x_axis, y_axis = hunger()
        f.display_quote("Reflection: Hunger", "End", t.hendingquote)
        played_hunger = True
        setup_modern()

    played_intro = True
    f.save(x_axis, y_axis, played_hunger, played_coldness, played_wrath, played_intro, played_middle, played_end)

#Play middle

if played_middle == False:
    setup_modern()

    if (played_hunger == True) and (played_middle == False):
        middle = f.turn(t.middle1, t.middlechoicehunger, x=x_axis, y=y_axis, modern = True)
        if middle == 1:
            play_wrath()
            x_axis, y_axis = wrath()
            f.display_quote("Reflection: Wrath", "End", t.wendingquote)
            played_wrath = True
            setup_modern()
        elif middle == 2:
            play_coldness()
            x_axis, y_axis = coldness()
            f.display_quote("Reflection: Coldness", "End", t.cendingquote)
            played_coldness = True
            setup_modern()
        played_middle = True

    if (played_coldness == True) and (played_middle == False):
        middle = f.turn(t.middle1, t.middlechoicecoldness, x=x_axis, y=y_axis, modern = True)
        if middle == 1:
            play_wrath()
            x_axis, y_axis = wrath()
            f.display_quote("Reflection: Wrath", "End", t.wendingquote)
            played_wrath = True
            setup_modern()
        elif middle == 2:
            play_hunger()
            x_axis, y_axis = hunger()
            f.display_quote("Reflection: Hunger", "End", t.hendingquote)
            played_hunger = True
            setup_modern()


    if (played_wrath == True) and (played_middle == False):
        middle = f.turn(t.middle1, t.middlechoicewrath, x=x_axis, y=y_axis, modern = True)
        if middle == 1:
            play_coldness()
            x_axis, y_axis = coldness()
            f.display_quote("Reflection: Coldness", "End", t.cendingquote)
            played_coldness = True
            setup_modern()
        elif middle == 2:
            play_hunger()
            x_axis, y_axis = hunger()
            f.display_quote("Reflection: Hunger", "End", t.hendingquote)
            played_hunger = True
            setup_modern()
        played_middle = True
    played_middle = True
    f.save(x_axis, y_axis, played_hunger, played_coldness, played_wrath, played_intro, played_middle, played_end)

#Play end
if played_end == False:
    setup_modern()
    end = f.turn(t.end1, t.endchoice1, num_choices = 0, x=x_axis, y=y_axis, modern = True)
    if played_hunger and played_coldness:
        play_wrath()
        x_axis, y_axis = wrath()
        f.display_quote("Reflection: Wrath", "End", t.wendingquote)
        played_wrath = True
    if played_coldness and played_wrath:
        play_hunger()
        x_axis, y_axis = hunger()
        f.display_quote("Reflection: Hunger", "End", t.hendingquote)
        played_hunger = True
        setup_modern()
    if played_hunger and played_wrath:
        play_coldness()
        x_axis, y_axis = coldness()
        f.display_quote("Reflection: Coldness", "End", t.cendingquote)
        played_coldness = True
        setup_modern()

    f.save(x_axis, y_axis, played_hunger, played_coldness, played_wrath, played_intro, played_middle, played_end)

    monster = ""
    monster_desc = ""

    if x_axis <= 0 and y_axis > 0:
        monster = 'Hand Monster'
        monster_desc = t.hand_desc
    if x_axis <= 0 and y_axis <= 0:
        monster = 'Teeth Monster'
        monster_desc = t.teeth_desc
    if x_axis > 0 and y_axis > 0:
        monster = "Eye Monster"
        monster_desc = t.eye_desc
    if x_axis  > 0 and y_axis <= 0:
        monster = "Throat Monster"
        monster_desc = t.throat_desc

    f.save(x_axis, y_axis, played_hunger, played_coldness, played_wrath, played_intro, played_middle, played_end,
           monster, monster_desc)

    f.display_monster_screen(monster, monster_desc)

    display_monster = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            display_monster = False

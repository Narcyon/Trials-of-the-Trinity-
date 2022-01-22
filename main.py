#*****************************************************************#
# Program Authors: Brandon Li and Lucas Fang
# Program Name: Trials of the Trinity
# Revision Date: January 19th, 2022
# Description: Trials of the Trinity explores the consequences one
# might suffer after angering the big three of the Olympian gods.
# You must survive five trials thrown at you, in the form of
# natural disasters if you wish to make it to tomorrow. Good luck,
# mortal.
#*****************************************************************#

# import modules
import pygame
import cv2
import random
from pygame import mixer

# import our own logic from other files
from button import Button, ItemButton
from text_box import InputBox
from text_wrap import render_text

# initialize pygame
pygame.init()

# display screen
size = (800, 450)
window = pygame.display.set_mode(size)
screen_width, screen_height = pygame.display.get_surface().get_size()

pygame.display.set_caption("Trials of the Trinity")
title_font = pygame.font.Font('fonts/pixel.ttf', 32)
text_font = pygame.font.Font('fonts/pixel.ttf', 15)
name_font = pygame.font.Font('fonts/pixel.ttf', 11)
answer_font = pygame.font.Font('fonts/pixel.ttf', 12)

# playing music
mixer.init()
main_channel = mixer.Channel(0)
main_music = mixer.Sound('music/celesteMenuMusic.mp3')
main_channel.set_volume(0.1)
main_channel.play(main_music, loops=-1)

start_channel = mixer.Channel(1)
start_music = mixer.Sound('music/emeraldStoryMusic.mp3')
start_channel.set_volume(0.1)

# for the book of insight pages:
header_font = pygame.font.Font('fonts/pixel.ttf', 20)

text = title_font.render('Trials of the Trinity', True, "#475F77")
textRect = text.get_rect(center=(screen_width // 2, 100))

capture = cv2.VideoCapture('resources/titlescreen.mp4')
_, image = capture.read()
shape = image.shape[1::-1]

# item pictures
item_page = pygame.image.load('resources/items.png')
stick = pygame.image.load('resources/stick.png')
fence = pygame.image.load('resources/fence.png')
vacuum = pygame.image.load('resources/vacuum.png')
board = pygame.image.load('resources/skateboard.png')
bubble = pygame.image.load('resources/bubble.png')
lightning_rod = pygame.image.load('resources/lightning_rod.png')
wall = pygame.image.load('resources/wall.png')
broomstick = pygame.image.load('resources/broomstick.png')
hoverboard = pygame.image.load('resources/hoverboard.png')
shield_bubble = pygame.image.load('resources/shield_bubble.png')
minotaur = pygame.image.load('resources/minotaur.png')
book_of_insights = pygame.image.load("resources/bookofinsights.png")

# resizing images
# Resizing images
lightning_rod = pygame.transform.scale(lightning_rod, (250, 250))
wall = pygame.transform.scale(wall, (250, 250))
broomstick = pygame.transform.scale(broomstick, (250, 250))
hoverboard = pygame.transform.scale(hoverboard, (250, 250))
bubble = pygame.transform.scale(bubble, (250, 250))
minotaur = pygame.transform.scale(minotaur, (175, 175))

# positioning variables
left_page_x_pos = 250
left_page_y_pos = 125
right_page_x_pos = 550
right_page_y_pos = 125
book_width = 210

page_id = 'home'
hide = False
quiz_score = 0
item_chosen = "resources/bubble.png"

# background rectangle
rect_border_color = (71, 95, 119)
rect_color = (115, 158, 201)
def create_rect(width, height, border, color, border_color):
    surf = pygame.Surface(
        (width + border * 2, height + border * 2), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (border, border, width, height), 0)
    for i in range(1, border):
        pygame.draw.rect(surf, border_color, (border - i,
                                              border - i, width + 5, height + 5), 1)
    return surf


# updating values
def update_item_button(item):
    global item_button
    global item_chosen
    item_chosen = item
    item_button = ItemButton([item_chosen], 60, 60, (20, 380), 7, 0, window)

def update_book_button():
    global book_button
    book_button = ItemButton([
        'book_of_insights/book_1.png',
        'book_of_insights/book_2.png',
        'book_of_insights/book_3.png',
        'book_of_insights/book_4.png',
        'book_of_insights/book_5.png',
        'book_of_insights/book_6.png',
        'book_of_insights/book_7.png',
        'book_of_insights/book_8.png',
        'book_of_insights/book_9.png',
        'book_of_insights/book_10.png',
        'book_of_insights/book_11.png'
    ], 60, 60, (700, 380), 7, 0.2, window)

def update_page_id(id):
    global page_id
    page_id = id


def update_quiz_score(score):
    global quiz_score
    quiz_score = score


def reset_quiz_score():
    update_quiz_score(0)


def increase_score():
    update_quiz_score(quiz_score + 1)


def update_return_button(page_id):
    global return_button
    return_button = Button('Return >', 80, 40, (700, 400), 7,
                           window, text_font, page_id, update_page_id)

def update_back_button(page_id):
    global back_button
    back_button = Button('< Back', 80, 40, (20, 400), 7,
                           window, text_font, page_id, update_page_id)


def set_page_button():
    update_return_button('home')
    update_back_button('home')

# randomized chance to go to different pages
# level one randomized chances
def choice1B_chance():
    global page_id
    global hide
    hide = True
    page_id = 'choice1B next'


def choice1C_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.25:
        page_id = 'secret ending one'
    else:
        page_id = 'choice1C next'


# level two randomized chances
def choice2A_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.15:
        page_id = 'volcano ending one'
    else:
        page_id = 'choice2A next'


def choice2B_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.75:
        page_id = 'volcano ending two'
    else:
        page_id = 'choice2B next'


# level three randomized chances
def choice3A_chance():
    global page_id
    if hide:
        chance = random.uniform(0, 1)
        if chance <= 0.75:
                page_id = 'choice3A basement'
        else:
            page_id = 'earthquake ending'
    else:
        page_id = 'choice3A next'


def choice3B_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.30:
        page_id = 'secret ending two'
    else:
        page_id = 'choice3B next'


def choice3C_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.25:
        page_id = 'earthquake ending'
    elif chance >= 0.50:
        page_id = 'secret ending one'
    else:
        page_id = 'choice3C next'


# level four randomized chances
def choice4A_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.50:
        page_id = 'tsunami ending'
    else:
        page_id = 'choice4A next'


def choice4B_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.30:
        page_id = 'tsunami ending'
    else:
        page_id = 'choice4B next'


def choice4C_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.25:
        page_id = 'tsunami ending'
    else:
        page_id = 'choice4C next'


def choice4E_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.20:
        page_id = 'secret ending three'
    else:
        page_id = 'survival ending one'


# level 5
new_order = ['', '', '', '']
def text_order(index, text):
    new_order[index] = text


def submit_answers():
    order = ['3', '2', '4', '1']
    success = False
    for index in range(4):
        if order[index] == new_order[index]:
            success = True
        else:
            success = False
            break
    reset_new_order()

    global page_id
    if success:
        page_id = 'survival ending two'
    else:
        page_id = 'hurricane ending'


# home buttons
home_button_one = Button('< Home', 80, 40, (20, 400), 7,
                       window, text_font, 'home', update_page_id)
home_button_two = Button('Home >', 80, 40, (700, 400), 7,
                       window, text_font, 'home', update_page_id)
home_button_three = Button('Home >', 80, 40, (505, 225), 7,
                         window, text_font, 'home', update_page_id)

# info buttons
info_p1_next = Button(
    'Info', 80, 40, (160, 350), 7, window, text_font, 'info_page_one', update_page_id)
info_p2_next = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'info_page_one', update_page_id)
info_p2 = Button('Next >', 80, 40, (700, 400),
                           7, window, text_font, 'info_page_two', update_page_id)

# book of insights
book_p1 = Button('Lesson', 80, 40, (260, 350),
                           7, window, text_font, 'book_page_one', update_page_id, set_page_button)
book_p1_back = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_one', update_page_id)
book_p2_next = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_two', update_page_id)
book_p2_back = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_two', update_page_id)
book_p3_next = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_three', update_page_id)
book_p3_back = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_three', update_page_id)
book_p4_next = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_four', update_page_id)
book_p4_back = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_four', update_page_id)
book_p5_next = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_five', update_page_id)
book_p5_back = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_five', update_page_id)
book_p6_next = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_six', update_page_id)
book_p6_back = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_six', update_page_id)
book_p7_next = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_seven', update_page_id)

# animation buttons
start_button = Button('Start', 80, 40, (360, 350), 7,
                     window, text_font, 'start', update_page_id)
stick_button = Button('Stick', 80, 40, (165, 230), 7,
                     window, text_font, 'stick', update_page_id)
fence_button = Button('Fence', 80, 40, (268, 230), 7,
                     window, text_font, 'fence', update_page_id, )
vacuum_button = Button('Vacuum', 80, 40, (375, 230), 7,
                      window, text_font, 'vacuum', update_page_id)
board_button = Button('Board', 80, 40, (480, 230), 7,
                     window, text_font, 'board', update_page_id)
bubble_button = Button('Bubble', 80, 40, (582, 230), 7,
                      window, text_font, 'bubble', update_page_id)
try_again = Button('Try Again >', 80, 40, (505, 175), 7,
                        window, text_font, 'start', update_page_id)
leave_button = Button('Quit >', 80, 40, (505, 275), 7,
                     window, text_font, 'quit', update_page_id)

# item skip buttons
lightning_skip = Button('Next >', 80, 40, (700, 400),
                                7, window, text_font, 'survival ending one', update_page_id)

wall_skip = Button('Next >', 80, 40, (700, 400),
                        7, window, text_font, 'level five', update_page_id)

broomstick_skip = Button('Next >', 80, 40, (700, 400),
                              7, window, text_font, 'level two', update_page_id)

hoverboard_skip = Button('Next >', 80, 40, (700, 400),
                              7, window, text_font, 'level four', update_page_id)

bubble_skip = Button('Next >', 80, 40, (700, 400),
                          7, window, text_font, 'level three', update_page_id)

# level one buttons
level_one_button = Button('Begin! >', 80, 40, (700, 400),
                        7, window, text_font, 'level one', update_page_id)
choice_1A = Button('', 215, 150, (47, 200), 7, window,
                  text_font, 'tornado ending', update_page_id)
choice_1B = Button('', 215, 150, (297, 200), 7, window,
                  text_font, None, update_page_id, choice1B_chance)
choice_1B_next = Button('Level Two >', 215, 150, (307.5, 200), 7, window,
                      header_font, 'level two', update_page_id)
choice_1C = Button('', 215, 150, (547, 200), 7, window, text_font,
                  None, update_page_id, choice1C_chance)
choice_1C_next = Button('Level Two >', 215, 150, (307.5, 200), 7, window,
                      header_font, 'level two', update_page_id)

# level two buttons
choice_2A = Button('', 215, 150, (130, 250), 7, window,
                  text_font, None, update_page_id, choice2A_chance)
choice_2A_next = Button('Level Three >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level three', update_page_id)
choice_2B = Button('', 215, 150, (460, 250), 7, window,
                  text_font, None, update_page_id, choice2B_chance)
choice_2B_next = Button('Level Three >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level three', update_page_id)
# level three buttons
choice_3A = Button('', 215, 150, (47, 200), 7, window,
                  text_font, None, update_page_id, choice3A_chance)
choice_3A_next = Button('Level Four >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level four', update_page_id)
choice_3B = Button('', 215, 150, (297, 200), 7, window,
                  text_font, None, update_page_id, choice3B_chance)
choice_3B_basement = Button('Find Alternatives >', 215, 150, (307.5, 250), 7, window, header_font, 'excluding basement',
                          update_page_id)
choice_3B_next = Button('Level Four >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level four', update_page_id)
choice_3C = Button('', 215, 150, (547, 200), 7, window,
                  text_font, None, update_page_id, choice3C_chance)
choice_3C_Next = Button('Level Four >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level four', update_page_id)

# level four buttons
choice_4A = Button('', 180, 150, (100, 130), 7, window,
                  text_font, None, update_page_id, choice4A_chance)
choice_4A_next = Button('Level Five >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level five', update_page_id)
choice_4B = Button('', 180, 150, (300, 130), 7, window,
                  text_font, None, update_page_id, choice4B_chance)
choice_4B_Next = Button('Level Five >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level five', update_page_id)
choice_4C = Button('', 180, 150, (500, 130), 7, window,
                  text_font, None, update_page_id, choice4C_chance)
choice_4C_next = Button('Level Five >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level five', update_page_id)
choice_4D = Button('', 180, 150, (190, 290), 7, window,
                  text_font, 'choice4D next', update_page_id)
choice_4D_next = Button('Level Five >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level five', update_page_id)
choice_4E = Button('', 180, 150, (390, 290), 7, window,
                  text_font, None, update_page_id, choice4E_chance)
choice_4E_next = Button('Level Five >', 215, 150, (307.5, 250), 7, window,
                      header_font, 'level five', update_page_id)

# level five buttons and text boxes
box_5A = InputBox(55, 270, 160, 40, text_font, window, '', text_order, 0)
box_5B = InputBox(235, 270, 160, 40, text_font, window, '', text_order, 1)
box_5C = InputBox(415, 270, 160, 40, text_font, window, '', text_order, 2)
box_5D = InputBox(595, 270, 160, 40, text_font, window, '', text_order, 3)
submit_button = Button('Submit >', 80, 40, (695, 330), 7, window,
                      text_font, None, update_page_id, submit_answers)

# quiz buttons
quiz_button = Button('Quiz', 80, 40, (460, 350), 7, window,
                    text_font, 'quiz', update_page_id, reset_quiz_score)

# question 1 options
q1_option_1 = Button('Basement', 170, 30, (465, 150), 7, window,
                   text_font, 'question_2', update_page_id, increase_score)
q1_option_2 = Button('On top of a mountain', 170, 30, (465, 200),
                   7, window, text_font, 'question_2', update_page_id)
q1_option_3 = Button('The ocean', 170, 30, (465, 250), 7,
                   window, text_font, 'question_2', update_page_id)
q1_option_4 = Button('Under a tree', 170, 30, (465, 300), 7,
                   window, text_font, 'question_2', update_page_id)

# question 2 options
q2_option_1 = Button('Go underwater', 170, 30, (465, 150), 7,
                   window, text_font, 'question_3', update_page_id)
q2_option_2 = Button('Hold on to something', 170, 30, (465, 200),
                   7, window, text_font, 'question_3', update_page_id, increase_score)
q2_option_3 = Button('Swim away', 170, 30, (465, 250), 7,
                   window, text_font, 'question_3', update_page_id)

# question 3 options
q3_option_1 = Button('True', 170, 30, (465, 150), 7, window,
                   text_font, 'question_4', update_page_id)
q3_option_2 = Button('False', 170, 30, (465, 200), 7, window,
                   text_font, 'question_4', update_page_id, increase_score)

# question 4 options
q4_option_1 = Button('Yes', 170, 30, (465, 150), 7, window,
                   text_font, 'question_5', update_page_id, increase_score)
q4_option_2 = Button('No', 170, 30, (465, 200), 7, window,
                   text_font, 'question_5', update_page_id)
q4_option_3 = Button('Why take cover?', 170, 30, (465, 250), 7, window,
                   text_font, 'question_5', update_page_id)

# question 5 options

q5_option_1 = Button('Where the clouds are', 170, 30, (465, 250),
                   7, window, text_font, 'results', update_page_id)
q5_option_2 = Button('Through the hurricane', 170, 30, (465, 200),
                   7, window, text_font, 'results', update_page_id)
q5_option_3 = Button('Eye of the storm', 170, 30, (465, 150),
                   7, window, text_font, 'results', update_page_id, increase_score)
q5_option_4 = Button("Stay in one place", 170, 30, (465, 300), 7,
                   window, text_font, 'results', update_page_id)

# quit button
quit_button = Button('Quit', 80, 40, (560, 350), 7, window,
                    text_font, 'quit', update_page_id)


# new order
def reset_new_order():
    box_5A.reset()
    box_5B.reset()
    box_5C.reset()
    box_5D.reset()

# background image/video

def video_frames():
    success, image = capture.read()
    if success:
        surface = pygame.image.frombuffer(image.tobytes(), shape, "BGR")
        window.blit(surface, (0, 0))
    else:
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)


def show_book_of_insights():
    window.blit(book_of_insights, (0, 0))


def show_items():
    window.blit(item_page, (0, 0))


# home page
def show_home():
    window.blit(text, textRect)
    info_p1_next.draw()
    book_p1.draw()
    start_button.draw()
    quiz_button.draw()
    quit_button.draw()

    render_text('Brandon Li and Lucas Fang ', name_font, '#475F77',
                         90, 25, window, 225)
    render_text('ICS207-01 ', name_font, '#475F77',
                         90, 40, window, 225)
    render_text('Laura Keras', name_font, '#475F77',
                         90, 55, window, 225)
    render_text('January 19th, 2022 ', name_font, '#475F77',
                         90, 70, window, 225)

# info pages
def info_page_one():
    show_book_of_insights()

    render_text('Info Page', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "Trials of the Trinity is an interactive story in which you are a mortal that has angered the Big Three of the Olympian gods. Zeus, the God of the Sky - Poseidon, the God of the Sea - and Hades, the God of the Underworld. To punish you for what you have done, they've decided to give you a trial, and have teleported you to an island.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Info Page', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    render_text(
        "If you want to make it to tomorrow, you must survive the trials given to you by the gods. Pick your choices wisely, for your fate rests in your hands, mortal.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    home_button_one.draw()
    info_p2.draw()


def info_page_two():
    show_book_of_insights()

    render_text('Info Page', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "There will be five different natural disasters you must conquer. Each disaster will ask for a choice. This decision will affect the overall outcome, sometimes with lasting effects.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Info Page', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    render_text(
        "In addition to choosing the right choice, the user will be prompted with a special item of their choice, courtesy of the gods - they grant you a guaranteed pass to the next level. While you can use these items at any point during the game, it is crucial you use it at the appropriate level. There is a chance that the item does absolutely nothing, so be prepared for that as well.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    info_p2_next.draw()
    home_button_two.draw()


# book of insights pages
def lesson_one():
    show_book_of_insights()

    render_text('Book of', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text("Welcome to the Book of Insights.", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Insights', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    render_text(
        "Here, you can learn all about natural disasters to help overcome obstacles in the interactive story. Let's get started!",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    back_button.draw()
    book_p2_next.draw()


def lesson_two():
    show_book_of_insights()

    render_text('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "The tornado is the first natural disaster we're going to explore. A violent rotating column of air, a tornado is deadly to anything that gets in the way. The column extends from the base of a thunderstorm down to the ground. Oftentimes, tornadoes are just a result of the four Anemoi having a fight amongst themselves. They have a pretty bad temper!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Tornados', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    render_text(
        "The best way to survive a tornado is to hide and stay in a sturdy building. Stay away from windows and doors, and get to the lowest floor (such as a basement). Always avoid being inside a vulnerable shelter, like a car or tent. In addition, get under something heavy within your shelter for extra protection.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    book_p1_back.draw()
    book_p3_next.draw()


def lesson_three():
    show_book_of_insights()

    render_text('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "A volcano is an opening in the Earth's crust through which an avalanche of lava, volcanic ash, and gases escape. One of the deadliest disasters, volcanoes are catastrophic during both the actual eruption phase, and the aftermath. Volcanic ash can cause damage thousands of kilometers away, including destroying crops, contaminating water supplies, while also causing respiratory problems for anyone with the misfortune of being caught in the ash.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Volcanos', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    render_text(
        "If you are caught in the initial wave of pyroclastic flow, there is little you could do.  However, you should always be aware of the residing ash in the air, which can be lethal to humans when inhaled. It's advised to wear a mask or to cover your mouth during and after a volcanic eruption. Also, geothermal lands are especially prone to collapsing during a volcanic eruption, so avoid those at all costs!",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    book_p2_back.draw()
    book_p4_next.draw()


def lesson_four():
    show_book_of_insights()

    render_text('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "When the Earth rumbles and shakes, you know something is about to happen. Earthquakes are classified as days when the tectonic plates below us get into a fight. But one lingering question you might have is, who sent it? Was it Poseidon, the earthshaker - or was it Hades, the god of the underworld? It's difficult to tell, so all you can do is flip a coin and hope you prayed to the right god!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Earthquakes', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    render_text(
        "Earthquakes are destructive natural disasters that are deadliest in a dense and civilized area. Buildings topple, cracks form - and you are left to wonder what you have done. Get somewhere as low as possible, like a basement, and hide under something heavy so falling debris is unlikely to hit you.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    book_p3_back.draw()
    book_p5_next.draw()


def lesson_five():
    show_book_of_insights()

    render_text('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "The tsunami is a natural disaster that occurs when tectonic plates under water get into an argument. I know, these tectonic plates are so troublesome and naughty!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Tsunamis', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    render_text(
        "Tsunamis are a wall of water rushing towards the shore. So what do you do? Get as far away from the water as possible, even if you can't outrun it. Getting to as high of an elevation as possible might also be helpful. If you are dragged into the current, your best chance at survival is to find something floating and cling onto it. Your fate's been sealed if Poseidon is having a bad hair day!",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    book_p4_back.draw()
    book_p6_next.draw()


def lesson_six():
    show_book_of_insights()

    render_text('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "It's not a good idea to make both Zeus and Poseidon mad! Forming over tropical waters, hurricanes (tropical cyclones) are a mixture of water and wind. They strengthen when it feeds on unstable air, such as turbulence and rising motion.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Hurricanes', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    render_text(
        "The safest place during a hurricane is the eye of the storm. It's the calmest part during the storm, with light winds and fair weather. Stay away from any objects that can be lifted off the ground, and make sure to avoid drowning in water. That would be unfortunate.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    book_p5_back.draw()
    book_p7_next.draw()


def lesson_seven():
    show_book_of_insights()

    render_text('Book of', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text("Congratulations! You made it through the Book of Insights.",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Insights', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    render_text(
        "The gods were betting you wouldn't be able to. By the way, Athena always had faith you would. She's the goddess of wisdom for a reason.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    book_p6_back.draw()
    return_button.draw()

# story pages
def show_start():
    show_items()

    render_text('Items', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    stick_button.draw()
    fence_button.draw()
    vacuum_button.draw()
    board_button.draw()
    bubble_button.draw()

# cannot use variable, otherwise ItemButton class won't work
    if stick_button.pressed:
        update_item_button('resources/lightning_rod.png')
    elif fence_button.pressed:
        update_item_button('resources/wall.png')
    elif vacuum_button.pressed:
        update_item_button('resources/broomstick.png')
    elif board_button.pressed:
        update_item_button('resources/hoverboard.png')
    elif bubble_button.pressed:
        update_item_button('resources/shield_bubble.png')
    update_book_button()

    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 310))
    render_text(
        "Each item is assigned to a specific disaster. When used during the correct level, you can skip that level and move onto the next. If the items are used for the wrong disaster, the item is discarded and you can no longer use it, so be careful, mortal. The item is displayed at the bottom right.",
        text_font, '#475F77', 400, 325, window, 700)

# item pages
def stick_page():
    render_text('Stick turns into... a Lightning Rod!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    level_one_button.draw()
    window.blit(lightning_rod, (300, 200))


def fence_page():
    render_text('Fence turns into... a Durable Wall!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    level_one_button.draw()
    window.blit(wall, (300, 150))


def vacuum_page():
    render_text('Vacuum turns into... a Powerful Broom!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    level_one_button.draw()
    window.blit(broomstick, (300, 150))


def board_page():
    render_text('Board turns into... a Hoverboard!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    level_one_button.draw()
    window.blit(hoverboard, (300, 150))


def bubble_page():
    render_text('Bubble turns into a... Shield Bubble!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    level_one_button.draw()
    window.blit(shield_bubble, (105, 80))

def lightning_rod_skip_page():
    background_rect = create_rect(770, 85, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "You successfully used the lightning rod! Surprisingly this attracted the wrath of Zeus and Posiedon and deterred the hurricane away from you. Congratulations!",
        header_font, '#475F77', 400, 50, window, 750)

    lightning_skip.draw()


def broomstick_skip_page():
    background_rect = create_rect(770, 85, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "You successfully used the broomstick! Apparently some magic from Harry Potter is all you need to escape from Zephyrus. Congratulations!",
        header_font, '#475F77', 400, 50, window, 750)

    broomstick_skip.draw()


def hoverboard_skip_page():
    background_rect = create_rect(770, 85, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "You successfully used the hoverboard! Seems like modern technology is all you need to avoid the after effects of Hades throwing a tantrum. Congratulations!",
        header_font, '#475F77', 400, 50, window, 750)

    hoverboard_skip.draw()


def bubble_skip_page():
    background_rect = create_rect(770, 85, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "You successfully used the bubble! Seems like even the flames from Hephaestus' forge weren't even able to graze it. Congratulations!",
        header_font, '#475F77', 400, 50, window, 750)

    bubble_skip.draw()


def wall_skip_page():
    background_rect = create_rect(770, 85, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "You successfully used the wall! The wall must have been built different, and  completely blocked the incoming Tsunami. Turns out Poseidon's weakness are walls. Congratulations!",
        header_font, '#475F77', 400, 50, window, 750)

    wall_skip.draw()


# animation levels
def level_one():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "Welcome to the beginning of the end. Zeus, unhappy with your actions, sends a large tornado hurtling your direction. What do you do?",
        header_font, '#475F77', 400, 50, window, 800)

    choice_1A.draw()
    choice_1B.draw()
    choice_1C.draw()
    item_button.draw()
    book_button.draw()

    render_text('Save a monkey!', header_font,
                         '#FFFFFF', 154, 260, window, 200)
    render_text('Explore a creepy shack',
                         header_font, '#FFFFFF', 407, 250, window, 200)
    render_text('Hide in a hole', header_font,
                         '#FFFFFF', 655, 260, window, 200)

    if item_button.pressed and item_chosen == "resources/broomstick.png":
        update_page_id('broomstick skip page')
    if book_button.pressed:
        book_button.release()
        update_return_button(page_id)
        update_back_button(page_id)
        update_page_id('book_page_one')


def level_two():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "Woah! The volcano suddenly became active, and the ash hurries your way! Quick, make a choice!",
        header_font, '#475F77', 400, 50, window, 750)

    choice_2A.draw()
    choice_2B.draw()
    item_button.draw()
    book_button.draw()

    render_text('Craft a mask!', header_font,
                         '#FFFFFF', 238, 310, window, 200)
    render_text('Run from the ash', header_font,
                         '#FFFFFF', 570, 310, window, 200)
    if item_button.pressed and item_chosen == "resources/shield_bubble.png":
        update_page_id('bubble skip page')
    if book_button.pressed:
        book_button.release()
        update_return_button(page_id)
        update_back_button(page_id)
        update_page_id('book_page_one')


def level_three():
    background_rect = create_rect(770, 110, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "That was close one. Gasping for air, you plead to the gods saying that you've learned your lesson, but no response comes. And to make matters worse, the ground below you starts shaking uncontrollably as you realize you are now being challenged with an earthquake.",
        header_font, '#475F77', 400, 50, window, 775)

    choice_3A.draw()
    choice_3B.draw()
    choice_3C.draw()
    item_button.draw()
    book_button.draw()

    render_text('Hide in the shack', header_font,
                         '#FFFFFF', 154, 260, window, 200)
    render_text('Go into the dark cave', header_font,
                         '#FFFFFF', 407, 250, window, 200)
    render_text('Stop, drop, pray', header_font,
                         '#FFFFFF', 655, 260, window, 200)

    if item_button.pressed and item_chosen == "resources/hoverboard.png":
            update_page_id('hoverboard skip page')
    if book_button.pressed:
        book_button.release()
        update_return_button(page_id)
        update_back_button(page_id)
        update_page_id('book_page_one')


def level_four():
    background_rect = create_rect(785, 85, 5, rect_color, rect_border_color)
    window.blit(background_rect, (4, 10))
    render_text(
        "After the earthquake, the ensuing aftershocks create a tsunami. Crsah! A wave of  tsunami comes and submerges the land, and you are caught in it. There is no telling if another wave will still rush towards you. What do you do?",
        header_font, '#475F77', 400, 30, window, 780)

    choice_4A.draw()
    choice_4B.draw()
    choice_4C.draw()
    choice_4D.draw()
    choice_4E.draw()
    item_button.draw()
    book_button.draw()

    render_text('Swim to shore!', header_font,
                         '#FFFFFF', 192, 184, window, 200)
    render_text('Hang onto a drifting wood piece',
                         header_font, '#FFFFFF', 390, 175, window, 150)
    render_text('Climb to the top of a palm tree',
                         header_font, '#FFFFFF', 593, 184, window, 175)
    render_text('Collect drifting materials',
                         header_font, '#FFFFFF', 280, 340, window, 200)
    render_text('Crawl to peak of volcano!',
                         header_font, '#FFFFFF', 480, 340, window, 190)

    if item_button.pressed and item_chosen == "resources/wall.png":
            update_page_id('wall skip page')
    if book_button.pressed:
        book_button.release()
        update_return_button(page_id)
        update_back_button(page_id)
        update_page_id('book_page_one')


def level_five():
    background_rect = create_rect(770, 85, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "Well, that was fun. The gods are pleased with you and offer one last challenge. A plane flies over you but fails to notice the screaming person below. Abruptly, a mixture of thunderstorms, wind and rain clashes onto you.",
        header_font, '#475F77', 400, 50, window, 750)

    background_rect = create_rect(150, 100, 5, rect_color, rect_border_color)
    window.blit(background_rect, (55, 150))
    background_rect = create_rect(150, 100, 5, rect_color, rect_border_color)
    window.blit(background_rect, (235, 150))
    background_rect = create_rect(150, 100, 5, rect_color, rect_border_color)
    window.blit(background_rect, (415, 150))
    background_rect = create_rect(150, 100, 5, rect_color, rect_border_color)
    window.blit(background_rect, (595, 150))

    render_text('Take cover until the eye of the storm reaches you',
                         header_font, '#FFFFFF', 137, 167, window, 125)
    render_text('Build a boat',
                         header_font, '#FFFFFF', 316, 195, window, 125)
    render_text('Follow the eye of the storm',
                         header_font, '#FFFFFF', 495, 176, window, 125)
    render_text('Find materials',
                         header_font, '#FFFFFF', 676, 185, window, 125)

    background_rect = create_rect(150, 30, 5, rect_color, rect_border_color)
    window.blit(background_rect, (55, 270))
    background_rect = create_rect(150, 30, 5, rect_color, rect_border_color)
    window.blit(background_rect, (235, 270))
    background_rect = create_rect(150, 30, 5, rect_color, rect_border_color)
    window.blit(background_rect, (415, 270))
    background_rect = create_rect(150, 30, 5, rect_color, rect_border_color)
    window.blit(background_rect, (595, 270))

    box_5A.draw_textbox()
    box_5B.draw_textbox()
    box_5C.draw_textbox()
    box_5D.draw_textbox()

    background_rect = create_rect(350, 90, 5, rect_color, rect_border_color)
    window.blit(background_rect, (210, 340))
    render_text('You must type in the correct order of placement in the text boxes (ranging 1-4) below the options and submit the answers. ',
                         header_font, '#FFFFFF', 395, 350, window, 325)

    item_button.draw()
    book_button.draw()

    if item_button.pressed and item_chosen == "resources/lightning_rod.png":
            update_page_id('lightning rod skip page')
    if book_button.pressed:
        book_button.release()
        update_return_button(page_id)
        update_back_button(page_id)
        update_page_id('book_page_one')

    submit_button.draw()


# animation in-between level pages
def choice1B_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "You chose to explore the creepy shack. Luckily for you, it turned out to have a basement as you hide in there to wait out the tornado.",
        header_font, '#475F77', 400, 50, window, 800)

    choice_1B_next.draw()


def choice1C_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "Unsure what to do, you find a hole nearby to hide in and pray, waiting out the tornado.",
        header_font, '#475F77', 400, 50, window, 800)

    choice_1C_next.draw()


def choice2A_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "As the ash gets closer and closer to you, you scramble to find materials to craft a mask... successfully.",
        header_font, '#475F77', 400, 55, window, 700)

    choice_2A_next.draw()


def choice2B_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "Not knowing what to do, you run as far away from the coming dark cloud as possible, as you pray it goes away.",
        header_font, '#475F77', 400, 50, window, 800)

    choice_2B_next.draw()


def choice3A_basement():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "You arrive at the shack where you realize it has collapsed. You scramble for another way to survive.",
        header_font, '#475F77', 400, 50, window, 800)

    choice_3B_basement.draw()


def excluding_basement():
    background_rect = create_rect(770, 80, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))
    render_text(
        "As the earthquake situation worsens, you desperately pray to the gods, but still, no response. You look for alternative methods to survive.",
        header_font, '#475F77', 400, 50, window, 775)

    choice_3B.draw()
    choice_3C.draw()
    item_button.draw()
    book_button.draw()

    render_text('Go into the dark cave', header_font,
                         '#FFFFFF', 407, 262, window, 200)
    render_text('Stop, drop, pray', header_font,
                         '#FFFFFF', 655, 262, window, 200)

    if item_button.pressed:
        if item_chosen == "resources/hoverboard.png":
            update_page_id('level four')
        else:
            update_page_id('earthquake ending')
    if book_button.pressed:
        update_return_button(page_id)
        update_page_id('book_page_one')


def choice3A_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))

    render_text(
        "It turns out there is a basement in the shack! You go into it, to wait out the earthquake. But is it really over?",
        header_font, '#475F77', 400, 50, window, 800)
    choice_3A_next.draw()


def choice3B_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))

    render_text(
        "You hurry into the dark, spooky cave. Each time the ground tremors, you pray, until it suddenly stops as you realize the earthquake is over. But is it?",
        header_font, '#475F77', 400, 50, window, 800)

    choice_3B_next.draw()


def choice3C_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))

    render_text(
        "As the earth tremors, you stop, drop, and cling onto anything you can, until the earthquake stops. But is it over?",
        header_font, '#475F77', 400, 50, window, 800)

    choice_3C_Next.draw()


def choice4A_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))

    render_text(
        "You swim and swim and swim until finally, you've reached a non-submerged part of the island.",
        header_font, '#475F77', 400, 50, window, 700)

    choice_4A_next.draw()


def choice4B_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))

    render_text(
        "Treading in the water, you spot a floating piece of wood from the remains of the shack. You hold onto it, as you eventually float to shore.",
        header_font, '#475F77', 400, 50, window, 700)

    choice_4B_Next.draw()


def choice4C_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))

    render_text(
        "A palm tree near you stands true and strong, as you climb onto it. You eventually build up enough courage to swim to shore.",
        header_font, '#475F77', 400, 50, window, 700)

    choice_4C_next.draw()


def choice4D_page():
    background_rect = create_rect(770, 90, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))

    render_text(
        "Gathering miscellaneous materials in the water, you were able to build a treehouse on a palm tree nearby. After a bit, you build up enough strength to swim to shore.",
        header_font, '#475F77', 400, 50, window, 710)

    choice_4D_next.draw()


def choice4E_page():
    background_rect = create_rect(770, 70, 5, rect_color, rect_border_color)
    window.blit(background_rect, (10, 30))

    render_text(
        "With all your energy you climb to the top of the now dormant volcano, watching waves of water crash into the island below.",
        header_font, '#475F77', 400, 50, window, 800)

    choice_4E_next.draw()


# ending pages - death, survival, or secret
def tornado_ending():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('Results', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "You chose to go save the monkey. As you reach him, you pick him up and also realize that you're being picked up. Turns out, the tornado had caught up to you guys, so as you're flying through the air while cuddling with the baby monkey, some final thoughts flow through your head. I hope you end up meeting the Wizard of Oz!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def volcano_ending_one():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('Game Over', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "After inhaling too much volcanic ash, you start coughing, and coughing, until you start losing consciousness. And slowly, as you leave this world, the last thought you will ever have is praying pathetically to the gods. A fiery blaze engulfs you, as the land below you reveals itself to be a dangerous geothermal area.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def volcano_ending_two():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('Game Over', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "You die a fiery death, but at least you went down in style, by drowning in a pool of burning lava! The lava was a comfortable 1250 degrees, just a little over your average hot tub. Yet again, you realize you shouldn't have stolen Cerberus from Hades.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def earthquake_ending():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('Game Over', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "The ground below you cracks open and you fall into an endless pit. And that was when you realized you probably shouldn't have taken Hades' favourite helmet!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def tsunami_ending():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('Game Over', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "Navigating the fully submerged island, you hear a loud sound as you turn around and discover a huge wave of water building up. With one final look at the sun, you apologize to the gods as you choke on water.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def hurricane_ending():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('Game Over', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "The endless swirls of water, rain, and thunder eventually was too much for you to handle.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def survival_ending_one():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('Victory!', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "You reach the peak of the volcano, but also carefully avoid falling in. And suddenly, a plane flies past you. Waving your hands like a madman, the pilot sees you and picks you up. You survived!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def survival_ending_two():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('Victory!', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "The hurricane passes and you finally open your eyes. Hooray! You survived! The gods congratulate you and you go back to your normal life. This time, you shouldn't anger the gods.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def secret_ending_one():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('* SECRET ENDING *', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "Praying, you beg Zeus to spare you. And suddenly, you are at Mount Olympus. You get on your knees, thanking the gods when you realize Zeus had something else in mind.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    window.blit(minotaur, (185, 230))

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def secret_ending_two():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('* SECRET ENDING *', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "Hiding in the cave, you think you are safe when you hear a low, grumbling voice behind you. Slowly turning around, you see the monstrosity which is the Minotaur. The two-horned creature grabs you and eats you for dinner. And that, kids, is why you should never enter a dark cave!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


def secret_ending_three():
    show_book_of_insights()

    try_again.draw()
    home_button_three.draw()
    leave_button.draw()

    render_text('* SECRET ENDING *', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text(
        "Wondering how water levels could rise so high, you are submerged underwater where it is revealed that Poseidon has taken a liking towards you. You are made into an immortal and forced to work for Poseidon for the rest of your eternal life.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text('Thanks for playing!', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)


# quiz pages
def show_question1():
    show_book_of_insights()

    render_text('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text("Question 1: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text("Where is the best place to go when there's a tornado? ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    render_text('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q1_option_1.draw()
    q1_option_2.draw()
    q1_option_3.draw()
    q1_option_4.draw()

    home_button_one.draw()


def show_question2():
    show_book_of_insights()

    render_text('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text("Question 2: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text("When in water during a tsunami, what's the best course of action? ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    render_text('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q2_option_1.draw()
    q2_option_2.draw()
    q2_option_3.draw()


def show_question3():
    show_book_of_insights()

    render_text('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text("Question 3: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text("True or False: Geothermal land is safe to cross during a volcanic eruption.", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    render_text('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q3_option_1.draw()
    q3_option_2.draw()


def show_question4():
    show_book_of_insights()

    render_text('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text("Question 4: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text("In the event of an Earthquake, is it safe to take cover underneath a sturdy table?",
                         text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    render_text('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q4_option_1.draw()
    q4_option_2.draw()
    q4_option_3.draw()


def show_question5():
    show_book_of_insights()

    render_text('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text("Question 5: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    render_text("If you're already caught in a hurricane, what's the safest place to head towards?", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    render_text('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q5_option_1.draw()
    q5_option_2.draw()
    q5_option_3.draw()
    q5_option_4.draw()


def show_quiz_results():
    show_book_of_insights()

    render_text('Thanks for finishing the quiz!', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    render_text("Q1: Where is the best place to when there's a tornado? Ans: The Basement", answer_font,
                         '#475F77',
                         left_page_x_pos, left_page_y_pos + 15, window, book_width)

    render_text(
        "Q2: When in water during a tsunami, what's the best course of action? Ans: Hold on to something.", answer_font,
        '#475F77',
        left_page_x_pos, left_page_y_pos + 55, window, book_width)

    render_text("Q3: Geothermal land is safe to cross during a volcanic eruption. Ans:  False", answer_font,
                         '#475F77',
                         left_page_x_pos, left_page_y_pos + 95, window, book_width)

    render_text(
        "Q4: In the event of an Earthquake, is it safe to take cover underneath a sturdy table? Ans: Yes", answer_font,
        '#475F77',
        left_page_x_pos, left_page_y_pos + 135, window, book_width)

    render_text(
        "Q5: If you're already caught in a hurricane, what's the safest place to head towards? Ans: The eye of the storm",
        answer_font, '#475F77',
        left_page_x_pos, left_page_y_pos + 190, window, book_width)

    render_text('Your result was: ', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos, window, book_width)

    render_text(str(quiz_score) + '/5 questions correct', header_font, '#475F77', right_page_x_pos,
                         right_page_y_pos + 30, window, book_width)

    home_button_one.draw()


# pygame loop
def main():
    try:
        clock = pygame.time.Clock()
        run = True
        input_boxes = [box_5A, box_5B, box_5C, box_5D]
        fps = capture.get(cv2.CAP_PROP_FPS)
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if page_id == 'level five':
                    for box in input_boxes:
                        box.handle_event(event)

            video_frames()

            if page_id == 'home':
                show_home()

            # info windows
            elif page_id == 'info_page_one':
                info_page_one()
            elif page_id == 'info_page_two':
                info_page_two()

            # book of insights windows
            elif page_id == 'book_page_one':
                lesson_one()
            elif page_id == 'book_page_two':
                lesson_two()
            elif page_id == 'book_page_three':
                lesson_three()
            elif page_id == 'book_page_four':
                lesson_four()
            elif page_id == 'book_page_five':
                lesson_five()
            elif page_id == 'book_page_six':
                lesson_six()
            elif page_id == 'book_page_seven':
                lesson_seven()

            # animation windows
            # items
            elif page_id == 'start':
                show_start()
            elif page_id == 'stick':
                stick_page()
            elif page_id == 'fence':
                fence_page()
            elif page_id == 'vacuum':
                vacuum_page()
            elif page_id == 'board':
                board_page()
            elif page_id == 'bubble':
                bubble_page()

            # item skip pages
            elif page_id == 'lightning rod skip page':
                lightning_rod_skip_page()
            elif page_id == 'wall skip page':
                wall_skip_page()
            elif page_id == 'broomstick skip page':
                broomstick_skip_page()
            elif page_id == 'hoverboard skip page':
                hoverboard_skip_page()
            elif page_id == 'bubble skip page':
                bubble_skip_page()


            # level one
            elif page_id == 'level one':
                level_one()
            elif page_id == 'choice1B next':
                choice1B_page()
            elif page_id == 'choice1C next':
                choice1C_page()

            # level two
            elif page_id == 'level two':
                level_two()
            elif page_id == 'choice2A next':
                choice2A_page()
            elif page_id == 'choice2B next':
                choice2B_page()

            # level three
            elif page_id == 'level three':
                level_three()
            elif page_id == 'choice3A next':
                choice3A_page()
            elif page_id == 'choice3A basement':
                choice3A_basement()
            elif page_id == 'excluding basement':
                excluding_basement()
            elif page_id == 'choice3B next':
                choice3B_page()
            elif page_id == 'choice3C next':
                choice3C_page()

            # level four
            elif page_id == 'level four':
                level_four()
            elif page_id == 'choice4A next':
                choice4A_page()
            elif page_id == 'choice4B next':
                choice4B_page()
            elif page_id == 'choice4C next':
                choice4C_page()
            elif page_id == 'choice4D next':
                choice4D_page()
            elif page_id == 'choice4E next':
                choice4E_page()

            # level five
            elif page_id == 'level five':
                level_five()

            # ending windows
            elif page_id == 'tornado ending':
                tornado_ending()
            elif page_id == 'volcano ending one':
                volcano_ending_one()
            elif page_id == 'volcano ending two':
                volcano_ending_two()
            elif page_id == 'earthquake ending':
                earthquake_ending()
            elif page_id == 'tsunami ending':
                tsunami_ending()
            elif page_id == 'hurricane ending':
                hurricane_ending()
            elif page_id == 'survival ending one':
                survival_ending_one()
            elif page_id == 'survival ending two':
                survival_ending_two()
            elif page_id == 'secret ending one':
                secret_ending_one()
            elif page_id == 'secret ending two':
                secret_ending_two()
            elif page_id == 'secret ending three':
                secret_ending_three()

            # Quiz pages
            elif page_id == 'quiz':
                show_question1()
            elif page_id == 'question_2':
                show_question2()
            elif page_id == 'question_3':
                show_question3()
            elif page_id == 'question_4':
                show_question4()
            elif page_id == 'question_5':
                show_question5()
            elif page_id == "results":
                show_quiz_results()
            # Quit Page
            elif page_id == 'quit':
                run = False

            pygame.display.update()

        pygame.quit()
    except:
        print("System Error Detected.")


if __name__ == '__main__':
    main()

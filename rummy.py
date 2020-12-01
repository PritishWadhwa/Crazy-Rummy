#developed by Pritish Wadhwa
#Roll NUmber : 2019440

import pygame
import math
import random
import time

AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
moves = 10

class deck(object):
    """This is a parent class"""

    def __init__(self, x, y):
        self.cards = []
        self.rect = pygame.Rect(x, y, 71, 96)

    def check_pos(self):
        """This check if the cursor is on the card"""
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.rect.left and pos[0] <= self.rect.right:
            if pos[1] >= self.rect.top and pos[1] <= self.rect.bottom:
                return True
            else:
                return False
        else:
            return False


class deck_1(deck):
    """
    deck of cards with face down
    """
    deck_1_list = []

    def __init__(self, x, y):
        deck.__init__(self, x, y)
        self.x = x
        self.y = y
        self.hidden = []

    def extend_list(self, lst):
        for i in lst:
            deck_1.deck_1_list.append(i)

    def draw_card(self, screen, card_set):
        """This will draw all the cards on the screen"""
        rect1 = pygame.Rect(550, 300, 71, 96)
        pygame.draw.rect(screen, BLACK, rect1)
        rect2 = pygame.Rect(555, 305, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect2)
        # drawing cards for computer
        rect00 = pygame.Rect(100, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect00)
        rect01 = pygame.Rect(105, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect01)
        rect10 = pygame.Rect(196, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect10)
        rect11 = pygame.Rect(201, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect11)
        rect20 = pygame.Rect(292, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect20)
        rect21 = pygame.Rect(297, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect21)
        rect30 = pygame.Rect(388, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect30)
        rect31 = pygame.Rect(393, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect31)
        rect40 = pygame.Rect(484, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect40)
        rect41 = pygame.Rect(489, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect41)
        rect50 = pygame.Rect(580, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect50)
        rect51 = pygame.Rect(585, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect51)
        rect60 = pygame.Rect(676, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect60)
        rect61 = pygame.Rect(681, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect61)
        rect70 = pygame.Rect(772, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect70)
        rect71 = pygame.Rect(777, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect71)
        rect80 = pygame.Rect(868, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect80)
        rect81 = pygame.Rect(873, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect81)
        rect90 = pygame.Rect(964, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect90)
        rect91 = pygame.Rect(969, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect91)
        rect100 = pygame.Rect(1060, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect100)
        rect101 = pygame.Rect(1065, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect101)
        rect110 = pygame.Rect(1156, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect110)
        rect111 = pygame.Rect(1161, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect111)
        rect120 = pygame.Rect(1252, 75, 71, 96)
        pygame.draw.rect(screen, BLACK, rect120)
        rect121 = pygame.Rect(1257, 80, 61, 86)
        pygame.draw.rect(screen, OLIVE, rect121)




class deck_2(deck):
    """
    pile of cards
    """
    deck_2_list = [0]

    def __init__(self, x, y):
        deck.__init__(self, x, y)
        self.x = x
        self.y = y
        self.hidden = []

    def extend_list(self, lst):

        for i in lst:
            deck_2.deck_2_list.append(i)

    def draw_card(self, screen, card_set):
        card_img = deck_2.deck_2_list[-1]
        card_img_str = str(card_img)
        first_ = card_img_str.find("_")
        last_ = card_img_str.rfind("_")
        card_name = "playing_cards/" + card_img_str[first_ + 1:last_ + 1] + card_img_str[:first_] + ".png"
        card = pygame.image.load(card_name)
        screen.blit(card, (750, 300))


class deck_3(deck):
    """
    cards with the player
    """
    deck_3_list = []
    deck_3_list_copy = deck_3_list[:]

    def __init__(self, x, y):
        deck.__init__(self, x, y)
        self.x = x
        self.y = y
        self.hidden = []

    def extend_list(self, lst):
        for i in lst:
            deck_3.deck_3_list.append(i)

    def draw_card(self, screen, card_set):
        x = 50
        for i in range(len(deck_3.deck_3_list)):
            card_img = deck_3.deck_3_list[i]
            card_img_str = str(card_img)
            first_ = card_img_str.find("_")
            last_ = card_img_str.rfind("_")
            card_name = "playing_cards/" + card_img_str[first_ + 1:last_ + 1] + card_img_str[:first_] + ".png"
            card = pygame.image.load(card_name)
            screen.blit(card, (x, 500))
            x = x + 95

    def throw_card(self, card):
        i = deck_3.deck_3_list.index(card)
        deck_2.deck_2_list.append(card)
        deck_3.deck_3_list.pop(i)




class deck_4(deck):
    """
    cards with the computer
    """
    deck_4_list = []

    def __init__(self, x, y):
        deck.__init__(self, x, y)
        self.x = x
        self.y = y
        self.hidden = []

    def extend_list(self, lst):
        for i in lst:
            deck_4.deck_4_list.append(i)


def shuffle_cards():
    """This function will shuffle the cards"""
    r = []
    lst = ["clubs_01_1", "clubs_02_1", "clubs_03_1", "clubs_04_1", "clubs_05_1", "clubs_06_1",
           "clubs_07_1", "clubs_08_1", "clubs_09_1", "clubs_10_1", "clubs_11_1", "clubs_12_1",
           "clubs_13_1", "clubs_01_2", "clubs_02_2", "clubs_03_2", "clubs_04_2", "clubs_05_2", "clubs_06_2",
           "clubs_07_2", "clubs_08_2", "clubs_09_2", "clubs_10_2", "clubs_11_2", "clubs_12_2",
           "clubs_13_2", "spades_01_1", "spades_02_1", "spades_03_1", "spades_04_1", "spades_05_1",
           "spades_06_1", "spades_07_1", "spades_08_1", "spades_09_1", "spades_10_1", "spades_11_1",
           "spades_12_1", "spades_13_1", "spades_01_2", "spades_02_2", "spades_03_2", "spades_04_2", "spades_05_2",
           "spades_06_2", "spades_07_2", "spades_08_2", "spades_09_2", "spades_10_2", "spades_11_2",
           "spades_12_2", "spades_13_2", "hearts_01_2", "hearts_02_2", "hearts_03_2", "hearts_04_2",
           "hearts_05_2", "hearts_06_2", "hearts_07_2", "hearts_08_2", "hearts_09_2", "hearts_10_2",
           "hearts_11_2", "hearts_12_2", "hearts_13_2",
           "hearts_01_1", "hearts_02_1", "hearts_03_1", "hearts_04_1",
           "hearts_05_1", "hearts_06_1", "hearts_07_1", "hearts_08_1", "hearts_09_1", "hearts_10_1",
           "hearts_11_1", "hearts_12_1", "hearts_13_1",

           "diamonds_01_1", "diamonds_02_1", "diamonds_03_1",
           "diamonds_04_1", "diamonds_05_1", "diamonds_06_1", "diamonds_07_1", "diamonds_08_1", "diamonds_09_1",
           "diamonds_10_1", "diamonds_11_1", "diamonds_12_1", "diamonds_13_1",
           "diamonds_01_2", "diamonds_02_2", "diamonds_03_2",
           "diamonds_04_2", "diamonds_05_2", "diamonds_06_2", "diamonds_07_2", "diamonds_08_2", "diamonds_09_2",
           "diamonds_10_2", "diamonds_11_2", "diamonds_12_2", "diamonds_13_2",

           "joker_1", "joker_2", "joker_3", "joker_4"]
    for i in range(108):
        c = random.choice(lst)
        r.append(c)
        lst.remove(c)
    return r


def is_valid_run_player():
    deck_3.deck_3_list.sort()
    for i in range(len(deck_3.deck_3_list) - 2):
        first_ = deck_3.deck_3_list[i].find("_")
        last_ = deck_3.deck_3_list[i].rfind("_")
        second_ = deck_3.deck_3_list[i + 1].find("_")
        second_last_ = deck_3.deck_3_list[i + 1].rfind("_")
        third_ = deck_3.deck_3_list[i + 2].find("_")
        third_last_ = deck_3.deck_3_list[i + 2].rfind("_")
        if deck_3.deck_3_list[i][:first_] == deck_3.deck_3_list[i + 1][:second_] == deck_3.deck_3_list[i + 2][:third_]:
            if int(deck_3.deck_3_list[i][first_ + 1:last_]) + 2 == int(deck_3.deck_3_list[i + 1][second_ + 1:second_last_]) + 1 == int(deck_3.deck_3_list[i + 2][third_ + 1:third_last_]):
                return True


def is_valid_run_computer():
    deck_4.deck_4_list.sort()
    for i in range(len(deck_4.deck_4_list) - 2):
        first_ = deck_4.deck_4_list[i].find("_")
        last_ = deck_4.deck_4_list[i].rfind("_")
        second_ = deck_4.deck_4_list[i + 1].find("_")
        second_last_ = deck_4.deck_4_list[i + 1].rfind("_")
        third_ = deck_4.deck_4_list[i + 2].find("_")
        third_last_ = deck_4.deck_4_list[i + 2].rfind("_")
        if deck_4.deck_4_list[i][:first_] == deck_4.deck_4_list[i + 1][:second_] == deck_4.deck_4_list[i + 2][:third_]:
            if int(deck_4.deck_4_list[i][first_ + 1:last_]) + 2 == int(deck_4.deck_4_list[i + 1][second_ + 1:second_last_]) + 1 == int(deck_4.deck_4_list[i + 2][third_ + 1:third_last_]):
                return True


def is_valid_joker_run_player():
    deck_3.deck_3_list.sort()
    flag_joker = False
    for i in deck_3.deck_3_list:
        if i[:5] == "joker":
            flag_joker = True

    for i in range(len(deck_3.deck_3_list) - 2):
        first_ = deck_3.deck_3_list[i].find("_")
        last_ = deck_3.deck_3_list[i].rfind("_")
        second_ = deck_3.deck_3_list[i + 1].find("_")
        second_last_ = deck_3.deck_3_list[i + 1].rfind("_")
        third_ = deck_3.deck_3_list[i + 2].find("_")
        third_last_ = deck_3.deck_3_list[i + 2].rfind("_")
        if (deck_3.deck_3_list[i][:first_] == deck_3.deck_3_list[i + 1][:second_]) and (flag_joker == True):
            if int(deck_3.deck_3_list[i][first_ + 1:last_]) + 2 == int(
                    deck_3.deck_3_list[i + 1][second_ + 1:second_last_]) + 1:
                return True
        elif (deck_3.deck_3_list[i][:first_] == deck_3.deck_3_list[i + 2][:third_]) and (flag_joker == True):
            if int(deck_3.deck_3_list[i][first_ + 1:last_]) + 2 == int(
                    deck_3.deck_3_list[i + 2][third_ + 1:third_last_]):
                return True
        elif (deck_3.deck_3_list[i + 1][:second_] == deck_3.deck_3_list[i + 2][:third_] and (flag_joker == True)):
            if int(deck_3.deck_3_list[i + 1][second_ + 1:second_last_]) + 1 == int(deck_3.deck_3_list[i + 2][third_ + 1:third_last_]):
                return True


def is_valid_joker_run_computer():
    deck_4.deck_4_list.sort()
    flag_joker = False
    for i in deck_4.deck_4_list:
        if i[:5] == "joker":
            flag_joker = True

    for i in range(len(deck_4.deck_4_list) - 2):
        first_ = deck_4.deck_4_list[i].find("_")
        last_ = deck_4.deck_4_list[i].rfind("_")
        second_ = deck_4.deck_4_list[i + 1].find("_")
        second_last_ = deck_4.deck_4_list[i + 1].rfind("_")
        third_ = deck_4.deck_4_list[i + 2].find("_")
        third_last_ = deck_4.deck_4_list[i + 2].rfind("_")
        if (deck_4.deck_4_list[i][:first_] == deck_4.deck_4_list[i + 1][:second_]) and (flag_joker == True):
            if int(deck_4.deck_4_list[i][first_ + 1:last_]) + 2 == int(
                    deck_4.deck_4_list[i + 1][second_ + 1:second_last_]) + 1:
                return True
        elif (deck_4.deck_4_list[i][:first_] == deck_4.deck_4_list[i + 2][:third_]) and (flag_joker == True):
            if int(deck_4.deck_4_list[i][first_ + 1:last_]) + 2 == int(
                    deck_4.deck_4_list[i + 2][third_ + 1:third_last_]):
                return True
        elif (deck_4.deck_4_list[i + 1][:second_] == deck_4.deck_4_list[i + 2][:third_]) and (flag_joker == True):
            if int(deck_4.deck_4_list[i + 1][second_ + 1:second_last_]) + 1 == int(
                    deck_4.deck_4_list[i + 2][third_ + 1:third_last_]):
                return True


def pick_card_computer():
    if deck_2.deck_2_list[-1][:5] == "joker":
        deck_4.deck_4_list.append(deck_2.deck_2_list[-1])
        deck_2.deck_2_list.pop(-1)
        return None
    for i in range(len(deck_4.deck_4_list) - 2):
        first_ = deck_4.deck_4_list[i].find("_")
        last_ = deck_4.deck_4_list[i].rfind("_")
        second_ = deck_4.deck_4_list[i + 1].find("_")
        second_last_ = deck_4.deck_4_list[i + 1].rfind("_")
        third_ = deck_4.deck_4_list[i + 2].find("_")
        third_last_ = deck_4.deck_4_list[i + 2].rfind("_")
        first__ = deck_2.deck_2_list[-1].find("_")
        last__ = deck_2.deck_2_list[-1].rfind("_")
        second__ = deck_2.deck_2_list[-1].find("_")
        second_last__ = deck_2.deck_2_list[-1].rfind("_")
        third__ = deck_2.deck_2_list[-1].find("_")
        third_last__ = deck_2.deck_2_list[-1].rfind("_")
        if deck_4.deck_4_list[i][:first_] == deck_4.deck_4_list[i + 1][:second_] == deck_2.deck_2_list[-1][:third__]:
            if int(deck_4.deck_4_list[i][first_ + 1:last_]) + 2 == int(
                    deck_4.deck_4_list[i + 1][second_ + 1:second_last_]) + 1 == int(
                    deck_2.deck_2_list[-1][third__ + 1:third_last__]):
                deck_4.deck_4_list.append(deck_2.deck_2_list[-1])
                deck_2.deck_2_list.pop(-1)
                return None
        elif deck_4.deck_4_list[i][:first_] == deck_2.deck_2_list[-1][:second__] == deck_4.deck_4_list[i + 2][:third_]:
            if int(deck_4.deck_4_list[i][first_ + 1:last_]) + 2 == int(
                    deck_2.deck_2_list[-1][second__ + 1: second_last__]) + 1 == int(
                    deck_4.deck_4_list[i + 2][third_ + 1:third_last_]):
                deck_4.deck_4_list.append(deck_2.deck_2_list[-1])
                deck_2.deck_2_list.pop(-1)
                return None
        elif deck_2.deck_2_list[-1][:first__] == deck_4.deck_4_list[i + 1][:second_] == deck_4.deck_4_list[i + 2][
                                                                                        :third_]:
            if int(deck_2.deck_2_list[-1][first__ + 1: last__]) + 2 == int(
                    deck_4.deck_4_list[i + 1][second_ + 1:second_last_]) + 1 == int(
                    deck_4.deck_4_list[i + 2][third_ + 1:third_last_]):
                deck_4.deck_4_list.append(deck_2.deck_2_list[-1])
                deck_2.deck_2_list.pop(-1)
                return None
    deck_4.deck_4_list.append(deck_1.deck_1_list[-1])
    deck_1.deck_1_list.insert(0,deck_1.deck_1_list[-1])
    deck_1.deck_1_list.pop(-1)
    return None


def throw_card_computer():
    deck_4.deck_4_list.sort()
    for i in range(len(deck_4.deck_4_list) - 1):
        if deck_4.deck_4_list[i] == deck_4.deck_4_list[i + 1]:
            deck_2.deck_2_list.append(deck_4.deck_4_list[i + 1])
            deck_4.deck_4_list.pop(i + 1)
            return None
    for i in range(len(deck_4.deck_4_list) - 3):
        first_ = deck_4.deck_4_list[i].find("_")
        last_ = deck_4.deck_4_list[i].rfind("_")
        second_ = deck_4.deck_4_list[i + 1].find("_")
        second_last_ = deck_4.deck_4_list[i + 1].rfind("_")
        third_ = deck_4.deck_4_list[i + 2].find("_")
        third_last_ = deck_4.deck_4_list[i + 2].rfind("_")
        if deck_4.deck_4_list[i][:first_] == deck_4.deck_4_list[i + 1][:second_] == deck_4.deck_4_list[i + 2][:third_]:
            if int(deck_4.deck_4_list[i][first_ + 2:last_]) == deck_4.deck_4_list[i + 1][second_ + 1:second_last_]== deck_4.deck_4_list[i + 2][third_ + 1:third_last_]:
                deck_2.deck_2_list.append(deck_4.deck_4_list[i + 1])
                deck_4.deck_4_list.pop(i + 1)
                return None
    if deck_4.deck_4_list[-1][:5] == 'joker':
        deck_2.deck_2_list.append(deck_4.deck_4_list[-1])
        deck_4.deck_4_list.pop(-1)
        return None
    deck_2.deck_2_list.append(deck_4.deck_4_list[-1])
    deck_4.deck_4_list.pop(-1)
    return None


def calculate_player_points():
    p_points = 0
    for i in range(len(deck_3.deck_3_list)):
        if deck_3.deck_3_list[i][:5] == "joker":
            p_points = p_points + 0
        else:
            first_ = deck_3.deck_3_list[i].find("_")
            last_ = deck_3.deck_3_list[i].rfind("_")
            p_points = p_points + int(deck_3.deck_3_list[i][first_ + 1:last_])
    return p_points


def calculate_computer_points():
    c_points = 0
    for i in range(len(deck_4.deck_4_list)):
        if deck_4.deck_4_list[i][:5] == "joker":
            c_points = c_points + 0
        else:
            first_ = deck_4.deck_4_list[i].find("_")
            last_ = deck_4.deck_4_list[i].rfind("_")
            print(deck_4.deck_4_list)
            c_points = c_points + int(deck_4.deck_4_list[i][first_ + 1:last_])
    return c_points

def player_pick_card():
    current_mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (550 <= current_mouse[0] <= 621) and (300 <= current_mouse[1] <= 396) and (len(deck_3.deck_3_list) < 14):
        if click[0] == 1:
            deck_3.deck_3_list.append(deck_1.deck_1_list[-1])
            deck_1.deck_1_list.pop(-1)
    if (750 <= current_mouse[0] <= 821) and (300 <= current_mouse[1] <= 396) and (len(deck_3.deck_3_list) < 14):
        if click[0] == 1:
            deck_3.deck_3_list.append(deck_2.deck_2_list[-1])
            deck_2.deck_2_list.pop(-1)

def player_throw_card():
    current_mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (click[0] == 1) and (len(deck_3.deck_3_list) == 14):
        if (50 <= current_mouse[0] <= 121) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[0])
            deck_3.deck_3_list.pop(0)
        elif (145 <= current_mouse[0] <= 216) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[1])
            deck_3.deck_3_list.pop(1)
        elif (240 <= current_mouse[0] <= 311) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[2])
            deck_3.deck_3_list.pop(2)
        elif (335 <= current_mouse[0] <= 406) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[3])
            deck_3.deck_3_list.pop(3)
        elif (430 <= current_mouse[0] <= 501) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[4])
            deck_3.deck_3_list.pop(4)
        elif (525 <= current_mouse[0] <= 596) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[5])
            deck_3.deck_3_list.pop(5)
        elif (620 <= current_mouse[0] <= 691) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[6])
            deck_3.deck_3_list.pop(6)
        elif (715 <= current_mouse[0] <= 786) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[7])
            deck_3.deck_3_list.pop(7)
        elif (810 <= current_mouse[0] <= 881) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[8])
            deck_3.deck_3_list.pop(8)
        elif (905 <= current_mouse[0] <= 976) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[9])
            deck_3.deck_3_list.pop(9)
        elif (1000 <= current_mouse[0] <= 1071) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[10])
            deck_3.deck_3_list.pop(10)
        elif (1095 <= current_mouse[0] <= 1166) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[11])
            deck_3.deck_3_list.pop(11)
        elif (1190 <= current_mouse[0] <= 1261) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[12])
            deck_3.deck_3_list.pop(12)
        elif (1285 <= current_mouse[0] <= 1356) and (475 <= current_mouse[1] <= 571):
            deck_2.deck_2_list.append(deck_3.deck_3_list[13])
            deck_3.deck_3_list.pop(13)



def main():
    pygame.init()
    c_points = p_points = 0
    screen = pygame.display.set_mode(([1425, 750]))  # it sets the size of the screen([width, height])
    pygame.display.set_caption("Rummy")  # it sets the name of the game at the top
    done = False  # loop until user closes the game
    clock = pygame.time.Clock()  # how fast the screen will update





    card_set = {}  # this dictionary will hold all the cards
    card = pygame.image.load("playing_cards/joker.png").convert()
    card_set["joker_1"] = card
    card = pygame.image.load("playing_cards/joker.png").convert()
    card_set["joker_2"] = card
    card = pygame.image.load("playing_cards/joker.png").convert()
    card_set["joker_3"] = card
    card = pygame.image.load("playing_cards/joker.png").convert()
    card_set["joker_4"] = card
    card = pygame.image.load("playing_cards/01_clubs.png").convert()
    card_set["1_clubs_1"] = card
    card = pygame.image.load("playing_cards/01_clubs.png").convert()
    card_set["1_clubs_2"] = card
    card = pygame.image.load("playing_cards/01_diamonds.png").convert()
    card_set["1_diamonds_1"] = card
    card = pygame.image.load("playing_cards/01_diamonds.png").convert()
    card_set["1_diamonds_2"] = card
    card = pygame.image.load("playing_cards/01_hearts.png").convert()
    card_set["1_hearts_1"] = card
    card = pygame.image.load("playing_cards/01_hearts.png").convert()
    card_set["1_hearts_2"] = card
    card = pygame.image.load("playing_cards/01_spades.png").convert()
    card_set["1_spades_1"] = card
    card = pygame.image.load("playing_cards/01_spades.png").convert()
    card_set["1_spades_2"] = card
    card = pygame.image.load("playing_cards/02_clubs.png").convert()
    card_set["2_clubs_1"] = card
    card = pygame.image.load("playing_cards/02_clubs.png").convert()
    card_set["2_clubs_2"] = card
    card = pygame.image.load("playing_cards/02_diamonds.png").convert()
    card_set["2_diamonds_1"] = card
    card = pygame.image.load("playing_cards/02_diamonds.png").convert()
    card_set["2_diamonds_2"] = card
    card = pygame.image.load("playing_cards/02_hearts.png").convert()
    card_set["2_hearts_1"] = card
    card = pygame.image.load("playing_cards/02_hearts.png").convert()
    card_set["2_hearts_2"] = card
    card = pygame.image.load("playing_cards/02_spades.png").convert()
    card_set["2_spades_1"] = card
    card = pygame.image.load("playing_cards/02_spades.png").convert()
    card_set["2_spades_2"] = card
    card = pygame.image.load("playing_cards/03_clubs.png").convert()
    card_set["3_clubs_1"] = card
    card = pygame.image.load("playing_cards/03_clubs.png").convert()
    card_set["3_clubs_2"] = card
    card = pygame.image.load("playing_cards/03_diamonds.png").convert()
    card_set["3_diamonds_1"] = card
    card = pygame.image.load("playing_cards/03_diamonds.png").convert()
    card_set["3_diamonds_2"] = card
    card = pygame.image.load("playing_cards/03_hearts.png").convert()
    card_set["3_hearts_1"] = card
    card = pygame.image.load("playing_cards/03_hearts.png").convert()
    card_set["3_hearts_2"] = card
    card = pygame.image.load("playing_cards/03_spades.png").convert()
    card_set["3_spades_1"] = card
    card = pygame.image.load("playing_cards/03_spades.png").convert()
    card_set["3_spades_2"] = card
    card = pygame.image.load("playing_cards/04_clubs.png").convert()
    card_set["4_clubs_1"] = card
    card = pygame.image.load("playing_cards/04_clubs.png").convert()
    card_set["4_clubs_2"] = card
    card = pygame.image.load("playing_cards/04_diamonds.png").convert()
    card_set["4_diamonds_1"] = card
    card = pygame.image.load("playing_cards/04_diamonds.png").convert()
    card_set["4_diamonds_2"] = card
    card = pygame.image.load("playing_cards/04_hearts.png").convert()
    card_set["4_hearts_1"] = card
    card = pygame.image.load("playing_cards/04_hearts.png").convert()
    card_set["4_hearts_2"] = card
    card = pygame.image.load("playing_cards/04_spades.png").convert()
    card_set["4_spades_1"] = card
    card = pygame.image.load("playing_cards/04_spades.png").convert()
    card_set["4_spades_2"] = card
    card = pygame.image.load("playing_cards/05_clubs.png").convert()
    card_set["5_clubs_1"] = card
    card = pygame.image.load("playing_cards/05_clubs.png").convert()
    card_set["5_clubs_2"] = card
    card = pygame.image.load("playing_cards/05_diamonds.png").convert()
    card_set["5_diamonds_1"] = card
    card = pygame.image.load("playing_cards/05_diamonds.png").convert()
    card_set["5_diamonds_2"] = card
    card = pygame.image.load("playing_cards/05_hearts.png").convert()
    card_set["5_hearts_1"] = card
    card = pygame.image.load("playing_cards/05_hearts.png").convert()
    card_set["5_hearts_2"] = card
    card = pygame.image.load("playing_cards/05_spades.png").convert()
    card_set["5_spades_1"] = card
    card = pygame.image.load("playing_cards/05_spades.png").convert()
    card_set["5_spades_2"] = card
    card = pygame.image.load("playing_cards/06_clubs.png").convert()
    card_set["6_clubs_1"] = card
    card = pygame.image.load("playing_cards/06_clubs.png").convert()
    card_set["6_clubs_2"] = card
    card = pygame.image.load("playing_cards/06_diamonds.png").convert()
    card_set["6_diamonds_1"] = card
    card = pygame.image.load("playing_cards/06_diamonds.png").convert()
    card_set["6_diamonds_2"] = card
    card = pygame.image.load("playing_cards/06_hearts.png").convert()
    card_set["6_hearts_1"] = card
    card = pygame.image.load("playing_cards/06_hearts.png").convert()
    card_set["6_hearts_2"] = card
    card = pygame.image.load("playing_cards/06_spades.png").convert()
    card_set["6_spades_1"] = card
    card = pygame.image.load("playing_cards/06_spades.png").convert()
    card_set["6_spades_2"] = card
    card = pygame.image.load("playing_cards/07_clubs.png").convert()
    card_set["7_clubs_1"] = card
    card = pygame.image.load("playing_cards/07_clubs.png").convert()
    card_set["7_clubs_2"] = card
    card = pygame.image.load("playing_cards/07_diamonds.png").convert()
    card_set["7_diamonds_1"] = card
    card = pygame.image.load("playing_cards/07_diamonds.png").convert()
    card_set["7_diamonds_2"] = card
    card = pygame.image.load("playing_cards/07_hearts.png").convert()
    card_set["7_hearts_1"] = card
    card = pygame.image.load("playing_cards/07_hearts.png").convert()
    card_set["7_hearts_2"] = card
    card = pygame.image.load("playing_cards/07_spades.png").convert()
    card_set["7_spades_1"] = card
    card = pygame.image.load("playing_cards/07_spades.png").convert()
    card_set["7_spades_2"] = card
    card = pygame.image.load("playing_cards/08_clubs.png").convert()
    card_set["8_clubs_1"] = card
    card = pygame.image.load("playing_cards/08_clubs.png").convert()
    card_set["8_clubs_2"] = card
    card = pygame.image.load("playing_cards/08_diamonds.png").convert()
    card_set["8_diamonds_1"] = card
    card = pygame.image.load("playing_cards/08_diamonds.png").convert()
    card_set["8_diamonds_2"] = card
    card = pygame.image.load("playing_cards/08_hearts.png").convert()
    card_set["8_hearts_1"] = card
    card = pygame.image.load("playing_cards/08_hearts.png").convert()
    card_set["8_hearts_2"] = card
    card = pygame.image.load("playing_cards/08_spades.png").convert()
    card_set["8_spades_1"] = card
    card = pygame.image.load("playing_cards/08_spades.png").convert()
    card_set["8_spades_2"] = card
    card = pygame.image.load("playing_cards/09_clubs.png").convert()
    card_set["9_clubs_1"] = card
    card = pygame.image.load("playing_cards/09_clubs.png").convert()
    card_set["9_clubs_2"] = card
    card = pygame.image.load("playing_cards/09_diamonds.png").convert()
    card_set["9_diamonds_1"] = card
    card = pygame.image.load("playing_cards/09_diamonds.png").convert()
    card_set["9_diamonds_2"] = card
    card = pygame.image.load("playing_cards/09_hearts.png").convert()
    card_set["9_hearts_1"] = card
    card = pygame.image.load("playing_cards/09_hearts.png").convert()
    card_set["9_hearts_2"] = card
    card = pygame.image.load("playing_cards/09_spades.png").convert()
    card_set["9_spades_1"] = card
    card = pygame.image.load("playing_cards/09_spades.png").convert()
    card_set["9_spades_2"] = card
    card = pygame.image.load("playing_cards/10_clubs.png").convert()
    card_set["10_clubs_1"] = card
    card = pygame.image.load("playing_cards/10_clubs.png").convert()
    card_set["10_clubs_2"] = card
    card = pygame.image.load("playing_cards/10_diamonds.png").convert()
    card_set["10_diamonds_1"] = card
    card = pygame.image.load("playing_cards/10_diamonds.png").convert()
    card_set["10_diamonds_2"] = card
    card = pygame.image.load("playing_cards/10_hearts.png").convert()
    card_set["10_hearts_1"] = card
    card = pygame.image.load("playing_cards/10_hearts.png").convert()
    card_set["10_hearts_2"] = card
    card = pygame.image.load("playing_cards/10_spades.png").convert()
    card_set["10_spades_1"] = card
    card = pygame.image.load("playing_cards/10_spades.png").convert()
    card_set["10_spades_2"] = card
    card = pygame.image.load("playing_cards/11_clubs.png").convert()
    card_set["11_clubs_1"] = card
    card = pygame.image.load("playing_cards/11_clubs.png").convert()
    card_set["11_clubs_2"] = card
    card = pygame.image.load("playing_cards/11_diamonds.png").convert()
    card_set["11_diamonds_1"] = card
    card = pygame.image.load("playing_cards/11_diamonds.png").convert()
    card_set["11_diamonds_2"] = card
    card = pygame.image.load("playing_cards/11_hearts.png").convert()
    card_set["11_hearts_1"] = card
    card = pygame.image.load("playing_cards/11_hearts.png").convert()
    card_set["11_hearts_2"] = card
    card = pygame.image.load("playing_cards/11_spades.png").convert()
    card_set["11_spades_1"] = card
    card = pygame.image.load("playing_cards/11_spades.png").convert()
    card_set["11_spades_2"] = card
    card = pygame.image.load("playing_cards/12_clubs.png").convert()
    card_set["12_clubs_1"] = card
    card = pygame.image.load("playing_cards/12_clubs.png").convert()
    card_set["12_clubs_2"] = card
    card = pygame.image.load("playing_cards/12_diamonds.png").convert()
    card_set["12_diamonds_1"] = card
    card = pygame.image.load("playing_cards/12_diamonds.png").convert()
    card_set["12_diamonds_2"] = card
    card = pygame.image.load("playing_cards/12_hearts.png").convert()
    card_set["12_hearts_1"] = card
    card = pygame.image.load("playing_cards/12_hearts.png").convert()
    card_set["12_hearts_2"] = card
    card = pygame.image.load("playing_cards/12_spades.png").convert()
    card_set["12_spades_1"] = card
    card = pygame.image.load("playing_cards/12_spades.png").convert()
    card_set["12_spades_2"] = card
    card = pygame.image.load("playing_cards/13_clubs.png").convert()
    card_set["13_clubs_1"] = card
    card = pygame.image.load("playing_cards/13_clubs.png").convert()
    card_set["13_clubs_2"] = card
    card = pygame.image.load("playing_cards/13_diamonds.png").convert()
    card_set["13_diamonds_1"] = card
    card = pygame.image.load("playing_cards/13_diamonds.png").convert()
    card_set["13_diamonds_2"] = card
    card = pygame.image.load("playing_cards/13_hearts.png").convert()
    card_set["13_hearts_1"] = card
    card = pygame.image.load("playing_cards/13_hearts.png").convert()
    card_set["13_hearts_2"] = card
    card = pygame.image.load("playing_cards/13_spades.png").convert()
    card_set["13_spades_1"] = card
    card = pygame.image.load("playing_cards/13_spades.png").convert()
    card_set["13_spades_2"] = card

    card_list = shuffle_cards()  # this list will hold all the shuffled cards

    deck_list = [deck_1(500, 175),
                 deck_2(771, 175),
                 deck_3(50, 475), deck_3(145, 475), deck_3(240, 475), deck_3(335, 475),
                 deck_3(430, 475), deck_3(525, 475), deck_3(620, 475),
                 deck_3(715, 475), deck_3(810, 475), deck_3(905, 475), deck_3(1000, 475),
                 deck_3(1095, 475), deck_3(1190, 475), deck_3(1285, 475),
                 deck_4(100, 100)
                 ]
    free_card_img = pygame.image.load("playing_cards/free_card.png")
    screen.blit(free_card_img, (750, 300))
    deck_list[0].extend_list(card_list[:80])
    del card_list[:80]
    deck_list[1].extend_list(card_list[:2])
    del card_list[:2]
    deck_list[2].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[3].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[4].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[5].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[6].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[7].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[8].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[9].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[10].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[11].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[12].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[13].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[14].extend_list(card_list[:1])
    del card_list[:1]
    deck_list[16].extend_list(card_list[:])
    del card_list[:]
    moves = 10
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        screen.fill(GREEN)
        rect_sort = pygame.Rect(100, 650, 80, 50)
        pygame.draw.rect(screen, BLACK, rect_sort)
        rect_sort = pygame.Rect(102, 652, 76, 46)
        pygame.draw.rect(screen, TEAL, rect_sort)

        rect_give = pygame.Rect(1250,650,80,50)
        pygame.draw.rect(screen, BLACK, rect_give)
        rect_give = pygame.Rect(1252, 652, 76, 46)
        pygame.draw.rect(screen, AQUA, rect_give)

        deck_list[0].draw_card(screen, card_set)
        deck_list[1].draw_card(screen, card_set)
        deck_list[14].draw_card(screen, card_set)

        current_mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.display.update()
        for i in range(5):
            player_pick_card()

            if (100 <= current_mouse[0] <= 180) and (650 <= current_mouse[1] <= 700):
                if click[0] == 1:
                    deck_3.deck_3_list.sort()
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('s'):
                        deck_3.deck_3_list.sort()
            player_throw_card()
            pick_card_computer()
            throw_card_computer()
            if (1250<= current_mouse[0] <=1330) and (650<= current_mouse[1]<=700):
                if click[0] == 1:
                    you_win = pygame.image.load("playing_cards/you_win.png")
                    you_lose = pygame.image.load("playing_cards/you_lose.png")
                    tie = pygame.image.load("playing_cards/tie.png")
                    if (is_valid_run_player() == True) and (is_valid_run_computer() == False):
                        screen.blit(you_win, (562, 625))
                    elif (is_valid_run_player() == False) and (is_valid_run_computer() == True):
                        screen.blit(you_lose, (625, 625))
                    elif (is_valid_joker_run_player() == True) and (is_valid_joker_run_computer() == False):
                        screen.blit(you_win, (562, 625))
                    elif (is_valid_joker_run_player() == False) and (is_valid_joker_run_computer() == True):
                        screen.blit(you_lose, (625, 625))
                    elif (calculate_player_points() < calculate_computer_points()):
                        screen.blit(you_win, (562, 625))
                    elif (calculate_computer_points() < calculate_player_points()):
                        screen.blit(you_lose, (625, 625))
                    else:
                        screen.blit(tie, (650, 625))
                    for k in range(10000):
                        l=k
                    # pygame.time.delay(5000)
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('g'):
                        you_win = pygame.image.load("playing_cards/you_win.png")
                        you_lose = pygame.image.load("playing_cards/you_lose.png")
                        tie = pygame.image.load("playing_cards/tie.png")
                        if (is_valid_run_player() == True) and (is_valid_run_computer() == False):
                            screen.blit(you_win, (562, 625))
                        elif (is_valid_run_player() == False) and (is_valid_run_computer() == True):
                            screen.blit(you_lose, (625, 625))
                        elif (is_valid_joker_run_player() == True) and (is_valid_joker_run_computer() == False):
                            screen.blit(you_win, (562, 625))
                        elif (is_valid_joker_run_player() == False) and (is_valid_joker_run_computer() == True):
                            screen.blit(you_lose, (625, 625))
                        elif (calculate_player_points() < calculate_computer_points()):
                            screen.blit(you_win, (562, 625))
                        elif (calculate_computer_points() < calculate_player_points()):
                            screen.blit(you_lose, (625, 625))
                        else:
                            screen.blit(tie, (650, 625))
                        done = True
        you_win = pygame.image.load("playing_cards/you_win.png")
        you_lose = pygame.image.load("playing_cards/you_lose.png")
        tie = pygame.image.load("playing_cards/tie.png")
        pygame.display.update()
        clock.tick(1000)

    if(done == True):

        for k in range(10000000):
            l=k
    pygame.quit()



if __name__ == '__main__':
    moves = 10
    main()

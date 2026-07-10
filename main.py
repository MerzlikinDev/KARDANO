#!/bin/python3
'''1. ввести текст для шифровки
   2. подобрать сторону квадрата
   3. нарисовать квадратики и буквы в них
'''
'''
    1. чтобы при нажатии на пробел появлялись группы повернутые на 90 
    градусов, а старые группы становились ближе к серому.
    2. чтобы при нажатии на пробел результат был не в терминале, а в отдельном окошке
    3. сделать расшифровка режим - подается файл с шифром, а затем высвечивается окно, в котором пользователь выбирает решетку кардано, а затем программма читает шифро-текст по этим выделенным клеткам.
    4. сделать дефифровка - подается шифротекст, программа рассматривает все варианты и пытается найти осмысленные фразы

'''
from sys import exit
import pygame
from collections import defaultdict
import platform
pygame.init()

'''получает строку, которую мы помещаем в квадрат. 
   Возвращает минимальный размер квадрата, в которую можно уместить эту строку.'''
def get_square_size(string: str) -> int:
    length = len(string)
    i  = 0
    while (i ** 2) < length:
        i += 1
    if i % 2:
       return i + 1 
    return i

'''получает строку, которую мы помещаем в квадрат, а также индекс буквы.
   Возвращает буквы в строке по заданному индексу
'''
def get_letter_by_index(string: str, index: int) -> str:
    if index < 0 or index > len(string) - 1:
        return "*"
    else:
        return string[index]
WINDOW_SIZE = 1000
GAP = 5
font = pygame.font.SysFont("arial", 40)

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
text = ""
color_when_pressed = pygame.Color('lightskyblue3')
color_when_not_pressed = pygame.Color('chartreuse4')
current_color = color_when_not_pressed
is_pressed = False
input_box = pygame.Rect(250, 470, 500, 45)
pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos): # проверка что я попалл
                is_pressed = True
                current_color = color_when_pressed
            else:
                is_pressed = False
                current_color = color_when_not_pressed
            
        if event.type == pygame.TEXTINPUT:
            if is_pressed:
                text += event.text
            
        elif event.type == pygame.KEYDOWN:
            if is_pressed:
                if event.key == pygame.K_RETURN:
                    MODE = text
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1] # в помойку

    screen.fill((30, 30, 30))
        
    pygame.draw.rect(screen, current_color, input_box, 2)
    text1 = font.render("введите режим", True, (255, 255, 255))
    screen.blit(text1, (360, 350))
    txt_surface = font.render(text, True, (255, 255, 255))
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        
    pygame.display.flip()

pygame.quit()
pygame.init()
SYSTEM = str(platform.system())
print(f'(TEST) YOUR SYSTEM IS {SYSTEM}')


if MODE == "standart":
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    font = pygame.font.SysFont("arial", 40)
    text = ""
    color_when_pressed = pygame.Color('lightskyblue3')
    color_when_not_pressed = pygame.Color('chartreuse4')
    current_color = color_when_not_pressed
    is_pressed = False
    input_box = pygame.Rect(250, 470, 500, 45)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos): # проверка что я попалл
                    is_pressed = True
                    current_color = color_when_pressed
                else:
                    is_pressed = False
                    current_color = color_when_not_pressed
            
            if event.type == pygame.TEXTINPUT:
                if is_pressed:
                    text += event.text
            
            elif event.type == pygame.KEYDOWN:
                if is_pressed:
                    if event.key == pygame.K_RETURN:
                        InputString = text
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1] # в помойку

        screen.fill((30, 30, 30))
        
        pygame.draw.rect(screen, current_color, input_box, 2)
        text1 = font.render("введите текст для шифрования", True, (255, 255, 255))
        screen.blit(text1, (230, 350))
        txt_surface = font.render(text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        
        pygame.display.flip()

    pygame.quit()
elif MODE == "decode":
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    font = pygame.font.SysFont("arial", 40)
    font1 = pygame.font.SysFont("arial", 25)
    text = ""
    color_when_pressed = pygame.Color('lightskyblue3')
    color_when_not_pressed = pygame.Color('chartreuse4')
    current_color = color_when_not_pressed
    is_pressed = False
    input_box = pygame.Rect(375, 470, 250, 45)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos): # проверка что я попалл
                    is_pressed = True
                    current_color = color_when_pressed
                else:
                    is_pressed = False
                    current_color = color_when_not_pressed
            
            if event.type == pygame.TEXTINPUT:
                if is_pressed:
                    text += event.text
            
            elif event.type == pygame.KEYDOWN:
                if is_pressed:
                    if event.key == pygame.K_RETURN:
                        InputString = text
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1] # в помойку

        screen.fill((30, 30, 30))
        
        pygame.draw.rect(screen, current_color, input_box, 2)
        text1 = font1.render("введите названия фала для извлечения шифротекста", True, (255, 255, 255))
        screen.blit(text1, (250, 350))
        txt_surface = font.render(text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        
        pygame.display.flip()

    pygame.quit()
    with open((InputString).strip("\n"), "r") as file:
        InputString = list(file)[0].strip("\n")
pygame.init()
N = get_square_size(InputString)
SQUARES_SIZE = (WINDOW_SIZE - ((N + 1) * GAP)) // N
FONT_SIZE = SQUARES_SIZE // 3 * 2
FONT = pygame.font.Font(None, FONT_SIZE)
X0 = GAP
Y0 = GAP
TOTAL = SQUARES_SIZE * N + GAP * (N - 1)
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("KARDANO")
space_is_pressed = False
if MODE == "standart":
    clock = pygame.time.Clock()
    is_pressed = defaultdict(bool)
    group_is_pressed = defaultdict(bool)
    while True:  
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            # потом и кровью...
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_x_pos, mouse_y_pos = ev.pos
                for row in range(N):
                    for col in range(N):
                        current_x = X0 + col * (SQUARES_SIZE + GAP)
                        current_y = Y0 + row * (SQUARES_SIZE + GAP)
                        if (current_x <= mouse_x_pos <= current_x + SQUARES_SIZE and current_y <= mouse_y_pos <= current_y + SQUARES_SIZE):
                            n1 = (col, N - 1 - row)
                            n2 = (n1[1], N - 1 - n1[0])
                            n3 = (n2[1], N  - 1 - n2[0])
                            
                            if all([not is_pressed[i] for i in (n1, n2, n3)]):
                                is_pressed[(row, col)] = True
                                group_is_pressed[n1] = True
                                group_is_pressed[n2] = True
                                group_is_pressed[n3] = True
                            else:
                                is_pressed[(row, col)] = False
                                if all((not i in group_is_pressed) for i in (n1, n2, n3)):
                                    group_is_pressed[n1] = False
                                    group_is_pressed[n2] = False
                                    group_is_pressed[n3] = False
            # чтобы результат выводить (по тупому с двумя циклами)
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    res = ""
                    index1 = 0
                    for row in range(N):
                        for col in range(N):
                            print(f'тек. индекс: {index1}; тек. рез: {res}')
                            if is_pressed.get((row, col), False):
                                res += get_letter_by_index(InputString, index1)
                            index1 += 1
                    print("------------")
                    print(res)
                    print("------------")
                    screen.fill((255, 255, 255))
                    space_is_pressed = True
                    text = FONT.render("RESULT: " + res, True, (0, 0, 0))  
                    screen.blit(text, (0, 0))
        
        # цикл который рисует квадратики и буквы на них (а еще картинки)
        if not space_is_pressed:
            positions = []          
            screen.fill((255, 0, 255))
            index = 0
            for row in range(N):
                for col in range(N):
                    n1 = (col, N - 1 - row)
                    n2 = (n1[1], N - 1 - n1[0])
                    n3 = (n2[1], N  - 1 - n2[0])
                    current_x = X0 + col * (SQUARES_SIZE + GAP) # djdjd
                    current_y = Y0 + row * (SQUARES_SIZE + GAP)
                    if group_is_pressed[(row, col)] == True:
                        rect = pygame.draw.rect(screen, (84, 92, 78), (current_x, current_y, SQUARES_SIZE, SQUARES_SIZE))
                    elif is_pressed.get((row, col), False):
                        rect = pygame.draw.rect(screen, (0, 102, 0), (current_x, current_y, SQUARES_SIZE, SQUARES_SIZE))

                    else:
                        rect = pygame.draw.rect(screen, (0, 0, 0), (current_x, current_y, SQUARES_SIZE, SQUARES_SIZE))
                    text_for_square = get_letter_by_index(InputString, index)
                    text = FONT.render(text_for_square, True, (255, 255, 255))  

                    text_x = current_x + SQUARES_SIZE // 2 - text.get_width() // 2
                    text_y = current_y + SQUARES_SIZE // 2 - text.get_height() // 2 

                    screen.blit(text, (text_x, text_y))
            
                    index += 1                     
        pygame.display.flip()
        clock.tick(60)
elif MODE == "decode":
    is_pressed = defaultdict(bool)
    clock = pygame.time.Clock()
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_x_pos, mouse_y_pos = ev.pos
                for row in range(N):
                    for col in range(N):
                        current_x = X0 + col * (SQUARES_SIZE + GAP)
                        current_y = Y0 + row * (SQUARES_SIZE + GAP)
                        if (current_x <= mouse_x_pos < current_x + SQUARES_SIZE) and (current_y <= mouse_y_pos < current_y + SQUARES_SIZE):
                            n1 = (col, N - 1 - row)
                            n2 = (n1[1], N - 1 - n1[0])
                            n3 = (n2[1], N  - 1 - n2[0])
                            if all([not is_pressed[i] for i in (n1, n2, n3)]):
                                is_pressed[(row, col)] = True
                                is_pressed[n1] = 67
                                is_pressed[n2] = 67
                                is_pressed[n3] = 67
            if ev.type == pygame.KEYDOWN and not space_is_pressed:
                if ev.key == pygame.K_SPACE:
                    res = ""
                    index1 = 0
                    for row in range(N):
                        for col in range(N):
                            if is_pressed[(row, col)] == True:
                                res += get_letter_by_index(InputString, index1)
                            index1 += 1
                    print(res)
                    screen.fill((255, 255, 255))
                    space_is_pressed = True
                    text = FONT.render("RESULT: " + res, True, (0, 0, 0))  
                    screen.blit(text, (0, 0))
        if not space_is_pressed:
            screen.fill((255, 0, 255))
            for row in range(N):
                for col in range(N):
                    current_x = X0 + col * (SQUARES_SIZE + GAP)
                    current_y = Y0 + row * (SQUARES_SIZE + GAP)
                    if is_pressed[(row, col)] == 67:
                        pygame.draw.rect(screen, (84, 92, 78), (current_x, current_y, SQUARES_SIZE, SQUARES_SIZE))
                    elif is_pressed.get((row, col), False):
                        pygame.draw.rect(screen, (0, 108, 0), (current_x, current_y, SQUARES_SIZE, SQUARES_SIZE))
                    else:
                        pygame.draw.rect(screen, (0, 0, 0), (current_x, current_y, SQUARES_SIZE, SQUARES_SIZE))
        pygame.display.flip()
        clock.tick(60)

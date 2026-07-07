from sys import exit
import tkinter as tk
import pygame
from collections import defaultdict
from tkinter import scrolledtext
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
MODE = input("введите режим: ")
if MODE == "standart":
    InputString = input("введите входную строку: ").replace(" ", "")
elif MODE == "decode":
    with open(input("введите имя файла для извлечения шифротекста: "), "r") as pisun:
        InputString = list(pisun)[0]
WITH_LINA_AND_PUDGE = input()
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
                    text = FONT.render(res, True, (0, 0, 0))  
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
                        if WITH_LINA_AND_PUDGE == "OK":
                            scaled_image = pygame.transform.scale(pygame.image.load("Изображения/pudge.png"), (rect.width, rect.height))
                            screen.blit(scaled_image, rect)
                    else:
                        rect = pygame.draw.rect(screen, (0, 0, 0), (current_x, current_y, SQUARES_SIZE, SQUARES_SIZE))
                        if WITH_LINA_AND_PUDGE == "OK":
                            scaled_image = pygame.transform.scale(pygame.image.load("Изображения/2026-06-30_21-32.png"), (rect.width, rect.height))
                            screen.blit(scaled_image, rect)

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
                    text = FONT.render(res, True, (0, 0, 0))  
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

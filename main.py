import pygame
import sys
from map import load_level
from random import choice

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Инициализация экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PACMAN ЗАГАТОВКА")

# Загрузка изображений значков
icon_on = pygame.image.load("sounds/on.png")
icon_off = pygame.image.load("sounds/off.png")
hearticon = pygame.image.load("heart.png")

# Установка начального состояния (включено)
music_on = True
icon = icon_on

# Загрузка музыкального файла
pygame.mixer.music.load("sounds/pacman.mp3")
pygame.mixer.music.play(-1)

# Основной цикл программы
running = True


class Pacman:
    def __init__(self, l, r):
        self.pos = (l, r)
        self.direct = 1


class GameBoard:
    def __init__(self):
        self.board = load_level('map2.txt')
        self.db = load_level('map2.txt')
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.clrs = [[None for i in range(self.width)] for j in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                self.clrs[i][j] = None
        self.left = 100
        self.top = 100
        self.cell_size = 20
        self.pc = Pacman(self.left + self.cell_size + 10, self.top + self.cell_size + 10)

    def get_color(self):
        return (152, 251, 152)

    def print_board(self, screen):
        if self.pc.direct == 1:
            y = (self.pc.pos[0]-self.top+10) // self.cell_size
            x = (self.pc.pos[1]-self.left) // self.cell_size
            print(y,x,self.board[y][x])
            if self.board[x][y] != 'X':
                self.pc.pos = (self.pc.pos[0] + 2, self.pc.pos[1])
        for h in range(self.height):
            for w in range(self.width):
                if self.board[h][w] == 'X':
                    self.db[h][w] = pygame.draw.rect(screen, self.get_color(), (
                        self.left + w * self.cell_size, self.top + h * self.cell_size, self.cell_size, self.cell_size))

                    if w - 1 > 0 and (self.board[h][w - 1] in [' ', 'C', 'P', 'G']) or (w == 0):
                        pygame.draw.line(screen, 'black', (
                            self.left + w * self.cell_size, self.top + h * self.cell_size), (
                                             self.left + w * self.cell_size, self.top + (h + 1) * self.cell_size), 2)

                    if h - 1 > 0 and (self.board[h - 1][w] in [' ', 'C', 'P', 'G']) or (h == 0):
                        pygame.draw.line(screen, 'black', (
                            self.left + w * self.cell_size, self.top + h * self.cell_size), (
                                             self.left + (w + 1) * self.cell_size, self.top + (h) * self.cell_size), 2)

                    if h + 1 < self.height and (self.board[h + 1][w] in [' ', 'C', 'P', 'G']) or (
                            h == self.height - 1):
                        pygame.draw.line(screen, 'black', (
                            self.left + (w) * self.cell_size, self.top + (h + 1) * self.cell_size), (
                                             self.left + (w + 1) * self.cell_size, self.top + (h + 1) * self.cell_size),
                                         2)

                    if w + 1 < self.width and (self.board[h][w + 1] in [' ', 'C', 'P', 'G']) or (w == self.width - 1):
                        pygame.draw.line(screen, 'black', (
                            self.left + (w + 1) * self.cell_size, self.top + h * self.cell_size), (
                                             self.left + (w + 1) * self.cell_size, self.top + (h + 1) * self.cell_size),
                                         2)
        pygame.draw.circle(screen, color='black', center=self.pc.pos, radius=10)
        pygame.draw.circle(screen, color='yellow', center=self.pc.pos, radius=9)


brd = GameBoard()
fps = 50  # количество кадров в секунду
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка клика по значку
            if icon.get_rect(topleft=(10, 10)).collidepoint(event.pos):
                # Включение/выключение музыки
                if music_on:
                    pygame.mixer.music.pause()
                    icon = icon_off
                else:
                    pygame.mixer.music.unpause()
                    icon = icon_on
                music_on = not music_on

    # Отрисовка экрана
    screen.fill(pygame.Color('white'))
    screen.blit(icon, (10, 10))
    screen.blit(hearticon, (720, 550))
    screen.blit(hearticon, (690, 550))
    screen.blit(hearticon, (750, 550))
    brd.print_board(screen)
    # Обновление экрана
    pygame.display.flip()
    clock.tick(fps)
# Завершение работы Pygame
pygame.quit()
sys.exit()

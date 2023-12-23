import pygame
import sys

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

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
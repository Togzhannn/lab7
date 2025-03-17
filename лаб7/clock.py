import pygame
from datetime import datetime

pygame.init()
pygame.display.set_caption("Mickey Clock")

# Настройки окна
WIDTH, HEIGHT = 500, 500
scr = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка изображений
im1 = pygame.image.load("mickeyclock.png").convert_alpha()
im1 = pygame.transform.scale(im1, (410, 400))

im2 = pygame.image.load("lefthand.png").convert_alpha()
im3 = pygame.image.load("righthand.png").convert_alpha()

# Легкое уменьшение стрелок
scale_factor = 1.03  # Было 1.05, еще чуть уменьшил
im2 = pygame.transform.scale(im2, (int(im2.get_width() * scale_factor), int(im2.get_height() * scale_factor)))
im3 = pygame.transform.scale(im3, (int(im3.get_width() * scale_factor), int(im3.get_height() * scale_factor)))

clock = pygame.time.Clock()
run = True

while run:
    scr.fill((255, 255, 255))
    scr.blit(im1, (50, 50))  # Отрисовка фона

    # Получаем текущее время
    now = datetime.now()
    sec = now.second
    min = now.minute

    # Углы поворота
    sec_angle = - (sec * 6)
    min_angle = - (min * 6)

    # Центр вращения рук (ТОЧНО В ПЛЕЧАХ)
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 40  # Еще чуть опустил центр
    offset_x, offset_y = 0, -65  # Финальная точка вращения

    # Поворот и позиционирование стрелок
    rotated_im2 = pygame.transform.rotate(im2, sec_angle)
    rotated_im3 = pygame.transform.rotate(im3, min_angle)

    sec_rect = rotated_im2.get_rect(center=(center_x + offset_x, center_y + offset_y))
    min_rect = rotated_im3.get_rect(center=(center_x + offset_x, center_y + offset_y))

    # Отрисовка стрелок
    scr.blit(rotated_im2, sec_rect.topleft)
    scr.blit(rotated_im3, min_rect.topleft)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(30)

pygame.quit()

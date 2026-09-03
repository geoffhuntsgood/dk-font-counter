from os import path
import pygame
from pygame import display, event, image, key, time, transform

# Setup
pygame.init()
screen = display.set_mode((300, 110), pygame.NOFRAME)
clock = time.Clock()
current_num = 0

# Preload images
imgs = [
    image.load(path.join("numbers/0.png")),
    image.load(path.join("numbers/1.png")),
    image.load(path.join("numbers/2.png")),
    image.load(path.join("numbers/3.png")),
    image.load(path.join("numbers/4.png")),
    image.load(path.join("numbers/5.png")),
    image.load(path.join("numbers/6.png")),
    image.load(path.join("numbers/7.png")),
    image.load(path.join("numbers/8.png")),
    image.load(path.join("numbers/9.png")),
]

running = True

while running:
    for ev in event.get():
        # Exit
        if key.get_pressed()[pygame.K_ESCAPE]:
            running = False

    screen.fill("chartreuse4")

    str_num = str(current_num).zfill(3)
    hundreds = imgs[int(str_num[0])]
    tens = imgs[int(str_num[1])]
    ones = imgs[int(str_num[2])]

    screen.blits(
        [
            (transform.scale_by(hundreds, 5), (0, 0)),
            (transform.scale_by(tens, 5), (100, 0)),
            (transform.scale_by(ones, 5), (200, 0)),
        ]
    )

    pygame.display.flip()

    if current_num < 999 and (
        key.get_pressed()[pygame.K_RIGHT] or key.get_pressed()[pygame.K_UP]
    ):
        current_num += 1
    if current_num > 0 and (
        key.get_pressed()[pygame.K_LEFT] or key.get_pressed()[pygame.K_DOWN]
    ):
        current_num -= 1

    clock.tick(15)

pygame.quit()

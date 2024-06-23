# 工具和游戏主控
import os.path

import pygame
import random


class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()

    def run(self, state):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            state.update(self.screen, self.keys)
            pygame.display.update()
            self.clock.tick(60)


def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics


def get_image(sheet, x, y, width, height, color_key, scale):
    image = pygame.Surface((width, height))
    # 0，0 表示画到哪个位置，x,y,w,h代表sheet里哪个区域要取出来
    image.blit(sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(color_key)
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    return image

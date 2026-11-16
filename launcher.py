import pygames
import sys
import os
from common.constants import *

from games.snake.main import run_snake
from games.flappy.main import run_flappy
from games.shooter.main import run_shooter

pygame.init()

# O laucher usa suas proprias dimensoes correspondentes à proporção de bg-new.png (16:9)
# Laucher_W, LAUCHER_H = 800, 450

screen = pygames.display.set_mode((LAUCHER_w, LAUNCHER_H))
clock = pygame.time .Clock()

base = os.path.abspath(os.path.join(os.path.dirname(__file__), "assets/launcher"))
bg = pygame.image.load(os.path.join(base, "bg-new.png"))
bg = pygame.transform.scale(bg, (LAUCHER_W, LAUCHER_H))

# Tamanho original da imagem para cálculos de proporção
IMG_W, IMG_H = 1672, 941
sx = LAUNCHER_W / IMG_W
SY = LAUNCHER_H / IMG_H

# Posições dos cards mapeados do layout original bg-new.png (verificadas visualmente)
# Todos os 3 cards tem o mesmo tamanho; ordem: Flappy (esquerda), Shooter (centro), Snake(direita)
def scaled_rect(x, y, w, h):
    return pygame.Rect(int(x * sx), int(y * sy), int(w * sx), int(h * sy))

CARD_W, CARD_H = 312, 358
CARD_Y = 430

card_flappy = scaled_rect(342, CARD_Y, CARD_W, CARD_H)
card_shooter = scaled_rect(680, CARD_Y, CARD_W, CARD_H)
card_snake   = scaled_rect(1026, CARD_Y, CARD_W, CARD_H)

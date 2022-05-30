'''EXERCÍCIO 021: Tocando um MP3
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

'''O arquivo ex21.mp é uma arquivo mp3 que esta localizada dentro da mesma pasta desse programa'''

import pygame
from time import sleep
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()





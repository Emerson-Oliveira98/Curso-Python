import pygame
# precisamos iniciar a pygame
pygame.init()
# informar o arquivo que será executado
pygame.mixer.music.load('regard-ride-it-official-video-ucVUEmjKsko.mp3')
# tocar o arquivo
pygame.mixer.music.play()
#esperar o evento de tocar a musica terminar
pygame.event.wait()
import pygame_play

pygame.init()

pygame.mixer.music.load('sample.mp3')

while True:
    cmd = input("play:p, pause:pp, unpause:up, stop:s, quit:q > ")
    if cmd == 'p':
        pygame.mixer.music.play()
    elif cmd == 'pp':
        pygame.mixer.music.pause()a
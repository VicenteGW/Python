import pygame

print('=' * 46)
print('{:^46}'.format('BATIDÃO DO VICENTÃO'))
print('=' * 46)
pygame.init()
pygame.mixer.music.load('C:/Users/VicenteGW/GitHub/Python/PythonExercicios/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

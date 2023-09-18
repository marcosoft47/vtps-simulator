import sys
import os
import random
try:
    import pygame
    from pygame.locals import *
except:
    os.system("pip install pygame")
    import pygame
    from pygame.locals import *

class Ricardo:
    def __init__(self):
        global ricardo
        self.square = 400
        self.contador = 0
        self.x = random.randint(1, largura-self.square)
        self.xdir = 1
        self.y = random.randint(1, altura-self.square)
        self.ydir = 1
        self.imagem = ricardo
        self.estado = True

    def update(self):
        surface.blit(self.imagem,(self.x,self.y))
        global speed, ricardo, feliz
        if self.y >= altura - self.square:
            self.ydir = -1
            self.contador += 1
        if self.y <= 0:
            self.ydir = 1
            self.contador += 1
        if self.x >= largura - self.square:
            self.xdir = -1
            self.contador += 1
        if self.x <= 0:
            self.xdir = 1
            self.contador += 1
        self.y += self.ydir * speed
        self.x += self.xdir * speed
        if self.contador >= 1:
            self.trocarImagem()

        if self.contador>=2:
            tocar_som()
                
        self.contador = 0
        
    def trocarImagem(self):
        if self.estado:
            self.imagem = feliz
        else:
            self.imagem = ricardo
        self.estado = not self.estado

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def tocar_som():
    pygame.mixer.find_channel(force=True).play(audio)        
    #pygame.mixer.fadeout(5000)






pygame.init()
pygame.mixer.init()
largura = 1920
altura = 1020
speed = 5
surface = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption('ricardofm.me')

audio = pygame.mixer.Sound(resource_path('ratinho.ogg'))
pygame.mixer.music.load(resource_path('ratinho.ogg'))
tamanho = audio.get_length()
qntchannels = 1

ricardo = pygame.transform.scale(pygame.image.load(resource_path('imagens/ricardo.jpeg')).convert(), (400,400))
feliz = pygame.transform.scale(pygame.image.load(resource_path('imagens/feliz.jpeg')).convert(), (400,400))
relogio = pygame.time.Clock()
fm = [Ricardo()]





running = True
while running:
    relogio.tick(60)
    surface.fill((0,0,0))
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if e.key == K_KP_PLUS:
                fm.append(Ricardo())
                pygame.mixer.set_num_channels(pygame.mixer.get_num_channels()+1)
            if e.key == K_KP_MINUS:
                if len(fm)>0:
                    fm.pop()
                    pygame.mixer.set_num_channels(pygame.mixer.get_num_channels()-1)
            if e.key == K_UP:
                speed += 5
            if e.key == K_DOWN or e.key == K_DOWN:
                speed -= 5
    
    largura, altura = surface.get_size()
    for i in range(len(fm)):
        fm[i].update()

    pygame.display.update()

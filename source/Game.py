import pygame
import Resources, ScreenManager, Intro

class Game():
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('NOMEDOJOGO')
        pygame.mouse.set_visible(False)
        
        icon = pygame.Surface((32,32))
        iconImage = pygame.image.load("res/img/icon.png")
        iconRect = iconImage.get_rect()
        icon.blit(iconImage,iconRect)
        pygame.display.set_icon(icon)
        
        pygame.display.set_mode(Resources.DEFAULT_SCREEN_SIZE, pygame.FULLSCREEN)
        
        manager = ScreenManager.ScreenManager()
        #s = Stage.Stage1(manager)
        
        pygame.mixer.init()
        
        manager.setBaseObjectToUpdate(Intro.Intro(manager))
        manager.run()
        
        pygame.mixer.quit()
        pygame.quit()

# cria uma classe Game, que ja chama o metodo ScreenManager.run() que executa o jogo
Game()
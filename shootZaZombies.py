
# -*- coding: utf-8 -*-
"""
@author: andrew.scott
"""
#sounds
#gunshot https://opengameart.org/content/light-machine-gun
#deathSound https://opengameart.org/content/2-male-death-voices
#backgroundMusic https://opengameart.org/content/ambient-apocalyptic-soundtracks
#sprites
#zombie https://opengameart.org/content/animated-top-down-zombie
#player https://opengameart.org/content/animated-top-down-survivor-player
#background https://opengameart.org/content/2d-top-down-highway-background
#splat https://opengameart.org/content/8-wet-squish-slurp-impacts

import pygame, simpleGE, random, sys

pygame.init()

pygame.mixer.init()

def splat():
    sound = pygame.mixer.Sound("impactsplat01.mp3.flac")
    sound.play()
    
def play_gunshot():
    sound = pygame.mixer.Sound("lmg_fire01.mp3")
    sound.play()
    
def backroundMusic():
    sound = pygame.mixer.Sound("Szymon Matuszewski - Hospital.mp3")
    sound.play()
    sound.play(loops=-1)
    
def deathSound():
    sound = pygame.mixer.Sound("16.wav")
    sound.play()
    
class Background(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = {
            "bg": pygame.image.load("background.png"),
        }
        self.imageMaster = self.images["bg"]
        self.setSize(900, 900)
        
    
class BtnQuit(simpleGE.Button):
    def __init__(self, scene):
        super().__init__()
        self.text = "Quit"
        self.hide()
            
    
class LblTimer(simpleGE.Label):
    def __init__(self, scene):
        super().__init__()
        self.center = (325, 100)
        self.timer = simpleGE.Timer()
        self.size = (300, 30)
        self.hide()
        
class LblVictory(simpleGE.Label):
    def __init__(self, scene):
        super().__init__()
        self.center = (300, 100)
        self.text = "You Survived the Horde"
        self.size = (300, 30)
        self.hide()
        
        
class LblZombie_Kill(simpleGE.Label):
    def __init__(self, scene):
        super().__init__()
        self.center = (75, 20)
        self.zombies_killed = 0
        self.text = "Zombies Killed: 0"
        self.size = (200, 30)
        self.hide()
   
    def reset(self):
        self.zombies_killed = 0
        self.text = f"Zombies Killed: {self.zombies_killed}"

class LblWaves(simpleGE.Label):
    def __init__(self, scene):
        super().__init__()
        self.center = (550, 20)
        self.waves = 0
        self.text = "WAVE: 0"
        self.hide()

    def reset(self):
        self.waves = 0
        self.text = f"WAVE: {self.waves}"

class StartScreen(simpleGE.MultiLabel):
    def __init__(self, scene):
        super().__init__()
        self.textLines = [
            "Move With WASD",
            "Shoot with LMouseClick",
            "Survive the oncoming waves",
            "There is no time between waves so,"
            "Shoot to kill",
            "No Matter What Happens",
            "SURVIVE",
            "Click The Screen to continue",
        ]
        self.center = ((320, 240))
        self.size = ((350, 400))

class Bullet(simpleGE.SuperSprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.imageMaster = pygame.Surface((5, 5))
        self.imageMaster.fill(pygame.Color("white"))
        self.setBoundAction(self.HIDE)
        self.hide()

    def fire(self):
        self.show()
        self.setPosition(self.parent.rect.center)
        self.setMoveAngle(self.parent.rotation)
        self.setSpeed(30)
        
    def reset(self):
        self.hide()
        self.setSpeed(0)
        
class Player(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = {
            "pistol": pygame.image.load("playerPistol.gif"),
        }
        self.imageMaster = self.images["pistol"]
        self.setAngle(90)
        self.setSize(50, 50)
        self.hide()
       
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_w):
            self.y += -3

        if self.scene.isKeyPressed(pygame.K_s):
            self.y += 3

        if self.scene.isKeyPressed(pygame.K_a):
            self.x += -3

        if self.scene.isKeyPressed(pygame.K_d):
            self.x += 3

        pos = pygame.mouse.get_pos()
        direction_to_mouse = self.dirTo(pos)
        self.setAngle(direction_to_mouse)

    def reset(self):
        self.x = 325
        self.y = 250

    def update(self):
        super().update()

class Zombie(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = {
            "walk": pygame.image.load("topdownZomb.png")
        }
        self.imageMaster = self.images["walk"]
        self.setSize(50, 50)
        self.x = 999
        self.y = 20
        self.setBoundAction(self.CONTINUE)
        
    def checkEvents(self):
        #set angle towards player
        dirToPlayer = self.dirTo(self.scene.player.rect.center)
        self.setAngle(dirToPlayer)
        
        for bullet in self.scene.bullets:
            if self.collidesWith(bullet):
                bullet.reset()
                self.hide()
                splat()
                self.scene.enemiesLeft -= 1 
                self.scene.zombiesKilled.zombies_killed += 1
                break
            
        if self.rect.colliderect(self.scene.player.rect):
            self.scene.pauseGame()
            for i in range(1):
                deathSound()

                
        if self.x > 800:
            self.setSpeed(0)
        else:
            self.setSpeed(1.5)
            
            
       
    def reset(self):
        side = random.randint(0, 3)
        if side == 0:
            # top            
            self.x = random.randint(0, self.screen.get_width())
            self.y = random.randint(-130, 0)
        elif side == 1:
            # left
            self.x = random.randint(-130, 0)
            self.y = random.randint(0, self.screen.get_height())
        elif side == 2:
            # bottom
            self.x = random.randint(0, self.screen.get_width())
            self.y = random.randint(480, 600)
        else:
            # right
            self.x = random.randint(640, 799)
            self.y = random.randint(0, self.screen.get_height())


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.bg = Background(self)
        self.btnQuit = BtnQuit(self)
        self.victory = LblVictory(self)
        self.zombiesKilled = LblZombie_Kill(self)
        self.startScreen = StartScreen(self)
        self.player = Player(self)
        self.waves_label = LblWaves(self)
        self.lblTimer = LblTimer(self)
        
        self.NUM_BULLETS = 100
        self.currentBullet = 0
        self.waveNum = 0
        self.enemiesLeft = 0 
        self.zombies = []
        for i in range(100):
            self.zombies.append(Zombie(self))
           
        self.bullets = []
        for i in range(self.NUM_BULLETS):
            self.bullets.append(Bullet(self, self.player))
           
        self.lblTimer.hide()
       
        backroundMusic()
        
        self.sprites = [self.bg, self.player, self.victory, self.startScreen, self.bullets,
                        self.waves_label, self.zombies, self.zombiesKilled, self.lblTimer, self.btnQuit]
       
               
    def doEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.currentBullet += 1
            if self.currentBullet >= self.NUM_BULLETS:
                self.currentBullet = 0
            self.bullets[self.currentBullet].fire()
            play_gunshot()
            
    def pauseGame(self):
        self.btnQuit.show((320, 240))
        self.player.hide()
        self.startScreen.hide()
        for bullet in self.bullets:
            bullet.hide()
        self.waves_label.hide()
        for zombie in self.zombies:
            zombie.hide()
        self.lblTimer.hide()

    def resetGame(self):
        self.startScreen.hide()
        self.player.reset()
        self.waves_label.show((550, 20))
        self.zombiesKilled.show((100, 20))
        self.lblTimer.show((325, 100))

    def update(self):
        print (self.enemiesLeft)
        self.zombiesKilled.text = f"Zombies Killed: {self.zombiesKilled.zombies_killed}"
        self.waves_label.text = f"Wave: {self.waveNum}"
        
        if self.startScreen.clicked:
            self.resetGame()
            
        if self.btnQuit.clicked:
            pygame.quit()
                
        if self.enemiesLeft == 0: 
            self.lblTimer.show((325, 100))
            timeLeft = 15 - self.lblTimer.timer.getElapsedTime()
            self.lblTimer.text = f"Time until Horde Arrives: {timeLeft:.2f}"
            if timeLeft < 0:
                self.waveNum += 1
                self.lblTimer.hide()
            
            if self.waveNum == 1:
                for zombie in self.zombies[:10]:
                    zombie.reset()
                    self.enemiesLeft += 1
                    
            elif self.waveNum == 2:
                for zombie in self.zombies[11:26]:
                    zombie.reset()
                    self.enemiesLeft += 1
                    
            elif self.waveNum == 3:
                for zombie in self.zombies[27:57]:
                    zombie.reset()
                    self.enemiesLeft += 1
                    
            elif self.waveNum == 4:
                self.victory.show((300, 100))
                self.pauseGame()
                    
                
        super().update()

def main():
    game = Game()
    game.start()
    sys.exit()
    
if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 01:12:02 2023

@author: theaw
"""

import pygame, simpleGE, random
pygame.init()

class LblWaves(simpleGE.Label):
    def __init__(self, scene):
        super().__init__()
        self.center = (550,20)
        self.waves = 0
        self.text = "WAVE: 0"
        self.hide()
    
    def reset(self):
        self.lives = 0
        self.text = f"WAVE: {self.waves}"
        
class StartScreen(simpleGE.MultiLabel):
    def __init__(self, scene):
        super().__init__()
        self.textLines = [
            "Move With WASD",
            "Shoot with LMouseClick",
            "Survive the oncoming horde",
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
        self.setSpeed(20)

class Player(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.images = {
            "pistol": pygame.image.load("playerPistol.gif"),
        }
        self.imageMaster = self.images["pistol"]
        self.setAngle(90)
        self.setSize(50, 50)
        self.forward = 0
        self.dx = 0

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

        self.x += self.dx
        self.y += self.forward
   
class Zombie(simpleGE.SuperSprite):
    def __initad__(self, scene):
        super().__init(scene)
        self.images = {
            "walk": pygame.image.load("topdownZomb.png")
            }
        self.imageMaster = self.images["walk"]
        self.setAngel(90)
        self.setSize(50, 50)
        self.forward = 0
        self.dx = 0
       
    def checkEvents(self):
        if self.collidesWith(self.scene.bullet):
            self.reset()
            
    
   
    def doEvents(self):
        self.setAngle(Player)
        self.forward = 5
    
       
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.startScreen = StartScreen(self)
        self.player = Player(self)
        self.waves = LblWaves(self)
        self.NUM_BULLETS = 100
        self.currentBullet = 0    
        self.zombies = []
        self.bullets = []
        for i in range(self.NUM_BULLETS):
            self.bullets.append(Bullet(self, self.player))
       
        self.sprites = [self.player, self.startScreen, self.bullets, self.waves]
        
        self.zombies =[]
       
        self.player.hide()
        
    def waves(waveNumber, self):
        global normalEnemy,speedyEnemy, tankEnemy, enemiesList, waveCount
        if waveNumber == 1:
            zombie = 5
            boss = 0
            for i in range(zombie):
                self.zombies.append(Zombie(self, self.player))

        if waveNumber == 2:
            zombie = 7
            boss = 0
       
    def doEvents(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.currentBullet += 1
                if self.currentBullet >= self.NUM_BULLETS:
                    self.currentBullet = 0
                self.bullets[self.currentBullet].fire()
     
    def resetGame(self):
        self.startScreen.hide()
        self.player.reset()
        self.waves.show((550, 20))
       
    def update(self):
        if self.startScreen.clicked:
            self.resetGame()
        
        if zombie == 0:
            if boss == 0:
                self.scene.lives.lives -= 1
        
        self.waves.text = f"WAVES: {self.waves.waves}"
           


def main():
    game = Game()
    game.start()

   

if __name__ == "__main__":
    main()

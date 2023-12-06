import pygame, simpleGE, random, sys

pygame.init()

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
       
    def collide(self,zombie,zombies):
        if self.collidesWith(zombie.rect):
            self.reset

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
        self.setAngle(0)
        self.setSize(50, 50)
        self.reset()
       
    def checkEvents(self):
        #set angle towards player
        dirToPlayer = self.dirTo(self.scene.player.rect.center)
        self.setAngle(dirToPlayer)
        self.setSpeed(1.5)
       

    def reset(self):
        side = random.randint(0,3)
        if side == 0:
            #top            
            self.x = random.randint(0, self.screen.get_width())
            self.y = 0
        elif side == 1:
            #left
            self.x = 0
            self.y = random.randint(0, self.screen.get_height())
        elif side == 2:
            #bottom
            self.x = random.randint(0, self.screen.get_width())
            self.y = 480
        else:
            #right
            self.x = 640
            self.y = random.randint(0, self.screen.get_height())
           
           

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.zombiesKilled = LblZombie_Kill(self)
        self.startScreen = StartScreen(self)
        self.player = Player(self)
        self.waves_label = LblWaves(self)
        self.NUM_BULLETS = 100
        self.currentBullet = 0
        self.zombie = 0
       
        self.zombies = []
        for i in range(5):
            self.zombies.append(Zombie(self))
           
        self.bullets = []
        for i in range(self.NUM_BULLETS):
            self.bullets.append(Bullet(self, self.player))
           
        self.bullets_group = pygame.sprite.Group(self.bullets)
       

        self.sprites = [self.player, self.startScreen, self.bullets,
                        self.waves_label, self.zombies, self.zombiesKilled]
       

    def spawnWave(self):
        if self.waves_label.waves == 1:
            self.zombie = 1

            for i in range(self.zombie):
                self.zombies.append(Zombie(self))
           
            for zombie in self.zombies:
                zombie.reset()
               
    def checkEvents(self, event):
        for zombie in self.zombies:
            if zombie.collidesGroup(self.bullets):
                zombie.hide()
               
    def doEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.currentBullet += 1
            if self.currentBullet >= self.NUM_BULLETS:
                self.currentBullet = 0
            self.bullets[self.currentBullet].fire()

    def resetGame(self):
        self.startScreen.hide()
        self.player.reset()
        self.waves_label.show((550, 20))
        self.spawnWave()
        for zombie in self.zombies:
            zombie.reset()
        self.zombiesKilled.show((100, 20))

    def update(self):
        self.zombiesKilled.text = f"Zombies Killed: {self.zombiesKilled.zombies_killed}"
        
        if self.startScreen.clicked:
            self.resetGame()

        if self.zombie == 0:
            self.waves_label.waves += 1
            self.waves_label.text = f"WAVE: {self.waves_label.waves}"
            self.spawnWave()
            
        for bullet in self.bullets:
            for zombie in self.zombies:
                if bullet.collidesWith(zombie):
                    zombie.reset()
                    self.zombiesKilled.zombies_killed += 1
                    self.zombiesKilled.text = f"Zombies Killed: {self.zombiesKilled.zombies_killed}"
                
        
        for zombie in self.zombies:
            zombieHitBullet = zombie.collidesGroup(self.bullets)
            if zombieHitBullet:
                zombieHitBullet.hide()
                zombieHitBullet.setSpeed(0)
            
        for zombie in self.zombies:
            if zombie.collidesWith(self.player):
                zombie.reset()

        super().update()

def main():
    game = Game()
    game.start()
    sys.exit()

if __name__ == "__main__":
    main()

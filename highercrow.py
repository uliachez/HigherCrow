import pygame
pygame.init()

W = 800
H = 600
screen = pygame.display.set_mode((W, H))

FPS = 60
clock = pygame.time.Clock()

font_path = 'crow_font.ttf'
font_large = pygame.font.Font(font_path, 48)
font_small = pygame.font.Font(font_path, 24)

game_over = False
retry_text = font_small.render('PRESS ANY KEY', True, (255, 255, 255))
retry_rect = retry_text.get_rect()
retry_rect.midtop = (W // 2, H // 2)

ground_image =pygame.image.load('ground.jpg')
ground_image = pygame.transform.scale(ground_image, (804,60))
GROUND_H = ground_image.get_height()

enemy_image =pygame.image.load('vrag.jpg')
enemy_image = pygame.transform.scale(enemy_image, (80,80))

enemy_dead_image =pygame.image.load('vrag_dead.jpg')
enemy_dead_image = pygame.transform.scale(enemy_dead_image, (80,80))

player_image =pygame.image.load('vorona.png')
player_image = pygame.transform.scale(player_image, (60,80))

class Entity:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 5
        self.is_out = False
        self.is_dead = False
        self.jump_speed = -12
        self.gravity = 0.5
        self.is_grounded = False
    
    def handle_input(self):
        pass
    
    def kill(self, dead_image):
        self.image = dead_image
        self.is_dead = True
        self.x_speed = -self.x_speed
        self.y_speed = self.jump_speed
    
    def update(self):
        self.rect.x += self.x_speed
        self.y_speed += self.gravity
        self.rect.y += self.y_speed

        if self.is_dead:
            if self.rect.top > H - GROUND_H:
                self.is_out = True
        else:
            self.handle_input()

            if self.rect.bottom > H - GROUND_H:
                self.is_grounded = True
                self.y_speed = 0
                self.rect.bottom = H - GROUND_H
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(Entity):
    def __init__(self):
        super().__init__(player_image)

    def handle_input(self):
        self.x_speed = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_speed = -self.speed
        elif keys[pygame.K_d]:
            self.x_speed = self.speed
        
        if self.is_grounded and keys[pygame.K_w]:
            self.is_grounded = False
            self.jump()
    
    def respawn(self):
        self.is_out = False
        self.is_dead = False
        self.rect.midbottom = (W//2, H - GROUND_H)

    def jump(self):
        self.y_speed = self.jump_speed

player = Player()
score = 0

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
    clock.tick(FPS)
    
    screen.fill((178, 34, 34))

    screen.blit(ground_image, (0, H - GROUND_H))

    score_text= font_large.render(str(score), True, (255,255,255))
    score_rect = score_text.get_rect()

    if player.is_out:
        score_rect.midbottom = (W//2, H//2)

        screen.blit(retry_text, retry_rect)
    else:
        player.update()
        player.draw(screen)

        score_rect.midtop = (W//2, 5)
    
    screen.blit(score_text, score_rect)
    pygame.display.flip()
quit()
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
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

entity = Entity(pygame.Surface((100, 100)))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
    clock.tick(FPS)
    
    screen.fill((178, 34, 34))
    
    entity.update()
    entity.draw(screen)
    
    pygame.display.flip()
quit()
import pygame
import random
pygame.init()

#custom image id for colour change event
SPRITE_COLOUR_CHANGE = pygame.USEREVENT +1
BACKGROUND_COLOUR_CHANGE = pygame.USEREVENT +2

#bg color
BLUE= pygame.Color("blue")
NAVYBLUE= pygame.Color("navyblue")
LIGHTBLUE= pygame.Color("lightblue")

#sprite colour
RED= pygame.Color("red")
MAROON= pygame.Color("maroon")
PINK= pygame.Color("pink")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super(). __init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(-1, 1),random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)

        boundry_hit= False

        if self.rect.left <= 0 or self.rect.right >= 640:
            self.velocity[0] = -self.velocity[0]
            boundry_hit= True

        if self.rect.top <= 0 or self.rect.bottom >= 480:
            self.velocity[1] =-self.velocity[1]
            boundry_hit= True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE))
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE))
    
    def change_colour(self):
        self.image.fill(random.choice([RED, MAROON, PINK]))
def change_bg_color():
    global bg_color
    bg_color= random.choice([BLUE, NAVYBLUE, LIGHTBLUE])
allspritelist= pygame.sprite.Group()
sp1= Sprite(RED, 50, 50)
sp1.rect.x=random.randint(0, 590)
sp1.rect.y=random.randint(0, 430)

allspritelist.add(sp1)

screen= pygame.display.set_mode((640, 480))
pygame.display.set_caption("Colourful Bounce")
bg_color= BLUE
screen.fill(bg_color)
exit=False
clock= pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit= True
        elif event.type == SPRITE_COLOUR_CHANGE:
            sp1.change_colour()
        elif event.type == BACKGROUND_COLOUR_CHANGE:
            change_bg_color()
    allspritelist.update()
    screen.fill(bg_color)
    allspritelist.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()



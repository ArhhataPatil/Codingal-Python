import random
import pygame

Screen_height = 400
Screen_width = 500
movement_speed = 5
font_size = 80

pygame.init()

# Load and scale background
background_image = pygame.transform.scale(
    pygame.image.load("game_bg.jpeg"),
    (Screen_width, Screen_height)
)

font_type = pygame.font.SysFont("Comic Sans MS", font_size)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(pygame.Color("navy"))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, Screen_width - self.rect.width), 0
        )
        self.rect.y = max(
            min(self.rect.y + y_change, Screen_height - self.rect.height), 0
        )


screen = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Level Up Game")

all_sprites = pygame.sprite.Group()

# Player
sprite1 = Sprite(pygame.Color("red"), 20, 30)
sprite1.rect.x, sprite1.rect.y = (
    random.randint(0, Screen_width - sprite1.rect.width),
    random.randint(0, Screen_height - sprite1.rect.height)
)
all_sprites.add(sprite1)

# Target
sprite2 = Sprite(pygame.Color("green"), 20, 30)
sprite2.rect.x, sprite2.rect.y = (
    random.randint(0, Screen_width - sprite2.rect.width),
    random.randint(0, Screen_height - sprite2.rect.height)
)
all_sprites.add(sprite2)

running = True
won = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movement_speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movement_speed

        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font_type.render("You win!", True, pygame.Color("black"))
        screen.blit(
            win_text,
            (
                (Screen_width - win_text.get_width()) // 2,
                (Screen_height - win_text.get_height()) // 2,
            ),
        )

    pygame.display.flip()
    clock.tick(90)

pygame.quit()

import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("✨ Fancy Particle Playground Deluxe")

clock = pygame.time.Clock()

particles = []

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 7)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.randint(50, 100)
        self.max_life = self.life

        self.size = random.randint(4, 8)
        self.hue = random.random()  # 색상 변화용

    def update(self):
        self.x += self.vx
        self.y += self.vy

        self.vy += 0.05      # 중력
        self.vx *= 0.99      # 마찰
        self.vy *= 0.99

        self.life -= 1
        self.hue += 0.01

    def get_color(self):
        # HSV → RGB 느낌 간단 구현
        r = int(127 + 127 * math.sin(self.hue))
        g = int(127 + 127 * math.sin(self.hue + 2))
        b = int(127 + 127 * math.sin(self.hue + 4))
        return (r, g, b)

    def draw(self, surf):
        if self.life <= 0:
            return

        alpha = self.life / self.max_life
        size = int(self.size * alpha)

        color = self.get_color()

        # 글로우 효과 (겹쳐서 그리기)
        for i in range(3, 0, -1):
            glow_size = size + i * 3
            glow_surf = pygame.Surface((glow_size*2, glow_size*2), pygame.SRCALPHA)
            pygame.draw.circle(
                glow_surf,
                (*color, int(40 * alpha)),
                (glow_size, glow_size),
                glow_size
            )
            surf.blit(glow_surf, (self.x - glow_size, self.y - glow_size))

        pygame.draw.circle(
            surf,
            color,
            (int(self.x), int(self.y)),
            size
        )

    def alive(self):
        return self.life > 0


def fade_background(surface):
    fade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    fade.fill((0, 0, 0, 30))  # 잔상 효과 핵심!
    surface.blit(fade, (0, 0))


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    if buttons[0]:
        for _ in range(10):
            particles.append(Particle(mouse[0], mouse[1]))

    fade_background(screen)

    for p in particles:
        p.update()
        p.draw(screen)

    particles = [p for p in particles if p.alive()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
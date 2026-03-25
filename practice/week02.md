import pygame
import random
import math

pygame.init()

# 화면 설정
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌈 Ultimate Fancy Particle Playground")

clock = pygame.time.Clock()
particles = []

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # 속도
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(3, 8)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        # 생명과 크기
        self.life = random.randint(60, 120)
        self.max_life = self.life
        self.size = random.randint(4, 9)
        self.hue = random.random()  # 색상 변화용
        self.wind_offset = random.uniform(0, math.pi*2)

    def update(self):
        # 중력
        self.vy += 0.06

        # 마찰
        self.vx *= 0.99
        self.vy *= 0.99

        # 바람 효과
        self.vx += math.sin(pygame.time.get_ticks() * 0.002 + self.wind_offset) * 0.15

        # 위치 이동
        self.x += self.vx
        self.y += self.vy

        # 생명 감소
        self.life -= 1
        self.hue += 0.02

    def get_color(self):
        # 무지개 그라데이션 느낌
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

        # 글로우 효과 (3개 레이어 겹치기)
        for i in range(3, 0, -1):
            glow_size = size + i*4
            glow_surf = pygame.Surface((glow_size*2, glow_size*2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*color, int(50*alpha)), (glow_size, glow_size), glow_size)
            surf.blit(glow_surf, (self.x - glow_size, self.y - glow_size))

        # 중심 원
        pygame.draw.circle(surf, color, (int(self.x), int(self.y)), size)

    def alive(self):
        return self.life > 0

# 배경 페이드 (잔상 + 살짝 흐림)
def fade_background(surface):
    fade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    fade.fill((0, 0, 0, 15))  # 낮은 알파 → 부드러운 잔상
    surface.blit(fade, (0, 0))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    # 마우스 클릭하면 파티클 생성
    if buttons[0]:
        for _ in range(12):  # 한 번에 많이 생성
            particles.append(Particle(mouse[0], mouse[1]))

    fade_background(screen)

    # 파티클 업데이트 & 그리기
    for p in particles:
        p.update()
        p.draw(screen)

    # 살아있는 파티클만 유지
    particles = [p for p in particles if p.alive()]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

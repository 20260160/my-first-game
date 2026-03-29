# SAT OBB Collision with Rotating Center

```python
import pygame
import sys
import math

pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SAT OBB Collision with Rotating Center")

# 색상
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)      # AABB 테두리 및 충돌 배경
GREEN = (0, 255, 0)    # OBB 테두리
BLUE = (0, 0, 255)     # Circle 중심

# 이동 가능한 정사각형
player_size = 150
player = pygame.Rect(100, 100, player_size, player_size)
speed = 5

# 중앙 고정 정사각형 (회전)
center_size = 150
center_rect = pygame.Rect(
    screen_width // 2 - center_size // 2,
    screen_height // 2 - center_size // 2,
    center_size,
    center_size
)

# 회전 각도
player_angle = 0
center_angle = 0
rotation_speed_normal = 0.5  # 기본 회전 속도
rotation_speed_fast = 3      # Z 키 눌렀을 때 속도
rotation_speed = rotation_speed_normal

# 글꼴 설정
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
running = True

# ----------------- SAT 기반 OBB 충돌 함수 -----------------
def sat_obb_collision(rect1, angle1, rect2, angle2):
    """OBB 충돌 감지 - SAT(분리축 정리) 기반"""
   
    def get_corners(rect, angle):
        cx, cy = rect.center
        w, h = rect.width / 2, rect.height / 2
        corners = [(-w, -h), (w, -h), (w, h), (-w, h)]
        rad = math.radians(angle)
        cos_a, sin_a = math.cos(rad), math.sin(rad)
        rotated = []
        for x, y in corners:
            rx = x * cos_a - y * sin_a + cx
            ry = x * sin_a + y * cos_a + cy
            rotated.append((rx, ry))
        return rotated

    def project(axis, points):
        dots = [axis[0]*p[0] + axis[1]*p[1] for p in points]
        return min(dots), max(dots)

    def overlap(proj1, proj2):
        return proj1[0] <= proj2[1] and proj2[0] <= proj1[1]

    corners1 = get_corners(rect1, angle1)
    corners2 = get_corners(rect2, angle2)

    axes = []
    for corners in [corners1, corners2]:
        for i in range(4):
            p1 = corners[i]
            p2 = corners[(i+1) % 4]
            edge = (p2[0] - p1[0], p2[1] - p1[1])
            normal = (-edge[1], edge[0])
            length = math.hypot(*normal)
            axes.append((normal[0]/length, normal[1]/length))

    for axis in axes:
        proj1 = project(axis, corners1)
        proj2 = project(axis, corners2)
        if not overlap(proj1, proj2):
            return False

    return True

# ----------------- 회전된 사각형 그리기 -----------------
def draw_rotated_rect(surface, rect, angle, color, width=0):
    cx, cy = rect.center
    w, h = rect.width / 2, rect.height / 2
    corners = [(-w, -h), (w, -h), (w, h), (-w, h)]
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    rotated = []
    for x, y in corners:
        rx = x * cos_a - y * sin_a + cx
        ry = x * sin_a + y * cos_a + cy
        rotated.append((rx, ry))
    pygame.draw.polygon(surface, color, rotated, width)

# ----------------- 메인 루프 -----------------
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Z 키 눌렀을 때 회전 속도 변경
    rotation_speed = rotation_speed_fast if keys[pygame.K_z] else rotation_speed_normal

    # 중앙 사각형 회전
    center_angle += rotation_speed
    if center_angle >= 360:
        center_angle -= 360

    # ----------------- 충돌 감지 -----------------
    player_center = player.center
    center_center = center_rect.center

    # Circle 충돌
    player_radius = player_size // 2
    center_radius = center_size // 2
    dx = player_center[0] - center_center[0]
    dy = player_center[1] - center_center[1]
    distance = math.hypot(dx, dy)
    circle_hit = distance < (player_radius + center_radius)

    # AABB 충돌
    aabb_hit = player.colliderect(center_rect)

    # OBB 충돌 (SAT)
    obb_hit = sat_obb_collision(player, player_angle, center_rect, center_angle)

    # ----------------- 화면 그리기 -----------------
    # 배경 (충돌 시 빨간색)
    bg_color = RED if circle_hit or aabb_hit or obb_hit else BLACK
    screen.fill(bg_color)

    # 회색 사각형
    pygame.draw.rect(screen, GRAY, player)
    draw_rotated_rect(screen, center_rect, center_angle, GRAY)

    # AABB 테두리
    pygame.draw.rect(screen, RED, player, 2)
    pygame.draw.rect(screen, RED, center_rect, 2)

    # OBB 테두리
    draw_rotated_rect(screen, player, player_angle, GREEN, 2)
    draw_rotated_rect(screen, center_rect, center_angle, GREEN, 2)

    # Circle Bounding Box
    pygame.draw.circle(screen, BLUE, player_center, player_radius, 2)
    pygame.draw.circle(screen, BLUE, center_center, center_radius, 2)

    # 중심점 표시
    pygame.draw.circle(screen, BLUE, player_center, 5)
    pygame.draw.circle(screen, BLUE, center_center, 5)

    # 충돌 상태 표시
    texts = []
    if circle_hit:
        texts.append("Circle HIT")
    if aabb_hit:
        texts.append("AABB HIT")
    if obb_hit:
        texts.append("OBB HIT")
    for i, text in enumerate(texts):
        img = font.render(text, True, (255, 255, 255))
        screen.blit(img, (10, 10 + i*30))

    pygame.display.flip()

pygame.quit()
sys.exit()
```

## 무슨 일이 일어나는가?

- 정사각형 오브젝트의 모서리 부분에서 **원형 Bounding Box와 사각형 면이 동시에 접촉**하게 된다.
- 원형이 먼저 닿는 상황은 발생하지 않으며, 충돌 판단은 대부분 **동시에 일어나거나 AABB 면이 먼저 감지**된다.

## 왜 그런 현상이 나타나는가?

- 원형 Bounding Box는 중심에서 반지름만큼 확장된 원 형태이지만, 오브젝트가 정사각형이므로 **사각형 면과 코너가 거의 같은 거리**이다.
- 따라서 코너 근처에서도 **원형이 먼저 닿는 것은 불가능**하며, 실제 충돌 판단에는 큰 차이가 없다.

## AABB vs OBB: 회전 시 차이

### AABB

- 오브젝트가 회전해도 사각형은 회전하지 않는다.
- 회전 후 실제 모서리와 충돌 영역이 달라진다.
- 따라서 회전할수록 **충돌 판정이 실제와 다르게 나타날 수 있다.**

### OBB

- 오브젝트와 함께 사각형도 회전한다.
- 회전 후에도 모서리까지 포함해 충돌 영역이 오브젝트와 일치한다.
- 회전해도 **충돌 판정이 실제와 정확하게 맞는다.**

#### 캐릭터 구현 관점에서 OBB

- 캐릭터 회전, 방향 전환, 자세 변화까지 **정확하게 충돌 판정 가능**하다.
- 회전하는 캐릭터, 회전 공격, 정밀한 충돌 처리 등 **세밀한 동작 구현에 적합**하다.
- 단, 계산이 AABB보다 조금 더 복잡하다.

> 결론: **캐릭터 구현에서 회전과 정밀한 움직임을 표현하고 싶다면 OBB가 더 적합하다.**

---

## 오브젝트가 완전한 원일 경우

- **AABB, OBB, Circle** 모두 **충돌 범위가 같다.**
- 이유: 원은 회전해도 모양이 변하지 않으므로, **회전 여부와 상관없이 Bounding Box가 항상 원을 완전히 포함**한다.

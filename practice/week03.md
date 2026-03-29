# Pygame Slime vs Arrows (Week03)

```python
import pygame
import sys
import random

# ----------------------
# 초기화
# ----------------------
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cute Slime vs Flying Arrows with Timer")

# 색상 정의
WHITE = (255, 255, 255)
SLIME_COLOR = (135, 206, 250)  # 하늘색 슬라임
GRAY = (128, 128, 128)         # 화살표 삼각형
BROWN = (139, 69, 19)          # 꼬리 직사각형
BLACK = (0, 0, 0)              # 글자
BLUSH_COLOR = (255, 182, 193)  # 볼터치 핑크

# 시계와 글꼴
clock = pygame.time.Clock()
font_large = pygame.font.SysFont(None, 72)
font_small = pygame.font.SysFont(None, 36)

# ----------------------
# 함수 정의
# ----------------------
def create_arrows(num):
    arrows = []
    for _ in range(num):
        rect = {
            "width": 30,
            "height": 20,
            "x": screen_width + random.randint(0, 300),
            "y": random.randint(0, screen_height - 20),
            "speed": random.randint(3, 8)
        }
        arrows.append(rect)
    return arrows

def circle_rect_collision(cx, cy, r, rx, ry, rw, rh):
    closest_x = max(rx, min(cx, rx + rw))
    closest_y = max(ry, min(cy, ry + rh))
    distance_x = cx - closest_x
    distance_y = cy - closest_y
    return distance_x**2 + distance_y**2 < r**2

def draw_slime(surface, x, y, radius):
    # 몸통
    pygame.draw.circle(surface, SLIME_COLOR, (x, y), radius)

    # 눈
    eye_radius = radius // 2.5
    eye_offset_x = radius // 2
    eye_offset_y = radius // 3
    pygame.draw.circle(surface, (255, 255, 255), (x - eye_offset_x, y - eye_offset_y), eye_radius)
    pygame.draw.circle(surface, (0, 0, 0), (x - eye_offset_x, y - eye_offset_y), eye_radius // 2)
    pygame.draw.circle(surface, (255, 255, 255), (x + eye_offset_x, y - eye_offset_y), eye_radius)
    pygame.draw.circle(surface, (0, 0, 0), (x + eye_offset_x, y - eye_offset_y), eye_radius // 2)

    # 볼터치
    blush_radius = 10
    blush_offset_x = radius // 2
    blush_offset_y = radius // 3
    pygame.draw.circle(surface, BLUSH_COLOR, (x - blush_offset_x, y + blush_offset_y), blush_radius)
    pygame.draw.circle(surface, BLUSH_COLOR, (x + blush_offset_x, y + blush_offset_y), blush_radius)

# ----------------------
# 게임 상태 초기화
# ----------------------
def reset_game():
    global circle_x, circle_y, circle_radius, circle_speed, rects, game_over, start_time
    circle_x = 400
    circle_y = 300
    circle_radius = 50
    circle_speed = 5
    rects = create_arrows(5)
    game_over = False
    start_time = pygame.time.get_ticks()  # 타이머 초기화

reset_game()

# ----------------------
# 게임 루프
# ----------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        # 슬라임 이동
        if keys[pygame.K_LEFT]:
            circle_x -= circle_speed
        if keys[pygame.K_RIGHT]:
            circle_x += circle_speed
        if keys[pygame.K_UP]:
            circle_y -= circle_speed
        if keys[pygame.K_DOWN]:
            circle_y += circle_speed

        # 화면 밖으로 나가지 않도록 제한
        circle_x = max(circle_radius, min(screen_width - circle_radius, circle_x))
        circle_y = max(circle_radius, min(screen_height - circle_radius, circle_y))

        # 화살표 이동
        for rect in rects:
            rect["x"] -= rect["speed"]
            if rect["x"] < -rect["width"] - 40:  # 꼬리 길이 포함
                rect["x"] = screen_width + random.randint(0, 300)
                rect["y"] = random.randint(0, screen_height - rect["height"])
                rect["speed"] = random.randint(3, 8)

            # 충돌 판정 (삼각형만)
            if circle_rect_collision(circle_x, circle_y, circle_radius,
                                     rect["x"], rect["y"], rect["width"], rect["height"]):
                game_over = True

    else:
        # 게임 오버 상태에서 엔터 누르면 재시작
        if keys[pygame.K_RETURN]:
            reset_game()

    # ----------------------
    # 화면 그리기
    # ----------------------
    screen.fill(WHITE)

    # 슬라임 그리기
    draw_slime(screen, circle_x, circle_y, circle_radius)

    # 화살표 + 꼬리 직사각형
    for rect in rects:
        x, y, w, h = rect["x"], rect["y"], rect["width"], rect["height"]

        # 삼각형 (충돌 판정)
        point1 = (x, y + h // 2)
        point2 = (x + w, y)
        point3 = (x + w, y + h)
        pygame.draw.polygon(screen, GRAY, [point1, point2, point3])

        # 꼬리 직사각형 (충돌 판정 제외)
        tail_width = 40
        tail_height = 10
        tail_x = x + w
        tail_y = y + h//2 - tail_height//2
        pygame.draw.rect(screen, BROWN, (tail_x, tail_y, tail_width, tail_height))

    # 타이머 표시
    elapsed_time_s = (pygame.time.get_ticks() - start_time) // 1000
    timer_text = font_small.render(f"Time: {elapsed_time_s}s", True, BLACK)
    screen.blit(timer_text, (10, 10))

    # 게임 오버 화면
    if game_over:
        text = font_large.render("GAME OVER", True, BLACK)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

        hint = font_small.render("Press ENTER to restart", True, BLACK)
        hint_rect = hint.get_rect(center=(screen_width // 2, screen_height // 2 + 60))
        screen.blit(hint, hint_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

//이번주 목표: 움직이는 물체 구현해보기

// Q. pygame에서 원의 방향 이동을 구현하는 방법을 알려줘
//ai:keys = pygame.key.get_pressed() 사용 
//적용결과: 성공

//Q. 도형이 랜덤한 좌표에서 생성되도록 하는 방법
//ai:random.randint() 사용
//시행착오: 창보다 너무 많이 떨어진 좌표에서 생성되어 오는데 시간이 오래걸림
//해결: screen_width + random.randint(0,300)으로 생성 범위를 정함

//Q.움직이는 슬라임의 눈을 생성하는 방법
//ai: 원과 동일하게 눈을 좌표화하여 방향이동을 구현
//적용결과: 성공

//Q.타이머 기능을 설정하는 방법
//ai:pygame.time.get_ticks()를 적용
//적용결과: 생존시간 기록 가능

//배운점: 이번 과정을 통해 Pygame을 활용한 기본적인 게임 개발 구조를 전반적으로 이해할 수 있었다. 화면을 생성하고 게임 루프를 구성하며, 이벤트 처리와 키 입력을 통해 객체를 움직이는 방법을 익혔다. 또한 원, 삼각형, 
//직사각형 등 다양한 도형을 활용해 게임 요소를 표현하는 방법을 배웠고, 좌표를 이용해 위치를 제어하는 원리도 이해하게 되었다. 더불어 충돌 판정을 통해 게임의 상호작용을 구현하고, 게임 오버 상태와 재시작 기능을
//추가하면서 게임의 흐름을 제어하는 방법을 경험했다. 함수로 코드를 나누어 구조를 정리하는 중요성도 알게 되었으며, 색상 변경이나 슬라임 캐릭터 꾸미기 등을 통해 시각적인 완성도를 높이는 방법도 익힐 수 있었다.

```
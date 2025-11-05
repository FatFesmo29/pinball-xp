import pygame
import sys

# Инициализация
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pinball XP (Prototype)")
clock = pygame.time.Clock()

# Цвета
BACKGROUND = (10, 10, 30)
BALL_COLOR = (255, 220, 100)

# Шарик
ball_radius = 12
ball_x, ball_y = WIDTH // 2, 100
ball_vx, ball_vy = 0, 0  # скорость по x и y

# Физика
GRAVITY = 0.5
FRICTION = 0.99  # замедление по горизонтали
BOUNCE_DAMPING = 0.8  # потеря энергии при отскоке

running = True
while running:
    dt = clock.tick(60) / 1000.0  # время между кадрами (в секундах)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Гравитация
    ball_vy += GRAVITY

    # Применяем скорость
    ball_x += ball_vx
    ball_y += ball_vy

    # Трение (постепенное торможение по горизонтали)
    ball_vx *= FRICTION

    # Отскок от стен
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_vx *= -BOUNCE_DAMPING
        ball_x = max(ball_radius, min(WIDTH - ball_radius, ball_x))  # коррекция позиции

    # Отскок от пола
    if ball_y + ball_radius >= HEIGHT:
        ball_vy *= -BOUNCE_DAMPING
        ball_y = HEIGHT - ball_radius

    # Отскок от потолка (опционально)
    if ball_y - ball_radius <= 0:
        ball_vy *= -BOUNCE_DAMPING
        ball_y = ball_radius

    # Очистка экрана
    screen.fill(BACKGROUND)

    # Рисуем шарик
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), ball_radius)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()
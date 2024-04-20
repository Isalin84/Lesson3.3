import random
import pygame

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("image/picture.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("image/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
score = 0
hit_sound = pygame.mixer.Sound("sound/hit.mp3")

# Настройка таймера
game_time = 15000  # 15 секунд в миллисекундах
start_time = pygame.time.get_ticks()

running = True
game_over = False  # Новое состояние для проверки, закончилась ли игра
while running:
    current_time = pygame.time.get_ticks()
    time_left = max(0, game_time - (current_time - start_time))
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over:  # Обрабатывать ввод только если игра не закончилась
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                    hit_sound.play()
                    score += 10
                    target_x = random.randint(0, SCREEN_WIDTH - target_width)
                    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                else:
                    score -= 20

    if time_left == 0 and not game_over:
        game_over = True  # Остановить игру и перейти в режим показа результатов

    screen.blit(target_img, (target_x, target_y))
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    time_text = font.render(f"Time Left: {time_left // 1000 if not game_over else 0}", True, (255, 255, 255))
    screen.blit(time_text, (650, 10))

    pygame.display.update()

pygame.quit()

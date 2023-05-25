import pygame
import random

# 初始化 Pygame
pygame.init()

# 贪吃蛇方块的大小
block_size = 20

# 创建 Pygame 窗口
screen = pygame.display.set_mode((640, 480))

# 设置窗口标题
pygame.display.set_caption('贪吃蛇游戏')

# 定义蛇的颜色和初始位置
snake_color = (0, 255, 0)
snake_head = [block_size * 5, block_size * 5]
snake_body = [[snake_head[0], snake_head[1]], [snake_head[0]-block_size, snake_head[1]], [snake_head[0]-2*block_size, snake_head[1]]]

# 定义食物的颜色和初始位置
food_color = (255, 0, 0)
food_pos = [random.randint(0, screen.get_width() // block_size - 1) * block_size,
            random.randint(0, screen.get_height() // block_size - 1) * block_size]

# 定义蛇移动的方向和速度
direction = 'right'
speed = block_size

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'

    # 根据方向更新蛇的位置
    if direction == 'left':
        snake_head[0] -= speed
    elif direction == 'right':
        snake_head[0] += speed
    elif direction == 'up':
        snake_head[1] -= speed
    elif direction == 'down':
        snake_head[1] += speed

    # 判断是否吃到食物
    if snake_head == food_pos:
        food_pos = [random.randint(0, screen.get_width() // block_size - 1) * block_size,
                    random.randint(0, screen.get_height() // block_size - 1) * block_size]
    else:
        snake_body.pop()

    # 在蛇头处添加一个方块
    snake_body.insert(0, [snake_head[0], snake_head[1]])

    # 绘制游戏界面
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, food_color, [food_pos[0], food_pos[1], block_size, block_size])
    for body_part in snake_body:
        pygame.draw.rect(screen, snake_color, [body_part[0], body_part[1], block_size, block_size])

    # 刷新界面
    pygame.display.update()

    # 判断游戏是否结束
    if snake_head[0] < 0 or snake_head[0] >= screen.get_width() or snake_head[1] < 0 or snake_head[1] >= screen.get_height():
        pygame.quit()
        quit()
    for body_part in snake_body[1:]:
        if snake_head == body_part:
            pygame.quit()
            quit()

    # 控制游戏速度
    pygame.time.Clock().tick(10)

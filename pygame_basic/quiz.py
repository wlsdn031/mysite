import random
import pygame

pygame.init()

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Maple")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace/pygame_basic/background.png")

character = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height
index = 0
to_x = 0

character_speed = 0.6

enemy = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2) - (enemy_width/2)
enemy_y_pos = -(enemy_height)


game_font = pygame.font.Font(None, 40)

total_time = 100

start_ticks = pygame.time.get_ticks()


running = True

while running:
    dt = clock.tick(30)

    enemy_y_pos += 30
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -=  character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            
    character_x_pos += to_x*dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    gamescore = index + elapsed_time

    if character_rect.colliderect(enemy_rect):
        print("""충돌했어요
        점수 : {}""".format(round(gamescore)))
        running = False

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))


    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10, 10))
    score = game_font.render(str(int(round(gamescore))), True, (255,255,255))
    screen.blit(score, (100, 10))


    if enemy_y_pos == screen_height + enemy_height :
        enemy_y_pos = -enemy_height
        index += 10
        if character_x_pos <= 150:
            enemy_x_pos = random.randrange(0, int(character_x_pos) + 150)
        elif 150 < character_x_pos <= screen_width - 150 - character_width :
            enemy_x_pos = random.randrange(int(character_x_pos) - 150, int(character_x_pos) + 150)
        else :
            enemy_x_pos = random.randrange(int(character_x_pos) - 150, screen_width - character_width)

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        print("점수 : {}".format(gamescore))
        running = False

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()
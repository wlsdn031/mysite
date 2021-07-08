from random import randrange
import pygame

pygame.init()

screen_width = 1280
screen_height = 413

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Maple")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace/pygame_basic/bg.jpg")

character = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0] - 20
character_height = character_size[1] - 20
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height-70
index = 0
to_x = 0

character_speed = 0.5

en1m = en2m = en3m = en4m = en5m = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace/pygame_basic/enemyG.gif")
en1m_size = en2m_size = en3m_size = en4m_size = en5m_size = en1m.get_rect().size
en1m_width = en2m_width=en3m_width=en4m_width=en5m_width=en1m_size[0]
en1m_height =en2m_height=en3m_height=en4m_height=en5m_height = en1m_size[1]
en1m_x_pos =en2m_x_pos=en3m_x_pos=en4m_x_pos=en5m_x_pos= (screen_width/2) - ((en1m_width)/2)
en1m_y_pos =en2m_y_pos=en3m_y_pos=en4m_y_pos=en5m_y_pos= -(en1m_height)

en6m = en7m = en8m = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace/pygame_basic/enemyB.gif")
en6m_size =en7m_size =en8m_size = en6m.get_rect().size
en6m_width =en7m_width =en8m_width = en6m_size[0]
en6m_height =en7m_height =en8m_height = en6m_size[1]
en6m_x_pos =en7m_x_pos =en8m_x_pos = (screen_width/2) - (en6m_width/2)
en6m_y_pos =en7m_y_pos =en8m_y_pos = -(en6m_height)

en9m = en10m = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace/pygame_basic/enemyP.gif")
en9m_size = en10m_size = en9m.get_rect().size
en9m_width =en10m_width = en9m_size[0]
en9m_height =en10m_height = en9m_size[1]
en9m_x_pos =en10m_x_pos = (screen_width/2) - (en9m_width/2)
en9m_y_pos =en10m_y_pos = -(en9m_height)





game_font = pygame.font.Font(None, 40)

total_time = 100

start_ticks = pygame.time.get_ticks()

print(en1m_size)
running = True

while running:
    dt = clock.tick(300)

    en1m_y_pos += 0.3
    en2m_y_pos += 0.5
    en3m_y_pos += 0.6
    en4m_y_pos += 0.8
    en5m_y_pos += 1
    en6m_y_pos += 0.4
    en7m_y_pos += 0.8
    en8m_y_pos += 0.6
    en9m_y_pos += 0.3
    en10m_y_pos += 1

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
    
    en1m_rect = en1m.get_rect()
    en1m_rect.left = en1m_x_pos
    en1m_rect.top = en1m_y_pos
    en2m_rect = en2m.get_rect()
    en2m_rect.left = en2m_x_pos
    en2m_rect.top = en2m_y_pos
    en3m_rect = en3m.get_rect()
    en3m_rect.left = en3m_x_pos
    en3m_rect.top = en3m_y_pos
    en4m_rect = en4m.get_rect()
    en4m_rect.left = en4m_x_pos
    en4m_rect.top = en4m_y_pos
    en5m_rect = en5m.get_rect()
    en5m_rect.left = en5m_x_pos
    en5m_rect.top = en5m_y_pos
    en6m_rect = en6m.get_rect()
    en6m_rect.left = en6m_x_pos
    en6m_rect.top = en6m_y_pos
    en7m_rect = en7m.get_rect()
    en7m_rect.left = en7m_x_pos
    en7m_rect.top = en7m_y_pos
    en8m_rect = en8m.get_rect()
    en8m_rect.left = en8m_x_pos
    en8m_rect.top = en8m_y_pos
    en9m_rect = en9m.get_rect()
    en9m_rect.left = en9m_x_pos
    en9m_rect.top = en9m_y_pos
    en10m_rect = en10m.get_rect()
    en10m_rect.left = en10m_x_pos
    en10m_rect.top = en10m_y_pos
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    gamescore = index + elapsed_time

    if character_rect.colliderect(en1m_rect) or character_rect.colliderect(en2m_rect) \
        or character_rect.colliderect(en3m_rect) or character_rect.colliderect(en4m_rect)\
        or character_rect.colliderect(en5m_rect) or character_rect.colliderect(en6m_rect)\
        or character_rect.colliderect(en7m_rect) or character_rect.colliderect(en8m_rect)\
        or character_rect.colliderect(en9m_rect) or character_rect.colliderect(en10m_rect):
        print("""충돌했어요
        점수 : {}""".format(round(gamescore)))
        running = False

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(en1m, (en1m_x_pos, en1m_y_pos))
    screen.blit(en2m, (en2m_x_pos, en2m_y_pos))
    screen.blit(en3m, (en3m_x_pos, en3m_y_pos))
    screen.blit(en4m, (en4m_x_pos, en4m_y_pos))
    screen.blit(en5m, (en5m_x_pos, en5m_y_pos))
    screen.blit(en6m, (en6m_x_pos, en6m_y_pos))
    screen.blit(en7m, (en7m_x_pos, en7m_y_pos))
    screen.blit(en8m, (en8m_x_pos, en8m_y_pos))
    screen.blit(en9m, (en9m_x_pos, en9m_y_pos))
    screen.blit(en10m, (en10m_x_pos, en10m_y_pos))


    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10, 10))
    score = game_font.render(str(int(round(gamescore))), True, (255,255,255))
    screen.blit(score, (100, 10))


    if en1m_y_pos >= 600 :
        en1m_y_pos = -en1m_height
        index += 10
        en1m_x_pos = randrange(0, 1200)

    if en2m_y_pos >= 600 :
        en2m_y_pos = -en2m_height
        index += 10
        en2m_x_pos = randrange(0, 1200)
    if en3m_y_pos >= 600 :
        en3m_y_pos = -en1m_height
        index += 10
        en3m_x_pos = randrange(0, 1200)
    if en4m_y_pos >= 600 :
        en4m_y_pos = -en1m_height
        index += 10
        en4m_x_pos = randrange(0, 1200)
    if en5m_y_pos >= 600 :
        en5m_y_pos = -en1m_height
        index += 10
        en5m_x_pos = randrange(0, 1200)
    if en6m_y_pos >= 600 :
        en6m_y_pos = -en6m_height
        index += 20
        en6m_x_pos = randrange(0, 1200)
    if en7m_y_pos >= 600 :
        en7m_y_pos = -en6m_height
        index += 20
        en7m_x_pos = randrange(0, 1200)
    if en8m_y_pos >= 600 :
        en8m_y_pos = -en6m_height
        index += 20
        en8m_x_pos = randrange(0, 1200)
    if en9m_y_pos >= 600 :
        en9m_y_pos = -en9m_height
        index += 50
        en9m_x_pos = randrange(0, 1200)
    if en10m_y_pos >= 600 :
        en10m_y_pos = -en10m_height
        index += 50
        en10m_x_pos = randrange(0, 1200)
        

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        print("점수 : {}".format(gamescore))
        running = False

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()
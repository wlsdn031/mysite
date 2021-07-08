import pygame
# 필수설정
pygame.init()

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("게임이름")

clock = pygame.time.Clock()
#필수 여기까지
#1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트, 이동속도 등)
Character


running = True
while running:
    dt = clock.tick(30)

#2. 이벤트 처리(키보드, 마우스)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False

    #3. 캐릭터 위치 정의

    #4. 충돌 처리

    #5. 화면에 그리기

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()
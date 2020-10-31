import pygame


pygame.init(); 
#초기화 반드시필요.

#화면 크기 설정

screen_width = 480 #가로크기
screen_heigth = 640 #세로크기
screen = pygame.display.set_mode((screen_width,screen_heigth))



#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임이름

#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background =pygame.image.load("C:\\Users\\hyunjin\\Desktop\\업무자동화프로그램\\game_basic\\background.png")

#스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\hyunjin\\Desktop\\업무자동화프로그램\\game_basic\\character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = (screen_width /2)- (character_width/2) #화면 가로의 절반크기에해당하는 곳에 위치
character_y_pos = screen_heigth-character_height #화면 세로크기 가장 아래에

# 이동할 좌표
to_x = 0
to_y = 0

#이동속도
character_speed = 0.6

#적 enemy 캐릭터
enemy = pygame.image.load("C:\\Users\\hyunjin\\Desktop\\업무자동화프로그램\\game_basic\\enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #가로
enemy_height = enemy_size[1] #세로
enemy_x_pos = (screen_width /2)- (enemy_width/2) #화면 가로의 절반크기에해당하는 곳에 위치
enemy_y_pos = (screen_heigth/2)-(enemy_height/2) #화면 세로크기 가장 아래에

# 폰트 정의
game_font =pygame.font.Font(None, 40) #폰트객체생성(폰트,크기)

#총시간
total_time = 10

#시간 시간
start_ticks = pygame.time.get_ticks() #시작tick 을 받아옴

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(120) #게임 화면의 초당 프레임수를 설정
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이아님
        
        if event.type == pygame.KEYDOWN:  #키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y= 0


    character_x_pos += to_x*dt   
    character_y_pos += to_y*dt 
    
    #가로경계값처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width -character_width:
        character_x_pos = screen_width-character_width
    #세로경계값처리
    if character_y_pos < 0:
        character_y_pos=0 
    elif character_y_pos > screen_heigth - character_height:
        character_y_pos = screen_heigth-character_height

    #충돌처리를 위한 rect정보 update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False
        
    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    

    #타이머 집어넣기
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks()- start_ticks) /1000
    #경과시간을 1000으로나눠서 초단위로 표시
    timer = game_font.render(str(int(total_time-elapsed_time)), True, (255,255,255))
    #출력할 글자, True, 글자 색상
    screen.blit(timer, (10,10))
    #만약 시간이 0이하면 게임 종료
    if total_time-elapsed_time <= 0:
        print("타임아웃")
        running = False
    pygame.display.update() #게임화면을 다시 그리기

#잠시 대기
pygame.time.delay(2000) #2초정도 대기

# pygame 종료
pygame.quit()

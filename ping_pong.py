import pygame,sys,random

pygame.init()
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Pong Ball Game')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10,screen_height/2-70,10,150)
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 10 * random.choice((1,-1))
ball_speed_y = 10 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

def ball_restart():
    global ball_speed_x,ball,ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

def ball_animation():
    global ball_speed_x,ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >=screen_height:
        ball_speed_y *= -1
    if ball.left <=0 or ball.right >=screen_width:
        ball_restart()
    
    if ball.colliderect(player) and ball_speed_x > 0:
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
    if ball.colliderect(opponent) and ball_speed_x < 0:
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
    
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if abs(opponent.centery - ball.y) > 10:  # Only move if the ball is > 10px away
        if opponent.centery < ball.y:
            opponent.y += opponent_speed
        else:
            opponent.y -= opponent_speed
    
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
        

    ball_animation()
    player_animation()
    opponent_animation()
    
    
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))

    pygame.display.flip()
    clock.tick(60)

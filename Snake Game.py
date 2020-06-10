import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600)) #window size 800*600
pygame.display.set_caption("sneak") #set window name

fclock = pygame.time.Clock()


food = (4, 5)   #initial food position
body = [(1, 1)] #initial body position
head = (1, 2)   #initial head position

times = 0
speed = 30
direction = "right"
old_direction = "right"
alive = True
pause = False
game_begin = False
restart = False

#define the color 
BLACK = 0, 0, 0
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
GREY = 220, 220, 220

background = pygame.image.load('timg.jpg').convert()
start_pic = pygame.image.load('snake.jpg').convert()

gameover_font = pygame.font.SysFont("arial", 60)
text_surface = gameover_font.render("GAME OVER", True, (100, 20, 140))
result_font = pygame.font.SysFont("arial", 40)
score_font = pygame.font.SysFont("arial", 20)
begin_font = pygame.font.SysFont("arial", 40)
begin = begin_font.render("Press Any Key To Start", True, (0, 0, 0), (255, 255, 255))
reset_font = pygame.font.SysFont("arial", 25)
reset = reset_font.render("Press r to Restart", True, (255, 255, 255))

#drew the body rect
def new_draw_rect(zb, color,screen):
    pygame.draw.rect(screen,color,((zb[1]-1)*25+1,(zb[0]-1)*25+1,23,23))

#determine which way head should move
def get_front(head, direction):
    x, y = head
    if direction == "up":
        return x-1, y
    elif direction == "left":
        return x, y-1
    elif direction == "down":
        return x+1, y
    elif direction == "right":
        return x, y+1

#determine if head is out of screen
def ask_alive(front, body):
    x, y = front
    if x < 0 or x > 24 or y < 0 or y >32 :
        return False
    if front in body:
        return False
    return True


def new_food(head, body):
    i = 0
    while i < 100:
        x = random.randint(1, 24)
        y = random.randint(1, 32)
        if (x, y) != head and (x, y) not in body:
            return (x, y), True
        i += 1
    else:
        return (0, 0), False

# direction can not be opposite
def direction_yes_no(direction, old_direction):
    d = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if d[direction] == old_direction:
        return old_direction
    return direction

    
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #determine the direction
        elif event.type == pygame.KEYDOWN:
            game_begin = True
            if event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_DOWN:
                direction = "down"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_p:
                pause = not pause
            elif event.key == pygame.K_q:
                pygame.quit()
            elif event.key == pygame.K_r:
                restart = True
        
        
    if times >= speed and alive and (not pause) and game_begin == True:#pause is false so not pause is true, when press p for pause, it become true, not pause become false, so it can not move
        direction = direction_yes_no(direction, old_direction)
        old_direction = direction
        front = get_front(head, direction)
        alive = ask_alive(front, body)
        if alive:
            body.append(head)
            head = front
            if food == head:
                food, alive = new_food(head, body)
                if speed > 10:  #speed up when get food 
                    speed = speed*4/5
                elif speed >5:
                    speed = speed * 9 / 10
            else:
                body.pop(0)
        else:
            pygame.display.set_caption("GAME OVER")

        times = 0
    else:
        times += 1
        
    if game_begin == False:#start screen
        screen.blit(start_pic,(0,0))
        screen.blit(begin,(240,330))
    else:
        screen.blit(background,(0,0)) #fill the background picture
        score = score_font.render("Score: "+str(len(body)-1), True, (255, 255, 255))
        screen.blit(score,(720,10)) #print score when play
        new_draw_rect(food, RED, screen) #draw food 
        for i in body:
            new_draw_rect(i, WHITE, screen) #draw body
        new_draw_rect(head, GREEN, screen) #draw head
        

    if not alive:#when game over, print black background,gameover and score
        screen.fill(BLACK)
        screen.blit(text_surface,(235, 230))
        result = result_font.render("Your Score is "+str(len(body)-1), True, (100, 20, 140))
        screen.blit(result,(280, 300))
        screen.blit(reset, (300, 370))
        
    if restart == True:
        food = (4, 5)   #initial food position
        body = [(1, 1)] #initial body position
        head = (1, 2)
        game_begin = False
        alive = True
        times = 0
        speed = 30
        direction = "right"
        old_direction = "right"
        restart = False
            

    fclock.tick(100)


    pygame.display.update()



import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
dark_red = (200,0,0)
blue = (0,0,255)
orange = (255,100,0)
yellow = (200,200,0)
dgrey = (110,110,110)
dark_gray = (75,75,75)
green = (0,200,0)

car_width = 80  

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Car Racing Game")

clock = pygame.time.Clock()

carImg = pygame.image.load('carv2.png')
introCar = pygame.image.load('introcar_lg.png')
gameIcon = pygame.image.load('gameicon.png')

pygame.display.set_icon(gameIcon)

pause = True


def print_str (string,xpos,ypos):
    font=pygame.font.Font ("BloodyImpact.ttf",25)
    text=font.render(string, True,blue)
    gameDisplay.blit(text, (xpos,ypos))                     
    
def things_dodged (count):
    font = pygame.font.Font ("BloodyImpact.ttf", 25)
    text = font.render("Score: " + str(count), True, yellow)
    gameDisplay.blit(text, (20,0))

def things (thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def enemy2 (thing2x, thing2y,thing2w, thing2h, color):
    pygame.draw.rect(gameDisplay, color, [thing2x, thing2y, thing2w, thing2h])

def car (x,y):
    gameDisplay.blit(carImg,(x,y))

def intcar (ix,iy):
    gameDisplay.blit(introCar,(ix,iy))
    
def text_objects (text, font):
    textSurface = font.render(text, True, red) 
    return textSurface, textSurface.get_rect()

def message_display (text):
    largeText = pygame.font.Font('BloodyImpact.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update() 

    time.sleep(4)

    

def quit_game ():
    pygame.quit ()
    quit ()
    
def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    message_display('You Crashed')
    time.sleep(1)
    gameDisplay.fill (black)
    message_display('Game Over')
    time.sleep (1)
    game_intro()
    
def button(msg,x,y,w,h,ic,ac,action): 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h),1)
        if click [0] == 1 and action != None:
            action()    
    else:

        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("BloodyImpact.ttf",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def unpause():
    global pause
    pygame.mixer.music.load('running.wav')
    pygame.mixer.music.play(-1)
    pause = False


def paused():
   
    
    pygame.mixer.music.stop()
    
    
    largeText2 = pygame.font.Font("BloodyImpact.ttf",115)
    TextSurf, TextRect = text_objects("Paused", largeText2)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_r: 
                    unpause()
                 if event.key == pygame.K_q:
                     game_intro()
                         

        

        button("Resume",150,450,100,50,dark_gray,green,unpause)
        button("Quit",550,450,100,50,dark_gray,red,game_intro)

        pygame.display.update()
        clock.tick(15)  

def game_intro():

    
    pygame.mixer.music.load('wardrums.mp3')
    pygame.mixer.music.play(-1)

    intro = True
    
    while intro:
            
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit_game ()
                if event.key == pygame.K_s:
                    game_loop()
                
        gameDisplay.fill (black) 
        largeText = pygame.font.Font('BloodyImpact.ttf',90)
        TextSurf, TextRect = text_objects("Car Racing Game", largeText)
        TextRect.center = ((display_width/2), (45)) 
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("2.0", largeText)
        TextRect.center = ((display_width/2), (150)) 
        gameDisplay.blit(TextSurf, TextRect)
        
        print_str ("Pygame by Angelo boys",260,550)
        
        intcar (280,260)

        button("Start",100,400,150,75,dark_gray,green,game_loop)
        button("Quit",550,400,150,75,dark_gray,red,quit_game)

        pygame.display.update()
        clock.tick(30)
        
def game_loop():
    
    pygame.mixer.music.load('running.wav')
    pygame.mixer.music.play(-1)
    
    x = 400
    y = (display_height * 0.8)

    x_change = 0

    
    thing_startx = random.randrange(15, 710)
    thing_starty = -200
    thing_speed = 11
    thing_width = 80
    thing_height = 80
    

    enemy_startx = random.randrange(15, 710)
    enemy_starty = -100
    enemy_speed = 9
    enemy_width= 80
    enemy_height=80
    
    thingCount = 1
    dodged = 0
   
    car2=0
        
    gameExit = False

    while not gameExit:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_q:
                    game_intro ()
                if event.key == pygame.K_p:
                    global pause 
                    pause= True  
                    paused()     
                    
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(dgrey)

        
        pygame.draw.rect(gameDisplay, white, [0, 0, 15, 600])
        pygame.draw.rect(gameDisplay, white, [785, 0, 15, 600])
        pygame.draw.rect(gameDisplay, yellow, [390, 0, 10, 600])
        pygame.draw.rect(gameDisplay, yellow, [405, 0, 10, 600])

        
        pygame.draw.rect(gameDisplay, black, [19, 3, 115, 27])
        
        
        things(thing_startx, thing_starty, thing_width, thing_height, red)
        thing_starty += thing_speed

        
        enemy2 (enemy_startx, enemy_starty, enemy_width, enemy_height, blue)
        enemy_starty += enemy_speed
        
        
        car(x,y)

        
        things_dodged(dodged)
        
        
        
        if x > display_width - car_width or x < 0:
            crash()
            
            
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(16,710) 
            dodged += 1





        if enemy_starty > display_height:
           enemy_starty = 0 -enemy_height
           enemy_startx = random.randrange(16,710)
           dodged += 1
           
        

        if y < enemy_starty+enemy_height:
            if x > enemy_startx and x < enemy_startx +enemy_width or x + car_width > enemy_startx and x+ car_width < enemy_startx + enemy_width:
                crash()    

        if y < thing_starty+thing_height:
            
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()

        
        pygame.display.update()
        clock.tick(60)
        
game_intro()
game_loop()
pygame.quit()
quit()

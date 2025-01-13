import pygame
import random
#initialization
pygame.init()

screen_width = 1200
screen_height = 700
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
pygame.display.update() 
clock = pygame.time.Clock()
game= False

#colors
white= (255,255,255)
black= (0,0,0)

#fonts
font = pygame.font.SysFont('Impact', 55)
bigFont = pygame.font.SysFont('Impact', 100)
midFont= pygame.font.SysFont('Roboto', 32)



def text_screen(font,text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def welcome():
    game = False
    while not game:
        gameWindow.fill(black)
        text_screen(bigFont,"PONG!!!", white, 475, 100)
        text_screen(midFont, "Space to play", white, 555, 320)
        text_screen(midFont, "Escape to exit", white, 550, 360)
        text_screen(midFont, "Enter to start", white, 555, 400)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
                    
        pygame.display.update()
        clock.tick(60)
        
def gameloop():
    game= False
    fps= 60
    Y_Player1= screen_height/2-60
    Y_Player2 = screen_height/2-60
    PaddleSpeed_P1=0
    PaddleSpeed_P2= 0
    Ball_Y= screen_height/2-10
    Ball_X= screen_width/2-10
    Ball_Speed_Y=0
    Ball_Speed_X=0
    Score_P1= 0
    Score_P2= 0
    mode = 5
        
    while not game:  
        #Drawing the shapes and text
        player1= pygame.Rect(10, Y_Player1, 10, 100)
        player2= pygame.Rect(screen_width-25 ,Y_Player2 , 10, 100)  
        ball= pygame.Rect(Ball_X, Ball_Y,20,20 )
        
        gameWindow.fill(black)
        pygame.draw.rect(gameWindow,white,player1)
        pygame.draw.rect(gameWindow,white,player2)
        pygame.draw.ellipse(gameWindow,white,ball)
        pygame.draw.aaline(gameWindow, white, (screen_width / 2, 0),(screen_width / 2, screen_height))
        
        text_screen(font,f"{Score_P1}", white, 250, 20)
        text_screen(font, f"{Score_P2}", white, 900, 20)

        #Event Handling
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game = True
                        pygame.quit()
                        quit()
                
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_1:
                        mode = 7
                    if event.key == pygame.K_2:
                        mode = 12     
                    if event.key == pygame.K_w:
                        PaddleSpeed_P1 = -mode
                    if event.key == pygame.K_s:
                        PaddleSpeed_P1 =mode
                    if event.key == pygame.K_UP:
                        PaddleSpeed_P2 = -mode
                    if event.key == pygame.K_DOWN:
                        PaddleSpeed_P2 =mode
                    if event.key == pygame.K_RETURN:
                        Ball_Speed_X+=mode
                        Ball_Speed_Y+=mode
                        num= random.randint(1,2)
                        if num==1:
                            Ball_Speed_X*=-1
                            Ball_Speed_Y*=-1
                        elif num==2:
                            Ball_Speed_X*=1
                            Ball_Speed_Y*=1
                    if event.key == pygame.K_ESCAPE:
                        welcome()
                    
        
        #Ball Bouncing          
        if Ball_Y>=screen_height:
            Ball_Speed_Y*=-1
        elif Ball_Y<=0: 
            Ball_Speed_Y*=-1
            
        #Collisions    
        if player2.colliderect(ball) or player1.colliderect(ball):
            Ball_Speed_X*=-1
            Ball_Speed_Y = mode
            
        #Scoring and Resetting the screen 
        if Ball_X>=screen_width:
            Score_P1+=1
            Y_Player1= screen_height/2-60
            Y_Player2 = screen_height/2-60
            PaddleSpeed_P1=0
            PaddleSpeed_P2= 0
            Ball_Y= screen_height/2-10
            Ball_X= screen_width/2-10
            Ball_Speed_Y=0
            Ball_Speed_X=0
            
        elif Ball_X<=0:
            Score_P2+=1
            Y_Player1= screen_height/2-60
            Y_Player2 = screen_height/2-60
            PaddleSpeed_P1=0
            PaddleSpeed_P2= 0
            Ball_Y= screen_height/2-10
            Ball_X= screen_width/2-10
            Ball_Speed_Y=0
            Ball_Speed_X=0
            
        #Movement
        Ball_Y+= Ball_Speed_Y
        Ball_X+= Ball_Speed_X             
        Y_Player1 += PaddleSpeed_P1 
        Y_Player2 += PaddleSpeed_P2  
        
        #Paddle Movement Restriction
        if Y_Player1>=screen_height-100:
            Y_Player1= screen_height-100
        elif Y_Player1<=0:
            Y_Player1= 0
            
        if Y_Player2>= screen_height-100:
            Y_Player2= screen_height-100
        elif Y_Player2<= 0:
            Y_Player2= 0 
            
        pygame.display.update()                       
        clock.tick(fps)   
                
    pygame.quit()
    quit()
    
welcome()
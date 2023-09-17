import pygame
import sys
import random

fps=sys.maxsize
marker=1
flag=True
xstate=[0,0,0,0,0,0,0,0,0]
ystate=[0,0,0,0,0,0,0,0,0]
turn=1
x="X"
xscore=0
yscore=0
prev=-1

def checkdraw(xstate, ystate):
    total = sum(xstate) + sum(ystate)
    
    if total == 9 and checkwin(xstate, ystate) == -1:
        return True
    return False

def checkwin(xstate, ystate):
    xwins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwins:
        if sum(xstate[i] for i in win) == 3:
            return 1
        if sum(ystate[i] for i in win) == 3:
            return 0
        
    return -1

def getnextmove(xstate, ystate):
    bestscore = -1e9
    bestmove = -1
    for i in range(9):
        if xstate[i] == 0 and ystate[i] == 0:
            ystate[i] = 1
            score = minimax(xstate, ystate, 0, True)
            ystate[i] = 0
            if score > bestscore:
                bestscore = score
                bestmove = i
    return bestmove

def minimax(xstate, ystate, depth, ismax):
    result = checkwin(xstate, ystate)
    tie = checkdraw(xstate, ystate)
    if tie:
        return 0
    if result == 1:
        return -1
    if result == 0:
        return 1
    if ismax:
        bestscore = -1e9
        for i in range(9):
            if xstate[i] == 0 and ystate[i] == 0:
                xstate[i] = 1
                score = minimax(xstate, ystate, depth + 1, False)
                xstate[i] = 0
                bestscore = max(score, bestscore)
        return bestscore
    else:
        bestscore = 1e9
        for i in range(9):
            if xstate[i] == 0 and ystate[i] == 0:
                ystate[i] = 1
                score = minimax(xstate, ystate, depth + 1, True)
                ystate[i] = 0
                bestscore = min(score, bestscore)
        return bestscore



pygame.init()
screen=pygame.display.set_mode((375,375))
screen_width=screen.get_width()
screen_height=screen.get_width()
pygame.display.set_caption("TIC TAC TOE")
clock=pygame.time.Clock()
text_font=pygame.font.Font("arial-geo-bolditalic-webfont.ttf",35)
text_font1=pygame.font.Font("arial-geo-bolditalic-webfont.ttf",25)
game_active=True
continuation=True

while (continuation):
    value=-1
    if game_active:
        screen.fill((135,206,250))
    if xstate[0]:
        zero="X"
    elif ystate[0]:
        zero="O"
    else:
        zero="?"
    
    if xstate[1]:
        one="X"
    elif ystate[1]:
        one="O"
    else:
        one="?"
        
    if xstate[2]:
        two="X"
    elif ystate[2]:
        two="O"
    else:
        two="?"
    
    if xstate[3]:
        three="X"
    elif ystate[3]:
        three="O"
    else:
        three="?"
        
    if xstate[4]:
        four="X"
    elif ystate[4]:
        four="O"
    else:
        four="?"
        
    if xstate[5]:
        five="X"
    elif ystate[5]:
        five="O"
    else:
        five="?"
        
    if xstate[6]:
        six="X"
    elif ystate[6]:
        six="O"
    else:
        six="?"
        
    if xstate[7]:
        seven="X"
    elif ystate[7]:
        seven="O"
    else:
        seven="?"
        
    if xstate[8]:
        eight="X"
    elif ystate[8]:
        eight="O"
    else:
        eight="?"
        

    xscore_surface=text_font.render("X="+str(xscore),True,(64,64,64))
    xscore_rect=xscore_surface.get_rect(topright=(screen_width,0))
    h=xscore_surface.get_height()
    yscore_surface=text_font.render("O="+str(yscore),True,(64,64,64))
    yscore_rect=yscore_surface.get_rect(topright=(screen_width,0+h))
    
    
    text_surface0=text_font.render(f" {zero} |",True,(64,64,64))
    text_rect0=text_surface0.get_rect(topleft=(0,0))
    height=text_surface0.get_height()
    width=text_surface0.get_width()
    text_surface1=text_font.render(f" {one} |",True,(64,64,64))
    text_rect1=text_surface1.get_rect(topleft=(0+width,0))
    text_surface2=text_font.render(f" {two}",True,(64,64,64))
    text_rect2=text_surface2.get_rect(topleft=(0+2*width,0))
    
    text_surfacemid1=text_font.render(f"---|---|---",True,(64,64,64))
    text_rectmid1=text_surfacemid1.get_rect(topleft=(0,0+height))
    
    text_surface3=text_font.render(f" {three} |",True,(64,64,64))
    text_rect3=text_surface3.get_rect(topleft=(0,0+2*height))
    text_surface4=text_font.render(f" {four} |",True,(64,64,64))
    text_rect4=text_surface4.get_rect(topleft=(0+width,0+2*height))
    text_surface5=text_font.render(f" {five}",True,(64,64,64))
    text_rect5=text_surface5.get_rect(topleft=(0+2*width,0+2*height))
    
    text_surfacemid2=text_font.render(f"---|---|---",True,(64,64,64))
    text_rectmid2=text_surfacemid1.get_rect(topleft=(0,0+3*height))
    
    text_surface6=text_font.render(f" {six} |",True,(64,64,64))
    text_rect6=text_surface6.get_rect(topleft=(0,0+4*height))
    text_surface7=text_font.render(f" {seven} |",True,(64,64,64))
    text_rect7=text_surface7.get_rect(topleft=(0+width,0+4*height))
    text_surface8=text_font.render(f" {eight}",True,(64,64,64))
    text_rect8=text_surface8.get_rect(topleft=(0+2*width,0+4*height))
    
    
    title_surface5=text_font1.render("Press Spacebar for next round",True,(64,64,64))
    title_rect5=title_surface5.get_rect(midbottom=(screen_width/2,0.98*screen_height))
    
    xyz=title_surface5.get_height()
    
    title_surface1=text_font1.render("X's chance",True,(64,64,64))
    title_rect1=title_surface1.get_rect(midbottom=(screen_width/2,0.98*screen_height))
    title_surface2=text_font1.render("O's chance",True,(64,64,64))
    title_rect2=title_surface2.get_rect(midbottom=(screen_width/2,0.98*screen_height))
    
    title_surface3=text_font1.render("GAME OVER!!! X WON",True,(64,64,64))
    title_rect3=title_surface3.get_rect(midbottom=(screen_width/2,0.98*screen_height-xyz))
    title_surface4=text_font1.render("GAME OVER!!! O WON",True,(64,64,64))
    title_rect4=title_surface4.get_rect(midbottom=(screen_width/2,0.98*screen_height-xyz))
    title_surface6=text_font1.render("GAME OVER!!! DRAW",True,(64,64,64))
    title_rect6=title_surface6.get_rect(midbottom=(screen_width/2,0.98*screen_height-xyz))
    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_active=False
            continuation=False
            pygame.quit()
            exit()
            break
            
        if event.type==pygame.KEYDOWN and flag==False:
                if(event.key==pygame.K_SPACE):
                    flag=True
                    marker=1
                    xstate=[0,0,0,0,0,0,0,0,0]
                    ystate=[0,0,0,0,0,0,0,0,0]
                    turn=1
                    
            
        if event.type==pygame.MOUSEBUTTONDOWN:
                if text_rect0.collidepoint(event.pos):
                    value=0
                if text_rect1.collidepoint(event.pos):
                    value=1
                if text_rect2.collidepoint(event.pos):
                    value=2
                if text_rect3.collidepoint(event.pos):
                    value=3
                if text_rect4.collidepoint(event.pos):
                    value=4
                if text_rect5.collidepoint(event.pos):
                    value=5
                if text_rect6.collidepoint(event.pos):
                    value=6
                if text_rect7.collidepoint(event.pos):
                    value=7
                if text_rect8.collidepoint(event.pos):
                    value=8
                    
        

            
            

                    
    if game_active:       
        screen.blit(text_surface0,text_rect0)
        screen.blit(text_surfacemid1,text_rectmid1)
        screen.blit(text_surfacemid2,text_rectmid2)
        screen.blit(text_surface1,text_rect1)
        screen.blit(text_surface6,text_rect6)
        screen.blit(text_surface8,text_rect8)
        screen.blit(text_surface7,text_rect7)
        screen.blit(text_surface2,text_rect2)
        screen.blit(text_surface3,text_rect3)
        screen.blit(text_surface4,text_rect4)
        screen.blit(text_surface5,text_rect5)
        screen.blit(xscore_surface,xscore_rect)
        screen.blit(yscore_surface,yscore_rect)
        if(turn==1 and flag):
            screen.blit(title_surface1,title_rect1)
            if(value!=-1 and xstate[value]!=1 and ystate[value]!=1):
                xstate[value]=1
                turn=1-turn
        elif(turn==0 and flag):
            screen.blit(title_surface2,title_rect2)
            #value=random.randint(0,8)
            value=getnextmove(xstate,ystate)
            if(value!=-1 and xstate[value]!=1 and ystate[value]!=1 and value>=0 and value<=8):
                ystate[value]=1
                turn=1-turn        
       
        w=checkwin(xstate,ystate)
        if(w!=-1):
            flag=False
            if(w==0):
                if(marker):
                    yscore+=1
                    marker=0
                screen.blit(title_surface4,title_rect4)
                screen.blit(title_surface5,title_rect5)
            elif(w==1):
                if(marker):
                    xscore+=1
                    marker=0
                screen.blit(title_surface3,title_rect3)
                screen.blit(title_surface5,title_rect5)
                
        
       
        if(checkdraw(xstate,ystate)):
            flag=False
            marker=0
            screen.blit(title_surface6,title_rect6)
            screen.blit(title_surface5,title_rect5)
                
    
        pygame.display.update()
    clock.tick(fps)
# import pygame
import pygame
import sys
from pygame import mixer

#initializes all imported pygame modules
pygame.init()

#defines colors
white = (255, 255, 255)
light_grey = (170,170,170)
dark_grey = (100,100,100)


#initialize size of display
DISPLAY_WIDTH = 1350
DISPLAY_HEIGHT = 750

size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
screen = pygame.display.set_mode(size)

#game display size
gameDisplay = pygame.display.set_mode(size)

#name of the game
pygame.display.set_caption("The ISS")

#start the clock
clock = pygame.time.Clock()

#Background Music Player (looped)
mixer.music.load('backgroundmusic.wav')
mixer.music.set_volume(0.5)
mixer.music.play(-1, 0.0)

#special mouse cursor
pygame.mouse.set_cursor(*pygame.cursors.arrow)

#font and font size
smallfont = pygame.font.SysFont('Corbel',35)

mainmenubackground = pygame.image.load("mainmenubackground.png")
mainmenubackground = pygame.transform.scale(mainmenubackground, size)
gameDisplay.blit(mainmenubackground, (0,0))



# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
main_menu = smallfont.render('Main Menu' , True , white)
interactive_game = smallfont.render('Interactive Game' , True , white)
lesson = smallfont.render('Lesson' , True , white)
instructions = smallfont.render('Instructions' , True , white)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            #if the mouse is clicked on the button then it goes to main menu
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade 
    if 150 <= mouse[0] <= 450 and 600 <= mouse[1] <= 675:
        pygame.draw.rect(screen,light_grey,[100,100,300,75])

    else:
        pygame.draw.rect(screen,dark_grey,[100,100,300,75])
        
    if 150 <= mouse[0] <= 450 and 600 <= mouse[1] <= 675:
        pygame.draw.rect(screen,light_grey,[800,100,75])
        
    else:
        pygame.draw.rect(screen,dark_grey,[800,100,300,75])

    if 150 <= mouse[0] <= 450 and 600 <= mouse[1] <= 675:
        pygame.draw.rect(screen,light_grey,[100,300,375])
        
    else:
        pygame.draw.rect(screen,dark_grey,[100,300,300,75])

    if 150 <= mouse[0] <= 450 and 600 <= mouse[1] <= 675:
        pygame.draw.rect(screen,light_grey,[800,300,75])
        
    else:
        pygame.draw.rect(screen,dark_grey,[800,300,300,75])
    
    # superimposing the text onto our button
    screen.blit(main_menu, (180, 125))
    screen.blit(interactive_game, (850, 125))
    screen.blit(lesson, (900, 325))
    screen.blit(instructions, (180, 325))
    # updates the frames of the game
    pygame.display.update()


#establishing a game loop
def gameLoop():
    gameExit = False
    
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(60)

gameLoop()

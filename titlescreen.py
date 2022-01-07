# import pygame
import pygame
import sys
import time
from pygame import mixer

#initializes all imported pygame modules
pygame.init()

#defines colors
white = (255, 255, 255)
light_grey = (170,170,170)
dark_grey = (100,100,100)
light_blue = (125, 239, 255)


#initialize size of display
DISPLAY_WIDTH = 1350
DISPLAY_HEIGHT = 750

size = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
#game display size
gameDisplay = pygame.display.set_mode(size)

#name of the game
pygame.display.set_caption("The ISS")

#start the clock
clock = pygame.time.Clock()

#Background Music Player (looped)
mixer.music.load('music/backgroundmusic.wav')
mixer.music.set_volume(0.5)
mixer.music.play(-1, 0.0)

#special mouse cursor
pygame.mouse.set_cursor(*pygame.cursors.arrow)

#font and font size
smallText = pygame.font.Font("OriginTech.ttf", 50)

#loading the background images
title_background = pygame.image.load("backgrounds/titlepagebackground3.png")
title_background = pygame.transform.scale(title_background, size)
main_menu_background = pygame.image.load("backgrounds/mainmenubackground.png")
main_menu_background = pygame.transform.scale(main_menu_background, size)
instructions_background = pygame.image.load("backgrounds/instructionsbackground.png")
instructions_background = pygame.transform.scale(instructions_background, size)

#loading sprites


# stores the width of the screen into a variable
width = gameDisplay.get_width()

# stores the height of the screen into a variable
height = gameDisplay.get_height()


#allows text to be displayed
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

#----------------------------------------------------------------------------------------------------------

def button(function, text, fontsize, x, y, w, h, inactive_colour, active_colour,special):
    
    #defines coordinates of mouse action
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    #checks if mouse is in coordinates of button
    if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h:
        #draws button in active colour
        pygame.draw.rect(gameDisplay, active_colour, [x, y, w, h])
        #checks if user left clicks on the button
        if click[0] == 1:
            #performs function based on the button's said function
            if function == "main_menu":
                main_menu()
            if function == "animation":
                animation()
            if function == "quiz":
                quiz()
            if function == "game":
                game()
            if function == "instructions":
                instructions()
            if function == "settings":
                settings()
            if function == "quit":
                credits()
    #checks if mouse is not in coordinates of button
    else:
        pygame.draw.rect(gameDisplay, inactive_colour, [x, y, w, h])
        
    if special == "home":
        home_button = pygame.image.load("sprites/house.png")
        home_button = pygame.transform.scale(home_button, (w,h))
        gameDisplay.blit(home_button, (x,y))
    if special == "settings":
        settings_button = pygame.image.load("sprites/settings.png")
        settings_button = pygame.transform.scale(settings_button, (w,h))
        gameDisplay.blit(settings_button, (x,y))
    
    if special == "none":
        #draws text on the button
        smallText = pygame.font.Font("OriginTech.ttf", fontsize)
        textSurf, textRect = text_objects(text, smallText)
        #Centers the text on the button
        textRect.center = ( (x + (w/2)), (y + (h/2)))
        gameDisplay.blit(textSurf, textRect)    
    
#----------------------------------------------------------------------------------------------------------
# Title screen loop
def TitleScreen():
    TitleScreen = True
    x = 0
    y = 0    
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(title_background, (0,0))
        button("main_menu", "Main Menu", 40, 150, 600, 300, 75, dark_grey, light_grey, "none")

        # Update display
        pygame.display.update()        
        clock.tick(60)
    
#----------------------------------------------------------------------------------------------------------
#defines the main menu for the game
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # draws background image
        gameDisplay.blit(main_menu_background, (0,0))
        
        #draws buttons
        button("animation", "Animation/Lesson",50,50,50,600,200, dark_grey, light_grey, "none")
        button("quiz", "Quiz",100,700,50,600,200, dark_grey, light_grey, "none")
        button("game", "Interactive Game",50,50,300,600,200, dark_grey, light_grey, "none")
        button("instructions", "Instructions",50,700,300,600,200, dark_grey, light_grey, "none")
        button("settings", " ",0,50,625,75,75, light_grey, white, "settings")
        button("quit", "Quit",25, 1150, 650, 150, 50, dark_grey, light_grey, "none")
        #updates the display
        pygame.display.flip()
        clock.tick(60)        
#----------------------------------------------------------------------------------------------------------
def instructions():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(instructions_background, (0, 0))
        button("main_menu", " ",0,1250,20,85,85, light_grey, white, "home") #home button
        
        #updates the display
        pygame.display.flip()
        clock.tick(60)       

#----------------------------------------------------------------------------------------------------------

def quiz():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
#----------------------------------------------------------------------------------------------------------
def settings():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #Background Music Player (looped)
        mixer.music.load('music/backgroundmusic.wav')
        mixer.music.set_volume(0.5)
        mixer.music.play(-1, 0.0)    
#----------------------------------------------------------------------------------------------------------               
#loads the titlescreen
TitleScreen()
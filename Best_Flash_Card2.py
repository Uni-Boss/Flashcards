# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 06:57:25 2018

@author: Mike
"""
# import the necessary modules
import os
import csv
import pygame
import time
from resize_flash_card_images import resize_aspect_fit
from text_wrap1 import my_text_wrap1
# asign the location of the program to the variable cwd
cwd = os.getcwd()



#############################################################################
# This generates the terms and definitions from the csv file
# and resizes all the images in the images directory
results = []
with open(cwd + "\\flash_cards.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)
for x in range(0,len(results),1):
    pad = 200 - len(results[x][1])
    results[x][1] = results[x][1] + " "*pad
resize_aspect_fit()
#############################################################################
##############################################################################


flag_up = False

# initiate PyGame, and allow you to then make various commands with PyGame.
pygame.init()
x = 0 
ims = 0
# this is the height and width of the program
display_width = 1200
display_height = 700
# Generate a "surface," as this is basically our canvas that we will draw things to, and the function literally returns a pygame.
# Surface object. We are saying right now that we want the resolution of our game to be display_width px wide and display_height px tall.
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Set display caption
pygame.display.set_caption('Uni-Boss Flashcards')

# Create the game clock
clock = pygame.time.Clock()

gameIcon = pygame.image.load(cwd + '\\icons\\small_uni_boss_logo.png')
pygame.display.set_icon(gameIcon)
# define the colours that will be used in the program
black = (0,0,0)
white = (255,255,255)
grey = (192,192,192)


# create variable to exit game loop
crashed = False



# get the images for the program background and logos
small_logo = pygame.image.load(cwd + '\\icons\\small_uni_boss_logo.png')
entire_logo = pygame.image.load(cwd + '\\icons\\entire_logo.png')
my_ims = cwd + '\\flash_card_images\\' + str(ims) + 'resized.jpg'


def entire_logos(x,y):
    gameDisplay.blit(entire_logo, (x,y))

def pics(x,y):
    my_ims = cwd + '\\flash_card_images\\' + str(ims) + 'resized.jpg'
    if os.path.isfile(my_ims):
        my_ims = cwd + '\\flash_card_images\\' + str(ims) + 'resized.jpg'
        gameDisplay.blit(pygame.image.load(my_ims), (x,y))
    else:
        my_ims = cwd + '\\icons\\Default_logo.png'
        gameDisplay.blit(pygame.image.load(my_ims), (x,y))

ans_x = 0.7
ans_y = [0.85, 0.80, 0.75, 0.70]

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def question_display(text,ans_x, ans_y):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width*ans_x),(display_height*ans_y))
    gameDisplay.blit(TextSurf, TextRect)

def answer_display3(text,ans_x, ans_y):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width*ans_x),(display_height*ans_y))
    gameDisplay.blit(TextSurf, TextRect)
    time.sleep(0.05)
def answer_display2(text,ans_x, ans_y):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width*ans_x),(display_height*ans_y))
    gameDisplay.blit(TextSurf, TextRect)

def answer_display1(text, ans_x, ans_y):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width*ans_x),(display_height*ans_y))
    gameDisplay.blit(TextSurf, TextRect)

def answer_display(text, ans_x, ans_y):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width*ans_x),(display_height*ans_y))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(0.1)
    game_loop()



    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    gameExit = False
    


pix_x =  (display_width * 0.20)
pic_y =  (display_height * 0.3)


small_logo_x =  (display_width * 0.50)
small_logo_y =  (display_height * 0.1)

entire_logo_x =  (display_width * 0.30)
entire_logo_y =  (0)

my_images_x =  (display_width * 0.05)
my_images_y =  (display_height * 0.34)

x_change = 0
ims = int(0)

def button1(msg,x,y,w,h,ic,ac,action=None):
    pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("freesansbold.ttf",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def button2(msg,x,y,w,h,ic,ac,action=None):
    pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("freesansbold.ttf",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
disp_defs = True  
disp_term = True 

while not crashed:
    for event in pygame.event.get():
        # if user clicks 'x' on window, close game
        if event.type == pygame.QUIT:
            crashed = True
        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -1
                time.sleep(0.3)
            elif event.key == pygame.K_RIGHT:
                x_change = 1
                time.sleep(0.3)
            elif event.key == pygame.K_UP:
                if(disp_term == True):
                    disp_term = False
                elif(disp_term == False):
                    disp_term = True
                flag_term = not disp_term
            elif event.key == pygame.K_DOWN:
                if(disp_defs == True):
                    disp_defs = False
                elif(disp_defs == False):
                    disp_defs = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ######################
    ##
    x += int(x_change)
    ims += int(x_change)
    if(x == len(results)):
        x = 0
        ims = 0
    if(x < 0):
        x = int(len(results)-1)
        ims = int(len(results)-1)
    #ims += x_change
   ##
    gameDisplay.fill(white)
    entire_logos(entire_logo_x, entire_logo_y)
    pics(my_images_x, my_images_y)
    button1(" ", display_width * 0.45, display_height * 0.35,  display_width * 0.50, display_height * 0.25, grey, grey, None)
    button2(" ", display_width * 0.45, display_height * 0.65,  display_width * 0.50, display_height * 0.25, grey, grey, None)
    #pygame.draw.rect(gameDisplay, black, [display_width * 0.45, display_height * 0.65,  display_width * 0.50, display_height * 0.25])
    wrapper = my_text_wrap1(results[x][1])
    if(disp_term == True):
        question_display(results[x][0], 0.7, 0.4)
    if(disp_defs == True):
        answer_display3(results[x][1][wrapper[2]:200], ans_x, ans_y[0])
        answer_display2(results[x][1][wrapper[1]:wrapper[2]], ans_x, ans_y[1])
        answer_display1(results[x][1][wrapper[0]:wrapper[1]], ans_x, ans_y[2])
        answer_display(results[x][1][0:wrapper[0]], ans_x, ans_y[3])
        

    # display.flip updates the entire screen display update updates specific areas of the screen
    pygame.display.update()
    # runnning at 60 frames per second
    clock.tick(40)
    
pygame.quit()
quit()    
    
    

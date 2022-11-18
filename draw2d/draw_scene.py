# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

import random
# import math

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    frog_color = random.choice(['green','blue','maroon','yellow','orange','purple','red','tan','coral','cyan','pink','oliveDrab','chartreuse','seaGreen','springGreen','aquamarine'])

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas)
    for i in range(20): # Set the number of mountains here
        draw_mountain(canvas)
    for i in range(10): # Set the number of clouds here
        draw_cloud(canvas)
    draw_ground(canvas)
    draw_pond(canvas)
    draw_lilypad(canvas)
    # for i in range(10000):
    #     draw_grass(canvas, y_low=0)
    #     draw_grass(canvas, y_low=150)
    draw_frog(canvas, frog_color)
    for i in range(4): # Set the number of insects here
        draw_insect(canvas)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_frog(canvas, color='green'):
    '''Draws a frog in a set location. Color is customizable'''
    draw_polygon(canvas, 400,140, 345,100, 310,110, 300,135, 350,150, width=5, fill=color+'3', outline=color) # Left foot
    draw_polygon(canvas, 400,140, 455,100, 490,110, 500,135, 450,150, width=5, fill=color+'3', outline=color) # Right foot
    draw_oval(canvas, 275,125, 525,340, width=5, fill=color+'3', outline=color) # Body
    draw_oval(canvas, 265,115, 310,255, width=5, fill=color+'2', outline=color) # Left arm
    draw_oval(canvas, 490,115, 535,255, width=5, fill=color+'2', outline=color) # Right arm
    draw_oval(canvas, 350,335, 385,400, width=5, fill=color+'2', outline=color) # Left eye
    draw_oval(canvas, 360,335, 375,390, width=5, fill='black', outline='white') # Left pupil
    draw_oval(canvas, 415,335, 450,400, width=5, fill=color+'2', outline=color) # Right eye
    draw_oval(canvas, 425,335, 440,390, width=5, fill='black', outline='white') # Right pupil
    draw_oval(canvas, 300,260, 500,365, width=5, fill=color+'3', outline=color) # Face
    draw_arc(canvas, 325,300, 475,325, width=5, outline='black', start=220, extent=100) # Mouth

def draw_sky(canvas, color='lightSkyBlue1'):
    '''Sets the background color of the scene. This covers the entire screen. Color is customizable'''
    draw_rectangle(canvas, 0,0, 800,500, fill=color)

def draw_mountain(canvas):
    '''Draws a mountain in a random location limited to where the ground and sky meet. If the mountain exceeds a certain altitude, it will have a snowcap'''
    x = random.randint(0,650)
    y = random.randint(250,290)
    draw_polygon(canvas, x,y, x+75,y+75, x+150,y, width=5, fill='gray60', outline='gray75')
    if y > 270:
        draw_polygon(canvas, x+60,y+60, x+75,y+75, x+90,y+60, width=5, fill='snow1', outline='snow1')

def draw_cloud(canvas):
    '''Draws a cloud in a random location limited to a certain range of the sky'''
    x = random.randint(50,500)
    y = random.randint(350,450)
    width = random.randint(100,300)
    height = random.randint(25,50)
    draw_oval(canvas, x,y, x+width,y+height, width=5, fill='white', outline='snow2')

def draw_ground(canvas, color='oliveDrab', y_high=300):
    '''Draws the ground. Covers the whole screen up to a certain y value (default is 300). Color is customizable'''
    draw_rectangle(canvas, 0,0, 800,y_high, width=5, fill=color+'3', outline=color+'4')

def draw_pond(canvas, color='steelBlue'):
    '''Draws a pond in a set location on the screen. Color is customizable'''
    draw_oval(canvas, 25,15, 775,270, width=5, fill=color+'2', outline=color+'3')

# def draw_grass(canvas, color='oliveDrab', y_low=0, y_high=300):
#     x = random.randint(0,796)
#     y = random.randint(y_low,y_high)
#     if ((x-400)**2)/(375**2) + ((y-140)**2)/(132**2) > 1:
#         height = random.randint(4,int((320-y)/5))
#         draw_polygon(canvas, x,y, x+2,y+height, x+4,y, width=0, fill=color+'3', outline=color+'4')

def draw_lilypad(canvas, color='springGreen'):
    '''Draws a lilypad in a set location on the screen. Color is customizable'''
    # draw_arc(canvas, 125,65, 675,215, width=5, fill=color, outline=color+'4', start=250, extent=340)
    draw_oval(canvas, 125,65, 675,215, width=5, fill=color+'4', outline=color+'3')

def draw_insect(canvas):
    '''Draws a fly buzzing around in a random location limited so as not to cover the frog'''
    x = random.choice([random.randint(15,250),random.randint(565, 775)])
    y = random.randint(100,400)
    draw_oval(canvas, x,y, x+10,y+10, width=5, fill='black', outline='black')
    draw_oval(canvas, x+12,y, x+22,y+10, width=5, fill='white', outline='white')
    draw_oval(canvas, x-12,y, x-2,y+10, width=5, fill='white', outline='white')

# Call the main function so that
# this program will start executing.
main()
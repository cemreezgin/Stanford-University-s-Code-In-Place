import random
from graphics import Canvas
    


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    
CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

FLAGS = [
    'Belgium',
    'Italy',
    'Ireland',
    'France',
    'Romania',
    'Austria',
    'Bulgaria',
    'Netherlands',
    'Luxembourg',
    'Estonia',
    'Hungary',
    'Russia'
]

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    quiz_flag(canvas)
    canvas.mainloop()



def quiz_flag(canvas):
    correct_answers = 0
    repeat = True

    while repeat:
        random_flag = random.choice(FLAGS)
        
        if random_flag == 'Belgium':
            draw_belgium_flag(canvas)
        elif random_flag == 'Italy':
            draw_italy_flag(canvas)
        elif random_flag == 'Ireland':
            draw_ireland_flag(canvas)
        elif random_flag == 'France':
            draw_france_flag(canvas)
        elif random_flag == 'Romania':
            draw_romania_flag(canvas)
        elif random_flag == 'Austria':
            draw_austria_flag(canvas)
        elif random_flag == 'Bulgaria':
            draw_bulgaria_flag(canvas)
        elif random_flag == 'Netherlands':
            draw_netherlands_flag(canvas)
        elif random_flag == 'Luxembourg':
            draw_luxembourg_flag(canvas)
        elif random_flag == 'Estonia':
            draw_estonia_flag(canvas)
        elif random_flag == 'Hungary':
            draw_hungary_flag(canvas)
        elif random_flag == 'Russia':
            draw_russia_flag(canvas)
        
        
        correct_answers += prompt_user(random_flag)
        
        
        play_again = input("Do you want to play again after this round? (yes/no): ")
        if play_again.lower() == "no":
            break
        print("Game Over")

    
    correct_answers += prompt_user(random_flag)
    

    print("Number of correct answers:", correct_answers)


def prompt_user(flag_name):
    guess = input("Guess the name of the flag displayed: ")
    if guess.lower() == flag_name.lower():
        print("Correct!")
        return 1
    else:
        print("Incorrect. The correct answer is:", flag_name)
        return 0


def draw_japan_flag(canvas):
    draw_circle(canvas, CANVAS_WIDTH/2, CANVAS_HEIGHT/2, 120, 'red')


    
def draw_belgium_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH * 1/3
    bottom_y = CANVAS_HEIGHT
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'black')
    canvas.create_rectangle(left_x + inset_x, top_y, right_x + inset_x, bottom_y + inset_y, 'yellow')
    canvas.create_rectangle(left_x + (inset_x*2), top_y, right_x + (inset_x*2), bottom_y + (inset_y*2), 'red')
    
def draw_italy_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH * 1/3
    bottom_y = CANVAS_HEIGHT
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'green')
    canvas.create_rectangle(left_x + inset_x, top_y, right_x + inset_x, bottom_y + inset_y, 'white')
    canvas.create_rectangle(left_x + (inset_x*2), top_y, right_x + (inset_x*2), bottom_y + (inset_y*2), 'red')
    
def draw_ireland_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH * 1/3
    bottom_y = CANVAS_HEIGHT
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'green')
    canvas.create_rectangle(left_x + inset_x, top_y, right_x + inset_x, bottom_y + inset_y, 'white')
    canvas.create_rectangle(left_x + (inset_x*2), top_y, right_x + (inset_x*2), bottom_y + (inset_y*2), 'orange')
    
def draw_france_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH * 1/3
    bottom_y = CANVAS_HEIGHT
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
    canvas.create_rectangle(left_x + inset_x, top_y, right_x + inset_x, bottom_y + inset_y, 'white')
    canvas.create_rectangle(left_x + (inset_x*2), top_y, right_x + (inset_x*2), bottom_y + (inset_y*2), 'red')
    
def draw_romania_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH * 1/3
    bottom_y = CANVAS_HEIGHT
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'darkblue')
    canvas.create_rectangle(left_x + inset_x, top_y, right_x + inset_x, bottom_y + inset_y, 'yellow')
    canvas.create_rectangle(left_x + (inset_x*2), top_y, right_x + (inset_x*2), bottom_y + (inset_y*2), 'darkred')

def draw_austria_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT * 1/3
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'red')
    canvas.create_rectangle(left_x , top_y + inset_y, right_x + inset_x, bottom_y + inset_y, 'white')
    canvas.create_rectangle(left_x , top_y + (inset_y*2), right_x + (inset_x*2), bottom_y + (inset_y*2), 'red')


def draw_bulgaria_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT * 1/3
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'white')
    canvas.create_rectangle(left_x , top_y + inset_y, right_x + inset_x, bottom_y + inset_y, 'green')
    canvas.create_rectangle(left_x , top_y + (inset_y*2), right_x + (inset_x*2), bottom_y + (inset_y*2), 'red') 
    
    
def draw_netherlands_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT * 1/3
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'darkred')
    canvas.create_rectangle(left_x , top_y + inset_y, right_x + inset_x, bottom_y + inset_y, 'white')
    canvas.create_rectangle(left_x , top_y + (inset_y*2), right_x + (inset_x*2), bottom_y + (inset_y*2), 'darkblue')


    
def draw_luxembourg_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT * 1/3
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'red')
    canvas.create_rectangle(left_x , top_y + inset_y, right_x + inset_x, bottom_y + inset_y, 'white')
    canvas.create_rectangle(left_x , top_y + (inset_y*2), right_x + (inset_x*2), bottom_y + (inset_y*2), 'dodgerblue')
    

def draw_estonia_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT * 1/3
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'dodgerblue')
    canvas.create_rectangle(left_x , top_y + inset_y, right_x + inset_x, bottom_y + inset_y, 'black')
    canvas.create_rectangle(left_x , top_y + (inset_y*2), right_x + (inset_x*2), bottom_y + (inset_y*2), 'white')
    
    
def draw_hungary_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT * 1/3
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'darkred')
    canvas.create_rectangle(left_x , top_y + inset_y, right_x + inset_x, bottom_y + inset_y, 'white')
    canvas.create_rectangle(left_x , top_y + (inset_y*2), right_x + (inset_x*2), bottom_y + (inset_y*2), 'darkgreen')


def draw_russia_flag(canvas):
    left_x = 0
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT * 1/3
    inset_x = CANVAS_WIDTH / 3
    inset_y = CANVAS_HEIGHT / 3
    canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'white')
    canvas.create_rectangle(left_x , top_y + inset_y, right_x + inset_x, bottom_y + inset_y, 'blue')
    canvas.create_rectangle(left_x , top_y + (inset_y*2), right_x + (inset_x*2), bottom_y + (inset_y*2), 'red')




def draw_georgia_flag(canvas):
    x_left = CANVAS_WIDTH * 1/4
    x_right = CANVAS_WIDTH * 3/4
    y_top = CANVAS_HEIGHT * 1/4
    y_bottom = CANVAS_HEIGHT * 3/4
    
    
    draw_plus(canvas, x_left - 20, y_top - 20, x_left+20, y_top+20, 10)
    draw_plus(canvas, x_right - 20, y_top - 20, x_right+20, y_top+20, 10)
    draw_plus(canvas, x_left - 20, y_bottom - 20, x_left+20, y_bottom+20, 10)
    draw_plus(canvas, x_right - 20, y_bottom - 20, x_right+20, y_bottom+20, 10)
    
    
    draw_plus(canvas, 0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 30)

def draw_plus(canvas, x_1, y_1, x_2, y_2, width):
    
    mid_x = x_1 + (x_2 - x_1) / 2
    mid_y = y_1 + (y_2 - y_1) / 2
    
    half = width/2
    
    canvas.create_rectangle(x_1, mid_y - half, x_2, mid_y + half, 'red')
    canvas.create_rectangle(mid_x - half, y_1, mid_x + half, y_2, 'red')
    

def draw_circle(canvas, center_x, center_y, size, color):
    left_x = center_x - size/2
    top_y = center_y - size/2
    right_x = left_x + size
    bottom_y = top_y + size
    canvas.create_oval(left_x, top_y, right_x, bottom_y, color)

    
    
    
    
    
    
    
    

if __name__ == '__main__':
    main()

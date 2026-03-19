import pgzrun

TITLE = "Quiz guesser"
WIDTH = 600
HEIGHT = 700
#each rectangular box  is careted with 0,0 x and y and then width and hight of the box
title_box = Rect(0,0,600,80)
question_box = Rect(0,0,500,120)
timer_box = Rect(0,0,90,120)
answer1_box = Rect(0,0,250,120)
answer2_box = Rect(0,0,250,120)
answer3_box = Rect(0,0,250,120)
answer4_box = Rect(0,0,250,120)
skip = Rect(0,0,600,120)


titlemes= ""
timeleft = 10
score=0
question_file_name="c:/Users/Achil/Desktop/python games/Lesson2/quiz/questions.txt"
is_game_over=False
question_count=0
question_index=0
questions = []
#store all the answer boxes in a list
answerboxes = [answer1_box,answer2_box,answer3_box,answer4_box]

title_box.move_ip(0,0)
question_box.move_ip(0,100)
timer_box.move_ip(505,100)
answer1_box.move_ip(25,250)
answer2_box.move_ip(300,250)
answer3_box.move_ip(25,400)
answer4_box.move_ip(300,400)
skip.move_ip(0,550)

def draw():
    global titlemes

    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(title_box, "white")
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.filled_rect(timer_box, "pink")
    for box in answerboxes:
        screen.draw.filled_rect(box, "red")
    screen.draw.filled_rect(skip,"green")
    screen.draw.textbox("Skip",skip,color = "black")
    screen.draw.textbox(str(timeleft), timer_box, color = "white", shadow =(0.5,0.5), scolor = "dim grey")
    titlemes = "Welcome To Quiz Master "
    titlemes =  titlemes + f"Q: {question_index} / {question_count} "
    screen.draw.textbox( titlemes, title_box, color = "black", )
    screen.draw.textbox(question[0].strip(),question_box, color= "black", shadow = (0.5,0.5), scolor = "dim grey")
def update_time ():
    global timeleft

    if timeleft:
        timeleft = timeleft - 1
    else:
        timeleft = 0

def update():
    move_title()



def move_title():
    title_box.x -= 5
    if title_box.right < 0:
        title_box.left = WIDTH

def question_read():
    global question_count, questions,question_file_name
    q_file = open(question_file_name,"r")
    for q in q_file:
        questions.append(q)
        question_count +=1
        q_file.close()

def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0),split(",")



def correct_answer():
    global questions
    if questions:
        questions = read_next_question 


pgzrun.go()
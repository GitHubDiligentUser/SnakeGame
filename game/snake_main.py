from tkinter import *
import random
import pygame.mixer
import moving_snake
import update_file
import crash_or_not
import new_way

pygame.init()
pygame.mixer.music.load("resources/sounds/background_music2.wav")
pygame.mixer.music.play(-1)

pygame.mixer.init()
crunch_sound = pygame.mixer.Sound("resources/sounds/Sound_crunch.wav")
mistake_sound = pygame.mixer.Sound("resources/sounds/buzzer.wav")
jackpot_sound = pygame.mixer.Sound("resources/sounds/correct.wav")
eagle_effect = pygame.mixer.Sound("resources/sounds/Eagle_sound.mp3")

# constants for the game - they couldn't be changed
GAME_WIDTH: int = 900
GAME_HEIGHT: int = 600
DELAY: float = 25
PIXEL: int = 30
BODY_PARTS: int = 3
SNAKE_COLOUR: str = "#00ff00"
APPLE_COLOUR: str = "#FF0000"
COIN_COLOUR: str = "#FFEB3B"  # #ffff33
BACKGROUND_COLOUR: str = "#5D4037"  # #212121

# parameters - they could be changed during the game
way: str = 'down'
speed_of_snake: float = 100
score: int = 0
saved_high_score: int = 0
record: int = 0
level: int = 1
collected_coins: int = 0

# creating the playing court
window = Tk()
window.title("The best snake game version ever")
window.iconbitmap("resources/images/apple.ico")
window.resizable(False, False)

# open the file with the highest score saved - it's done only once - in the beginning if the program
file = open('high_scores.txt', 'r')
for line in file:
    # we're going to check if the substring 'high score' is in this line
    if 'high score: ' in line:
        # we use integer converter - we need to get the string value from the file as an integer
        # and save this integer value in variable "record":
        record = int(line.replace('high score: ', ''))
        # we don't know how many characters that could be => replace '' after the substring 'high score: '
        saved_high_score = 0


class Snake:
    # constructor of the class Snake
    def __init__(self) -> None:
        self.body_size = BODY_PARTS
        self.coordinates = []  # list
        self.segments = []  # list

        for i in range(0, BODY_PARTS):
            # the coordinates of each body segment in the beginning (at the start of the game) will be 0,0
            self.coordinates.append([0, 0])

        for x_snake, y_snake in self.coordinates:
            body_segment = canvas.create_rectangle(x_snake, y_snake, x_snake + PIXEL, y_snake + PIXEL,
                                                   fill=SNAKE_COLOUR, tags="snake")
            # add each body segment, that was created, into the list of segments.
            # Show all body parts on the playing court:
            self.segments.append(body_segment)


class Food:
    def __init__(self) -> None:
        # define coordinates of the fruit - they should be random and unpredictable from the player
        x_apple = round(random.randint(0, (int(GAME_WIDTH / PIXEL))-1) * PIXEL)
        y_apple = round(random.randint(0, (int(GAME_HEIGHT / PIXEL))-1) * PIXEL)

        # check if food appears over the snake body
        if x_apple == 0 and y_apple == 0:
            x_apple += PIXEL
            y_apple += PIXEL

        self.coordinates = [x_apple, y_apple]
        canvas.create_oval(x_apple, y_apple, x_apple + PIXEL, y_apple + PIXEL, fill=APPLE_COLOUR, tags='food')


class Coin:
    def __init__(self) -> None:
        # define coordinates of the fruit - they should be random and unpredictable from the player
        x_coin = round(random.randint(0, (int(GAME_WIDTH / PIXEL)) - 1) * PIXEL)
        y_coin = round(random.randint(0, (int(GAME_HEIGHT / PIXEL)) - 1) * PIXEL)

        # check if food appears over the snake body
        if x_coin == 0 and y_coin == 0:
            x_coin += PIXEL
            y_coin += PIXEL

        self.coordinates = [x_coin, y_coin]
        canvas.create_oval(x_coin, y_coin, x_coin + PIXEL, y_coin + PIXEL, fill=COIN_COLOUR, tags='coin')


def next_turn(reptile, apple, speed, levels, money) -> None:
    # the most up-left-sided point has coordinates 0,0
    x, y = reptile.coordinates[0]  # head

    if way == "up" or way == "down":
        y = moving_snake.move_body_parts(way, y, PIXEL)
    elif way == "left" or way == "right":
        x = moving_snake.move_body_parts(way, x, PIXEL)

    reptile.coordinates.insert(0, (x, y))
    body_segment = canvas.create_rectangle(x, y, x + PIXEL, y + PIXEL, fill=SNAKE_COLOUR)
    # we need to update our list of segments (every body segment moves to the place of the last but one)
    reptile.segments.insert(0, body_segment)

    global score, record, collected_coins

    if x == money.coordinates[0] and y == money.coordinates[1]:
        collected_coins += 1
        jackpot_sound.play()
        score += 3
        if score > record:
            record = score
        speed += 15
        # coin = Coin()
        label.config(text="Level: {}        Coins: {}       Score: {}       Highest score: {}".
                     format(levels, collected_coins, score, record))
        canvas.delete("coin")

    if x == apple.coordinates[0] and y == apple.coordinates[1]:
        crunch_sound.play()
        score += 1

        if score > record:
            record = score

        if score % 5 == 0:
            levels += 1
            canvas.delete("coin")
            money = Coin()
            speed -= DELAY
        label.config(text="Level: {}        Coins: {}       Score: {}       Highest score: {}".
                     format(levels, collected_coins, score, record))
        canvas.delete("food")
        apple = Food()

    else:
        # delete the last body_segment of the snake
        del reptile.coordinates[-1]
        canvas.delete(reptile.segments[-1])
        del reptile.segments[-1]

    if crash_or_not.check_hit(GAME_WIDTH, GAME_HEIGHT, reptile):
        game_over()
    else:
        window.after(speed, next_turn, reptile, apple, speed, levels, money)


def move(new_direction) -> None:
    global way
    way = new_way.move(new_direction, way)


def exit_game() -> None:
    window.destroy()


def game_over() -> None:
    global score, record, saved_high_score

    canvas.delete(ALL)
    pygame.mixer.music.stop()
    mistake_sound.play()

    if record > saved_high_score:
        saved_high_score = update_file.update_file(record, saved_high_score)

    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('Poor Richard', 30),
                       text="Game over\n\nReached points: {}\nHighest score: {}\n".
                       format(score, record),
                       fill="white", tags="endgame")

    exit_btn = Button(text="Exit", font=("", 15), relief=SOLID, command=exit_game)
    exit_btn.place(x=GAME_WIDTH - GAME_WIDTH/4, y=GAME_HEIGHT-100)


label = Label(window,
              text="Level: {}       Coins: {}       Score: {}       Highest score: {}".
              format(level, collected_coins, score, record),
              font=('Poor Richard', 24))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
# get the measurements of the playing court
court_width = window.winfo_width()
court_height = window.winfo_height()

# get measurements of the computer screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# position (coordinates) of the playing court on the computer screen
x = int((screen_width/2) - (court_width/2))
y = int((screen_height/2) - (court_height/2))

# we center the playing court on our screen
window.geometry(f"{court_width}x{court_height}+{x}+{y}")

window.bind('<Left>', lambda event: move('left'))
window.bind('<Right>', lambda event: move('right'))
window.bind('<Up>', lambda event: move('up'))
window.bind('<Down>', lambda event: move('down'))

# we create an object from the classes Snake, Food and Coin so that the project can start to run
snake = Snake()
food = Food()
coin = Coin()
next_turn(snake, food, speed_of_snake, level, coin)

window.mainloop()

import random
import turtle
from random import randint
from time import time

from PIL import Image
from playsound import playsound
import os
from threading import Thread


class Config:
    initialHealth = 4
    timer = 60  # seconds
    font_size = 20
    width = 1000
    height = 600
    questionSectionHeight = 200
    questions = [
        ["What's the command that you use to print items of a list reversed", "\n[1] enumerate[a]", "\n[2] reversed.(a)", "\n[3] list[a]", 2],
        ["Python creation date?", "\n[1] 2000", "\n[2] 2012",
         "\n[3] 1991",
         "\n[4] 2020", 3],
        ["Who invented python?", "\n[1] Bill Gates", "\n[2] Steve Jobs",
         "\n[3] I do not know, I'll skip", "\n[4] Guido van Rossum", 4],
        ["An error, or mistake, that prevents the program from being run correctly:", "\n[1] Bug", "\n[2] Debug",
         "\n[3] Loop", "\n[4] Algorithm", 1],
        ["dnatsrednu uoY?", "\n[1] What!?", "\n[2] !seY", "\n[3] No clue",
         "\n[4] It means nothing", 2]
    ]


def imageSize(imagePath):
    img = Image.open(imagePath)
    width = img.size[0]
    height = img.size[1]
    return width, height


def playSound(file):
    path = os.path.join(os.getcwd(), os.path.normpath(file))
    try:
        T = Thread(target=lambda: playsound(path))
        T.start()
    except Exception as e:
        print("Error playing audio: ", e)


def drawHeart(size, x, y):
    def func():
        for i in range(200):
            t.right(1)
            t.forward(size)

    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.pensize(1)
    t.color('red', 'red')
    t.begin_fill()
    t.left(140)
    t.forward(111.65 * size)
    func()
    t.left(120)
    func()
    t.forward(111.65 * size)
    t.hideturtle()
    t.end_fill()
    return t


class Label(turtle.Turtle):
    def __init__(self, text="Default Text", x=0, y=0, textcolor="black", align="center",
                 font=("Courier", 15, "normal")):
        super().__init__()
        self.text = text
        self.x = x
        self.y = y
        self.textcolor = textcolor
        self.align = align
        self.font = font
        self.color(textcolor)
        self.hideturtle()
        self.penup()
        self.goto(self.x, self.y)
        self.write(text, align=self.align, font=self.font)

    def setText(self, text):
        self.clear()
        self.write(text, align=self.align, font=self.font)


class Game:
    def __init__(self, ):
        # Screen setup
        screen = turtle.Screen()
        screen.tracer(0, 0)  # update delay 0 this makes everything the turtle draws appear immediately
        screen.listen()  # listen to keypress

        screen.title("My Game")
        screen.bgcolor('Black')  # set the color of the background you can use 'red', 'blue'
        # or any hex value https://htmlcolors.com/google-color-picker
        # you can try to set an image as a background if you are curious, but you will have to change the
        # width and height based on that image
        width = Config.width
        height = Config.height + Config.questionSectionHeight
        screen.setup(width, height)  # set the width and height of the window that will be created
        screen.cv._rootwindow.resizable(False, False)  # make the window non-resizable

        # every image that we want to use as a turtle image needs to be added as a shape to the screen
        # it is recommended to use 'gif' format https://ezgif.com/apng-to-gif
        # these files need to be placed in the same folder or in the specified path
        screen.addshape("Files/Images/coin.gif")
        screen.addshape("Files/Images/fox.gif")
        screen.addshape("Files/Images/foxflipped.gif")
        screen.addshape('Files/Images/download.gif')
        screen.addshape('Files/Images/download2.gif')

        killer = turtle.Turtle()
        killer.setposition(300 ,300)
        killer.shape('Files/Images/download.gif')
        killer.penup()
        killerSize = imageSize('Files/Images/download.gif')

        ht = turtle.Turtle()
        ht.setposition(-300 ,300)
        ht.shape('Files/Images/download2.gif')
        htSize = imageSize('Files/Images/download2.gif')


        # this is an example of how to create a turtle based on the image that you specify (i.e a coin)
        mycoin = turtle.Turtle()
        mycoin.shape("Files/Images/coin.gif")  # we set one of the shapes that we added above, note this image needs to be in the
        # folder you are working
        mycoin.penup()  # we set turtle.penup in order to not see the traces that turtle leaves by default
        mycoin.setposition(0, 0)  # we can move this coin around by using setposition(x, y)
        coinSize = imageSize("Files/Images/coin.gif")

        """
        Create the turtle, set the image as a shape and give it a position as the coin example above.
        """
        player = turtle.Turtle()
        player.shape("Files/Images/fox.gif")  # we set one of the shapes that we added above, note this image needs to be in the
        # folder you are working
        player.penup()  # we set turtle.penup in order to not see the traces that turtle leaves by default
        player.setposition(0, 100)  # we can move this coin around by using setposition(x, y)
        player_step = 20
        player.left(90)
        playerSize = imageSize("Files/Images/fox.gif")


        self.line = turtle.Turtle()
        self.line.pencolor('white')
        self.line.penup()
        self.line.hideturtle()
        self.line.goto(-width / 2, -height / 2 + Config.questionSectionHeight)
        self.line.pendown()
        self.line.forward(width)

        self.score = 0

        def moveRight():
            (x, y) = player.pos()
            if x < width / 2 - 50:
                player.shape("Files/Images/fox.gif")
                player.setx(x + player_step)

        def moveLeft():
            (x, y) = player.pos()
            if x > -width / 2 + 40:
                player.shape("Files/Images/foxflipped.gif")
                player.setx(x - player_step)

        def moveUp():
            if player.ycor() < height / 2 - playerSize[1] + 30:
                player.forward(player_step)

        def moveDown():
            if player.ycor() > - height / 2 + playerSize[1] - 30 + Config.questionSectionHeight:
                player.backward(player_step)

        def enableMovement():
            screen.onkeypress(moveUp, "w")
            screen.onkeypress(moveDown, "s")
            screen.onkeypress(moveLeft, "a")
            screen.onkeypress(moveRight, "d")
            screen.onkeypress(moveUp, "W")
            screen.onkeypress(moveDown, "S")
            screen.onkeypress(moveLeft, "A")
            screen.onkeypress(moveRight, "D")

        def emptyKeypressHandler(x=None, y=None):
            pass

        def disableMovement():
            screen.onkeypress(emptyKeypressHandler, "w")
            screen.onkeypress(emptyKeypressHandler, "a")
            screen.onkeypress(emptyKeypressHandler, "s")
            screen.onkeypress(emptyKeypressHandler, "d")
            screen.onkeypress(emptyKeypressHandler, "W")
            screen.onkeypress(emptyKeypressHandler, "A")
            screen.onkeypress(emptyKeypressHandler, "S")
            screen.onkeypress(emptyKeypressHandler, "D")

        def moveCoin():
            available_screen_width = width / 2 - 25
            available_screen_height = height / 2 - 25
            # mycoin.goto(randint(-available_screen_width, available_screen_width), randint(available_screen_height, available_screen_height)) # test x
            # mycoin.goto(randint(available_screen_width, available_screen_width), randint(-available_screen_height, available_screen_height)) # test y
            mycoin.goto(randint(-available_screen_width, available_screen_width),
                        randint(-available_screen_height + Config.questionSectionHeight, available_screen_height))
            if objectsOverlap(player, playerSize[0], playerSize[1], mycoin, coinSize[0],
                              coinSize[1]):  # if they overlap try another random position
                moveCoin()

        def objectsOverlap(object1, object1width, object1height, object2, object2width, object2height):
            object1X = object1.pos()[0]
            object1Y = object1.pos()[1]
            object2X = object2.pos()[0]
            object2Y = object2.pos()[1]

            object1Top = object1Y + object1height / 2
            object1Bottom = object1Y - object1height / 2
            object2Top = object2Y + object2height / 2
            object2Bottom = object2Y - object2height / 2

            # print("Horizontal debug: ", object1Top, object2Bottom, object1Bottom, object2Top)
            if object1Top >= object2Bottom and object1Bottom <= object2Top:
                # print("horizontally aligned")
                # horizontally on the same line from bottom AND top of object1
                object1Right = object1X + object1width / 2
                object1Left = object1X - object1width / 2
                object2Right = object2X + object2width / 2
                object2Left = object2X - object2width / 2
                # print("Vertical debug: ", object1Right, object2Left, object1Left, object2Right)
                if object1Right >= object2Left and object1Left <= object2Right:
                    # print("vertically aligned")
                    # vertically on the same line from left AND right of object1
                    # print("overlap")
                    return True
            return False

        # TODO: implement these methods given this example:
        health = []

        def addHealth():
            health.append(drawHeart(0.15, width / 2 - 35 * len(health) - 25, height / 2 - 30))

        def removeHealth():
            health.pop(-1).clear()

        def outOfLives():
            print("Out of lives")
            self.label = Label("You Lost All Your Lives!", 0, 0, textcolor="red", font=("Comic Sans MS", 30, "bold"))
            disableMovement()
            disable_answers()
            # screen.ontimer(self.changeScene, 3000)

        def ranOutOfTime():
            print("Out of time")
            playSound("Files/Audio/finish.mp3")
            self.label = Label("Your Time Is Over!", 0, height / 2 - 100, textcolor="red",
                               font=("Comic Sans MS", 30, "bold"))
            disableMovement()
            disable_answers()
            # screen.ontimer(self.changeScene, 3000)

        def clearMessage():
            self.ans0.clear()
            enable_answers()

        def endQuestion():
            self.question.clear()
            self.ans.clear()
            self.ans = None
            self.ans0.clear()
            Config.questions.pop(self.index)
            enableMovement()

        def checkAns(choice):
            disable_answers()
            if choice == Config.questions[self.index][-1]:
                playSound('Files/Audio/correct.mp3')
                self.ans0 = Label("")
                self.ans = Label("Correct!", 0, - height / 2 + Config.questionSectionHeight - 35, "green")
                self.score += 10
                scoreLabel.setText("Score: {}".format(self.score))
                screen.ontimer(endQuestion, 1500)
            else:
                disable_answers()
                self.ans0 = Label("Wrong!", 0, -height / 2 + Config.questionSectionHeight - 35, "red")
                self.ans = Label(
                    "Correct answer: " + Config.questions[self.index][Config.questions[self.index][-1]].lstrip('\n'), 0,
                    -height / 2 + Config.questionSectionHeight - 60, "green")
                removeHealth()
                screen.ontimer(endQuestion, 2000)

        def enable_answers():
            screen.onkeypress(lambda: checkAns(1), "1")
            screen.onkeypress(lambda: checkAns(2), "2")
            screen.onkeypress(lambda: checkAns(3), "3")
            screen.onkeypress(lambda: checkAns(4), "4")

        def disable_answers():
            screen.onkeypress(emptyKeypressHandler, "1")
            screen.onkeypress(emptyKeypressHandler, "2")
            screen.onkeypress(emptyKeypressHandler, "3")
            screen.onkeypress(emptyKeypressHandler, "4")

        def generateQuestion():
            playSound('Files/Audio/coin.wav')
            if len(Config.questions):
                disableMovement()
                self.index = randint(0, len(Config.questions) - 1)
                q = ''.join(Config.questions[self.index][0:len(Config.questions[self.index]) - 1])
                print(q)
                self.question = Label(q, 0, -height / 2 + 30, "white")
                enable_answers()
            else:
                print("OUT of Questions!")
                self.score += 1
                scoreLabel.setText("Score: {}".format(self.score))
                if self.ans == None:
                    self.ans = Label("You finished all questions!\nCollect as many coins as you want.", 0,
                                     -height / 2 + Config.questionSectionHeight - 100,
                                     "gold")
                    playSound('Files/Audio/completed.mp3')

        moveCoin()
        screen.onkeypress(moveCoin, "q")
        for i in range(Config.initialHealth):
            addHealth()
        scoreLabel = Label("Score: {}".format(self.score), -width / 2 + 60, height / 2 - 30, textcolor='orange')
        timer = Label("Timer: {}".format(Config.timer), 0, height / 2 - 30, textcolor='red')
        enableMovement()
        screen.onkeypress(moveCoin, "t")

        def moveHt():
            available_screen_width = width / 2 - 25
            available_screen_height = height / 2 - 25
            # mycoin.goto(randint(-available_screen_width, available_screen_width), randint(available_screen_height, available_screen_height)) # test x
            # mycoin.goto(randint(available_screen_width, available_screen_width), randint(-available_screen_height, available_screen_height)) # test y
            ht.goto(randint(-available_screen_width, available_screen_width),
                        randint(-available_screen_height + Config.questionSectionHeight, available_screen_height))
            if objectsOverlap(player, playerSize[0], playerSize[1], ht, htSize[0],
                              htSize[1]):  # if they overlap try another random position
                moveHt()

        def killers():
            available_screen_width = width / 2 - 25
            available_screen_height = height / 2 - 25

            killer.goto(random.randint(-available_screen_width, available_screen_width),
                        random.randint(-available_screen_height + Config.questionSectionHeight, available_screen_height))

            if objectsOverlap(player, playerSize[0], playerSize[1], killer, killerSize[0],
                              killerSize[1]):  # if they overlap try another random position
                moveHt()


        running = True
        while True:
            screen.update()
            if running:
                current_timer_val = Config.timer - int(time() - startTime)
                if len(health) <= 0:
                    outOfLives()
                    running = False
                if current_timer_val >= 0:
                    timer.setText("Timer: {}".format(current_timer_val))
                else:
                    ranOutOfTime()
                    running = False
                if objectsOverlap(player, playerSize[0], playerSize[1], mycoin, coinSize[0], coinSize[1]):
                    print("Overlap")

                    moveCoin()
                    killers()
                    moveHt()
                    generateQuestion()
                if objectsOverlap(player, playerSize[0], playerSize[1], killer, killerSize[0], killerSize[1]):
                    removeHealth()
                    killers()
                if objectsOverlap(player, playerSize[0], playerSize[1], ht, htSize[0], htSize[1]):
                    addHealth()
                    moveHt()

def showRules():
    screen = turtle.Screen()
    screen.setup(Config.width, Config.height)
    screen.bgcolor('#121212')
    screen.tracer(0, 0)  # update delay 0
    screen.listen()
    labels = []
    screen._bgcolor('#121212')
    labels.append(
        Label("RULES", 0, Config.height / 2 - 45, textcolor='#BB86FC',
              font=("Comic Sans MS", Config.font_size, "bold")))
    labels.append(Label("1. Use W,A,S,D to move around."
                        "\n2. Collect as many coins as possible."
                        "\n3. You can answer a question only once."
                        "\n4. For each correct answer you get +10 points."
                        "\n5. You have 5 lives."
                        "\n6. For each wrong answer/If you touch the killer, you lose 1 life, but if you catch a heart you earn +1 life"
                        "\n7. If the time ends or you lose all your lives the game ends."
                        "\n8. If you answer all the questions before the timer you can move "
                        "\n   freely and gather coins with a value of +1.", 0, Config.height / 2 - 350,
                        textcolor='#CF6679', font=("Comic Sans MS", Config.font_size, "normal")))
    labels.append(
        Label("*Press any key to continue", Config.height / 2 + 100, -Config.height / 2 + 20, textcolor='#03DAC6',
              font=("Comic Sans MS", 13, "normal")))

    global change_screen
    change_screen = False

    def changeScreen(x=None, y=None):
        global change_screen
        change_screen = True
        screen.clear()

    # press any key to continue
    screen.onkeyrelease(changeScreen, '')
    # press any mouse button to continue
    screen.onclick(changeScreen)
    screen.onclick(changeScreen, 2)
    screen.onclick(changeScreen, 3)

    while 1:
        screen.update()
        if change_screen:
            break


if __name__ == "__main__":
    showRules() # uncoment this to show the rules
    startTime = time()
    game = Game()

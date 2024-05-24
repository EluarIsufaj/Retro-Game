import turtle
from random import randint

from PIL import Image


def imageSize(imagePath):
    img = Image.open(imagePath)
    width = img.size[0]
    height = img.size[1]
    return width, height


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


class Game:
    def __init__(self, ):
        # Screen setup
        screen = turtle.Screen()
        screen.tracer(0, 0)  # update delay 0 this makes everything the turtle draws appear immediately
        screen.listen()  # listen to keypress

        screen.title("My Game")
        screen.bgcolor('#121212')  # set the color of the background you can use 'red', 'blue'
        # or any hex value https://htmlcolors.com/google-color-picker
        # you can try to set an image as a background if you are curious, but you will have to change the
        # width and height based on that image
        width = 1000
        height = 600
        screen.setup(width, height)  # set the width and height of the window that will be created
        screen.cv._rootwindow.resizable(False, False)  # make the window non-resizable

        # every image that we want to use as a turtle image needs to be added as a shape to the screen
        # it is recommended to use 'gif' format https://ezgif.com/apng-to-gif
        # these files need to be placed in the same folder or in the specified path
        screen.addshape("Files/Immages/coin.gif")
        screen.addshape("Files/Immages/fox.gif")
        screen.addshape("Files/Immages/foxflipped.gif")

        # this is an example of how to create a turtle based on the image that you specify (i.e a coin)
        mycoin = turtle.Turtle()
        mycoin.shape("Files/Immages/coin.gif")  # we set one of the shapes that we added above, note this image needs to be in the
        # folder you are working
        mycoin.penup()  # we set turtle.penup in order to not see the traces that turtle leaves by default
        mycoin.setposition(0, 0)  # we can move this coin around by using setposition(x, y)
        coinSize = imageSize("Files/Immages/coin.gif")
        """
        Create the turtle, set the image as a shape and give it a position as the coin example above.
        """
        player = turtle.Turtle()
        player.shape("fox.gif")  # we set one of the shapes that we added above, note this image needs to be in the
        # folder you are working
        player.penup()  # we set turtle.penup in order to not see the traces that turtle leaves by default
        player.setposition(0, 100)  # we can move this coin around by using setposition(x, y)
        player_step = 20
        player.left(90)
        playerSize = imageSize("Files/Immages/fox.gif")

        def moveRight():
            (x, y) = player.pos()
            if x < width / 2 - 50:
                player.shape("Files/Immages/fox.gif")
                player.setx(x + player_step)

        def moveLeft():
            (x, y) = player.pos()
            if x > -width / 2 + 40:
                player.shape("Files/Immages/foxflipped.gif")
                player.setx(x - player_step)

        def moveUp():
            if player.ycor() < height / 2 - playerSize[1] + 40:
                player.forward(player_step)

        def moveDown():
            # implement this yourself
            pass

        def enableMovement():
            screen.onkeypress(moveUp, "w")
            screen.onkeypress(moveLeft, "a")
            screen.onkeypress(moveRight, "d")
            screen.onkeypress(moveUp, "W")
            screen.onkeypress(moveLeft, "A")
            screen.onkeypress(moveRight, "D")
            # add move down listener

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
                        randint(-available_screen_height, available_screen_height))
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
        # health = []
        # health.append(drawHeart(0.15, width/2-30, height/2-30))
        # health.append(drawHeart(0.15, width/2-70, height/2-30))
        # health.append(drawHeart(0.15, width/2-110, height/2-30))
        # health.pop(-1).clear()
        # https://replit.com/@IndritBreti1/WheatSteepPrediction#health_2.py
        def addHealth():
            pass

        def removeHealth():
            pass

        enableMovement()
        screen.onkeypress(moveCoin, "t")
        while True:
            screen.update()
            if objectsOverlap(player, playerSize[0], playerSize[1], mycoin, coinSize[0], coinSize[1]):
                print("Overlap")
                # TODO: handle coin collection
                pass
            # you can write code that needs to run repetitively here


if __name__ == "__main__":
    game = Game()
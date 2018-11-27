class Color:
    Red = "\x1b[31m"
    Green = "\x1b[32m"
    Blue = "\x1b[36m"
    reset = "\x1b[0m"

def printr(text):
    print(Color.Red + str(text) + Color.reset)

def printg(text):
    print(Color.Green + str(text) + Color.reset)

def printb(text):
    print(Color.Blue + str(text) + Color.reset)


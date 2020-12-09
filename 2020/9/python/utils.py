import os

def submit(part, answer):
    os.system("./submit {} {}".format(part, answer))

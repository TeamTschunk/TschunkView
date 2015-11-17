from TschunkView import *
from CodeView import *
import time

t = TschunkView(TschunkMap1())
#c = CodeView(TschunkMap1())
direction = 0

def simple_main():
    print 'thread started!'
    direction = -1
    while True:
        time.sleep(1)
        if not t.move((0,direction)):
            direction *= -1

def move():
    time.sleep(1)
    t.move()

def drop():
    time.sleep(1)
    t.drop()

def rotateLeft():
    time.sleep(1)
    global direction
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    direction = (direction + 1) % 4
    t.setDirection(directions[direction])

def main():
    print 'thread started!'
    for i in range(0,4):
        # round i:
        move()
        move()
        rotateLeft()
        move()
        move()
        drop()
        rotateLeft()
        rotateLeft()
        move()
        move()
        rotateLeft()
        move()

if __name__ == '__main__':
    print 'starting thead ...'
    thread = threading.Thread(target=main)
    thread.setDaemon(True)
    thread.start()
    pyglet.app.run()



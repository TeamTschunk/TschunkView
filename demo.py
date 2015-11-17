from TschunkView import *
import time

t = TschunkView(TschunkMap1())

def simple_main():
    print 'thread started!'
    direction = -1
    while True:
        time.sleep(1)
        if not t.move((0,direction)):
            direction *= -1

def move(x, y):
    t.move((x, y))
    time.sleep(1)

def main():
    print 'thread started!'
    for i in range(0,4):
        # round i:
        move(0, -1)
        move(0, -1)
        move(1, 0)
        move(1, 0)
        # drop
        move(-1, 0)
        move(-1, 0)
        move(0, -1)

if __name__ == '__main__':
    print 'starting thead ...'
    thread = threading.Thread(target=main)
    thread.setDaemon(True)
    thread.start()
    pyglet.app.run()



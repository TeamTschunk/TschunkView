import sys
import pyglet
from pyglet.gl import *
import primitives
import utils

FPS = 60
smoothConfig = utils.getSmoothConfig()

class PrimWin(pyglet.window.Window):

    def __init__(self, filename='demo.jpg'):
        super(PrimWin, self).__init__(fullscreen=False, caption='Tschunk!', config=smoothConfig)

        self.image = pyglet.resource.image(filename)
        self.sprite = pyglet.sprite.Sprite(self.image)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.l = primitives.Line((0,0),(100,100),stroke=10,color=(1,0,0,1))
        # Setup debug framerate display:
        self.fps_display = pyglet.clock.ClockDisplay()

        # Schedule the update of this window, so it will advance in time at the
        # defined framerate.  If we don't, the window will only update on events
        # like mouse motion.

        #pyglet.clock.schedule_interval(self.update, 1.0/FPS)

    def on_draw(self):
        self.clear()
        self.sprite.draw()
        self.l.render()
        #self.fps_display.draw()

    #def on_mouse_motion(self, x, y, dx, dy):
        # nothing to do here if not in debug
        #print x, y

if __name__ == '__main__':
    PrimWin('img/demo.jpg')
    sys.exit(pyglet.app.run())

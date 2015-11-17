import sys
import pyglet
from pyglet.gl import *
import primitives
import utils
from map1 import *
import threading

FPS = 60
smoothConfig = utils.getSmoothConfig()

class TschunkView(pyglet.window.Window):

    def __init__(self, mymap):
        super(TschunkView, self).__init__(fullscreen=False, caption='Tschunk!', config=smoothConfig)

        self.image = pyglet.resource.image(mymap.img)
        self.sprite = pyglet.sprite.Sprite(self.image)

        self.y_step = self.image.height / mymap.rows + 1
        self.x_step = self.image.width / mymap.cols + 1

        cord_origin_x = self.x_step/2
        cord_origin_y = self.y_step/2

        start_x = cord_origin_x + mymap.origin_x * self.x_step
        start_y = cord_origin_y + mymap.origin_y * self.y_step

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.l = primitives.Line((0,0),(100,100),stroke=10,color=(1,0,0,1))
        self.c = primitives.Circle(start_x, start_y,width=self.y_step,color=(0.,.9,0.,1.))

        # Setup debug framerate display:
        self.fps_display = pyglet.clock.ClockDisplay()

        # Schedule the update of this window, so it will advance in time at the
        # defined framerate.  If we don't, the window will only update on events
        # like mouse motion.

        #pyglet.clock.schedule_interval(self.update, 1.0)

        self.set_size(self.image.width, self.image.height)

    def on_draw(self):
        self.clear()
        self.sprite.draw()
        #self.l.render()
        self.c.render()
        #self.fps_display.draw()

    #def update(self, dt):
     #   if self.c.y  - self.y_step > 0:
       #     self.c.y -= self.y_step

    #def on_mouse_motion(self, x, y, dx, dy):
        # nothing to do here if not in debug
        #print x, y

    def run(self, callback=lambda s:None):
        self.thread = threading.Thread(target=callback)
        self.thread.setDaemon(True)
        self.thread.start()
        pyglet.app.run()

    def move(self, direction):
        (x, y) = direction
        if self.c.y  + y * self.y_step > 0 and self.c.y  + y * self.y_step < self.image.height:
            self.c.y += y * self.y_step
        else:
         return False
        if self.c.x  + x * self.x_step > 0 and self.c.x  + x * self.x_step < self.image.width:
            self.c.x += x * self.x_step
        else:
            return False
        return True

if __name__ == '__main__':
    TschunkView(TschunkMap1())
    sys.exit(pyglet.app.run())



'''
Test program for the open-source 3D mouse

Move a cube around on the screen.

Adrian Bowyer
RepRap Ltd

4 June 2021

https://reprapltd.com

Licence: GPL

Uses code from https://stackoverflow.com/questions/16263727/3d-cube-didnt-show-correctly-writen-by-pyglet

'''

import pyglet
from pyglet.gl import *
from pyglet import window
import serial
import re
import time


# return a ctype array - GLfloat, GLuint

arduinoPort = '/dev/ttyUSB0'

class OS3DMouse:

 def __init__(self, port):
  self.usb = serial.Serial(port,115200,timeout=0.1)
  time.sleep(3) # Why so long???
  self.v0 = self.Get3HallReadings()[0]

 def Get3HallReadings(self):
  self.usb.write(str.encode('v\n'))
  data = self.usb.readline()
  data = str(data.decode('ascii'))
  data = re.findall('\d+', data)
  data = (int(data[0]), int(data[1]), int(data[2]))
  return data

 def Movement(self):
  v = self.v0 - self.Get3HallReadings()[0]
  return int(v/4)



def vector(type, *args):
    return (type*len(args))(*args)


class model:
    def __init__(self, vertices, colorMatrix, index, mouse):
        self.vertices = vector(GLfloat, *vertices)
        self.colorMatrix = vector(GLfloat, *colorMatrix)
        self.index = vector(GLuint, *index)
        self.angle = 0
        self.mouse = mouse

    def update(self):
        self.angle += self.mouse.Movement()
        self.angle %= 360

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glRotatef(self.angle, 1, 1, 1)

        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glColorPointer(3, GL_FLOAT, 0, self.colorMatrix)
        glVertexPointer(3, GL_FLOAT, 0, self.vertices)
        glDrawElements(GL_QUADS, len(self.index), GL_UNSIGNED_INT, self.index)

        glDisableClientState(GL_COLOR_ARRAY)
        glDisableClientState(GL_VERTEX_ARRAY)



class world:
    def __init__(self):
        self.element = []

    def update(self, dt):
        for obj in self.element:
            obj.update()

    def addModel(self, model):
        self.element.append(model)

    def draw(self):
        for obj in self.element:
            obj.draw()


def setup():
    # look for GL_DEPTH_BUFFER_BIT
    glEnable(GL_DEPTH_TEST)


win = window.Window(fullscreen=False, vsync=True, resizable=True, height=600, width=600)
mWorld = world()

cube = (
    1, 1, 1, #0
    -1, 1, 1, #1
    -1, -1, 1, #2
    1, -1, 1, #3
    1, 1, -1, #4
    -1, 1, -1, #5
    -1, -1, -1, #6
    1, -1, -1 #7
)


color = (
    1, 0, 0,
    1, 0, 0,
    1, 0, 0,
    1, 0, 0,
    0, 1, 0,
    0, 1, 0,
    0, 0, 1,
    0, 0, 1
)

index = (
    0, 1, 2, 3, # front face
    0, 4, 5, 1, # top face
    4, 0, 3, 7, # right face
    1, 5, 6, 2, # left face
    3, 2, 6, 7, # bottom face
    4, 7, 6, 5  #back face
)

mouse = OS3DMouse(arduinoPort)
obj = model(cube, color, index, mouse)
mWorld.addModel(obj)

@win.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

@win.event
def on_draw():
    glClearColor(0.2, 0.2, 0.2, 0.8)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mWorld.draw()


pyglet.clock.schedule(mWorld.update)
setup()
pyglet.app.run()

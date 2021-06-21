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
import numpy as np

arduinoPort = '/dev/ttyUSB0'

# Swap directions if needs be

sense = np.array([-1, -1, -1, 1, 1, 1])
mapping = (1, 2, 0, 3, 4, 5)

class OS3DMouse:

 def __init__(self, port):
  self.usb = serial.Serial(port,115200,timeout=0.1)
  time.sleep(3) # Why so long???
  self.v0 = self.GetHallReadings()

 def GetHallReadings(self):
  self.usb.write(str.encode('6\n'))
  data = self.usb.readline()
  data = str(data.decode('ascii'))
  data = re.findall('\d+', data)
  result =  np.zeros(shape=(6))
  for i in range(6):
    result[i] = int(data[mapping[i]])
  return result

 def Movement(self):
  v = np.subtract(self.v0, self.GetHallReadings())
  v = np.multiply(v, sense)
  v = np.multiply(v, 1.0/8.0).astype(int)
  return v


# return a ctype array - GLfloat, GLuint

def vector(type, *args):
    return (type*len(args))(*args)


class model:
    def __init__(self, vertices, colorMatrix, index, mouse):
        self.vertices = vector(GLfloat, *vertices)
        self.colourMatrix = vector(GLfloat, *colorMatrix)
        self.index = vector(GLuint, *index)
        self.angle = np.array([0.0, 0.0, 0.0])
        self.position = np.array([0.0, 0.0, 0.0])
        self.mouse = mouse

    def update(self):
        move = self.mouse.Movement()
        a = np.array([move[0], move[1], move[2]])
        p = np.array([move[3], move[4], move[5]])
        self.angle = np.remainder(np.add(self.angle, a), 360)
        self.position = np.add(self.position, np.multiply(p, 1.0/8.0))


    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glRotatef(self.angle[0], 1, 0, 0)
        glRotatef(self.angle[1], 0, 1, 0)
        glRotatef(self.angle[2], 0, 0, 1)
        glTranslatef(self.position[0], self.position[1], self.position[2])

        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glColorPointer(3, GL_FLOAT, 0, self.colourMatrix)
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
    3, 3, 3, #0
    -3, 3, 3, #1
    -3, -3, 3, #2
    3, -3, 3, #3
    3, 3, -3, #4
    -3, 3, -3, #5
    -3, -3, -3, #6
    3, -3, -3 #7
)


colour = (
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
obj = model(cube, colour, index, mouse)
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

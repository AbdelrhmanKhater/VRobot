from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import *
def rectangle(x, y, x1, y1, x2, y2, x3, y3):
    glBegin(GL_POLYGON)
    glVertex2d(x, y)
    glVertex2d(x1, y1)
    glVertex2d(x2, y2)
    glVertex2d(x3, y3)
    glEnd()
def circle(r, s, e, xnaught, ynaught):
    glBegin(GL_POLYGON)
    for theta in arange(s, e, 0.01):
        x = r * cos(theta) + xnaught
        y = r * sin(theta) + ynaught
        glVertex2d(x, y)
    glEnd()
def triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_POLYGON)
    glVertex2d(x1, y1)
    glVertex2d(x2, y2)
    glVertex2d(x3, y3)
    glEnd()
def bird(x, y, x1, y1, x2, y2, x3, y3):
    glBegin(GL_LINES)
    glVertex2d(x, y)
    glVertex2d(x1, y1)
    glEnd()
    glBegin(GL_LINES)
    glVertex2d(x2, y2)
    glVertex2d(x3, y3)
    glEnd()
def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    #Background
    glColor(1, 1, 0)
    rectangle(1, -1, -1, -1, -1, 0.1, 1, 0.1)
    glColor(0, 0.77, 1)
    rectangle(1, 1, -1, 1, -1, 0.1, 1, 0.1)
    #sword
    glColor(0, 0, 0)
    rectangle(0.1151, 0.43, 0.2, 0.74, 0.2, 0.61, 0.1151, 0.3)
    rectangle(-0.1151, 0.43, -0.2, 0.74, -0.2, 0.61, -0.1151, 0.3)
    #Body
    glColor(0.5, 0.5, 0.5)
    circle(0.45, pi / 9,  8 * (pi / 9), 0, 0)
    glColor(0, 0.77, 1)
    circle(0.35, pi / 9,  8 * (pi / 9), 0, 0)
    glColor(0.5, 0.5, 0.5)
    rectangle(0.15, 0.4, 0.15, -0.2, -0.152, -0.2, -0.15, 0.4)
    rectangle(0.32, 0.15, 0.419, 0.15, 0.419, -0.05, 0.32, -0.05)
    rectangle(-0.32, 0.15, -0.419, 0.15, -0.419, -0.05, -0.32, -0.05)
    #legs
    rectangle(0.15, -0.75, 0.05, -0.75, 0.05, -0.2, 0.15, -0.2)
    rectangle(-0.15, -0.75, -0.05, -0.75, -0.05, -0.2, -0.15, -0.2)
    circle(0.2, 0, 2 *pi, 0, 0.7)
    #Accessories
    glColor(0, 0, 0)
    circle(0.06, 0, 2 *pi, 0.375, 0.15)
    circle(0.06, 0, 2 *pi, -0.375, 0.15)
    circle(0.08, 0, 2 *pi, -0.375, -0.05)
    circle(0.08, 0, 2 *pi, 0.375, -0.05)
    rectangle(0.375, -0.01, 0.375, -0.05, 0.5, -0.05, 0.5, -0.01)
    rectangle(-0.375, -0.01, -0.375, -0.05, -0.5, -0.05, -0.5, -0.01)
    rectangle(-0.33, -0.05, -0.33, -0.23, -0.359, -0.23, -0.359, -0.05)
    rectangle(0.33, -0.05, 0.33, -0.23, 0.359, -0.23, 0.359, -0.05)
    rectangle(-0.419, -0.05, -0.419, -0.23, -0.39, -0.23, -0.39, -0.05)
    rectangle(0.419, -0.05, 0.419, -0.23, 0.39, -0.23, 0.39, -0.05)
    rectangle(0.05, 0.44, 0.05, 0.51, -0.05, 0.51, -0.05, 0.44)
    #shoes
    rectangle(0.2, -0.75, 0.05, -0.75, 0.05, -0.85, 0.2, -0.85)
    rectangle(-0.2, -0.75, -0.05, -0.75, -0.05, -0.85, -0.2, -0.85)
    circle(0.1, 0, pi, 0.2, -0.85)
    circle(0.1, 0, pi, -0.2, -0.85)
    rectangle(0.09, 0.441589, 0.24, 0.401404, 0.24, 0.451404, 0.09, 0.491589)
    rectangle(-0.09, 0.441589, -0.24, 0.401404, -0.24, 0.451404, -0.09, 0.491589)
    triangle(0.15, 0, 0.15, -0.15, 0.25, -0.4)
    triangle(-0.15, 0, -0.15, -0.15, -0.25, -0.4)
    circle(0.08, 0, 2 * pi, 0.1, -0.4)
    circle(0.08, 0, 2 * pi, -0.1, -0.4)
    rectangle(0.15, 0, 0.15, -0.1, -0.15, -0.1, -0.15, 0)
    #belt
    glColor(0.37, 0.22, 0.01)
    triangle(0.05, 0, 0, -0.1, -0.05, 0)
    glColor(0, 0, 0)
    triangle(0.025, 0, 0, -0.05, -0.025, 0)
    #sologan
    glColor(0.37, 0.22, 0.01)
    triangle(0.1, 0.4, 0, 0.1, -0.1, 0.4)
    glColor(0.5, 0.5, 0.5)
    triangle(0.05, 0.4, 0, 0.2, -0.05, 0.4)
    #mouth
    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    a = 0.07
    b = 0.025
    for theta in arange(0, 2 * pi, 0.01):
        x = a * cos(theta)
        y = b * sin(theta) + 0.6
        glVertex2d(x, y)
    glEnd()
    #eyes
    glColor(0, 0, 1)
    circle(0.025, 0, 2 * pi, 0.08, 0.72)
    circle(0.025, 0, 2 * pi, -0.08, 0.72)
    #birds
    glColor(0, 0, 0)
    bird(0.6, 0.7, 0.7, 0.85, 0.6, 0.85, 0.7, 0.7)
    bird(0.5, 0.45, 0.6, 0.6, 0.6, 0.45, 0.5, 0.6)
    bird(-0.5, 0.45, -0.6, 0.6, -0.6, 0.45, -0.5, 0.6)
    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"VRobot")
glutInitWindowSize(100, 100)
glutDisplayFunc(draw)
glutMainLoop()

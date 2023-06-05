'''
Grup 1-Proje 1
Emirhan Şimşek - 20120205046
Hamza Peker - 20120205024
Muhammed Emin Ay - 20120205038
02.05.2023
'''
import pygame
from OpenGL.GLUT import glutInit
from OpenGL.raw.GLUT import glutFullScreen
from pygame.locals import *
from model import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

from model import draw_cube, load_texture

pygame.init()
display = (1300, 800)
map = [
    '                ',
    '                ',
    '#######  #######',
    '#              #',
    '# ############ #',
    '# #          # #',
    '# # ######## # #',
    '# #        # # #',
    '# ######## # # #',
    '# #        # # #',
    '# # ######## # #',
    '# #          # #',
    '# ############ #',
    '#              #',
    '# ############ #',
    '#            # #',
    '#############  #',
    '#              #'
]
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

sphere = gluNewQuadric()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(1, -3.5, 0, 0, -3.5, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

up_down_angle = 0.0
paused = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter)
        if not paused:
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)

    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        # mouseMove = pygame.mouse.get_rel()

        # init model view matrix
        glLoadIdentity()

        # apply the look up and down
        up_down_angle += mouseMove[1] * 0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()

        # apply the movment
        if keypress[pygame.K_w]:
            glTranslatef(0, 0, 0.1)
        if keypress[pygame.K_s]:
            glTranslatef(0, 0, -0.1)
        if keypress[pygame.K_d]:
            glTranslatef(-0.1, 0, 0)
        if keypress[pygame.K_a]:
            glTranslatef(0.1, 0, 0)
        if keypress[pygame.K_SPACE]:
            glTranslatef(0.0, -0.1, 0)
        if keypress[pygame.K_LSHIFT]:
            glTranslatef(0.0, 0.1, 0)

        # apply the left and right rotation
        glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        glColor4f(0.5, 0.5, 0.5, 1)
        glBegin(GL_QUADS)
        glVertex3f(-10, -10, -0.76)
        glVertex3f(10, -10, -0.76)
        glVertex3f(10, 10, -0.76)
        glVertex3f(-10, 10, -0.76)

        glEnd()
        floor = load_texture("ground.png")
        texture = load_texture("texture.png")
        for i in range(0, 18):
            for z in range(0, 16):
                if map[i][z] == '#':
                    glPushMatrix();
                    glTranslatef(i * -0.5, z * -0.5, -0.5);
                    draw_cube(texture)
                    glPopMatrix();
        for i in range(0, 18):
            for z in range(0, 16):
                if map[i][z] == '#':
                    glPushMatrix();
                    glTranslatef(i * -0.5, z * -0.5, 0);
                    draw_cube(texture)
                    glPopMatrix()
        for i in range(0, 18):
            for z in range(0, 16):
                glPushMatrix();
                glTranslatef(i * -0.5, z * -0.5, -1.001);
                draw_cube(floor)
                glPopMatrix()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()
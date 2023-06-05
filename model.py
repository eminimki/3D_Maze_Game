'''
Grup 1-Proje 1
Emirhan Şimşek - 20120205046
Hamza Peker - 20120205024
Muhammed Emin Ay - 20120205038
02.05.2023
'''
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def load_texture(texture):
    texture_surface = pygame.image.load(texture)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    glEnable(GL_TEXTURE_2D)
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    return texture

def draw_cube(texture):
    vertices = (
        (0.25, -0.25, -0.25),
        (0.25, 0.25, -0.25),
        (-0.25, 0.25, -0.25),
        (-0.25, -0.25, -0.25),
        (0.25, -0.25, 0.25),
        (0.25, 0.25, 0.25),
        (-0.25, -0.25, 0.25),
        (-0.25, 0.25, 0.25)
    )
    faces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    for face in faces:
        for vertex, texture_coords in zip(face, [(0, 0), (1, 0), (1, 1), (0, 1)]):
            glTexCoord2fv(texture_coords)
            glVertex3fv(vertices[vertex])
    glEnd()

'''def draw_floor(texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(0, -32.0, 0)
    glTexCoord2f(32, 0)
    glVertex3f(0, 32, -32)
    glTexCoord2f(32, 32)
    glVertex3f(0, 32, 32)
    glTexCoord2f(0, 32)
    glVertex3f(0, -32, 32)
    glEnd()'''

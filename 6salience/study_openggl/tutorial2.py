import pyglet
from pyglet.gl import *

window = pyglet.window.Window()
image = pyglet.resource.image('pic.jpg')
back = pyglet.resource.image('back.jpg')
mask = pyglet.resource.image('mask.jpg')
createdtex=False;
imagetex = 0


@window.event
def on_draw():
    window.clear()

    global createdtex
    texfrmbuf =(GLuint*1)()
    global imagetex
    if createdtex!=True:
        imagetex = image.get_texture()
        glEnable(GL_BLEND)
        glBlendFunc(GL_ZERO, GL_SRC_COLOR)
        glGenFramebuffersEXT(1,texfrmbuf)
        glBindFramebufferEXT(GL_DRAW_FRAMEBUFFER_EXT,texfrmbuf[0])
        glFramebufferTexture2DEXT(GL_DRAW_FRAMEBUFFER_EXT,GL_COLOR_ATTACHMENT0_EXT, imagetex.target,imagetex.id,0)
        mask.blit(0,0)
        glFlush()
        glDisable(GL_BLEND)
        glDeleteFramebuffersEXT(1,texfrmbuf)
        glBindFramebufferEXT(GL_DRAW_FRAMEBUFFER_EXT,0)
        createdtex=True

    imagetex.blit(0,0)
    back.blit(0,0)
pyglet.app.run()

import struct
import moderngl
import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_FORWARD_COMPATIBLE_FLAG, True)
        self.screen = pg.Surface(VIRTUAL_RES).convert((255, 65280, 16711680, 0))
        pg.display.set_mode(REAL_RES, pg.DOUBLEBUF|pg.OPENGL)
        pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.ctx = moderngl.create_context()
        texture_coordinates = [0, 1,  1, 1,
                            0, 0,  1, 0]
        world_coordinates = [-1, -1,  1, -1,
                            -1,  1,  1,  1]
        render_indices = [0, 1, 2,
                        1, 2, 3]
        self.prog = self.ctx.program(
            vertex_shader=open("vertex.glsl").read(),
            fragment_shader=open("fragment.glsl").read()
        )

        self.screen_texture = self.ctx.texture(
            VIRTUAL_RES, 3,
            pg.image.tostring(self.screen, "RGB", 1))

        self.screen_texture.repeat_x = False
        self.screen_texture.repeat_y = False

        vbo = self.ctx.buffer(struct.pack('8f', *world_coordinates))
        uvmap = self.ctx.buffer(struct.pack('8f', *texture_coordinates))
        ibo= self.ctx.buffer(struct.pack('6I', *render_indices))

        vao_content = [
            (vbo, '2f', 'vert'),
            (uvmap, '2f', 'in_text')
        ]

        self.vao = self.ctx.vertex_array(self.prog, vao_content, ibo)

    def render(self):
        texture_data = self.screen.get_view('1')
        self.screen_texture.write(texture_data)
        self.ctx.clear(14/255,40/255,66/255)
        self.screen_texture.use()
        self.vao.render()
        pg.display.flip()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.render()
        #pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        #self.screen.fill('black')
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()

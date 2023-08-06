import pygame as pg
import moderngl as mgl
import sys


class GraphicsEngine:
    def __init__(self, win_size=(800, 800)):
        # initalize
        # like SDL_INIT_EVERYTHING
        pg.init()
        # set window size
        self.WIN_SIZE = win_size
        # opengl
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(
            pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE
        )
        # gl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # look for existing gl context
        self.ctx = mgl.create_context()
        # clock
        self.clock = pg.time.Clock()

    def eventHandler(self):
        for event in pg.event.get():
            # TODO(sako) improve this
            if event.type == pg.quit or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
                sys.exit()

    def renderWorker(self):
        # clear buffer
        self.ctx.clear(0.08, 0.16, 0.18)
        # swap buffer
        pg.display.flip()

    def run(self):
        while True:
            self.eventHandler()
            self.renderWorker()
            self.clock.tick(60)


if __name__ == "__main__":
    app = GraphicsEngine()
    app.run()

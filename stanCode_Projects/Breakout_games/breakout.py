"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program plays a game called
"break out" in which players
moving the paddle to make the ball bounce
and break all bricks!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    lives = NUM_LIVES
    while lives > 0:
        if graphics.num_brick > 0:
            pause(FRAME_RATE)
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.bouncing_obj()
            graphics.bouncing_window()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.reset_ball()
                if lives == 3:
                    graphics.window.remove(graphics.live3)
                elif lives == 2:
                    graphics.window.remove(graphics.live2)
                else:
                    graphics.window.remove(graphics.live1)
                lives -= 1
        else:
            break
    graphics.window.remove(graphics.ball)
    if lives == 0:
        graphics.window.add(graphics.gameover, graphics.window.width / 2 - graphics.gameover.width / 2,
                            graphics.window.height / 2)
    else:
        graphics.window.add(graphics.win, graphics.window.width / 2 - graphics.win.width / 2,
                            graphics.window.height / 2)
    graphics.window.remove(graphics.scoreboard)
    graphics.window.add(graphics.scoreboard, graphics.window.width / 2 - graphics.scoreboard.width / 2,
                        graphics.window.height / 2 + graphics.gameover.height)


if __name__ == '__main__':
    main()

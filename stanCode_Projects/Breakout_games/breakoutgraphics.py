"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program makes a game called
"break out".
This program set bricks, the ball, the velocity of ball,
the paddle, and all the items and conditions
which will be used in the "break out" game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'gray'
        self.window.add(self.paddle, self.window_width/2 - paddle_width/2, self.window_height - paddle_offset)
        self.paddle_ride_side = self.paddle.x + paddle_width
        self.paddle_left_side = self.paddle.x
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, self.window_width/2 - ball_radius, self.paddle.y - self.ball.height)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.set_ball_velocity)
        # Draw bricks
        brick_x = 0
        brick_y = brick_offset
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if (i + 1) % 2 == 0:
                    self.brick.fill_color = 'blue'
                else:
                    self.brick.fill_color = 'red'
                self.window.add(self.brick, brick_x, brick_y)
                brick_x += brick_width + brick_spacing
            brick_y += brick_height + brick_spacing
            brick_x = 0
        self.num_brick = brick_cols * brick_rows
        self.score = 0
        self.scoreboard = GLabel('Score: ' + str(self.score))
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard, 0, self.window_height)
        self.gameover = GLabel('Game over')
        self.gameover.font = '-50'
        self.gameover.color = 'red'
        self.win = GLabel('You win')
        self.win.font = '-35'
        self.win.color = 'yellow'
        self.live1 = GOval(self.scoreboard.height, self.scoreboard.height)
        self.live1.filled = True
        self.live1.fill_color = 'black'
        self.window.add(self.live1, self.window_width - self.scoreboard.height,
                        self.window_height - self.scoreboard.height)
        self.live2 = GOval(self.scoreboard.height, self.scoreboard.height)
        self.live2.filled = True
        self.live2.fill_color = 'black'
        self.window.add(self.live2, self.window_width - self.scoreboard.height - self.live1.width,
                        self.window_height - self.scoreboard.height)
        self.live3 = GOval(self.scoreboard.height, self.scoreboard.height)
        self.live3.filled = True
        self.live3.fill_color = 'black'
        self.window.add(self.live3, self.window_width - self.scoreboard.height - self.live1.width - self.live2.width,
                        self.window_height - self.scoreboard.height)

    def move_paddle(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width/2
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif self.paddle.x <= 0:
            self.paddle.x = 0
        if self.__dy == 0 and self.ball.y == self.paddle.y - self.ball.height:
            self.ball.x = self.paddle.x + self.paddle.width/2 - BALL_RADIUS

    def set_ball_velocity(self, start):
        if self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = -INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy

    def bouncing_window(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        elif self.ball.y <= 0:  # self.ball.y + self.ball.height >= self.window.height:
            self.__dy = -self.__dy

    def ball_in_paddle(self):
        center_ball_x = self.ball.x - BALL_RADIUS
        is_ball_x_in_paddle = self.paddle_left_side <= center_ball_x <= self.paddle_ride_side
        return is_ball_x_in_paddle

    def bouncing_obj(self):
        ball_top_left = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_bottom_left = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS*2)
        ball_top_right = self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y)
        ball_bottom_right = self.window.get_object_at(self.ball.x + BALL_RADIUS*2, self.ball.y + BALL_RADIUS*2)
        if self.ball.y + BALL_RADIUS <= self.paddle.y + self.paddle.height / 2:
            if ball_bottom_left is not None:
                if ball_bottom_left.y <= self.window_height / 2:
                    self.window.remove(ball_bottom_left)
                    self.num_brick -= 1
                    self.score += 10
                    self.scoreboard.text = 'Score: ' + str(self.score)
                    self.__dy = -self.__dy
                elif self.ball.y + self.ball.height < self.paddle.y:  # >=
                    self.__dx = -self.__dx
                    self.__dy = -self.__dy
                elif ball_bottom_left.y <= self.paddle.y:
                    self.__dy = -self.__dy
            elif ball_bottom_right is not None:
                if ball_bottom_right.y <= self.window_height / 2:
                    self.window.remove(ball_bottom_right)
                    self.num_brick -= 1
                    self.score += 10
                    self.scoreboard.text = 'Score: ' + str(self.score)
                    self.__dy = -self.__dy
                elif self.ball.y + self.ball.height < self.paddle.y:  # >=
                    self.__dx = -self.__dx
                    self.__dy = -self.__dy
                elif ball_bottom_right.y <= self.paddle.y:
                    self.__dy = -self.__dy
            elif ball_top_left is not None:
                if ball_top_left.y <= self.window_height / 2:
                    self.window.remove(ball_top_left)
                    self.num_brick -= 1
                    self.score += 10
                    self.scoreboard.text = 'Score: ' + str(self.score)
                    self.__dy = -self.__dy
                elif self.ball.y + self.ball.height < self.paddle.y:  # >=
                    self.__dx = -self.__dx
                    self.__dy = -self.__dy
                elif ball_top_left.y <= self.paddle.y:
                    self.__dy = -self.__dy
            elif ball_top_right is not None:
                if ball_top_right.y <= self.window_height / 2:
                    self.window.remove(ball_top_right)
                    self.num_brick -= 1
                    self.score += 10
                    self.scoreboard.text = 'Score: ' + str(self.score)
                    self.__dy = -self.__dy
                elif self.ball.y + self.ball.height < self.paddle.y:  # >=
                    self.__dx = -self.__dx
                    self.__dy = -self.__dy
                elif ball_top_right.y <= self.paddle.y:
                    self.__dy = -self.__dy

    def reset_ball(self):
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball, self.window_width/2 - BALL_RADIUS, self.paddle.y - self.ball.height)

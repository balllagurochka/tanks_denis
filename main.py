import arcade
import tanks_base
import time
import math
import red
from bullet import *
SCREEN_WIDTH=1200
SCREEN_HEIGHT=700
SCREEN_TITLE="WORD OF TANKS"
GREEN_TANK_SPAWN_X=100
GREEN_TANK_SPAWN_Y=100
GREEN_TANK_CANGE_ANGLE=1
SPEED_GREEN_TANK=5
SPEED_BULLET=5
class GreenTank(arcade.Sprite):
    def __init__(self,window):
        super().__init__("green.png",0.12)
        self.active=True
        self.hit = 0
        self.window=window
        self.reload=0
    def update(self):
        if self.active:
            self.angle+=self.change_angle
            self.part_x = math.cos(math.radians(self.angle))
            self.part_y = math.sin(math.radians(self.angle))
            self.center_x += self.change_x * self.part_x
            self.center_y += self.change_y * self.part_y
            hit_list = arcade.check_for_collision_with_list(self, self.window.green_bullets)
            for i in hit_list:
                if not i.side:
                    i.kill()
                    self.hit += 1
            if time.time()-self.window.spawn_time_bull<3:
                self.reload+=2.1
    def draw(self):
        super().draw()
        ident = self.hit * 7
        arcade.draw_rectangle_filled(self.center_x,self.center_y+35, 70 - ident, 10, (0, 255, 0))
        arcade.draw_arc_outline(30,SCREEN_HEIGHT-30,50,50,(0,0,0),0,360,3)
        arcade.draw_arc_filled(30,SCREEN_HEIGHT-30,50,50,(0,255,0),0,360-self.reload)
class Game(arcade.Window):
    def __init__(self,width,heigth,title):
        super().__init__(width,heigth,title)
        self.bg=arcade.load_texture("background.png")
        self.green_tank=GreenTank(self)
        self.left_pressed=False
        self.right_pressed=False
        self.up_pressed = False
        self.down_pressed = False
        self.green_base=tanks_base.GreenBase(self)
        self.red_base=tanks_base.RedBase(self)
        self.red_tanks=[]
        self.setup()
        self.green_bullets=arcade.SpriteList()
        self.spawn_time_bull = time.time()
        self.game=True
    def setup(self):
        self.green_tank.center_x=GREEN_TANK_SPAWN_X
        self.green_tank.center_y=GREEN_TANK_SPAWN_Y
        self.green_base.center_x=SCREEN_WIDTH/6
        self.green_base.center_y=SCREEN_HEIGHT/2
        self.red_base.center_x=SCREEN_WIDTH-200
        self.red_base.center_y=SCREEN_HEIGHT/2
        for i in range(1,7):
            red_tank=red.RedTank(self,0)
            red_tank.center_x=SCREEN_WIDTH-400
            red_tank.center_y=SCREEN_HEIGHT/7*i
            self.red_tanks.append(red_tank)
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg)
        self.green_tank.draw()
        self.green_bullets.draw()
        self.green_base.draw()
        self.red_base.draw()
        for y in self.red_tanks:
            y.draw()
    def update(self, delta_time: float):
        if self.game:
            self.green_tank.update()
            self.green_bullets.update()
            self.green_base.update()
            self.red_base.update()
            for i in self.red_tanks:
                i.update()
    def on_key_press(self, key: int, modifiers: int):
        if self.game:
            if key==arcade.key.LEFT:
                self.green_tank.change_angle=GREEN_TANK_CANGE_ANGLE
            if key==arcade.key.RIGHT:
                self.green_tank.change_angle=-GREEN_TANK_CANGE_ANGLE
            if key==arcade.key.UP:
                self.green_tank.change_y=SPEED_GREEN_TANK
                self.green_tank.change_x=SPEED_GREEN_TANK
            if key==arcade.key.DOWN:
                self.green_tank.change_y=-SPEED_GREEN_TANK
                self.green_tank.change_x=-SPEED_GREEN_TANK
            if key==arcade.key.SPACE:
                if time.time() - self.spawn_time_bull >= 3:
                    green_bullet = Bullet("green_bullet.png", self.green_tank,1)
                    self.green_bullets.append(green_bullet)
                    self.green_tank.reload=0
                    self.spawn_time_bull = time.time()
    def on_key_release(self, key: int, modifiers: int):
        if self.game:
            if key==arcade.key.UP:
                self.green_tank.change_y=0
                self.green_tank.change_x=0
            if key==arcade.key.DOWN:
                self.green_tank.change_y=0
                self.green_tank.change_x=0
            if key==arcade.key.LEFT:
                self.green_tank.change_angle=0
            if key==arcade.key.RIGHT:
                self.green_tank.change_angle=0
window=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()
import math
import time
import arcade
from bullet import *
class RedTank(arcade.Sprite):
    def __init__(self,window,side):
        super().__init__("red_tank.png",0.12)
        self.active=True
        self.angle=180
        self.hit = 0
        self.window=window
        self.side=side
        self.bullet_time=time.time()
        self.red_bullet=arcade.SpriteList()
    def fire(self):
        if time.time() - self.bullet_time >= 6:
            green_bullet = Bullet("green_bullet.png", self, 1)
            self.red_bullet.append(green_bullet)
            self.bullet_time = time.time()
    def draw(self):
        super().draw()
        ident = self.hit * 35
        arcade.draw_rectangle_filled(self.center_x,self.center_y+35, 70 - ident, 10, (255, 0, 0))
        if self.hit>=2:
            self.texture=arcade.load_texture("red_morre.png")
            self.active = False
        self.red_bullet.draw()
    def update(self):
        if self.active:
            self.red_bullet.update()
            radius=arcade.get_distance_between_sprites(self,self.window.green_tank)
            hit_list=arcade.check_for_collision_with_list(self,self.window.green_bullets)
            for i in hit_list:
                if i.side:
                    i.kill()
                    self.hit+=1
            hit_list=arcade.check_for_collision_with_list(self.window.green_tank,self.red_bullet)
            for i in hit_list:
                if i.side==0:
                    i.kill()
                    self.window.green_tank.hit += 1
            hit_list_base = arcade.check_for_collision_with_list(self.window.green_base, self.red_bullet)
            for i in hit_list_base:
                if i.side==0:
                    i.kill()
                    self.window.green_base.hit+=1
            delta_x=self.window.green_tank.center_x-self.center_x
            delta_y=self.window.green_tank.center_y-self.center_y
            if radius<=200:
                self.angle=math.degrees(math.atan2(delta_y,delta_x))
                if time.time()-self.bullet_time>=2:
                    self.part_x=math.cos(math.radians(self.angle))
                    self.part_y=math.sin(math.radians(self.angle))
                    bullet=Bullet("green_bullet.png",self,0)
                    self.red_bullet.append(bullet)
                    self.bullet_time=time.time()
            elif arcade.get_distance_between_sprites(self,self.window.green_base)<=250:
                delta_x=self.window.green_base.center_x-self.center_x
                delta_y=self.window.green_base.center_y-self.center_y
                self.angle = math.degrees(math.atan2(delta_y, delta_x))
                if time.time() - self.bullet_time >= 6:
                    self.part_x = math.cos(math.radians(self.angle))
                    self.part_y = math.sin(math.radians(self.angle))
                    bullet = Bullet("green_bullet.png", self, 0)
                    self.red_bullet.append(bullet)
                    self.bullet_time = time.time()

            else:
                self.angle=180
                self.center_x-=0.5
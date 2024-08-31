import arcade
SCREEN_WIDTH=1200
SCREEN_HEIGHT=700
class Base(arcade.Sprite):
    def __init__(self,image,hp,window):
        super().__init__(image,1.5)
        self.window=window
class GreenBase(Base):
    def __init__(self,window):
        super().__init__("green_base.png",100,window)
        self.hit=0
    def update(self):
        hit_list=arcade.check_for_collision_with_list(self,self.window.green_bullets)
        for i in hit_list:
            i.kill()
            self.hit+=1
    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x,self.center_y+200,250,10,(0,0,0),3)
        ident=self.hit*25
        arcade.draw_rectangle_filled(self.center_x-ident/2,self.center_y+200,250-ident,10,(0,255,0))
class RedBase(Base):
    def __init__(self,window):
        super().__init__("base_red.png",100,window)
        self.hit=0
    def update(self):
        hit_list=arcade.check_for_collision_with_list(self,self.window.green_bullets)
        for i in hit_list:
            i.kill()
            self.hit+=1
    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x,self.center_y+200,250,10,(0,0,0),3)
        ident=self.hit*25
        arcade.draw_rectangle_filled(self.center_x-ident/2,self.center_y+200,250-ident,10,(255,0,0))
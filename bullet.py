import  arcade
SCREEN_WIDTH=1200
SCREEN_HEIGHT=700
SPEED_BULLET=5
class Bullet(arcade.Sprite):
    def __init__(self,image,tank,side):
        super().__init__(image,0.12)
        self.center_x = tank.center_x
        self.center_y = tank.center_y
        self.change_x=SPEED_BULLET*tank.part_x
        self.change_y=SPEED_BULLET*tank.part_y
        self.angle=tank.angle
        self.side=side
    def update(self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        if self.left>SCREEN_WIDTH or self.right<0 or self.top<0 or self.bottom>SCREEN_HEIGHT:
            self.kill()
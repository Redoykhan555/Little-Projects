import turtle as tur
import time


class Drawable():
    def __init__(self):
        self.pen = tur.Pen()
        self.childs = []
    
    def draw(self):
        raise NotImplementedError

    def add(self):
        raise NotImplementedError

    def delete(self,moves=1):
        for c in self.childs:
            c.delete()

        for i in range(moves):
            self.pen.undo()

        self.pen.reset()
        self.childs = []
    
class Circle(Drawable):
    def __init__(self,c,r):
        super().__init__()
        self.c = c
        self.r = r

    def draw(self,col='red'):
        self.pen.color(col)
        self.pen.pu()
        self.pen.goto(self.c)
        self.pen.pd()
        self.pen.circle(self.r)

class Rectangle(Drawable):
    def __init__(self,a,b):
        super().__init__()
        self.point = None
        self.a = a
        self.b = b   

    def draw(self,col='black'):
        self.pen.color(col)
        self.pen.pu()
        self.pen.setpos(*self.a)
        self.pen.pd()
        self.pen.setpos(self.b[0],self.a[1])
        self.pen.setpos(*self.b)
        self.pen.setpos(self.a[0],self.b[1])
        self.pen.setpos(*self.a)

    def delete(self):
        super().delete(3)

class Triangle(Drawable):
    def __init__(self,a,b,c):
        super().__init__()
        self.a=a
        self.b=b
        self.c=c

    def draw(self,col='blue'):
        self.pen.color(col)
        self.pen.pu()
        self.pen.setpos(*self.a)
        self.pen.pd()
        self.pen.setpos(*self.b)
        self.pen.setpos(*self.c)
        self.pen.setpos(*self.a)

    def delete(self):
        super().delete(2)


class Home(Drawable):
    def __init__(self,c):
        super().__init__()
        self.c = c
    
    def draw(self):
        for c in self.childs:
            c.draw()


class Asian(Home):
    def __init__(self,c):
        super().__init__(c)
        roof = Rectangle(self.c,(c[0]+180,c[1]+120))
        body = Triangle((c[0],c[1]+120),(c[0]+180,c[1]+120),(c[0]+90,c[1]+180))
        door = Rectangle((c[0]+75,c[1]),(c[0]+105,c[1]+120))
        self.childs = [roof,body,door]

class African(Home):
    def __init__(self,c):
        super().__init__(c)
        cir = Circle((c[0]+60,c[1]-60),60)
        cr = Circle((c[0]+60,c[1]+120),60)
        rec = Rectangle(c,(c[0]+120,c[1]+180))
        tr = Triangle((c[0],c[1]+180),(c[0]+120,c[1]+180),(c[0]+60,c[1]+260))
        self.childs=[cr,cir,rec,tr]

a = Asian((0,0))
a.draw()
b=African((-300,0))
b.draw()

time.sleep(2)
a.delete()
b.delete()


        





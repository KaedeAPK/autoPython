import tkinter as tk
# P.229, about
# PDFはmarigin, padding:0で行こう

root = tk.Tk()
root.geometry('800x600')
canvas = tk.Canvas(root, width = 800,height = 600, bg = 'black')
canvas.place(x = 0, y = 0)

class Ball:
    def __init__(self, x, y, dx, dy, color,tag):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.tag = tag

    def erase(self, canvas):
        canvas.delete(self.tag)
    def draw(self,canvas):
        r = 20
        canvas.create_oval(
            self.x - r,  self.y - r,
            self.x + r,  self.y + r,
            fill = self.color, width = 0,
            tag = self.tag,
        )
    
    def move(self, canvas):
        self.erase(canvas)

        self.x += self.dx
        self.y += self.dy

        self.draw(canvas)
        
        if (self.x >= canvas.winfo_width()):
            self.dx = -1
        if (self.x <= 0):
            self.dx = 1
        if (self.y >= canvas.winfo_height()):
            self.dy = -1
        if (self.y <= 0):
            self.dy = 1

# erase(), draw()だけ同名で定義しておけば
# root.after()でのmove()内の呼び出しで実行されるわけか？

class Rect(Ball):
    #def erase(self, canvas):
        #canvas.delete(self.tag)
    def draw(self,canvas):
        print(id(self))
        r = 20
        canvas.create_rectangle(
            self.x - r,  self.y - r,
            self.x + r,  self.y + r,
            fill = self.color, width = 0,
            tag = self.tag,
        )

# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/
# create_polygon.html

# id = C.create_polygon(x0, y0, x1, y1, ..., option, ...)
class Tri(Ball):
    #def erase(self, canvas):
        #canvas.delete(self.tag)
    def draw(self,canvas):
        r = 20
        print(id(self))
        canvas.create_polygon(
            self.x, self.y - r,
            self.x + r,  self.y + r,
            self.x -r, self.y +r,
            fill = self.color, width = 0,
            tag = self.tag,
        )

balls = [
    Ball(400,300,1,1,'red','tagR'),
    Rect(200,100,-1,1,'green','tagG'),
    Tri(100,200,1,-1,'blue', 'tagB'),
]

def loop():
    for b in balls:
        b.move(canvas)
    root.after(10,loop)

root.after(10,loop)

root.mainloop()
    

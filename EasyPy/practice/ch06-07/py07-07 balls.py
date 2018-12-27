#coding:utf-8
import tkinter as tk

r = 20
balls = [
    {'x':400, 'y':300, 'dx': 1, 'dy': 1, 'color':'red',},
    {'x':200, 'y':100, 'dx': -1, 'dy': 1, 'color': 'green',},
    {'x':100, 'y':200, 'dx': 1, 'dy': -1, 'color': 'blue'},
]
print(balls[0]['color'],balls[1]['color'],balls[2]['color'],)

def move():
    global balls, r
    for b in balls:
        canvas.delete("prev")
        canvas.create_oval(
            b['x'] - r,  b['y'] - r,
            b['x'] + r,  b['y'] + r,
            fill = 'white', width = 0,
        )
        b['x'] += b['dx']
        b['y'] += b['dy']

        # 前の位置情報の円を消して
        # 座標を更新して
        # 次の円を描く

        
        if b['x'] >= canvas.winfo_width():
            b['dx'] = -1
        if b['x'] <= 0:
            b['dx'] = 1
            
        if b['y'] >= canvas.winfo_height():
            b['dy'] = -1
        if b['y'] <= 0:
            b['dy'] = 1

        canvas.create_oval(
            b['x'] - r,  b['y'] - r,
            b['x'] + r,  b['y'] + r,
            fill = b['color'], width = 0,
            #tag = 'prev',
        ) # tagをなんとかしないと動かない
    root.after(10, move)

root = tk.Tk()
root.geometry('600x400')
# tsundoku app

canvas = tk.Canvas(root, width = 600,height = 400, bg = 'white')
canvas.place(x = 0, y = 0)

root.after(10,move)
root.mainloop()

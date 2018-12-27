#coding:utf-8
import tkinter as tk

r = 20
balls = [
    {'x':400, 'y':300, 'dx': 1, 'dy': 1, 'color':'red', 'tag': 'redTag',},
    {'x':200, 'y':100, 'dx': -1, 'dy': 1, 'color': 'green','tag': 'greenTag',},
    {'x':100, 'y':200, 'dx': 1, 'dy': -1, 'color': 'blue','tag': 'blueTag',},
]
# tagですべて消してるはずなのにどんどん重くなって固まってしまう。どこに欠点が？
def move():
    global balls, r
    for b in balls:
        # 前の位置情報の円を(tagで)消して,
        canvas.delete(b['tag'])
        #座標を更新して,
        b['x'] += b['dx']
        b['y'] += b['dy']

        if b['x'] >= canvas.winfo_width():
            b['dx'] = -1
        if b['x'] <= 0:
            b['dx'] = 1
            
        if b['y'] >= canvas.winfo_height():
            b['dy'] = -1
        if b['y'] <= 0:
            b['dy'] = 1

        #次の円を描く, RED, GREEN, BLUEの3種類生成される.
        canvas.create_oval(
            b['x'] - r,  b['y'] - r,
            b['x'] + r,  b['y'] + r,
            fill = b['color'], width = 0,
            tag = b['tag'],
        ) # tag同じのをつけるとblueのものしか出ない。
    root.after(10, move)

root = tk.Tk()
root.geometry('600x400')
# tsundoku app

canvas = tk.Canvas(root, width = 600,height = 400, bg = 'white')
canvas.place(x = 0, y = 0)

root.after(10,move)
root.mainloop()

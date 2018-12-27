import tkinter as tk
x = 400
y = 300
r = 20
dx = 1

def move():
    global x, y, dx
    # Del previous Circle
    canvas.delete('prev')
    x += dx
    canvas.create_oval(x-r, y-r, x+r, y+r, fill='red', width='0', tag = 'prev')

    #　画面内に収める
    if canvas.winfo_width() <= x:
        dx = -3
    elif x <= 0:
        dx = +3
    root.after(10,move)

root = tk.Tk()
root.geometry('600x400')

# define canvas with tag.
canvas = tk.Canvas(root, width = 600, height = 400, bg = 'white',)
canvas.place(x = 0, y = 0)

root.after(10,move)
root.mainloop()

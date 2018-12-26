import tkinter as tk

r = 20
x = 400
y = 300

def move():
    global x, y
#    c.create_oval(x-r, y-r, x+r, y+r, fill = 'white', width = 0)
    c.delete("prev")
    x +=1
    c.create_oval(x-r, y-r, x+r, y+r, fill = 'red', width = 0, tag="prev")
    root.after(10,move)

root = tk.Tk()
root.geometry('600x400')

c = tk.Canvas(root, width = 600, height = 400, bg = 'white')
c.place(x = 0, y = 0)
# 1s/1000 x 10
root.after(10,move)

root.mainloop()

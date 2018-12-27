import tkinter as tk

root = tk.Tk()
root.geometry('600x400')
r = 20
x = 300
y = 200

def click(event):
    global x, y
    print(str(x) +' '+str(y))
    c.create_oval(
        x-r,  y-r,  x+r,  y+r, 
        fill = 'red', width = 0,
    )
    x = event.x
    y = event.y
    print(str(x)+' '+ str(y))
    c.create_oval(
        x-r,  y-r,  x+r,  y+r, 
        fill = 'white', width = 0,
    )

c = tk.Canvas(root, width = 600, height = 400, bg = 'red')
c.place(x = 0, y = 0)

c.bind('<Button-1>', click)

root.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry('600x400')

c = tk.Canvas(root, width = 600, height = 400, bg = '#444')
c.place(x = 0, y = 0)

r = 20
c.create_oval(
    300-r, 200-r, 300+r, 200+r, 
    fill = '#f00',outline = '#000',
    width = 5,
)

root.mainloop()

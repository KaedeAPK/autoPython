import tkinter as tk
import tkinter.messagebox as tmsg

def BtnOnClick():
    tmsg.showinfo('Test code.', 'Clicked.')

root = tk.Tk()
root.geometry('1000x500')
root.title('数当てゲーム')

label1 = tk.Label(root, text = 'Input number.',
 font = ('Apple SD Gothic Neo', 28))
label1.place(x = 20, y = 20)


editbox1 = tk.Entry(width = 8, font = ('Apple SD Gothic Neo', 28))
editbox1.place(x = 120, y = 60)

btn = tk.Button(root, 
        text = 'Check', 
        font = ('Apple SD Gothic Neo',28),
        command = BtnOnClick
    )
btn.place(x =300, y = 60)

root.mainloop()


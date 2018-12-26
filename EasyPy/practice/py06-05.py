import tkinter as tk
import tkinter.messagebox as tmsg
import random



def BtnOnClick():
    b = editbox1.get()

    # difine 4 dig or not
    isok = False
    if len(b) != 4:
        tmsg.showerror('Error.', 'Input 4 digits')
    else:
        numOk = True
        for i in range(4):
            if ( b[i]< '0') or ('9'<b[i]):
                tmsg.showerror('str(b[i])',' is Not a number.')
                numOk = False
                break
        if numOk:
            isok = True
    if isok:
        hit = 0
        for i in range(4):
            if a[i] == int(b[i]):
                hit +=1

    blow = 0
    for j in range(4):
        for i in range(4):
            if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j]!= int (b[j]) ):
                blow += 1
                break

    if hit == 4:
        tmsg.showinfo('You won!!')
        root.destroy()
    else:
        hisbox.insert(tk.END, b + '  /H:' + str(hit) + '/'
            + 'B: ' + str(blow) + '\n')

a = [
        random.randint(0,9),
        random.randint(0,9),
        random.randint(0,9),
        random.randint(0,9),
     ]

root = tk.Tk()
root.geometry('600x400')
root.title('数当てゲーム')

hisbox = tk.Text(root, font = ('Helvetica', 14))
hisbox.place(x = 400, y = 0, width = 200, height = 400)

label1 = tk.Label(root, text = 'Input number.',
 font = ('Apple SD Gothic Neo', 28))
label1.place(x = 20, y = 20)


editbox1 = tk.Entry(width = 8, font = ('Helvetica', 28))
editbox1.place(x = 120, y = 60)

btn = tk.Button(root, 
        text = 'Check', 
        font = ('Apple SD Gothic Neo',28),
        command = BtnOnClick
    )
btn.place(x =300, y = 60)

root.mainloop()


from tkinter import *

root = Tk()
frame1 = Frame(root, bg='green', bd=5)
frame2 = Frame(root, bg='red', bd=5)
button1 = Button(frame1, text='One button')
button2 = Button(frame2, text='Two button')
frame1.pack()
frame2.pack()
button1.pack()
button2.pack()
root.mainloop()


"""

Two buttons. One color = 'green', the other color = 'red'. Convenient for writing a program and for a mummy application

"""

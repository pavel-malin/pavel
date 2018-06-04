from tkinter import *

root = Tk()
var = IntVar()
rbutton1 = Radiobutton(root, text='1', variable=var, value=1)
rbutton2 = Radiobutton(root, text='2', variable=var, value=1)
rbutton3 = Radiobutton(root, text='3', variable=var, value=1)
rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
root.mainloop()



"""

point selection and point-to-point formation
need to finalize

"""

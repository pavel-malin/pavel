from tkinter import *
from tkinter.filedialog import *



def open_file():
    pass

def save_file():
    pass

def save_fil(event):
    pass

def exit_prog():
    root.destroy()


root = Tk()
root.geometry('800x600')
root.resizable(width=False, height=False)

root_menu = Menu(root)
root.configure(menu=root_menu)
one_item = Menu(root_menu, tearoff=0)
root_menu.add_cascade(label="file", menu=one_item)
one_item.add_command(label="open", command=open_file)
one_item.add_command(label="save as", command=save_file)
one_item.add_separator()
one_item.add_command(label="exit", command=exit_prog)



#Кнопки


n1 = Label(root, text="Тип звонка:")
n2 = Label(root, text="Дата звонка:")
n3 = Label(root, text="Время звонка:")
n4 = Label(root, text="Имя клиента:")
n5 = Label(root, text="Телефон:")
n6 = Label(root, text="Автомобиль:")
n7 = Label(root, text="Коментарии:", font=("Ubuntu", 30))
#n8 = Label(root, text=":")

n1.grid(row=2, column=1, sticky="W", pady=7, padx=15)
n2.grid(row=6, column=1, sticky="W", pady=7, padx=15)
n3.grid(row=10, column=1, sticky="W", pady=7, padx=15)
n4.grid(row=2, column=11, sticky="W", pady=7, padx=20)
n5.grid(row=6, column=11, sticky="W", pady=7, padx=20)
n6.grid(row=10, column=11, sticky="W", pady=7, padx=20)
n7.place(x=10, y=150)
#n8.grid(row=6, column=15, sticky="W", pady=7, padx=20,)


#Поля для галочек



pg1 = Checkbutton(root, text="Лучший звонок")
pg2 = Checkbutton(root, text="Механика")
pg3 = Checkbutton(root, text="Автомат")
pg4 = Checkbutton(root, text="Бензин")
pg5 = Checkbutton(root, text="ДТ")


pg1.grid(row=11, column=14, columnspan=2)
pg2.grid(columnspan=2, row=11, column=1)
pg3.grid(columnspan=2, row=11, column=3, sticky="W")
pg4.grid(columnspan=1, row=11, column=11, sticky="W")
pg5.grid(columnspan=2, row=11, column=13, sticky="W")


#enter


p1 = Entry(root)
p2 = Entry(root)
p3 = Entry(root)
p4 = Entry(root, width=40)
p5 = Entry(root, width=40)
p6 = Entry(root)
p7 = Text(root, width=86, height=14, font=("Ubuntu",12), wrap='word')




p1.grid(row=2, column=3)
p2.grid(row=6, column=3)
p3.grid(row=10, column=3)
p4.grid(row=2, column=14)
p5.grid(row=6, column=14)
p6.grid(row=10, column=14, sticky="W")
p7.place(x=10, y=200)


#button
kn1 = Button(root, text="save as")
kn1.bind("<Button-1>", save_fil)

kn1.place(x=680, y=550)



#image
#im = "/home/....."  # адрес картинки
#ph_im = PhotoImage(file=im)
#canv111 = Canvas(root,)
#canv111.create_image(1, 1, anchor=NW, image=ph_im)
#canv111.place(x=20, y=470


root.mainloop()


"""

program manager for calls to the client

"""

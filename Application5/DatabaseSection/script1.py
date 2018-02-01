from tkinter import *

window = Tk()

def transform_kg():
    gram = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.insert(END, gram)
    t2.insert(END, pounds)
    t3.insert(END, ounces)

b1 = Button(window, text = "Convert", command = transform_kg)
b1.grid(row = 0, column = 3)

e2=Label(window,text="Kg")
e2.grid(row = 0, column = 0)
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 2)


t1 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 2)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 1, column = 3)

t3 = Text(window, height = 1, width = 20)
t3.grid(row = 1, column = 4)

window.mainloop()
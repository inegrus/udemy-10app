
from tkinter import *
import backend

window = Tk()

label1 = Label(window, text = "Title")
label1.grid(row = 0, column = 0)

label2 = Label(window, text = "Author")
label2.grid(row = 0, column = 2)

label3 = Label(window, text = "Year")
label3.grid(row = 1, column = 0)

label4 = Label(window, text = "ISBN")
label4.grid(row = 1, column = 2)


titleText = StringVar()
e1 = Entry(window, textvariable = titleText)
e1.grid(row = 0, column = 1)

authorText = StringVar()
e2 = Entry(window, textvariable = authorText)
e2.grid(row = 0, column = 3)

yearText = StringVar()
e3 = Entry(window, textvariable = yearText)
e3.grid(row = 1, column = 1)

isbbText = StringVar()
e4 = Entry(window, textvariable = isbbText)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

scrollBar = Scrollbar(window)
scrollBar.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = scrollBar.set)
scrollBar.configure(command = list1.yview())

button1 = Button(window, text = "View all", width = 12)
button1.grid(row = 2, column = 3)

button2 = Button(window, text = "Search entry", width = 12)
button2.grid(row = 3, column = 3)

button3 = Button(window, text = "Add entry", width = 12)
button3.grid(row = 4, column = 3)

button4 = Button(window, text = "Update", width = 12)
button4.grid(row = 5, column = 3)

button5 = Button(window, text = "Delete", width = 12)
button5.grid(row = 6, column = 3)

button6 = Button(window, text = "Close", width = 12)
button6.grid(row = 7, column = 3)

window.mainloop()
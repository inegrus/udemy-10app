from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])



def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row) #the new row will be put at the end of the listbox

def search_command():

    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    if title_text.get() != "" and author_text.get() != "" and year_text.get() != "" and isbn_text.get() != "":
        backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    view_command()

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    view_command()


window = Tk()
window.wm_title("BookStore")

label1 = Label(window, text = "Title")
label1.grid(row = 0, column = 0)

label2 = Label(window, text = "Author")
label2.grid(row = 0, column = 2)

label3 = Label(window, text = "Year")
label3.grid(row = 1, column = 0)

label4 = Label(window, text = "ISBN")
label4.grid(row = 1, column = 2)


title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

list1.bind('<<ListboxSelect>>', get_selected_row)

scrollBar = Scrollbar(window)
scrollBar.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = scrollBar.set)
scrollBar.configure(command = list1.yview())

button1 = Button(window, text = "View all", width = 12, command = view_command)
button1.grid(row = 2, column = 3)

button2 = Button(window, text = "Search entry", width = 12, command = search_command)
button2.grid(row = 3, column = 3)

button3 = Button(window, text = "Add entry", width = 12, command = add_command)
button3.grid(row = 4, column = 3)

button4 = Button(window, text = "Update", width = 12, command = update_command)
button4.grid(row = 5, column = 3)

button5 = Button(window, text = "Delete", width = 12, command = delete_command)
button5.grid(row = 6, column = 3)

button6 = Button(window, text = "Close", width = 12, command = window.destroy)
button6.grid(row = 7, column = 3)

window.mainloop()
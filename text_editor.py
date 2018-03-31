#text_editor.py
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def load():
    with open(filename.get()) as file:
        contents.delete(1.0, END)
        contents.insert(INSERT, file.read())

def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get(1.0, END))

tk = Tk()
tk.title("Simple Text Editor")

contents = ScrolledText()
contents.pack(side=BOTTOM, fill= BOTH, expand= True)

filename = Entry()
filename.pack(side=LEFT, fill = X, expand= True)

Button(text="Open", command= load).pack(side=LEFT, fill= X, expand = True)
Button(text="Save", command= save).pack(side=LEFT, fill= X, expand = True)

mainloop()

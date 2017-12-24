
from tkinter import *



root = Tk()
frame = Frame(root)
frame.pack()


Start = Button(frame, text = "Start", fg = "green")
Start.pack( side = LEFT)


Stop = Button(frame, text = "Stop", fg="red")
Stop.pack( side = LEFT )



L1 = Label(frame, text = "Filter")
L1.pack( side = LEFT)


E1 = Entry(frame, bd =5)
E1.pack(side = LEFT)




Go = Button(frame, text = "Go", fg = "blue")
Go.pack( side = LEFT )


text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background = "yellow", foreground = "blue")
text.tag_config("start", background = "black", foreground = "green")



text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background = "yellow", foreground = "blue")
text.tag_config("start", background = "black", foreground = "green")



root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:43:01 2017

@author: Lenovo
"""


def fileSelection3(self):
    text_show.delete('1.0', END)
    hex_show.delete('1.0', END)
    selection = Destination.curselection()
    index=selection[0]
    text_show.insert(END,str(show_arr[index]))
    hex_show.insert(END,str(hex_arr[index]))
def fileSelection4(self):
    text_show.delete('1.0', END)
    hex_show.delete('1.0', END)
    selection = Length.curselection()
    index=selection[0]
    text_show.insert(END,str(show_arr[index]))
    hex_show.insert(END,str(hex_arr[index]))
def fileSelection5(self):
    text_show.delete('1.0', END)
    hex_show.delete('1.0', END)
    selection = Protocol.curselection()
    index=selection[0]
    text_show.insert(END,str(show_arr[index]))
    hex_show.insert(END,str(hex_arr[index]))
def fileSelection6(self):
    text_show.delete('1.0', END)
    hex_show.delete('1.0', END)
    selection = Time.curselection()
    index=selection[0]
    text_show.insert(END,str(show_arr[index]))
    hex_show.insert(END,str(hex_arr[index]))
    
   
    
    
    
text_show = Text(top,width = 90,height = 15)
text_show.pack()
text_show.place(x = 10, y = 245)

hex_show=Text(top,width = 90,height = 30)
hex_show.pack()
hex_show.place(x = 10, y = 480)
show_arr=[]
hex_arr=[]

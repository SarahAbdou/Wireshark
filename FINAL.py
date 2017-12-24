# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 16:52:14 2017

@author: Lenovo
"""



# coding: utf-8

# In[32]:

from tkinter import *
from tkinter import messagebox
import time
import threading
import scapy.all as scapy
import scapy.utils as utils
import scapy.all as hexdump
import scapy.all as conf
from types import *
import operator
import string, types, copy
import pickle
import array
import time


def fileSelection1(self):
    text_show.delete('1.0', END)
    hex_show.delete('1.0', END)
    selection = pktnum.curselection()
    index=selection[0]
    text_show.insert(END,str(show_arr[index]))
    hex_show.insert(END,str(hex_arr[index]))
def fileSelection2(self):
    text_show.delete('1.0', END)
    hex_show.delete('1.0', END)
    selection = Source.curselection()
    index=selection[0]
    text_show.insert(END,str(show_arr[index]))
    hex_show.insert(END,str(hex_arr[index]))
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
    
   

source = ""
destination = ""
protocol = ""
length = ""
time = ""
pktno = ""
pkt_no = 0
info = ""

top = Tk()
top.geometry("1350x750")


L4=Label(top, text = "Packet_No")
L4.pack( )
L4.place(x = 10, y = 60)

L_Dest = Label(top, text = "Source")
L_Dest.pack( )
L_Dest.place(x = 75, y = 60)

L_Dest = Label(top, text = "Destination")
L_Dest.pack( )
L_Dest.place(x = 250, y = 60)


L3 = Label(top, text = "Length")
L3.pack( )
L3.place(x = 430, y = 60)

L2 = Label(top, text = "Protocol")
L2.pack( )
L2.place(x = 480, y = 60)

L5 = Label(top, text = "Time")
L5.pack( )
L5.place(x = 550, y = 60)


scrollbar = Scrollbar(top)
scrollbar.pack(side = RIGHT, fill = Y)


pktnum = Listbox(top, width = 10, height = 10, yscrollcommand = scrollbar.set)
pktnum.bind('<<ListboxSelect>>', fileSelection1)
pktnum.pack()
pktnum.place(x = 10, y = 80)


Source = Listbox(top, width = 30, height = 10, yscrollcommand = scrollbar.set)
Source.bind('<<ListboxSelect>>', fileSelection2)
Source.pack()
Source.place(x = 70, y = 80)

# attach listbox to scrollbar
Source.config(yscrollcommand=scrollbar.set,)
scrollbar.config(command = Source.yview)


Destination = Listbox(top, width =30, height = 10, yscrollcommand = scrollbar.set)
Destination.bind('<<ListboxSelect>>', fileSelection3)
Destination.pack()
Destination.place(x = 250, y = 80)

Length = Listbox(top, width = 10, height = 10, yscrollcommand = scrollbar.set)
Length.bind('<<ListboxSelect>>', fileSelection4)
Length.pack()
Length.place(x = 430, y = 80)

Protocol = Listbox(top, width = 15, height = 10, yscrollcommand = scrollbar.set)
Protocol.bind('<<ListboxSelect>>', fileSelection5)
Protocol.pack()
Protocol.place(x = 480, y = 80)

Time = Listbox(top, width = 30, height = 10, yscrollcommand = scrollbar.set)
Time.bind('<<ListboxSelect>>', fileSelection6)
Time.pack()
Time.place(x = 550, y = 80)


text_show = Text(top,width = 90,height = 15)
text_show.pack()
text_show.place(x = 10, y = 245)

hex_show=Text(top,width = 90,height = 30)
hex_show.pack()
hex_show.place(x = 10, y = 480)
show_arr=[]
hex_arr=[]
i = 1
def trial(pkt):
    global i
   # global show_arr

    global show_arr,hex_arr

    global source , destination , protocol , length , time , pktno , pkt_no , info
    shoow1 = str(pkt.show(dump=True))
    hex1 = str(hexdump.hexdump(pkt,dump=True))
    show_arr.append(shoow1)
    hex_arr.append(hex1)
    time = str(pkt.time)
    pkt_no = pkt_no+1
    pktno = str(pkt_no)
    print("HELLOOOO  "+str(pkt_no)+"   "+shoow1)
    if(pkt.haslayer(scapy.IPv6)):
         source =pkt[scapy.IPv6].src
         destination = pkt[scapy.IPv6].dst
         length = str(pkt[scapy.IPv6].plen)
         proto_field = pkt[scapy.IPv6].get_field('nh')
         protocol = proto_field.i2s[pkt.nh]
    elif(pkt.haslayer(scapy.IP)):
        source = pkt[scapy.IP].src
        destination = pkt[scapy.IP].dst
        length =str(pkt[scapy.IP].len)
        proto_field = str(pkt[scapy.IP].proto)
        if(proto_field == "6"):
                   if(str(pkt[scapy.TCP].sport) == "80" or str(pkt[scapy.TCP].dport) == "80"):
                       protocol = "HTTP"
                   else:
                       protocol =  "TCP"
        elif(proto_field == "17"):
              protocol = "UDP"
        else:
              protocol = "ip other"
    elif(pkt.haslayer(scapy.ARP)):
         source =  pkt[scapy.ARP].psrc
         destination = pkt[scapy.ARP].pdst
         length =  str(pkt[scapy.ARP].plen)
         protocol = "ARP"

    else:
        source = "OTHER"
        destination = "OTHER"
        length = "OTHER"
        protocol = "OTHER"
        
    Source.insert(i, source)
    Destination.insert(i, destination)
    Protocol.insert(i,protocol)
    Length.insert(i,length)
    Time.insert(i,time)
    pktnum.insert(i,pkt_no)
    i=i+1
    print("SRC = " + source + " DESTINATION = " + destination + "LENGTH = " + length + " PROTOCOL = " + protocol + " TIME = " +time," PKT NUMBER = "+pktno)

okay = False
Filter = ""
def Stop():
    global okay
    okay = True

def stopperCheck(x):
    global okay
    if okay:
        return True
    return False

def Sniff():
      global pkts
      pkts = scapy.sniff(count=0,store = 0 ,prn = trial,iface="Realtek RTL8188EU Wireless LAN 802.11n USB 2.0 Network Adapter",stop_filter = stopperCheck)

  #  while (okay == False):
   #     pkts = scapy.sniff(count=1, store = 0 ,prn = trial , iface="Realtek RTL8188EU Wireless LAN 802.11n USB 2.0 Network Adapter")   

def start_alert_thread():
    t = threading.Thread(target = Sniff)
    t.start()
    t.join
    
def Restart():
    global okay
    okay = True
    okay = False
    t2 = threading.Thread(target = Sniff)
    t2.start()
    t2.join 
    
def FF ():
    global Filter
    print (Filter)
    i =  0
    while (True):
        if (i == Protocol.size()+1):
            break
        if Protocol.get(i) != Filter:
            print (Protocol.get(i))
            Protocol.delete(i)
            Source.delete(i)
            Destination.delete(i)
            Time.delete(i)
            pktnum.delete(i)
            Length.delete(i)
        else:
            i = i + 1
        
            
def filter_thread():
    global Filter
    Filter =  E1.get()
    t3 = threading.Thread(target = FF)
    t3.start()
    t3.join
    
B = Button(top, text = "Start Capture", bg = "green" ,command = start_alert_thread) 
B.place(x = 10, y = 10)

Restart = Button(top, text = "Restart", bg = "blue", command = Restart )
Restart.place(x = 100, y = 10)

Stop = Button(top, text = "Stop", bg = "red",command = Stop)
Stop.place(x = 150, y = 10)


E1 = Entry(top, bd =5)
E1.pack(side = LEFT)
E1.place(x = 250, y = 10)
E1.focus_set()

b = Button(top, text = "Filter", width = 10, bg = "orange", command = filter_thread)
b.place(x = 400, y = 10)

L1 = Label(top, text = "Filter")
L1.pack( side = LEFT)
L1.place(x = 220, y = 10)



print("THIS IS SHOW $$$$$"+str(len(show_arr)))

top.mainloop() 











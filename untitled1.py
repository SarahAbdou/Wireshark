# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:35:46 2017

@author: Lenovo
"""

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


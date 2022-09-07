#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:33:57 2022
"""
import tkinter as tk
from tkinter import ttk

def click_btn(num):
    tmp = var1.get()
    tmp = tmp + f'{num}'
    var1.set(tmp)

def ops_btn(num):
    tmp = var1.get()
    if not num == 4:
        tmp = tmp + f'{operators[num]}'
        var1.set(tmp)
    else: 
        tmp = tmp.replace(chr(247),"/").replace(chr(215),"*").replace(" ","")
        var1.set(eval(tmp))
      
def clear_btn(num):
    var1.set("")

root = tk.Tk()
root.title('Calculator')
root.wait_visibility(root)
root.wm_attributes('-alpha',1.0,'-topmost', True)

window = ttk.Frame(root, padding=(10, 10, 10, 10))
framel = ttk.Frame(window, borderwidth=5, relief="ridge", width=250, height=450, padding=(0, 0, 8, 8))
framec = ttk.Frame(window, borderwidth=5, relief="ridge", width=50, height=450)

window.grid(column=0, row=0)
framel.grid(column=0, row=0)
framec.grid(column=1, row=0)

cpaneTop = ttk.Frame(framel, height=2, borderwidth=1, relief="ridge")
cpaneTop.grid(column=0, row=0,  columnspan=3)
cpane7 = ttk.Frame(framel)
cpane7.grid(column=0, row=1)
cpane8 = ttk.Frame(framel)
cpane8.grid(column=1, row=1)
cpane9 = ttk.Frame(framel)
cpane9.grid(column=2, row=1)
cpane4 = ttk.Frame(framel)
cpane4.grid(column=0, row=2)
cpane5 = ttk.Frame(framel)
cpane5.grid(column=1, row=2)
cpane6 = ttk.Frame(framel)
cpane6.grid(column=2, row=2)
cpane1 = ttk.Frame(framel)
cpane1.grid(column=0, row=3)
cpane2 = ttk.Frame(framel)
cpane2.grid(column=1, row=3)
cpane3 = ttk.Frame(framel)
cpane3.grid(column=2, row=3)
cpane0 = ttk.Frame(framel)
cpane0.grid(column=0, row=4,  columnspan = 2)

var1 = tk.StringVar()
lbl1 = tk.Label(framel, borderwidth=1, textvariable=var1)
lbl1.grid(column=0, row=0, columnspan=5)
var1.set("")

btn7 = tk.Button(cpane7,text="7",width=4, command= lambda x1=7: click_btn(x1))
btn7.grid(column=0, row=0)
btn8 = tk.Button(cpane8,text="8",width=4, command= lambda x1=8: click_btn(x1))
btn8.grid(column=0, row=0)
btn9 = tk.Button(cpane9,text="9",width=4, command= lambda x1=9: click_btn(x1))
btn9.grid(column=0, row=0)
btn4 = tk.Button(cpane4,text="4",width=4, command= lambda x1=4: click_btn(x1))
btn4.grid(column=0, row=0)
btn5 = tk.Button(cpane5,text="5",width=4, command= lambda x1=5: click_btn(x1))
btn5.grid(column=0, row=0)
btn6 = tk.Button(cpane6,text="6",width=4, command= lambda x1=6: click_btn(x1))
btn6.grid(column=0, row=0)
btn1 = tk.Button(cpane1,text="1",width=4, command= lambda x1=1: click_btn(x1))
btn1.grid(column=0, row=0)
btn2 = tk.Button(cpane2,text="2",width=4, command= lambda x1=2: click_btn(x1))
btn2.grid(column=0, row=0)
btn3 = tk.Button(cpane3,text="3",width=4, command= lambda x1=3: click_btn(x1))
btn3.grid(column=0, row=0)
btn0 = tk.Button(cpane0,text="0",width=4, command= lambda x1=0: click_btn(x1))
btn0.grid(column=0, row=0)
clearBtn = tk.Button(cpane0,text=" Clear ",width=4, command= lambda x1=0: clear_btn(x1))
clearBtn.grid(column=1, row=0)


operators = [chr(247), chr(215), '-', '+', '=']
ops= []
for i, op in enumerate(operators):
    btn = tk.Button(framec,text=op,width=4, height=1, command= lambda x1=i: ops_btn(x1))
    btn.grid(column=0, row=i)
    ops.append(btn)


root.mainloop()


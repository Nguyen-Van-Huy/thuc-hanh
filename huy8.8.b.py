#bai 8.8 b:
from tkinter import *
tk=Tk()
tk.title('welcome')
tk.geometry('220x40')
var1=BooleanVar()
var1.set(False)
cb1=Checkbutton(tk,text='first',variable=var1)
cb1.place(x=0,y=0)
var2=BooleanVar()
var2.set(False)
cb2=Checkbutton(tk,text='second',variable=var2)
cb2.place(x=50,y=0)
var3=BooleanVar()
var3.set(False)
cb3=Checkbutton(tk,text='third',variable=var3)
cb3.place(x=100,y=0)
def click():
    if var1.get()== True:
        lb1=Label(tk,text='1')
        lb1.place(x=200,y=0)
    if var2.get()== True:
        lb2=Label(tk,text='2')
        lb2.place(x=200,y=50)
    if var3.get()== True:
        lb3=Label(tk,text='3')
        lb3.place(x=200,y=100)
bt=Button(tk,text='click me',command=click)
bt.place(x=150,y=0)
tk.mainloop()

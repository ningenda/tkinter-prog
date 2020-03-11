from tkinter import *


window=Tk()

def weight_convert():
    grams=float(e2_value.get())*1000
    t1.delete("1.0",END)
    t1.insert(END,grams)
    pound=float(e2_value.get())*2.20462
    t2.delete("1.0",END)
    t2.insert(END,pound)
    ounces=float(e2_value.get())*35.274
    t3.delete("1.0",END)
    t3.insert(END,ounces)

e1=Label(window,text="kg")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1 )

b1=Button(window,text="Convert",command=weight_convert)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()

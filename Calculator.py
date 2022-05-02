from argparse import MetavarTypeHelpFormatter
from ast import operator
from distutils import command
from faulthandler import disable
from tkinter import*
from math import*
from turtle import bgcolor
from tkinter import ttk
manslogs = Tk()
manslogs.title("Calculator")
# manslogs.geometry("300x300")
manslogs.configure(bg="black")


manslogs.attributes('-toolwindow', True)



def btnclick(number):
    current = e.get()  # nolasa esošo skaitli
    e.delete(0, END)  # nodzēš
    newnumber = str(current)+str(number)
    e.insert(0, newnumber)  # ievieto displejā
    return 0

def btncommand(command):
    global num1  # jaiegaume skaitlis
    global mathOp  # matemātiskais operātors
    mathOp = command  # +,-,x,:
    num1 = int(e.get())
    e.delete(0, END)
    return 0

def btnVienads():
    global num2
    num2 = (float(e.get()))
    result = 0
    if mathOp == "+":
        result = num1+num2
    elif mathOp == "-":
        result = num1-num2
    elif mathOp == "x":
        result = num1*num2
    elif mathOp == ":":
        result = num1/num2
    elif mathOp == "%":
        result = num1*0.01*num2
    else:
        result = 0
    e.delete(0, END)
    e.insert(0, str(result))
    return 0


def notirit():
    e.delete(0, END)
    num1 = 0
    mathOp = ""
    return 0

def sq_rt():
   global operator
   global num1
   num1 = (float(e.get()))
   num1=sqrt(num1) 
   e.delete(0,END)
   e.insert(0,num1)
   return 0

def logarithm():
   global operator
   global num1
   num1 = (float(e.get()))
   num2=log10(num1) 
   e.delete(0,END)
   e.insert(0,num2)
   return 0

def square():
    global num1
    num1=float(e.get())
    num2=num1*num1
    e.delete(0,END)
    e.insert(0,num2)




e = Entry(manslogs, bg="purple", width=20, bd=20, font=("Arial Black", 20))
e.grid(row=0, column=0, columnspan=5)

btn0 = Button(manslogs, font=5, bg='red', text="0", padx="40",
              pady="20", command=lambda: btnclick(0))
btn1 = Button(manslogs,font=5, bg='red',text="1", padx="40",
              pady="20", command=lambda: btnclick(1))
btn2 = Button(manslogs,font=5,bg='red', text="2", padx="40",
              pady="20", command=lambda: btnclick(2))
btn3 = Button(manslogs,font=5,bg='red', text="3", padx="40",
              pady="20", command=lambda: btnclick(3))
btn4 = Button(manslogs,font=5,bg='red', text="4", padx="40",
              pady="20", command=lambda: btnclick(4))
btn5 = Button(manslogs,font=5,bg='red', text="5", padx="40",
              pady="20", command=lambda: btnclick(5))
btn6 = Button(manslogs,font=5,bg='red', text="6", padx="40",
              pady="20", command=lambda: btnclick(6))
btn7 = Button(manslogs,font=5,bg='red', text="7", padx="40",
              pady="20", command=lambda: btnclick(7))
btn8 = Button(manslogs,font=5,bg='red', text="8", padx="40",
              pady="20", command=lambda: btnclick(8))
btn9 = Button(manslogs,font=5,bg='red', text="9", padx="40",
              pady="20", command=lambda: btnclick(9))

btnsum = Button(manslogs,font=5,bg='cyan', text="+", padx="39", pady="20",
                command=lambda: btncommand("+"))

btnsub = Button(manslogs,font=5,bg='cyan', text="-", padx="41", pady="20",
                command=lambda: btncommand("-"))

btnmul = Button(manslogs,font=5,bg='cyan', text="x", padx="40", pady="20",
                command=lambda: btncommand("x"))

btndiv = Button(manslogs,font=5,bg='cyan', text=":", padx="42", pady="20",
                command=lambda: btncommand(":"))

btnproc = Button(manslogs,font=5,bg='cyan', text="%", padx="37.5", pady="20",
                command=lambda: btncommand("%"))

btnclear = Button(manslogs,font=5,bg='yellow', text="C", padx="38", pady="20",command=notirit)
btnequals = Button(manslogs,font=5,bg='yellow', text="=", padx="40", pady="20",command=btnVienads)
btnsqrt = Button(manslogs,font=5,bg='lime', text="√", padx="40", pady="20",command=sq_rt)
btnlog = Button(manslogs,font=5,bg='lime', text="log", padx="35", pady="20",command=logarithm)
btnsquared = Button(manslogs,font=5,bg='lime', text="x²", padx="40", pady="20",command=square)


btnproc.grid(row=5, column=4)
btnsqrt.grid(row=5, column=1)
btnsquared.grid(row=5, column=2)
btnlog.grid(row=5, column=3)

btn1.grid(row=1, column=1)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=3)
btndiv.grid(row=1, column=4)

btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btnmul.grid(row=2, column=4)

btn7.grid(row=3, column=1)
btn8.grid(row=3, column=2)
btn9.grid(row=3, column=3)
btnsum.grid(row=3, column=4)

btn0.grid(row=4, column=2)
btnclear.grid(row=4, column=1)
btnequals.grid(row=4, column=3)
btnsub.grid(row=4, column=4)


manslogs.mainloop()

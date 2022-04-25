from argparse import MetavarTypeHelpFormatter
from ast import operator
from distutils import command
from tkinter import*
from math import*
manslogs = Tk()
manslogs.title("Calculator")
# manslogs.geometry("300x300")


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
   num1=log(num1,10) 
   e.delete(0,END)
   e.insert(0,num1)
   return 0




e = Entry(manslogs, width=15, bd=20, font=("Arial Black", 20))
e.grid(row=0, column=0, columnspan=5)

btn0 = Button(manslogs, text="0", padx="40",
              pady="20", command=lambda: btnclick(0))
btn1 = Button(manslogs, text="1", padx="40",
              pady="20", command=lambda: btnclick(1))
btn2 = Button(manslogs, text="2", padx="40",
              pady="20", command=lambda: btnclick(2))
btn3 = Button(manslogs, text="3", padx="40",
              pady="20", command=lambda: btnclick(3))
btn4 = Button(manslogs, text="4", padx="40",
              pady="20", command=lambda: btnclick(4))
btn5 = Button(manslogs, text="5", padx="40",
              pady="20", command=lambda: btnclick(5))
btn6 = Button(manslogs, text="6", padx="40",
              pady="20", command=lambda: btnclick(6))
btn7 = Button(manslogs, text="7", padx="40",
              pady="20", command=lambda: btnclick(7))
btn8 = Button(manslogs, text="8", padx="40",
              pady="20", command=lambda: btnclick(8))
btn9 = Button(manslogs, text="9", padx="40",
              pady="20", command=lambda: btnclick(9))

btnsum = Button(manslogs, text="+", padx="40", pady="20",
                command=lambda: btncommand("+"))
btnsub = Button(manslogs, text="-", padx="40", pady="20",
                command=lambda: btncommand("-"))
btnmul = Button(manslogs, text="x", padx="40", pady="20",
                command=lambda: btncommand("x"))
btndiv = Button(manslogs, text=":", padx="40", pady="20",
                command=lambda: btncommand(":"))



btnsquared = Button(manslogs, text="x²", padx="40", pady="20",
                command=lambda: btncommand("x²"))

btnclear = Button(manslogs, text="C", padx="40", pady="20",command=notirit)

btnequals = Button(manslogs, text="=", padx="40", pady="20",command=btnVienads)

btnsqrt = Button(manslogs, text="√", padx="40", pady="20",command=sq_rt)

btnlog = Button(manslogs, text="log", padx="40", pady="20",command=logarithm)
btnsquared = Button(manslogs, text="x²", padx="40", pady="20",command=btnVienads)


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

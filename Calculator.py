from tkinter import*
manslogs=Tk()
manslogs.title("Calculator")
#manslogs.geometry("300x300")
btn0=Button(manslogs,text="0",padx="40",pady="20")
btn1=Button(manslogs,text="1",padx="40",pady="20")
btn2=Button(manslogs,text="2",padx="40",pady="20")
btn3=Button(manslogs,text="3",padx="40",pady="20")
btn4=Button(manslogs,text="4",padx="40",pady="20")
btn5=Button(manslogs,text="5",padx="40",pady="20")
btn6=Button(manslogs,text="6",padx="40",pady="20")
btn7=Button(manslogs,text="7",padx="40",pady="20")
btn8=Button(manslogs,text="8",padx="40",pady="20")
btn9=Button(manslogs,text="9",padx="40",pady="20")

btnsum=Button(manslogs,text="+",padx="40",pady="20")
btnsub=Button(manslogs,text="-",padx="40",pady="20")
btnmul=Button(manslogs,text="x",padx="40",pady="20")
btndiv=Button(manslogs,text=":",padx="40",pady="20")
btnclear=Button(manslogs,text="Del",padx="40",pady="20")
btnequals=Button(manslogs,text="=",padx="40",pady="20")

btn1.grid(row=1,column=1)
btn2.grid(row=1,column=2)
btn3.grid(row=1,column=3)
btndiv.grid(row=1,column=4)

btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=2,column=3)
btnmul.grid(row=2,column=4)

btn7.grid(row=3,column=1)
btn8.grid(row=3,column=2)
btn9.grid(row=3,column=3)
btnsum.grid(row=3,column=4)

btn0.grid(row=4,column=2)
btnclear.grid(row=4,column=1)
btnequals.grid(row=4,column=3)
btnsub.grid(row=4,column=4)



manslogs.mainloop()
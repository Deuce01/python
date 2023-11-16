# import tkinter
# from tkinter import *

# r= Tk()
# r.geometry('500x500')
# r.configure(background='aqua')
# r.title('area calculator')

# class Rectangle :
#     def __init(self,M):
#         self.text=StringVar()
#     LF=LabelFrame(M,text="calculations",bg="aqua", relief="solid")
#     LF.pack(expand=None,fill=BOTH,padx=50,pady=50)
#     self.L1=Label(LF,text="length",bg="aqua")
#     self.L1.grid(row=0,sticky=W)
#     self.L2=Label(LF,text="width",bg="aqua")
#     self.L2.grid(row=1,sticky=W)
#     self.L3=Label(LF,text="area",bg="aqua")
#     self.L3.grid(row=2,sticky=W)
#     self.E1 = Entry(LF)
#     self.E1.grid(row=0,column=1)
#     self.E2 = Entry(LF)
#     self.E2.grid(row=1,column=1)
#     self.E3 = Entry(LF,text="",textvariable=self.text)
#     self.E3.grid(row=2,column=1)
#     self.Bu = Button(LF, text="ok")
#     self.Bu.grid(row=0,column=1)
# root.mainloop()
import tkinter as tk

r = tk.Tk()
r.geometry('500x500')
r.configure(background='aqua')
r.title('Area Calculator')

class Rectangle:
    def __init__(self):
        self.text = tk.StringVar()
        LF = tk.LabelFrame(r, text="Calculations", bg="aqua", relief="solid")
        LF.pack(expand=None, fill=tk.BOTH, padx=50, pady=50)
        self.L1 = tk.Label(LF, text="Length", bg="aqua")
        self.L1.grid(row=0, sticky=tk.W)
        self.L2 = tk.Label(LF, text="Width", bg="aqua")
        self.L2.grid(row=1, sticky=tk.W)
        self.L3 = tk.Label(LF, text="Area", bg="aqua")
        self.L3.grid(row=2, sticky=tk.W)
        self.E1 = tk.Entry(LF)
        self.E1.grid(row=0, column=1)
        self.E2 = tk.Entry(LF)
        self.E2.grid(row=1, column=1)
        self.E3 = tk.Entry(LF, text="", textvariable=self.text)
        self.E3.grid(row=2, column=1)
        self.Bu = tk.Button(LF, text="Calculate", command=self.calculate_area)
        self.Bu.grid(row=3, columnspan=2)

    def calculate_area(self):
        length = float(self.E1.get())
        width = float(self.E2.get())
        area = length * width
        self.text.set(area)

app = Rectangle()
r.mainloop()

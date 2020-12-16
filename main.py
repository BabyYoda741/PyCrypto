from tkinter import *
from tkinter import ttk
from random import *
from tkinter import messagebox
import os




class pycrypto():
    def __init__(self,root):
        self.root=root
        self.root.title("PyCrypto")
        self.root.geometry("1240x600+0+0")
        abg="SteelBlue1"
        self.root.configure(bg=abg)
        bg_clr="DodgerBlue2"
        t_clr="black"
        bclr="DodgerBlue2"
        title=Label(self.root,text="PyCrypto",bg=bg_clr,fg=t_clr,bd=12,relief=GROOVE,font=("arial", 30 ,"bold"))
        title.pack(fill=X)

        self.text = StringVar()
        self.algo = ""
        self.result = StringVar()
        self.key = IntVar()

        F1 = LabelFrame(self.root, text="Input", font=("arial", 15, "bold"), bg=bg_clr, fg=t_clr, bd=7,relief=SUNKEN)
        F1.place(x=5, y=100, width=320, height=370)
        Label(F1, text="Enter text", font=("arial", 15, "bold"), bg=bg_clr, fg=t_clr).grid(row=0, column=0, padx=80, pady=20)
        Entry(F1, width=20, font="arial 15", bd=7, relief=SUNKEN,textvariable=self.text).grid(row=1, column=0, padx=10, pady=3)


        Label(self.root, text="Choose algorithm", font=("arial", 15, "bold"), bg=abg, fg=t_clr, padx=20, pady=10).place(x=370, y=190)
        algochoosen = ttk.Combobox(self.root,values=[' Caesar Cipher',' Transposition Cipher',' Rail Fence Cipher'], font=("arial", 15, "bold"),width=22, textvariable=self.algo)
        algochoosen.place(x=350,y= 250)
        algochoosen.current(0)


        Label(self.root, text="Enter key", font=("arial", 15, "bold"), bg=abg, fg=t_clr, padx=30, pady=10).place(x=370, y=300)
        Entry(self.root,width=20, font="arial 15",bd=7,textvariable=self.key,relief=SUNKEN).place(x=350, y=350)


        Button(self.root,width=15,text="Encrypt", font=("arial", 14, "bold"), bg=bclr, fg=t_clr, bd=7, command=self.encrypt).place(x=650, y=243 )
        Button(self.root, width=15,text="Decrypt",font=("arial", 14, "bold"), bg=bclr, fg=t_clr,bd=7).place(x=650,y=343)


        F2 = LabelFrame(self.root, text="Output", font=("arial", 15, "bold"), bg=bg_clr, fg=t_clr, bd=7,relief=SUNKEN)
        F2.place(x=890, y=100, width=320, height=370)

        Label(F2, text="Result", font=("arial", 15, "bold"), bg=bg_clr, fg=t_clr).grid(row=0, column=0, padx=80, pady=20)
        Entry(F2, width=20, font="arial 15", bd=7,textvariable=self.result,  relief=SUNKEN).grid(row=1, column=0, padx=40, pady=3)

        exit_button = Button(self.root, width=15,text="Exit",command = self.exit ,font=("arial", 14, "bold"), bg="DodgerBlue2", fg=t_clr,bd=7)
        exit_button.place(x=950, y=500)

        clear_button = Button(self.root, width=15, text="Clear",command= self.clear_all ,font=("arial", 14, "bold"), bg="DodgerBlue2",fg=t_clr, bd=7)
        clear_button.place(x=750, y=500)

    def encrypt(self):
        a=str(self.text.get())
        a = a.upper()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.res=str(self.result.get())

        for letter in a:
            if letter in alpha:
                letter_index = (alpha.find(letter) + int(self.key.get())) % len(alpha)
                self.res = self.res + str(alpha[letter_index])
            else:
                self.res = self.res + str(letter)

        self.result.set(self.res)



    def clear_all(self):
        op = messagebox.askyesno("clear", "Do you really want to clear all data?")
        if op > 0:
            self.text.set("")
            self.result.set("")
            self.key.set(0)

    def exit(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

if __name__=="__main__":
    root=Tk()
    pycrypto(root)
    root.mainloop()

from tkinter import *
from random import *
from tkinter import messagebox
import os
class pycrypto():
    def __init__(self,root):
        self.root=root
        self.root.title("PyCrypto")
        self.root.geometry("1360x7200+0+0")
        bg_clr="navy blue"
        title=Label(self.root,text="PyCrypto Software",bg=bg_clr,fg="gold",bd=12,relief=GROOVE,font=("times new roman", 30 ,"bold"))
        title.pack(fill=X)

        # ************** variables *****************
        self.plain_text= StringVar()
        self.encrypted_text= StringVar()
        self.result= StringVar()

        F1 = LabelFrame(self.root, text="Encryption", font=("times new roman", 15, "bold"), bg=bg_clr, fg="gold", bd=7,
                        relief=SUNKEN)
        F1.place(x=5, y=100, width=365, height=370)

        F2 = LabelFrame(self.root, text="Decryption", font=("times new roman", 15, "bold"), bg=bg_clr, fg="gold", bd=7,
                        relief=SUNKEN)
        F2.place(x=400, y=100, width=365, height=370)

        F3 = LabelFrame(self.root, text="Encryption", font=("times new roman", 15, "bold"), bg=bg_clr, fg="gold", bd=7,
                        relief=SUNKEN)
        F3.place(x=800, y=100, width=365, height=370)

        F4 = LabelFrame(self.root, text="Working area", font=("times new roman", 15, "bold"), bg="cyan", fg="red",
                        bd=7, relief=SUNKEN)
        F4.place(x=0, y=600, relwidth=1, height=100)

        Label(F4, text="Thank You!", font=("times new roman", 40, "bold"), bg="cyan", fg="red", padx=550,
              pady=3).grid(row=0, column=0)




if __name__=="__main__":
    root=Tk()
    pycrypto(root)
    root.mainloop()

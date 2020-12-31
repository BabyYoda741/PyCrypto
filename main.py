from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyperclip
import math

class Pycrypto():
    def __init__(self, root):
        self.root = root
        self.root.title("PyCrypto 1.0")
        self.root.geometry("1230x600+0+0")
        abg1 = "navajo white"
        abg="SkyBlue"
        self.root.configure(bg=abg1)
        bg_clr = "Cyan4"
        t_clr = "black"
        bclr = "Orange"
        title = Label(self.root, text="PyCrypto", bg="DeepSkyBlue1", fg=t_clr, bd=12, relief=GROOVE, font=("arial", 30))
        title.pack(fill=X)
        self.text = StringVar()
        self.algo = StringVar()
        self.result = StringVar()
        self.key = IntVar()
        F1 = LabelFrame(self.root, text="Working Area", font=("arial", 15, "bold"), bg=abg, fg=t_clr, bd=7, relief=SUNKEN)
        F1.place(x=25, y=100, width=1190, height=380)
        Label(F1, text="Input Text", font=("arial", 15, "bold"), bg=abg, fg=t_clr).place(x=30, y=25)
        Entry(F1, width=100, font="arial 15", bd=7, relief=SUNKEN,textvariable=self.text).place(x=30, y=75)
        Label(F1, text="Choose Algorithm", font=("arial", 15, "bold"), bg=abg, fg=t_clr, padx=20, pady=10).place(x=100, y=155)
        algochoosen = ttk.Combobox(F1,values=['Caesar Cipher','ROT13 Cipher','Transposition Cipher'], font=("arial", 13),width=22, textvariable=self.algo)
        algochoosen.place(x=300,y= 165)
        algochoosen.current(0)
        algochoosen.bind("<<ComboboxSelected>>", self.rot)
        Label(F1, text="Enter Key", font=("arial", 15, "bold"), bg=abg, fg=t_clr, padx=30, pady=10).place(x=600, y=155)
        self.env = Entry(F1,width=20, font="arial 15",bd=7,textvariable=self.key,relief=SUNKEN)
        self.env.place(x=730, y=160)
        Button(self.root,width=15,text="Encrypt", font=("arial", 14, "bold"), bg=bclr, fg=t_clr, bd=7, command=self.encrypt).place(x=70, y=490 )
        Button(self.root, width=15,text="Decrypt",font=("arial", 14, "bold"), bg=bclr, fg=t_clr,bd=7, command=self.decrypt).place(x=290,y=490)
        Button(self.root, width=15,text="Swap Output",font=("arial", 14, "bold"), bg=bclr, fg=t_clr,bd=7, command=self.swap).place(x=510,y=490)
        Label(F1, text="Output Text", font=("arial", 15, "bold"), bg=abg, fg=t_clr).place(x=30, y=235)
        Entry(F1, width=100, font="arial 15", bd=7,textvariable=self.result,  relief=SUNKEN).place(x=30, y=285)
        exit_button = Button(self.root, width=15,text="Exit",command = self.exit ,font=("arial", 14, "bold"), bg=bclr, fg=t_clr,bd=7)
        exit_button.place(x=950, y=490)
        clear_button = Button(self.root, width=15, text="Clear",command= self.clear_all ,font=("arial", 14, "bold"), bg=bclr,fg=t_clr, bd=7)
        clear_button.place(x=730, y=490)

    def rot(self,event):
        alg = event.widget.get()
        if alg == 'ROT13 Cipher':
            self.key.set(13)
            self.env.configure(state=DISABLED)
        else:
            self.env.configure(state=NORMAL)

    def encrypt(self):
        self.result.set('')
        if str(self.algo.get()) == 'Transposition Cipher':
            a = str(self.text.get())
            ciphertext = [''] * self.key.get()
            for col in range(self.key.get()):
                position = col
                while position < len(a):
                    ciphertext[col] += a[position]
                    position += self.key.get()
            ciphertext = ''.join(ciphertext)
            self.result.set(ciphertext)
            pyperclip.copy(ciphertext)
        elif str(self.algo.get()) == 'Caesar Cipher' or 'ROT13 Cipher':
            if str(self.algo.get()) == 'ROT13 Cipher':
                self.key.set(13)
            a = str(self.text.get())
            alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphas = "abcdefghijklmnopqrstuvwxyz"
            self.res = str(self.result.get())
            for letter in a:
                if letter in alpha:
                    letter_index = (alpha.find(letter) + int(self.key.get())) % len(alpha)
                    self.res = self.res + str(alpha[letter_index])
                elif letter in alphas:
                    letter_index = (alphas.find(letter) + int(self.key.get())) % len(alpha)
                    self.res = self.res + str(alphas[letter_index])
                else:
                    self.res = self.res + str(letter)
            self.result.set(self.res)
            pyperclip.copy(self.res)
        if str(self.text.get()) == '':
            messagebox.showerror("Error", "Input text to encrypt")

    def decrypt(self):
        self.result.set('')
        if str(self.algo.get()) == 'Transposition Cipher' and self.key.get() != 0:
            a = str(self.text.get())
            numOfColumns = math.ceil(len(a) / self.key.get())
            numOfRows = self.key.get()
            numOfShadedBoxes = (numOfColumns * numOfRows) - len(a)
            plaintext = [''] * numOfColumns
            col = 0
            row = 0
            for symbol in a:
                plaintext[col] += symbol
                col += 1
                if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                    col = 0
                    row += 1
            plaintext = ''.join(plaintext)
            self.result.set(plaintext)
            pyperclip.copy(plaintext)
        elif str(self.algo.get()) == 'Caesar Cipher' or 'ROT13 Cipher':
            if str(self.algo.get()) == 'ROT13 Cipher':
                self.key.set(13)
            a = str(self.text.get())
            alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphas = "abcdefghijklmnopqrstuvwxyz"
            self.res = str(self.result.get())
            for letter in a:
                if letter in alpha:
                    letter_index = (alpha.find(letter) - int(self.key.get())) % len(alpha)
                    self.res = self.res + str(alpha[letter_index])
                elif letter in alphas:
                    letter_index = (alphas.find(letter) - int(self.key.get())) % len(alpha)
                    self.res = self.res + str(alphas[letter_index])
                else:
                    self.res = self.res + str(letter)
            self.result.set(self.res)
            pyperclip.copy(self.res)
        if str(self.text.get()) == '':
            messagebox.showerror("Error", "Input text to Decrypt")

    def swap(self):
        if str(self.result.get()) == '':
            messagebox.showerror("Error","Output is empty")
        else:
            self.text.set(str(self.result.get()))
            self.result.set('')

    def clear_all(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear all data?")
        if op > 0:
            self.text.set("")
            self.result.set("")
            self.key.set(0)

    def exit(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    Pycrypto(root)
    root.mainloop()

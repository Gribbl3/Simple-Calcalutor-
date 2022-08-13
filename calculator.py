from __future__ import division
from tkinter import *
from tkinter import messagebox


def main():
    wn = Tk()
    wn.title("Simple Calculator")

    user = Entry(wn, width=35, borderwidth=5)

    user.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def btn_click(n):
        user.insert(END, n)     


    def clr():
        user.delete(0, END)


    def eql():
        #converts current entry as string, uses eval() to calculate result
        #try-except for syntax errors 
        try:
            res = str(eval(user.get()))
            user.delete(0, END)
            user.insert(END,res)
        except Exception as e:
            messagebox.showerror("ERROR","INVALID SYNTAX")
            user.delete(0, END)

     
    #creating instance of buttons
    button_1 = Button(wn, text="1", padx=40, pady=20, command=lambda: btn_click(1))
    button_2 = Button(wn, text="2", padx=40, pady=20, command=lambda: btn_click(2))
    button_3 = Button(wn, text="3", padx=40, pady=20, command=lambda: btn_click(3))
    button_4 = Button(wn, text="4", padx=40, pady=20, command=lambda: btn_click(4))
    button_5 = Button(wn, text="5", padx=40, pady=20, command=lambda: btn_click(5))
    button_6 = Button(wn, text="6", padx=40, pady=20, command=lambda: btn_click(6))
    button_7 = Button(wn, text="7", padx=40, pady=20, command=lambda: btn_click(7))
    button_8 = Button(wn, text="8", padx=40, pady=20, command=lambda: btn_click(8))
    button_9 = Button(wn, text="9", padx=40, pady=20, command=lambda: btn_click(9))
    button_0 = Button(wn, text="0", padx=40, pady=20, command=lambda: btn_click(0))
    btn_clr = Button(wn, text="Clear", padx=79, pady=20, command=clr)
    btn_add = Button(wn, text="+", padx=40, pady=20, command=lambda: btn_click("+"))
    btn_sub = Button(wn, text="-", padx=40, pady=20, command=lambda: btn_click("-"))
    btn_mul = Button(wn, text="*", padx=40, pady=20, command=lambda: btn_click("*"))
    btn_div = Button(wn, text="÷", padx=40, pady=20, command=lambda: btn_click("/"))
    btn_eql = Button(wn, text="=", padx=40, pady=20, command=eql)

    #button places
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_0.grid(row=4, column=0)
    btn_clr.grid(row=4, column=1, columnspan=2)
    btn_add.grid(row=5, column=0)
    btn_sub.grid(row=5, column=1)
    btn_mul.grid(row=6, column=0)
    btn_div.grid(row=6, column=1)
    btn_eql .grid(row=6, column=2)

    wn.mainloop()


if __name__ == "__main__":
    main()

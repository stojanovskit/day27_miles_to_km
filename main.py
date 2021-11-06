from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=150, height=150)
window.config(padx=20, pady=20)
text = Entry(width=7)

text.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)
is_equal = Label(text="Is equal to")
is_equal.grid(column=0, row=2)
result = Label(text=0)
result.grid(column=1, row=2)
km = Label(text="Km")
km.grid(column=2, row=2)


def resu():
    result["text"] = float(text.get()) * 1.609


calc = Button(text="Calculate", command = resu)
calc.grid(column=1, row=3)
window.mainloop()

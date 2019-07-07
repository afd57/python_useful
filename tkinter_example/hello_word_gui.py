import tkinter as tk
from tkinter import messagebox


def say_hello(name='', surname=''):
    print(name, surname)

    messagebox.showinfo("Title", f"Hello {name.get()} {surname.get()}")
    # name.get() -> textbox daki degeri donduruyor


root = tk.Tk()
root.geometry('400x200')
# formun buyuklugu

root.title('Hello World')
# Formun basligi


name = tk.StringVar()
surname = tk.StringVar()

labelNum1 = tk.Label(root, text="Name", anchor="w").grid(row=1, column=0)

labelNum2 = tk.Label(root, text="Surname", anchor="e").grid(row=2, column=0)
# anchor saga ve sola yasmlamak icin

entry_name = tk.Entry(root, textvariable=name).grid(row=1, column=2)
# textVariable'a yazilan texti hangi degere dolduracaz onu yaziyoruz.


entry_surname = tk.Entry(root, textvariable=surname).grid(row=2, column=2)

buttonCal = tk.Button(root, text="Call Hello", command=lambda: say_hello(
    name, surname)).grid(row=3, column=0)
# command'a cagirmak istedigimiz fonksiyonu yaziyoruz


root.mainloop()

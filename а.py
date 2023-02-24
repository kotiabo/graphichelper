import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk


def show():
    label["text"] = entry.get()


root = Tk()
root.title("Калькулялтор")
root.geometry("250x200")

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Нажми", command=show)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()

plt.figure(figsize=(17, 10))

x = 2
y = 5

plt.plot(x, y)
plt.plot([-80,100],[0,0], color='b')
plt.plot([0,0], [-100,100], color='b')

plt.text(-90, 120, entry,
         bbox={"fill": False,
               "linestyle": "dotted",
               "linewidth": 2.5})
plt.show()

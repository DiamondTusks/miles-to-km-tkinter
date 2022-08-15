from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(pady=20, padx=20)


def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    answer.config(text=f"{km}")

# Entry
input = Entry(width=7)
input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)







window.mainloop()

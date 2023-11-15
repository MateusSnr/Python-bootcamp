import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
label = tkinter.Label(text="Label", font=("Times New Roman", 24, "bold"))
label.grid(column=0, row=0)
label["text"] = "New test"
label.config(text="New Text", padx=10, pady=5)

#Button

def button_clicked():
    label.config(text = input.get())
    print("I got clicked")

button = tkinter.Button(text="Click here", command=button_clicked)
button.place(x=0, y=0)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New button")
new_button.grid(column=2, row=0)

#Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
print(input.get())


window.mainloop()

#Unlimited Arguments
def add(*args):
    for n in args:
        print(n)
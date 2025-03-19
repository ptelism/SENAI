import tkinter as tk

result_calculated = False

def click_button(value):
    global result_calculated
    if result_calculated:
        entry.delete(0, tk.END)
        result_calculated = False
    entry.insert(tk.END, value)

def calculate():
    global result_calculated
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        result_calculated = True
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        result_calculated = False

def clear():
    global result_calculated
    entry.delete(0, tk.END)
    result_calculated = False

window = tk.Tk()
window.title("Calculator : ptelism")

entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief='groove')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == 'C':
        b = tk.Button(window, text=button, width=5, height=2, command=clear)
    elif button == '=':
        b = tk.Button(window, text=button, width=5, height=2, command=calculate)
    else:
        b = tk.Button(window, text=button, width=5, height=2, command=lambda v=button: click_button(v))

    b.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()

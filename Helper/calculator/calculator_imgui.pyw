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
        result_calculated = True

def clear():
    global result_calculated
    entry.delete(0, tk.END)
    result_calculated = False

window = tk.Tk()
window.title("Calculator : ptelism")
window.configure(bg='black')

entry = tk.Entry(window, font=('Arial', 24), borderwidth=2, relief='groove', bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

for i in range(4):
    window.columnconfigure(i, weight=1)

window.rowconfigure(0, weight=1)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'CL', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    if button == 'CL':
        b = tk.Button(window, text=button, command=clear, height=2, bg='black', fg='white')
    elif button == '=':
        b = tk.Button(window, text=button, command=calculate, height=2, bg='black', fg='white')
    else:
        b = tk.Button(window, text=button, command=lambda v=button: click_button(v), height=2, bg='black', fg='white')

    b.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

for i in range(1, 5):
    window.rowconfigure(i, weight=1) 

window.mainloop()

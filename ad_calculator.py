# File Name: ad_calculator.py

import tkinter as tk
from tkinter import messagebox
import math

# Create main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x550")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# String Variable
expression = ""

# Entry Display
display = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.FLAT,
                   bg="#2e2e3e", fg="white", justify="right")
display.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=20)

# Button Click Function
def click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

# Clear Function
def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

# Equal Function
def calculate():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = str(result)
    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear()

# Square Root
def square_root():
    global expression
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = str(result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# Cube Root
def cube_root():
    global expression
    try:
        num = float(display.get())
        result = num ** (1/3)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = str(result)
    except:
        messagebox.showerror("Error", "Invalid Input")

# Button Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

# Button Design
btn_style = {
    "font": ("Arial", 16),
    "bd": 0,
    "width": 5,
    "height": 2,
    "bg": "#3e3e5e",
    "fg": "white",
    "activebackground": "#5757a1"
}

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    tk.Button(frame, text=text, command=lambda t=text: click(t), **btn_style)\
        .grid(row=row, column=col, padx=8, pady=8)

# Special Buttons
tk.Button(frame, text="C", command=clear,
          font=("Arial", 16), bg="#ff4d4d", fg="white",
          width=5, height=2).grid(row=5, column=0, padx=8, pady=8)

tk.Button(frame, text="√", command=square_root,
          font=("Arial", 16), bg="#4da6ff", fg="white",
          width=5, height=2).grid(row=5, column=1, padx=8, pady=8)

tk.Button(frame, text="∛", command=cube_root,
          font=("Arial", 16), bg="#4da6ff", fg="white",
          width=5, height=2).grid(row=5, column=2, padx=8, pady=8)

tk.Button(frame, text="^", command=lambda: click("**"),
          font=("Arial", 16), bg="#ffa64d", fg="white",
          width=5, height=2).grid(row=5, column=3, padx=8, pady=8)

tk.Button(frame, text="=", command=calculate,
          font=("Arial", 18), bg="#33cc33", fg="white",
          width=22, height=2).grid(row=6, column=0, columnspan=4, padx=8, pady=10)

root.mainloop()

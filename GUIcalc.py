import tkinter as tk
from tkinter import messagebox

# --- Core Math Functions ---
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    if y == 0:
        return "Error (Div by 0)"
    return x / y

# --- GUI Logic ---
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        else:
            messagebox.showerror("Error", "Please select an operation.")
            return
            
        label_result.config(text=f"Result: {result}", fg="#00FF00" if type(result) != str else "#FF0000")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# --- Setting up the Main Window ---
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("350x400")
root.configure(bg="#212121")  # Clean dark mode look

# UI Elements
tk.Label(root, text="Simple GUI Calculator", font=("Arial", 16, "bold"), bg="#212121", fg="white").pack(pady=10)

# Input 1
tk.Label(root, text="Enter First Number:", bg="#212121", fg="white").pack()
entry_num1 = tk.Entry(root, font=("Arial", 12), justify="center")
entry_num1.pack(pady=5)

# Input 2
tk.Label(root, text="Enter Second Number:", bg="#212121", fg="white").pack()
entry_num2 = tk.Entry(root, font=("Arial", 12), justify="center")
entry_num2.pack(pady=5)

# Menu Dropdown (Operation Selection)
tk.Label(root, text="Select Operation:", bg="#212121", fg="white").pack(pady=5)
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0]) # Default value
menu = tk.OptionMenu(root, operation_var, *operations)
menu.config(font=("Arial", 10), bg="#C25050", fg="white")
menu.pack(pady=5)

# Calculate Button
btn_calc = tk.Button(root, text="Calculate", command=calculate, font=("Arial", 12, "bold"), bg="#00E676", fg="black")
btn_calc.pack(pady=15)

# Result Label
label_result = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#212121", fg="white")
label_result.pack(pady=10)

# Start the application loop
root.mainloop()
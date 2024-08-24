import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Conversion Functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Main Conversion Function
def convert_temperature():
    try:
        value = float(entry_temp.get())
        unit = selected_unit.get()
        
        if unit == 'C':
            fahrenheit = celsius_to_fahrenheit(value)
            kelvin = celsius_to_kelvin(value)
            result.set(f"{value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K.")
        elif unit == 'F':
            celsius = fahrenheit_to_celsius(value)
            kelvin = fahrenheit_to_kelvin(value)
            result.set(f"{value}°F is {celsius:.2f}°C and {kelvin:.2f}K.")
        elif unit == 'K':
            celsius = kelvin_to_celsius(value)
            fahrenheit = kelvin_to_fahrenheit(value)
            result.set(f"{value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F.")
        else:
            messagebox.showerror("Invalid Unit", "Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric temperature value.")

# Set up the GUI window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("570x350")
root.configure(bg="#e0f7fa")

# Styles
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), background="#eaeaea", foreground="black")  # Dark gray text
style.configure('TButton', font=('Arial', 12), background="#0288d1", foreground="black", padding=6, relief="flat")  # Blue button with padding and flat relief
style.configure('TRadiobutton', font=('Arial', 12), background="#ffd337", foreground="#333333")  # Matching background for radio buttons with dark gray text

# Temperature Entry
ttk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_temp = ttk.Entry(root, font=("Arial", 12))
entry_temp.grid(row=0, column=1, padx=10, pady=10)

# Unit Selection
selected_unit = tk.StringVar(value="C")
ttk.Label(root, text="Select Unit:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
ttk.Radiobutton(root, text="Celsius", variable=selected_unit, value="C").grid(row=1, column=1, padx=5, pady=5, sticky="w")
ttk.Radiobutton(root, text="Fahrenheit", variable=selected_unit, value="F").grid(row=1, column=2, padx=5, pady=5, sticky="w")
ttk.Radiobutton(root, text="Kelvin", variable=selected_unit, value="K").grid(row=1, column=3, padx=5, pady=5, sticky="w")

# Convert Button
convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Result Display
result = tk.StringVar()
result_label = ttk.Label(root, textvariable=result, wraplength=300)
result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# Run the application
root.mainloop()

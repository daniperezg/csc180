import tkinter as tk
from tkinter import ttk

def calculate_price():
    try:
        model = car_model.get()
        age = int(age_entry.get())
        mileage = int(mileage_entry.get())

        # Base prices depending on model
        base_prices = {
            "BMW": 50000,
            "Audi": 45000,
            "Mercedes": 55000
        }

        base_price = base_prices.get(model, 30000)

        # Formula: price decreases with age and mileage
        price = base_price - (age * 1000) - (mileage * 0.05)

        if price < 1000:
            price = 1000  # minimum price

        result_label.config(text=f"Estimated Price: ${price:,.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers for age and mileage.")

def reset_fields():
    car_model.set("")
    age_entry.delete(0, tk.END)
    mileage_entry.delete(0, tk.END)
    result_label.config(text="Estimated Price: ")

# GUI window
root = tk.Tk()
root.title("Car Price Estimator")
root.geometry("400x250")

# Car Model
tk.Label(root, text="Car Model:").pack()
car_model = ttk.Combobox(root, values=["BMW", "Audi", "Mercedes"])
car_model.pack()

# Age
tk.Label(root, text="Age (years):").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Mileage
tk.Label(root, text="Mileage (km):").pack()
mileage_entry = tk.Entry(root)
mileage_entry.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

calc_button = tk.Button(button_frame, text="Calculate Price", command=calculate_price)
calc_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_fields)
reset_button.grid(row=0, column=1, padx=5)

# Result Label
result_label = tk.Label(root, text="Estimated Price: ")
result_label.pack(pady=10)

root.mainloop()
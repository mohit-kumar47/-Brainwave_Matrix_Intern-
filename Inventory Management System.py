import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store inventory data
data_file = "inventory.json"

# Load existing data or create a new file if it doesn't exist
if not os.path.exists(data_file):
    with open(data_file, "w") as f:
        json.dump({}, f)

# Function to load inventory data
def load_data():
    with open(data_file, "r") as f:
        return json.load(f)

# Function to save inventory data
def save_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)

# User Authentication
def authenticate_user(username, password):
    users = {"admin": "admin123", "user": "user123"}
    return users.get(username) == password

# Main GUI Application
def main_app():
    def add_product():
        product_id = entry_product_id.get()
        name = entry_name.get()
        quantity = entry_quantity.get()
        price = entry_price.get()

        if not product_id or not name or not quantity.isdigit() or not price.isdigit():
            messagebox.showerror("Error", "Please enter valid product details.")
            return

        inventory = load_data()

        if product_id in inventory:
            messagebox.showerror("Error", "Product ID already exists.")
        else:
            inventory[product_id] = {
                "name": name,
                "quantity": int(quantity),
                "price": float(price)
            }
            save_data(inventory)
            messagebox.showinfo("Success", "Product added successfully.")
            refresh_inventory()

    def edit_product():
        product_id = entry_product_id.get()

        if not product_id:
            messagebox.showerror("Error", "Please enter a Product ID to edit.")
            return

        inventory = load_data()

        if product_id not in inventory:
            messagebox.showerror("Error", "Product ID does not exist.")
        else:
            name = entry_name.get()
            quantity = entry_quantity.get()
            price = entry_price.get()

            if name:
                inventory[product_id]["name"] = name
            if quantity.isdigit():
                inventory[product_id]["quantity"] = int(quantity)
            if price.isdigit():
                inventory[product_id]["price"] = float(price)

            save_data(inventory)
            messagebox.showinfo("Success", "Product updated successfully.")
            refresh_inventory()

    def delete_product():
        product_id = entry_product_id.get()

        if not product_id:
            messagebox.showerror("Error", "Please enter a Product ID to delete.")
            return

        inventory = load_data()

        if product_id in inventory:
            del inventory[product_id]
            save_data(inventory)
            messagebox.showinfo("Success", "Product deleted successfully.")
            refresh_inventory()
        else:
            messagebox.showerror("Error", "Product ID does not exist.")

    def refresh_inventory():
        inventory = load_data()
        text_inventory.delete(1.0, tk.END)
        for product_id, details in inventory.items():
            text_inventory.insert(tk.END, f"ID: {product_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}\n")

    def generate_report():
        inventory = load_data()
        low_stock = [
            f"ID: {product_id}, Name: {details['name']}, Quantity: {details['quantity']}"
            for product_id, details in inventory.items() if details['quantity'] < 5
        ]
        if low_stock:
            messagebox.showinfo("Low Stock Alert", "\n".join(low_stock))
        else:
            messagebox.showinfo("Low Stock Alert", "All products are sufficiently stocked.")

    root = tk.Tk()
    root.title("Inventory Management System")

    # Labels and Entry fields
    tk.Label(root, text="Product ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_product_id = tk.Entry(root)
    entry_product_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Quantity:").grid(row=2, column=0, padx=10, pady=5)
    entry_quantity = tk.Entry(root)
    entry_quantity.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Price:").grid(row=3, column=0, padx=10, pady=5)
    entry_price = tk.Entry(root)
    entry_price.grid(row=3, column=1, padx=10, pady=5)

    # Buttons
    tk.Button(root, text="Add Product", command=add_product).grid(row=4, column=0, padx=10, pady=10)
    tk.Button(root, text="Edit Product", command=edit_product).grid(row=4, column=1, padx=10, pady=10)
    tk.Button(root, text="Delete Product", command=delete_product).grid(row=5, column=0, padx=10, pady=10)
    tk.Button(root, text="Generate Report", command=generate_report).grid(row=5, column=1, padx=10, pady=10)

    # Inventory display
    text_inventory = tk.Text(root, height=15, width=50)
    text_inventory.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    refresh_inventory()
    root.mainloop()

# Login Window
def login():
    def validate_login():
        username = entry_username.get()
        password = entry_password.get()

        if authenticate_user(username, password):
            login_window.destroy()
            main_app()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    entry_username = tk.Entry(login_window)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    entry_password = tk.Entry(login_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(login_window, text="Login", command=validate_login).grid(row=2, column=0, columnspan=2, pady=10)

    login_window.mainloop()

# Start the application
if __name__ == "__main__":
    login()

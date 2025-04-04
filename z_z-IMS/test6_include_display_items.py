import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import pandas as pd

# Database setup
def connect_db():
    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="inventory_db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            quantity INT NOT NULL,
            price FLOAT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

connect_db()

# GUI Setup
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("800x500")
        
        # Split the window into two frames
        self.left_frame = tk.Frame(root, width=400, height=500, padx=10, pady=10)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.right_frame = tk.Frame(root, width=400, height=500, padx=10, pady=10)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # UI Elements (Left Frame)
        self.name_var = tk.StringVar()
        self.quantity_var = tk.IntVar()
        self.price_var = tk.DoubleVar()
        
        ttk.Label(self.left_frame, text="Product Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = ttk.Entry(self.left_frame, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(self.left_frame, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
        self.quantity_entry = ttk.Entry(self.left_frame, textvariable=self.quantity_var)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.left_frame, text="Price:").grid(row=2, column=0, padx=10, pady=5)
        self.price_entry = ttk.Entry(self.left_frame, textvariable=self.price_var)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.add_button = ttk.Button(self.left_frame, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, padx=10, pady=5)
        
        self.update_button = ttk.Button(self.left_frame, text="Update Item", command=self.update_item)
        self.update_button.grid(row=3, column=1, padx=10, pady=5)
        
        self.delete_button = ttk.Button(self.left_frame, text="Delete Item", command=self.delete_item)
        self.delete_button.grid(row=4, column=0, padx=10, pady=5)
        
        self.export_button = ttk.Button(self.left_frame, text="Export to Excel", command=self.export_to_excel)
        self.export_button.grid(row=4, column=1, padx=10, pady=5)
        
        self.display_button = ttk.Button(self.left_frame, text="Display Existing Items", command=self.load_items)
        self.display_button.grid(row=5, column=0, padx=10, pady=5)
        
        self.clear_button = ttk.Button(self.left_frame, text="Clear Fields", command=self.clear_fields)
        self.clear_button.grid(row=5, column=1, padx=10, pady=5)
        
        self.login_button = ttk.Button(self.left_frame, text="Login", command=self.login)
        self.login_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        
        # Inventory List (Right Frame)
        self.tree = ttk.Treeview(self.right_frame, columns=("ID", "Name", "Quantity", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.load_items()

    def execute_db(self, query, params=()):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="inventory_db")
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()

    def load_items(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="inventory_db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        conn.close()
        
        for row in rows:
            self.tree.insert("", "end", values=row)

    def add_item(self):
        name = self.name_var.get()
        quantity = self.quantity_var.get()
        price = self.price_var.get()
        
        if name and quantity > 0 and price > 0:
            self.execute_db("INSERT INTO inventory (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
            self.load_items()
            messagebox.showinfo("Success", "Item added successfully!")
        else:
            messagebox.showerror("Error", "Invalid input!")
    
    def update_item(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select an item to update")
            return
        
        item = self.tree.item(selected_item)['values']
        item_id = item[0]
        name = self.name_var.get()
        quantity = self.quantity_var.get()
        price = self.price_var.get()
        
        if name and quantity > 0 and price > 0:
            self.execute_db("UPDATE inventory SET name=%s, quantity=%s, price=%s WHERE id=%s", (name, quantity, price, item_id))
            self.load_items()
            messagebox.showinfo("Success", "Item updated successfully!")
        else:
            messagebox.showerror("Error", "Invalid input!")

    def delete_item(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select an item to delete")
            return
        
        item = self.tree.item(selected_item)['values']
        item_id = item[0]
        self.execute_db("DELETE FROM inventory WHERE id=%s", (item_id,))
        self.load_items()
        messagebox.showinfo("Success", "Item deleted successfully!")
    
    def export_to_excel(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="inventory_db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        conn.close()
        
        df = pd.DataFrame(rows, columns=["ID", "Name", "Quantity", "Price"])
        df.to_excel("inventory.xlsx", index=False)
        messagebox.showinfo("Success", "Data exported to Excel successfully!")

    def clear_fields(self):
        self.name_var.set("")
        self.quantity_var.set(0)
        self.price_var.set(0.0)
    
    def login(self):
        messagebox.showinfo("Login", "Login feature not implemented yet!")

    
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

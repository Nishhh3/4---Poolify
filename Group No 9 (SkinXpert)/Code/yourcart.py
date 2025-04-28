import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class YourCart:
    def __init__(self, root):
        # Database Connection
        self.connection = pymysql.connect(
            host='localhost', 
            user='root', 
            password='123456', 
            database='skinxpert'
        )
        self.cursor = self.connection.cursor()

        # Cart Window Setup
        self.root = root
        self.cart_window = tk.Toplevel(root)
        self.cart_window.title("Your Cart")
        self.cart_window.geometry("800x500")
        self.cart_window.configure(bg="#f5f5f5")

        # Cart Items Storage
        self.cart_items = []

        # Setup UI
        self.create_ui()

    def create_ui(self):
        """Create the entire cart user interface"""
        # Title Frame
        title_frame = tk.Frame(self.cart_window, bg="#d8e6d1", height=50)
        title_frame.pack(fill=tk.X, padx=10, pady=5)
        title_label = tk.Label(title_frame, text="Your Cart", 
                               font=("Helvetica", 16, "bold"), 
                               bg="#d8e6d1")
        title_label.pack(pady=10)

        # Treeview Setup
        self.setup_treeview()

        # Bottom Frame for Total and Buttons
        self.create_bottom_frame()

    def setup_treeview(self):
        """Configure the Treeview for displaying cart items"""
        # Treeview Frame
        tree_frame = tk.Frame(self.cart_window, bg="#f5f5f5")
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Custom Style
        style = ttk.Style()
        style.configure("Custom.Treeview", 
                        background="#ffffff", 
                        foreground="black", 
                        rowheight=40,
                        fieldbackground="#f5f5f5")
        style.configure("Custom.Treeview.Heading", 
                        font=('Arial', 12, 'bold'), 
                        background="#d8e6d1")
        style.map('Custom.Treeview', 
                  background=[('selected', '#b3d9b1')])

        # Create Treeview
        self.cart_tree = ttk.Treeview(tree_frame, 
                                      columns=("Product", "Price", "Quantity", "Total"), 
                                      show="headings", 
                                      style="Custom.Treeview")
        
        # Define headings
        self.cart_tree.heading("Product", text="Product Name")
        self.cart_tree.heading("Price", text="Price")
        self.cart_tree.heading("Quantity", text="Quantity")
        self.cart_tree.heading("Total", text="Total")
        
        # Set column widths
        self.cart_tree.column("Product", width=250, anchor="center")
        self.cart_tree.column("Price", width=100, anchor="center")
        self.cart_tree.column("Quantity", width=100, anchor="center")
        self.cart_tree.column("Total", width=100, anchor="center")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.cart_tree.yview)
        self.cart_tree.configure(yscroll=scrollbar.set)
        
        # Pack Treeview and Scrollbar
        self.cart_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind double-click to quantity adjustment
        self.cart_tree.bind('<Double-1>', self.adjust_quantity)

    def create_bottom_frame(self):
        """Create bottom frame with total and action buttons"""
        # Bottom Frame for Total and Buttons
        bottom_frame = tk.Frame(self.cart_window, bg="#d8e6d1", height=70)
        bottom_frame.pack(fill=tk.X, padx=10, pady=5)

        # Total Label
        self.total_label = tk.Label(bottom_frame, 
                                    text="Total: ₹0", 
                                    font=("Helvetica", 14, "bold"), 
                                    bg="#d8e6d1", 
                                    fg="green")
        self.total_label.pack(side="left", padx=20)

        # Buttons Frame
        btn_frame = tk.Frame(bottom_frame, bg="#d8e6d1")
        btn_frame.pack(side="right", padx=20)

        # Checkout Button
        checkout_btn = ttk.Button(btn_frame, text="Checkout", command=self.checkout)
        checkout_btn.pack(side="right", padx=5)

        # Clear Cart Button
        clear_btn = ttk.Button(btn_frame, text="Clear Cart", command=self.clear_cart)
        clear_btn.pack(side="right", padx=5)

    def add_to_cart(self, product_name, price):
        """Add a product to the cart"""
        # Check if product exists in cart
        for item in self.cart_items:
            if item['name'] == product_name:
                item['quantity'] += 1
                item['total'] = item['quantity'] * price
                self.update_cart_view()
                return

        # Add new item if not in cart
        cart_item = {
            'name': product_name, 
            'price': price, 
            'quantity': 1, 
            'total': price
        }
        self.cart_items.append(cart_item)
        self.update_cart_view()
        messagebox.showinfo("Cart", f"{product_name} added to cart!")

    def update_cart_view(self):
        """Update the Treeview with current cart items"""
        # Clear existing items
        for i in self.cart_tree.get_children():
            self.cart_tree.delete(i)
        
        # Add items to Treeview
        for item in self.cart_items:
            self.cart_tree.insert("", "end", 
                                  values=(item['name'], 
                                          f"₹{item['price']}", 
                                          item['quantity'], 
                                          f"₹{item['total']}"))
        
        # Update total
        total = sum(item['total'] for item in self.cart_items)
        self.total_label.config(text=f"Total: ₹{total}")

    def adjust_quantity(self, event):
        """Allow quantity adjustment by double-clicking"""
        # Get selected item
        selected_item = self.cart_tree.selection()
        if not selected_item:
            return

        # Get item details
        item_values = self.cart_tree.item(selected_item[0])['values']
        product_name = item_values[0]
        current_price = float(item_values[1].replace('₹', ''))
        current_quantity = item_values[2]

        # Popup for quantity
        quantity_window = tk.Toplevel(self.cart_window)
        quantity_window.title("Adjust Quantity")
        quantity_window.geometry("300x150")

        # Quantity Label and Entry
        tk.Label(quantity_window, text=f"Current Quantity for {product_name}:").pack(pady=10)
        quantity_var = tk.IntVar(value=current_quantity)
        quantity_entry = tk.Entry(quantity_window, textvariable=quantity_var)
        quantity_entry.pack(pady=10)

        def update_quantity():
            new_quantity = quantity_var.get()
            # Find and update the item in cart_items
            for item in self.cart_items:
                if item['name'] == product_name:
                    item['quantity'] = new_quantity
                    item['total'] = new_quantity * current_price
                    break
            self.update_cart_view()
            quantity_window.destroy()

        # Update Button
        tk.Button(quantity_window, text="Update", command=update_quantity).pack(pady=10)

    def checkout(self):
        """Process checkout"""
        if not self.cart_items:
            messagebox.showinfo("Cart", "Your cart is empty!")
            return
        
        total = sum(item['total'] for item in self.cart_items)
        response = messagebox.askyesno("Checkout", f"Total amount: ₹{total}\nProceed to checkout?")
        
        if response:
            try:
                # Here you can add database insertion logic for order
                for item in self.cart_items:
                    self.cursor.execute(
                        "INSERT INTO orders (product_name, quantity, total_price) VALUES (%s, %s, %s)",
                        (item['name'], item['quantity'], item['total'])
                    )
                self.connection.commit()
                
                messagebox.showinfo("Checkout", "Thank you for your purchase!")
                self.clear_cart()
            except Exception as e:
                messagebox.showerror("Error", f"Checkout failed: {str(e)}")

    def clear_cart(self):
        """Clear all items from the cart"""
        self.cart_items.clear()
        self.update_cart_view()

    def __del__(self):
        """Close database connection when object is destroyed"""
        if hasattr(self, 'connection'):
            self.connection.close()

# If you want to test the cart standalone
def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    cart = YourCart(root)
    root.mainloop()

if __name__ == "__main__":
    main()
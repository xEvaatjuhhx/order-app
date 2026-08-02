import tkinter as tk
from models.product import Product

def build_main_window(root):
    products = [
        Product("Coffee", 2.50),
        Product("Tea", 2.00),
        Product("Sandwich", 4.50),
    ]

    label = tk.Label(root, text="Welcome to the Order App", fg="white", bg="#2b2b2b")
    label.pack(pady=10)

    selections = []  # houdt bij welke producten geselecteerd zijn

    for product in products:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            root,
            text=str(product),
            variable=var,
            fg="white",
            bg="#2b2b2b",
            selectcolor="#2b2b2b"
        )
        checkbox.pack(anchor="w", padx=20)
        selections.append((product, var))

    def place_order():
        chosen = [product for product, var in selections if var.get()]
        for product in chosen:
            print(f"Ordered: {product}")

    button = tk.Button(root, text="Place Order", command=place_order)
    button.pack(pady=10)
import tkinter as tk
from models.product import Product
from ui.order_summary import show_order_summary

def build_main_window(root):
    products = [
        Product("Coffee", 2.50),
        Product("Tea", 2.00),
        Product("Sandwich", 4.50),
    ]

    # Frame voor de hoofdpagina (productenlijst)
    main_frame = tk.Frame(root, bg="#2b2b2b")
    main_frame.pack(fill="both", expand=True)

    label = tk.Label(main_frame, text="Welcome to the Order App", fg="white", bg="#2b2b2b")
    label.pack(pady=10)

    selections = []

    for product in products:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            main_frame,
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
        main_frame.pack_forget()  # verberg de hoofdpagina
        show_order_summary(root, chosen)

    button = tk.Button(main_frame, text="Place Order", command=place_order)
    button.pack(pady=10)
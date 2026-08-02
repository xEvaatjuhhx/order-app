import tkinter as tk

def show_order_summary(root, ordered_products):
    summary_frame = tk.Frame(root, bg="#2b2b2b")
    summary_frame.pack(fill="both", expand=True)

    label = tk.Label(summary_frame, text="Your Order", fg="white", bg="#2b2b2b", font=("Arial", 14))
    label.pack(pady=10)

    total = 0
    for product in ordered_products:
        item_label = tk.Label(summary_frame, text=str(product), fg="white", bg="#2b2b2b")
        item_label.pack(anchor="w", padx=20)
        total += product.price

    total_label = tk.Label(summary_frame, text=f"Total: €{total:.2f}", fg="white", bg="#2b2b2b", font=("Arial", 12, "bold"))
    total_label.pack(pady=20)
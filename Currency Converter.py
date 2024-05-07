import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates


class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.currency_rates = CurrencyRates()

        # Create GUI elements
        self.from_label = ttk.Label(root, text="From:")
        self.from_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.from_currency = ttk.Combobox(root, width=15, state="readonly")
        self.from_currency.grid(row=0, column=1, padx=5, pady=5)
        self.from_currency['values'] = list(self.currency_rates.get_rates('').keys())

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.amount_entry = ttk.Entry(root, width=15)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.to_label = ttk.Label(root, text="To:")
        self.to_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.to_currency = ttk.Combobox(root, width=15, state="readonly")
        self.to_currency.grid(row=2, column=1, padx=5, pady=5)
        self.to_currency['values'] = list(self.currency_rates.get_rates('').keys())

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, columnspan=2, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=4, columnspan=2, pady=5)

    def convert(self):
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        amount = float(self.amount_entry.get())

        result = self.currency_rates.convert(from_curr, to_curr, amount)
        self.result_label.config(text=f"Converted Amount: {result:.2f} {to_curr}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

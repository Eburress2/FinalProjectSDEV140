import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For image handling

# Sample currency rates (base currency is USD)
CURRENCY_RATES = {
    "USD": (1.0, "$"),  # 1 USD to USD
    "EUR": (0.85, "€"),  # 1 USD to EUR
    "JPY": (110.0, "¥"),  # 1 USD to JPY
    "GBP": (0.75, "£"),  # 1 USD to GBP
    "AUD": (1.35, "A$"),  # 1 USD to AUD
}

def validate_input(entry_value):
    """ 
    Validates user input to ensure it is a non-negative number. 
    Returns True if valid, False otherwise.
    """
    if not entry_value:  # Check if entry is empty
        return False
    try:
        value = float(entry_value)  # Attempt to convert to float
        return value >= 0  # Ensure non-negative
    except ValueError:
        return False  # Return False if conversion fails

def convert_currency():
    """ 
    Converts currency based on user input and selected options. 
    Updates the result label with the conversion details.
    """
    amount = amount_entry.get()  # Get amount from entry
    from_currency = from_currency_var.get()  # Get selected from currency
    to_currency = to_currency_var.get()  # Get selected to currency

    # Validate input
    if not validate_input(amount):  # Check for valid input
        messagebox.showerror("Input Error", "Please enter a valid non-negative number.")
        return

    amount = float(amount)  # Convert amount to float
    from_rate, from_symbol = CURRENCY_RATES[from_currency]  # Get from currency rate and symbol
    to_rate, to_symbol = CURRENCY_RATES[to_currency]  # Get to currency rate and symbol
    converted_amount = amount * (to_rate / from_rate)  # Calculate conversion

    # Update result label with conversion details
    result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_symbol} ({from_symbol}{amount:.2f} {from_currency} at rate {to_rate/from_rate:.2f})")  # Update result label

def open_conversion_window():
    """ 
    Opens the currency conversion window.
    Creates the layout for the conversion interface.
    """
    conversion_window = tk.Toplevel(root)  # Create new window
    conversion_window.title("Currency Converter")

    global amount_entry, from_currency_var, to_currency_var, result_label  # Make variables global for access

    tk.Label(conversion_window, text="Enter Amount:").pack()  # Label for amount
    amount_entry = tk.Entry(conversion_window)  # Entry for amount
    amount_entry.pack()

    tk.Label(conversion_window, text="From Currency:").pack()  # Label for from currency
    from_currency_var = tk.StringVar(value="USD")  # Default value
    from_currency_menu = tk.OptionMenu(conversion_window, from_currency_var, *CURRENCY_RATES.keys())  # Dropdown for from currency
    from_currency_menu.pack()

    tk.Label(conversion_window, text="To Currency:").pack()  # Label for to currency
    to_currency_var = tk.StringVar(value="EUR")  # Default value
    to_currency_menu = tk.OptionMenu(conversion_window, to_currency_var, *CURRENCY_RATES.keys())  # Dropdown for to currency
    to_currency_menu.pack()

    convert_button = tk.Button(conversion_window, text="Convert", command=convert_currency)  # Convert button
    convert_button.pack()

    result_label = tk.Label(conversion_window, text="Converted Amount: ")  # Label for displaying result
    result_label.pack()

    exit_button = tk.Button(conversion_window, text="Exit", command=conversion_window.destroy)  # Exit button
    exit_button.pack()

def exit_application():
    """ Exits the application. """
    root.destroy()  # Close the main application window

# Main application setup
root = tk.Tk()
root.title("Currency Converter")

# Load a single image
try:
    image = Image.open("F:/Python Projects/School Work/currency_image.jpg")  # Use one valid image path
    image = image.resize((100, 100))  # Resize image
    photo = ImageTk.PhotoImage(image)  # Create PhotoImage object

    # User Interface Elements
    tk.Label(root, text="Welcome to the Currency Converter", font=("Helvetica", 16)).pack()  # Welcome label
    tk.Label(root, image=photo).pack()  # Image without caption

    open_converter_button = tk.Button(root, text="Open Converter", command=open_conversion_window)  # Button to open converter
    open_converter_button.pack()

    exit_button = tk.Button(root, text="Exit", command=exit_application)  # Button to exit application
    exit_button.pack()

except FileNotFoundError:
    print("Error: The specified image file was not found.")
except UnidentifiedImageError:
    print("Error: Cannot identify the image file. It may be corrupted or in an unsupported format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Start the main loop
root.mainloop()  # Run the application

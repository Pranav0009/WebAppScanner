import tkinter as tk
from tkinter import ttk
from WebScanner import rce_func, xss_func, error_based_sqli_func, UserAgent
import sys

# Function to capture standard output
class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)

def scan_rce():
    url = url_entry.get()
    rce_output.delete(1.0, tk.END)
    rce_output.insert(tk.END, "Scanning for Remote Code/Command Execution...\n")

    # Redirect standard output to the Text widget
    sys.stdout = OutputRedirector(rce_output)
    rce_func(url, UserAgent)

def scan_xss():
    url = url_entry.get()
    xss_output.delete(1.0, tk.END)
    xss_output.insert(tk.END, "Scanning for XSS...\n")

    # Redirect standard output to the Text widget
    sys.stdout = OutputRedirector(xss_output)
    xss_func(url, UserAgent)

def scan_sqli():
    url = url_entry.get()
    sqli_output.delete(1.0, tk.END)
    sqli_output.insert(tk.END, "Scanning for SQL Injection...\n")

    # Redirect standard output to the Text widget
    sys.stdout = OutputRedirector(sqli_output)
    error_based_sqli_func(url, UserAgent)

# Create the main window
root = tk.Tk()
root.title("Web Vulnerability Scanner")

# Set custom background and foreground colors
root.configure(bg='#2E3B55')
root.option_add('*TButton*background', '#1E90FF')  # Set button background color
root.option_add('*TButton*foreground', 'white')   # Set button text color

# Create and configure the URL input field
url_label = ttk.Label(root, text="Enter URL:", background='#2E3B55', foreground='white')
url_label.pack()
url_entry = ttk.Entry(root)
url_entry.pack()

# Create scan buttons with custom colors
rce_button = ttk.Button(root, text="Scan RCE", command=scan_rce)
xss_button = ttk.Button(root, text="Scan XSS", command=scan_xss)
sqli_button = ttk.Button(root, text="Scan SQL Injection", command=scan_sqli)

rce_button.pack()
xss_button.pack()
sqli_button.pack()

# Create text output areas with custom colors
rce_output = tk.Text(root, height=10, width=80, background='black', foreground='lime')
xss_output = tk.Text(root, height=10, width=80, background='black', foreground='lime')
sqli_output = tk.Text(root, height=10, width=80, background='black', foreground='lime')

rce_output.pack()
xss_output.pack()
sqli_output.pack()

root.mainloop()

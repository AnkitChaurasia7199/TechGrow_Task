import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip
import random
import string
import webbrowser  # Import the webbrowser module

class URLShortener:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.geometry("400x300")

        self.url_mapping = {}

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to URL Shortener", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.input_label = tk.Label(self.root, text="Enter the URL to shorten:", font=("Helvetica", 12))
        self.input_label.pack(pady=5)

        self.url_entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.url_entry.pack(pady=5)

        self.shorten_button = tk.Button(self.root, text="Shorten URL", command=self.shorten_url, font=("Helvetica", 12))
        self.shorten_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12), fg="green")
        self.result_label.pack(pady=10)

        self.copy_button = tk.Button(self.root, text="Copy Short URL", command=self.copy_to_clipboard, font=("Helvetica", 12))
        self.copy_button.pack(pady=5)

        self.open_button = tk.Button(self.root, text="Open Short URL", command=self.open_short_url, font=("Helvetica", 12))
        self.open_button.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, font=("Helvetica", 12))
        self.quit_button.pack(pady=5)

    def shorten_url(self):
        original_url = self.url_entry.get().strip()
        if not original_url:
            messagebox.showerror("Error", "Please enter a valid URL.")
            return

        short_url = self.generate_short_url()
        self.url_mapping[short_url] = original_url

        self.result_label.config(text=f"Short URL: {short_url}")

    def generate_short_url(self):
        chars = string.ascii_letters + string.digits
        short_url = "https://short.ly/" + ''.join(random.choices(chars, k=6))
        while short_url in self.url_mapping:
            short_url = "https://short.ly/" + ''.join(random.choices(chars, k=6))
        return short_url

    def copy_to_clipboard(self):
        short_url = self.result_label.cget("text").replace("Short URL: ", "").strip()
        if short_url:
            pyperclip.copy(short_url)
            messagebox.showinfo("Copied", "Short URL copied to clipboard.")
        else:
            messagebox.showerror("Error", "No Short URL to copy.")

    def open_short_url(self):
        short_url = self.result_label.cget("text").replace("Short URL: ", "").strip()
        if short_url:
            original_url = self.url_mapping.get(short_url, "")
            if original_url:
                webbrowser.open(original_url)  # Open the original URL in a web browser
            else:
                messagebox.showerror("Error", "Could not find the original URL.")
        else:
            messagebox.showerror("Error", "No Short URL to open.")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortener(root)
    root.mainloop()

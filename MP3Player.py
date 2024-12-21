import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pygame

class MP3Player:
    def __init__(self, root):  # Corrected the constructor name
        self.root = root
        self.root.title("MP3 Player")
        self.root.geometry("400x300")

        pygame.mixer.init()

        self.current_file = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Welcome to MP3 Player", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Load MP3", command=self.load_mp3, font=("Helvetica", 12))
        self.load_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music, font=("Helvetica", 12))
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music, font=("Helvetica", 12))
        self.pause_button.pack(pady=5)

        self.resume_button = tk.Button(self.root, text="Resume", command=self.resume_music, font=("Helvetica", 12))
        self.resume_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music, font=("Helvetica", 12))
        self.stop_button.pack(pady=5)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_app, font=("Helvetica", 12))
        self.quit_button.pack(pady=5)

    def load_mp3(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.current_file = file_path
            messagebox.showinfo("File Loaded", f"Loaded: {file_path}")

    def play_music(self):
        if self.current_file:
            pygame.mixer.music.load(self.current_file)
            pygame.mixer.music.play()
        else:
            messagebox.showerror("No File", "Please load an MP3 file first.")

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def quit_app(self):
        pygame.mixer.music.stop()
        self.root.destroy()

if __name__ == "__main__":  # Corrected the typo in the special variable
    root = tk.Tk()
    player = MP3Player(root)
    root.mainloop()


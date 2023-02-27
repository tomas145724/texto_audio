import tkinter as tk
from tkinter import ttk
from gtts import gTTS
import os

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Text to Speech App")

        # Labels and entry widgets
        self.label1 = ttk.Label(master, text="Enter Text:")
        self.label1.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        self.text_entry = tk.Text(master, width=40, height=10)
        self.text_entry.grid(row=1, column=0, padx=10, pady=10)

        self.label2 = ttk.Label(master, text="Select Voice:")
        self.label2.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        self.voice_var = tk.StringVar(value="pt-br")
        self.voice_menu = ttk.Combobox(master, textvariable=self.voice_var, state="readonly", values=["en-us", "pt-br"])
        self.voice_menu.grid(row=3, column=0, padx=10, pady=10)

        self.label3 = ttk.Label(master, text="Select Speed:")
        self.label3.grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)
        self.speed_var = tk.StringVar(value="1.0")
        self.speed_menu = ttk.Combobox(master, textvariable=self.speed_var, state="readonly", values=["0.5", "0.75", "1.0", "1.25", "1.5", "2.0", "2.5"])
        self.speed_menu.grid(row=5, column=0, padx=10, pady=10)

        self.label4 = ttk.Label(master, text="Select Volume:")
        self.label4.grid(row=6, column=0, sticky=tk.W, padx=10, pady=10)
        self.volume_var = tk.StringVar(value="1.0")
        self.volume_menu = ttk.Combobox(master, textvariable=self.volume_var, state="readonly", values=["0.5", "0.75", "1.0", "1.25", "1.5"])
        self.volume_menu.grid(row=7, column=0, padx=10, pady=10)

        # Buttons
        self.play_button = ttk.Button(master, text="Play", command=self.play_audio)
        self.play_button.grid(row=8, column=0, padx=10, pady=10)

    def play_audio(self):
        text = self.text_entry.get("1.0", "end").strip()
        lang = self.voice_var.get()
        speed = float(self.speed_var.get())
        volume = float(self.volume_var.get())
        
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.volume = volume
            tts.speed = speed
            tts.save("output.mp3")
            os.system("start output.mp3")
        except ValueError as e:
            error_msg = "Error: " + str(e)
            tk.messagebox.showerror("Error", error_msg)

root = tk.Tk()
app = TextToSpeechApp(root)
root.mainloop()

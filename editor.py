import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("AFC Text Editor | Versão 1.0 | ")

        # create menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        # create file menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Novo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Sair do Editor", command=self.root.quit)

        # create text widget
        self.text_widget = tk.Text(self.root, wrap="word", font=("sans-serif", 16), bg="black", fg="white")
        self.text_widget.pack(fill="both", expand=True)
        self.text_widget.focus_set()
        self.blink_cursor()
        self.file_path = None

    def new_file(self):
        self.file_path = None
        self.root.title("AFC Text Editor")
        self.text_widget.delete("1.0", "end")

    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            self.root.title(f"AFC - Local:  {self.file_path}")
            with open(self.file_path, "r") as file:
                self.text_widget.delete("1.0", "end")
                self.text_widget.insert("1.0", file.read())

    def save_file(self):
        if not self.file_path:
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            self.root.title(f"AFC - Local:  {self.file_path}")
            with open(self.file_path, "w") as file:
                file.write(self.text_widget.get("1.0", "end"))

    def blink_cursor(self):
        self.text_widget.config(insertbackground="yellow")
        self.root.after(500, self.blink_cursor)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x400")
    textEditor = TextEditor(root)
    root.mainloop()



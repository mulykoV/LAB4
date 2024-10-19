import tkinter as tk
from tkinter import messagebox

class NotesStackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Нотатки на основі стеку")
        self.stack = []

        # Створюємо віджети
        self.label = tk.Label(root, text="Я ваш особистий записник:")
        self.label.pack()

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Занотувати", command=self.add_note)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Це мені вже не потрібно", command=self.remove_note)
        self.remove_button.pack()

        self.view_button = tk.Button(root, text="Що ж я там хотів зробити", command=self.view_notes)
        self.view_button.pack()

        self.clear_button = tk.Button(root, text="Очистити всі нотатки", command=self.clear_notes)
        self.clear_button.pack()

        self.save_button = tk.Button(root, text="Зберегти нотатки у файл, щоб точно не загубити", command=self.save_notes)
        self.save_button.pack()

        self.notes_display = tk.Text(root, height=10, width=50)
        self.notes_display.pack()

    def add_note(self):
        note = self.entry.get()
        if note:
            self.stack.append(note)
            self.entry.delete(0, tk.END)
            self.update_notes_display()
        else:
            messagebox.showwarning("Помилка", "Нотатка не може бути порожньою!")

    def remove_note(self):
        if self.stack:
            removed_note = self.stack.pop()
            self.update_notes_display()
            messagebox.showinfo("Нотатку видалено", f"Видалено: {removed_note}")
        else:
            messagebox.showwarning("Помилка", "Стек порожній, нічого видаляти!")

    def view_notes(self):
        if self.stack:
            self.update_notes_display()
        else:
            messagebox.showinfo("Інформація", "Стек порожній!")

    def clear_notes(self):
        self.stack.clear()
        self.update_notes_display()

    def save_notes(self):
        if self.stack:
            with open("notes.txt", "w") as file:
                for note in self.stack:
                    file.write(note + "\n")
            messagebox.showinfo("Збережено", "Нотатки успішно збережені у файл notes.txt!")
        else:
            messagebox.showwarning("Помилка", "Немає нотаток для збереження!")

    def update_notes_display(self):
        self.notes_display.delete(1.0, tk.END)
        if self.stack:
            for note in reversed(self.stack):
                self.notes_display.insert(tk.END, note + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = NotesStackApp(root)
    root.mainloop()

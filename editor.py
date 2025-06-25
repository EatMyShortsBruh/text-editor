import tkinter as tk

def create_main_window():
    root = tk.Tk()
    root.title("My Notepad")
    root.geometry("800x600")

    text_area = tk.Text(root)
    text_area.pack(expand=True, fill='both') # Makes text area re-size with window

    return root

if __name__ == "__main__":
    window = create_main_window()
    window.mainloop()

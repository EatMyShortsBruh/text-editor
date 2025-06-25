import unittest
import tkinter as tk
from editor import create_main_window

class TestNotepadGUI(unittest.TestCase):
    def test_window_title(self):
        window = create_main_window()
        self.assertEqual(window.title(), "My Notepad")

    def test_text_area_exists(self):
        window = create_main_window()
        text_widgets = [child for child in window.winfo_children() if isinstance(child, tk.Text)]
        self.assertEqual(len(text_widgets), 1)

    def test_menu_bar_exists(self):
        window = create_main_window()
        menu = window["menu"]
        file_menu_found = False
        for index in range(menu.index("end") + 1):
            label = menu.entrycget(index, "label")
            if label == "File":
                file_menu_found = True
                break
        self.assertTrue(file_menu_found)
        
if __name__ == "__main__":
    unittest.main()

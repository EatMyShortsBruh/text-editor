import unittest
import tkinter as tk
from editor import create_main_window

class TestNotepadGUI(unittest.TestCase):
    def test_window_title(self):
        window = create_main_window()
        self.assertEqual(window.title(), "My Notepad")

    def test_text_area_exists(self):
        window = create_main_window()
        text_widgets = [child for child in window.winfo_children() if instance(child, tk.Text)]
        self.assertEqual(len(text_widgets), 1)
        
if __name__ == "__main__":
    unittest.main()

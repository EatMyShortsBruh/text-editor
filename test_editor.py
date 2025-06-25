import unittest
import tkinter as tk
from editor import create_main_window

class TestNotepadGUI(unittest.TestCase):
    def test_window_title(self):
        window = create_main_window()
        self.assertEqual(window.title(), "My Notepad")

if __name__ == "__main__":
    unittest.main()

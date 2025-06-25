import unittest
import tkinter as tk
from editor import create_main_window

<<<<<<< HEAD
class TestNotepadGUI(unittest.TestCase):
=======
class TestNotepadGUI(unittest.Testcase):
>>>>>>> 9b5b46641000bc2adde0336f925ab9b3af425566
    def test_window_title(self):
        window = create_main_window()
        self.assertEqual(window.title(), "My Notepad")

if __name__ == "__main__":
    unittest.main()
import unittest as ut
from LaserGui import Project
import tkinter as tk

class TestGUI(ut.TestCase):
    def test_one(self):
        root = tk.TK()
        var = Project(root)
        self.assertIsNotNone(var)
        var.createTab()
        self.assertIsEqual(var.getTabCount,2)




if __name__ == '__main__':
    ut.main()
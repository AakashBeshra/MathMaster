#!/usr/bin/env python3
"""
MathMaster - Advanced Mathematical Application
Main entry point for the application
"""

import tkinter as tk
from calculator_gui import MathCalculatorApp

def main():
    """Main function to launch the MathMaster application"""
    root = tk.Tk()
    app = MathCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
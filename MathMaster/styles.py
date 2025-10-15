"""
StyleManager - Manages GUI styling for MathMaster
"""

import tkinter as tk
from tkinter import ttk

class StyleManager:
    """Manages application styling and themes"""
    
    def __init__(self):
        self.style = ttk.Style()
        
    def configure_styles(self):
        """Configure all application styles"""
        self.configure_main_style()
        self.configure_button_styles()
        self.configure_label_styles()
        self.configure_frame_styles()
        self.configure_scrollbar_styles()
        self.configure_entry_styles()
        
    def configure_main_style(self):
        """Configure main application style"""
        self.style.theme_use('clam')
        
        # Main style configuration
        self.style.configure('.', 
                           background='#2c3e50',
                           foreground='#ecf0f1',
                           font=('Arial', 10))
        
    def configure_button_styles(self):
        """Configure button styles"""
        # Regular button
        self.style.configure('TButton',
                           padding=(12, 6),
                           relief='flat',
                           background='#3498db',
                           foreground='white',
                           focuscolor='none',
                           font=('Arial', 10))
        
        self.style.map('TButton',
                      background=[('active', '#2980b9'),
                                 ('pressed', '#21618c')])
        
        # Accent button
        self.style.configure('Accent.TButton',
                           background='#e74c3c',
                           foreground='white')
        
        self.style.map('Accent.TButton',
                      background=[('active', '#c0392b'),
                                 ('pressed', '#a93226')])
        
        # Color variants for different operations
        colors = {
            '#27ae60': ('#2ecc71', '#27ae60', '#229954'),  # Green
            '#e74c3c': ('#ec7063', '#e74c3c', '#cb4335'),  # Red
            '#3498db': ('#5dade2', '#3498db', '#2e86c1'),  # Blue
            '#9b59b6': ('#bb8fce', '#9b59b6', '#8e44ad'),  # Purple
            '#e67e22': ('#f39c12', '#e67e22', '#d68910'),  # Orange
            '#f1c40f': ('#f7dc6f', '#f1c40f', '#d4ac0d'),  # Yellow
            '#1abc9c': ('#48c9b0', '#1abc9c', '#17a589'),  # Teal
            '#34495e': ('#5d6d7e', '#34495e', '#2c3e50'),  # Dark
            '#8e44ad': ('#a569bd', '#8e44ad', '#7d3c98'),  # Dark Purple
            '#d35400': ('#e67e22', '#d35400', '#ba4a00')   # Dark Orange
        }
        
        for color_name, (normal, active, pressed) in colors.items():
            self.style.configure(f'Color{color_name}.TButton',
                               background=normal,
                               foreground='white',
                               font=('Arial', 9, 'bold'),
                               padding=(8, 4))
            
            self.style.map(f'Color{color_name}.TButton',
                          background=[('active', active),
                                     ('pressed', pressed)])
        
    def configure_label_styles(self):
        """Configure label styles"""
        self.style.configure('TLabel',
                           background='#2c3e50',
                           foreground='#ecf0f1',
                           font=('Arial', 10))
        
        self.style.configure('Title.TLabel',
                           font=('Arial', 16, 'bold'),
                           foreground='#3498db')
        
        self.style.configure('Subtitle.TLabel',
                           font=('Arial', 12, 'bold'),
                           foreground='#ecf0f1')
        
    def configure_frame_styles(self):
        """Configure frame styles"""
        self.style.configure('TFrame',
                           background='#2c3e50')
        
        self.style.configure('TLabelframe',
                           background='#34495e',
                           foreground='#ecf0f1',
                           bordercolor='#7f8c8d',
                           relief='solid',
                           borderwidth=1)
        
        self.style.configure('TLabelframe.Label',
                           background='#34495e',
                           foreground='#3498db',
                           font=('Arial', 11, 'bold'))
        
    def configure_scrollbar_styles(self):
        """Configure scrollbar styles"""
        self.style.configure('TScrollbar',
                           background='#34495e',
                           troughcolor='#2c3e50',
                           bordercolor='#34495e',
                           arrowcolor='#ecf0f1',
                           relief='flat')
        
        self.style.map('TScrollbar',
                      background=[('active', '#3498db'),
                                 ('pressed', '#2980b9')])
        
    def configure_entry_styles(self):
        """Configure entry field styles"""
        # Note: For Entry widgets, we use direct tk.Entry configuration
        # This is handled in the calculator_gui.py file
        pass
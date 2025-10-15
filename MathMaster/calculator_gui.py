import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from math_operations import MathOperations
from styles import StyleManager

class MathCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MathMaster - Advanced Calculator")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c3e50')
        
        # Initialize components
        self.style_manager = StyleManager()
        self.operations = MathOperations()
        self.history = []
        
        self.setup_gui()
        self.apply_styles()
        
    def setup_gui(self):
        """Setup the main GUI components with scrolling"""
        # Create main container with scrollbar
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create a canvas for scrolling
        self.canvas = tk.Canvas(main_container, bg='#2c3e50', highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel to canvas
        self.canvas.bind("<Enter>", self._bind_to_mousewheel)
        self.canvas.bind("<Leave>", self._unbind_from_mousewheel)
        
        # Configure grid weights for scrollable frame
        self.scrollable_frame.columnconfigure(0, weight=1)
        
        # Title
        title_label = ttk.Label(self.scrollable_frame, text="🧮 MathMaster", 
                               font=('Arial', 24, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="ew")
        
        # Input Section
        self.create_input_section(self.scrollable_frame)
        
        # Operations Section
        self.create_operations_section(self.scrollable_frame)
        
        # Advanced Operations Section
        self.create_advanced_operations_section(self.scrollable_frame)
        
        # Results and History Section
        self.create_results_history_section(self.scrollable_frame)
        
        # Graph Section
        self.create_graph_section(self.scrollable_frame)
        
        # Footer
        self.create_footer(self.scrollable_frame)
        
    def _bind_to_mousewheel(self, event):
        """Bind mouse wheel to canvas when mouse enters"""
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
    def _unbind_from_mousewheel(self, event):
        """Unbind mouse wheel when mouse leaves"""
        self.canvas.unbind_all("<MouseWheel>")
        
    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def create_input_section(self, parent):
        """Create number input section"""
        input_frame = ttk.LabelFrame(parent, text="Number Input", padding="15")
        input_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 15))
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(3, weight=1)
        
        # First number
        ttk.Label(input_frame, text="First Number:", font=('Arial', 11, 'bold')).grid(
            row=0, column=0, sticky=tk.W, padx=(0, 15), pady=5
        )
        self.num1_entry = tk.Entry(input_frame, font=('Arial', 12), width=20, 
                                 bg='white', fg='black', insertbackground='black',
                                 relief='solid', bd=1)
        self.num1_entry.grid(row=0, column=1, sticky="ew", padx=(0, 30), pady=5)
        self.num1_entry.insert(0, "0")
        
        # Second number
        ttk.Label(input_frame, text="Second Number:", font=('Arial', 11, 'bold')).grid(
            row=0, column=2, sticky=tk.W, padx=(0, 15), pady=5
        )
        self.num2_entry = tk.Entry(input_frame, font=('Arial', 12), width=20,
                                 bg='white', fg='black', insertbackground='black',
                                 relief='solid', bd=1)
        self.num2_entry.grid(row=0, column=3, sticky="ew", pady=5)
        self.num2_entry.insert(0, "0")
        
        # Input buttons
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=1, column=0, columnspan=4, pady=(15, 5))
        
        ttk.Button(button_frame, text="🧹 Clear Inputs", 
                  command=self.clear_inputs, style="Accent.TButton").pack(side=tk.LEFT, padx=(0, 15))
        ttk.Button(button_frame, text="🎲 Set Random Numbers", 
                  command=self.set_random_numbers).pack(side=tk.LEFT, padx=(0, 15))
        ttk.Button(button_frame, text="🔢 Swap Numbers", 
                  command=self.swap_numbers).pack(side=tk.LEFT)
        
    def create_operations_section(self, parent):
        """Create basic operations buttons section"""
        ops_frame = ttk.LabelFrame(parent, text="🔢 Basic Operations", padding="15")
        ops_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(0, 15))
        
        # Configure equal column weights
        for i in range(4):
            ops_frame.columnconfigure(i, weight=1)
        
        basic_ops = [
            ("➕ Addition", self.addition, "#27ae60"),
            ("➖ Subtraction", self.subtraction, "#e74c3c"),
            ("✖ Multiplication", self.multiplication, "#3498db"),
            ("➗ Division", self.division, "#9b59b6"),
            ("📐 Modulus", self.modulus, "#e67e22"),
            ("💪 Power", self.power, "#f1c40f"),
            ("📊 Square Root", self.square_root, "#1abc9c"),
            ("📈 Percentage", self.percentage, "#34495e")
        ]
        
        for i, (text, command, color) in enumerate(basic_ops):
            btn = ttk.Button(ops_frame, text=text, command=command, 
                           style=f"Color{color}.TButton")
            row, col = divmod(i, 4)
            btn.grid(row=row, column=col, padx=8, pady=8, sticky="ew")
            
    def create_advanced_operations_section(self, parent):
        """Create advanced operations buttons section"""
        adv_frame = ttk.LabelFrame(parent, text="🚀 Advanced Operations", padding="15")
        adv_frame.grid(row=3, column=0, columnspan=3, sticky="ew", pady=(0, 15))
        
        # Configure equal column weights
        for i in range(5):
            adv_frame.columnconfigure(i, weight=1)
        
        advanced_ops = [
            ("📈 Sin/Cos/Tan", self.trig_functions, "#e74c3c"),
            ("🧮 Logarithm", self.logarithm, "#3498db"),
            ("📐 Factorial", self.factorial, "#9b59b6"),
            ("🎯 Absolute Value", self.absolute, "#f1c40f"),
            ("🔄 Round Number", self.round_number, "#27ae60"),
            ("π Pi Constant", self.pi_constant, "#1abc9c"),
            ("𝑒 Euler's Number", self.euler_constant, "#e67e22"),
            ("∞ Check Infinity", self.check_infinity, "#34495e"),
            ("🧮 GCD Calculator", self.gcd_calculator, "#8e44ad"),
            ("📏 LCM Calculator", self.lcm_calculator, "#d35400")
        ]
        
        for i, (text, command, color) in enumerate(advanced_ops):
            btn = ttk.Button(adv_frame, text=text, command=command,
                           style=f"Color{color}.TButton")
            row, col = divmod(i, 5)
            btn.grid(row=row, column=col, padx=6, pady=6, sticky="ew")
            
    def create_results_history_section(self, parent):
        """Create combined results and history section"""
        results_history_frame = ttk.Frame(parent)
        results_history_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(0, 15))
        results_history_frame.columnconfigure(0, weight=1)
        results_history_frame.columnconfigure(1, weight=1)
        
        # Results Section
        results_frame = ttk.LabelFrame(results_history_frame, text="📊 Results", padding="10")
        results_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        self.result_text = scrolledtext.ScrolledText(results_frame, height=12, font=('Arial', 11),
                                                   bg='#f8f9fa', fg='#2c3e50', wrap=tk.WORD,
                                                   insertbackground='black')
        self.result_text.grid(row=0, column=0, sticky="nsew")
        self.result_text.config(state=tk.DISABLED)
        
        # History Section
        history_frame = ttk.LabelFrame(results_history_frame, text="📜 Calculation History", padding="10")
        history_frame.grid(row=0, column=1, sticky="nsew")
        history_frame.columnconfigure(0, weight=1)
        history_frame.rowconfigure(0, weight=1)
        
        self.history_text = scrolledtext.ScrolledText(history_frame, height=12, font=('Arial', 10),
                                                    bg='#f8f9fa', fg='#2c3e50', wrap=tk.WORD,
                                                    insertbackground='black')
        self.history_text.grid(row=0, column=0, sticky="nsew")
        self.history_text.config(state=tk.DISABLED)
        
        # History controls
        history_controls = ttk.Frame(history_frame)
        history_controls.grid(row=1, column=0, pady=(10, 0), sticky="ew")
        
        ttk.Button(history_controls, text="🗑️ Clear History", 
                  command=self.clear_history).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(history_controls, text="💾 Export History", 
                  command=self.export_history).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(history_controls, text="📋 Copy Result", 
                  command=self.copy_result).pack(side=tk.LEFT)
        
    def create_graph_section(self, parent):
        """Create graphing section"""
        graph_frame = ttk.LabelFrame(parent, text="📈 Function Graph", padding="15")
        graph_frame.grid(row=5, column=0, columnspan=3, sticky="ew", pady=(0, 15))
        graph_frame.columnconfigure(0, weight=1)
        
        # Graph controls
        graph_controls = ttk.Frame(graph_frame)
        graph_controls.grid(row=0, column=0, pady=(0, 15), sticky="ew")
        
        ttk.Label(graph_controls, text="Function f(x) =", font=('Arial', 11, 'bold')).pack(side=tk.LEFT, padx=(0, 10))
        self.function_entry = tk.Entry(graph_controls, width=25, font=('Arial', 11),
                                     bg='white', fg='black', insertbackground='black',
                                     relief='solid', bd=1)
        self.function_entry.pack(side=tk.LEFT, padx=(0, 15))
        self.function_entry.insert(0, "x**2")
        
        ttk.Button(graph_controls, text="📊 Plot Graph", 
                  command=self.plot_graph, style="Accent.TButton").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(graph_controls, text="🗑️ Clear Graph", 
                  command=self.clear_graph).pack(side=tk.LEFT, padx=(0, 10))
        
        # Range controls
        range_frame = ttk.Frame(graph_frame)
        range_frame.grid(row=1, column=0, pady=(0, 15), sticky="w")
        
        ttk.Label(range_frame, text="Range:").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Label(range_frame, text="From").pack(side=tk.LEFT, padx=(0, 5))
        self.range_start = tk.Entry(range_frame, width=8, font=('Arial', 10),
                                  bg='white', fg='black', insertbackground='black',
                                  relief='solid', bd=1)
        self.range_start.pack(side=tk.LEFT, padx=(0, 15))
        self.range_start.insert(0, "-10")
        
        ttk.Label(range_frame, text="To").pack(side=tk.LEFT, padx=(0, 5))
        self.range_end = tk.Entry(range_frame, width=8, font=('Arial', 10),
                                bg='white', fg='black', insertbackground='black',
                                relief='solid', bd=1)
        self.range_end.pack(side=tk.LEFT, padx=(0, 15))
        self.range_end.insert(0, "10")
        
        # Graph display
        self.graph_frame = ttk.Frame(graph_frame, height=300)
        self.graph_frame.grid(row=2, column=0, sticky="ew")
        self.graph_frame.columnconfigure(0, weight=1)
        
    def create_footer(self, parent):
        """Create footer section"""
        footer_frame = ttk.Frame(parent)
        footer_frame.grid(row=6, column=0, columnspan=3, sticky="ew", pady=(20, 0))
        
        footer_label = ttk.Label(footer_frame, text="🧮 MathMaster - Your Advanced Mathematical Companion", 
                               font=('Arial', 10, 'italic'), foreground='#7f8c8d')
        footer_label.pack()
        
    def apply_styles(self):
        """Apply custom styles to the application"""
        self.style_manager.configure_styles()
        
    def get_numbers(self):
        """Get and validate input numbers"""
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers!")
            return None, None
            
    def get_single_number(self):
        """Get and validate a single input number"""
        try:
            return float(self.num1_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number!")
            return None

    # Basic Operations
    def addition(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = self.operations.add(num1, num2)
            self.display_result("➕ Addition", num1, num2, result)
            
    def subtraction(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = self.operations.subtract(num1, num2)
            self.display_result("➖ Subtraction", num1, num2, result)
            
    def multiplication(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = self.operations.multiply(num1, num2)
            self.display_result("✖ Multiplication", num1, num2, result)
            
    def division(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            try:
                result = self.operations.divide(num1, num2)
                self.display_result("➗ Division", num1, num2, result)
            except ValueError as e:
                messagebox.showerror("Math Error", str(e))
                
    def modulus(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            try:
                result = self.operations.modulus(num1, num2)
                self.display_result("📐 Modulus", num1, num2, result)
            except ValueError as e:
                messagebox.showerror("Math Error", str(e))
                
    def power(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            result = self.operations.power(num1, num2)
            self.display_result("💪 Power", num1, num2, result)
            
    def square_root(self):
        num1 = self.get_single_number()
        if num1 is not None:
            try:
                result = self.operations.square_root(num1)
                self.display_result("📊 Square Root", num1, None, result)
            except ValueError as e:
                messagebox.showerror("Math Error", str(e))

    def percentage(self):
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            try:
                result = self.operations.percentage(num1, num2)
                self.display_result("📈 Percentage", num1, num2, f"{result}%")
            except ValueError as e:
                messagebox.showerror("Math Error", str(e))
                
    # Advanced Operations
    def trig_functions(self):
        num1 = self.get_single_number()
        if num1 is not None:
            results = self.operations.trig_functions(num1)
            result_str = f"📈 Trigonometric Functions (angle in radians):\n\n"
            result_str += f"sin({num1}) = {results['sin']:.6f}\n"
            result_str += f"cos({num1}) = {results['cos']:.6f}\n"
            result_str += f"tan({num1}) = {results['tan']:.6f}"
            
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_str)
            self.result_text.config(state=tk.DISABLED)
            
            self.history.append(f"Trig functions({num1}) = {results}")
            self.update_history_display()
            
    def logarithm(self):
        num1 = self.get_single_number()
        if num1 is not None:
            try:
                result = self.operations.logarithm(num1)
                self.display_result("🧮 Natural Logarithm", num1, None, f"{result:.6f}")
            except ValueError as e:
                messagebox.showerror("Math Error", str(e))
                
    def factorial(self):
        num1 = self.get_single_number()
        if num1 is not None:
            try:
                result = self.operations.factorial(int(num1))
                self.display_result("📐 Factorial", int(num1), None, result)
            except ValueError as e:
                messagebox.showerror("Math Error", str(e))
                
    def absolute(self):
        num1 = self.get_single_number()
        if num1 is not None:
            result = self.operations.absolute(num1)
            self.display_result("🎯 Absolute Value", num1, None, result)
            
    def round_number(self):
        num1 = self.get_single_number()
        if num1 is not None:
            result = self.operations.round_number(num1)
            self.display_result("🔄 Rounded Value", num1, None, result)

    def pi_constant(self):
        """Display Pi constant"""
        result = math.pi
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"π (Pi) Constant:\n\n{result:.10f}")
        self.result_text.config(state=tk.DISABLED)
        self.history.append(f"π constant = {result:.10f}")
        self.update_history_display()

    def euler_constant(self):
        """Display Euler's number"""
        result = math.e
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"𝑒 (Euler's Number):\n\n{result:.10f}")
        self.result_text.config(state=tk.DISABLED)
        self.history.append(f"e constant = {result:.10f}")
        self.update_history_display()

    def check_infinity(self):
        """Check if number is infinite"""
        num1 = self.get_single_number()
        if num1 is not None:
            is_inf = math.isinf(num1)
            result_str = "∞ Infinite" if is_inf else "Finite"
            self.display_result("∞ Infinity Check", num1, None, result_str)

    def gcd_calculator(self):
        """Calculate Greatest Common Divisor"""
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            try:
                result = math.gcd(int(num1), int(num2))
                self.display_result("🧮 GCD", int(num1), int(num2), result)
            except ValueError as e:
                messagebox.showerror("Math Error", "GCD requires integer numbers!")

    def lcm_calculator(self):
        """Calculate Least Common Multiple"""
        num1, num2 = self.get_numbers()
        if num1 is not None and num2 is not None:
            try:
                result = math.lcm(int(num1), int(num2))
                self.display_result("📏 LCM", int(num1), int(num2), result)
            except (ValueError, AttributeError):
                # Fallback for older Python versions without math.lcm
                try:
                    gcd = math.gcd(int(num1), int(num2))
                    result = abs(int(num1) * int(num2)) // gcd
                    self.display_result("📏 LCM", int(num1), int(num2), result)
                except ValueError as e:
                    messagebox.showerror("Math Error", "LCM requires integer numbers!")
            
    def display_result(self, operation, num1, num2=None, result=None):
        """Display the result and add to history"""
        if result is None:
            return
            
        if num2 is not None:
            result_str = f"{operation}\n\n{num1} + {num2} = {result}"
            history_str = f"{num1} {operation} {num2} = {result}"
        else:
            result_str = f"{operation}\n\n{num1} = {result}"
            history_str = f"{operation}({num1}) = {result}"
            
        # Display in results
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_str)
        self.result_text.config(state=tk.DISABLED)
        
        # Add to history
        self.history.append(history_str)
        self.update_history_display()
        
    def update_history_display(self):
        """Update the history display"""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        for i, calc in enumerate(reversed(self.history[-20:]), 1):
            self.history_text.insert(tk.END, f"{i}. {calc}\n")
        self.history_text.config(state=tk.DISABLED)
        
    # Graph Functions
    def plot_graph(self):
        """Plot a mathematical function"""
        try:
            function_str = self.function_entry.get()
            start = float(self.range_start.get())
            end = float(self.range_end.get())
            
            x = np.linspace(start, end, 400)
            y = eval(function_str, {"x": x, "np": np, "math": math, "sin": np.sin, "cos": np.cos, "tan": np.tan})
            
            # Clear previous graph
            for widget in self.graph_frame.winfo_children():
                widget.destroy()
                
            # Create new figure
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {function_str}')
            ax.grid(True, alpha=0.3)
            ax.set_title(f"Graph of f(x) = {function_str}", fontsize=12, fontweight='bold')
            ax.set_xlabel("x", fontweight='bold')
            ax.set_ylabel("f(x)", fontweight='bold')
            ax.legend()
            
            # Embed in tkinter
            canvas = FigureCanvasTkAgg(fig, self.graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("Graph Error", f"Error plotting function: {str(e)}")
            
    def clear_graph(self):
        """Clear the graph display"""
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
            
    # Utility Functions
    def clear_inputs(self):
        """Clear all input fields"""
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.num1_entry.insert(0, "0")
        self.num2_entry.insert(0, "0")
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
        
    def set_random_numbers(self):
        """Set random numbers in input fields"""
        import random
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.num1_entry.insert(0, str(random.randint(1, 100)))
        self.num2_entry.insert(0, str(random.randint(1, 100)))
        
    def swap_numbers(self):
        """Swap the numbers in input fields"""
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.num1_entry.insert(0, num2)
        self.num2_entry.insert(0, num1)
        
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        self.update_history_display()
        
    def export_history(self):
        """Export history to a text file"""
        try:
            with open("math_calculations_history.txt", "w") as f:
                f.write("MathMaster Calculation History\n")
                f.write("=" * 50 + "\n")
                for i, calc in enumerate(self.history, 1):
                    f.write(f"{i}. {calc}\n")
            messagebox.showinfo("Export Successful", "History exported to 'math_calculations_history.txt'")
        except Exception as e:
            messagebox.showerror("Export Error", f"Could not export history: {str(e)}")
            
    def copy_result(self):
        """Copy the current result to clipboard"""
        try:
            self.result_text.config(state=tk.NORMAL)
            result = self.result_text.get(1.0, tk.END).strip()
            self.result_text.config(state=tk.DISABLED)
            if result:
                self.root.clipboard_clear()
                self.root.clipboard_append(result)
                messagebox.showinfo("Copy Successful", "Result copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Copy Error", f"Could not copy result: {str(e)}")
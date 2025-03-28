from tkinter import messagebox, simpledialog

# the pattern is : x² + bx + c

b = simpledialog.askinteger("x² + bx + c", "Enter b:")
c = (b/2)**2
equation = f"x² + {b}x + {int(c)}"
messagebox.showinfo("Answer", f"""
The equation is: {equation}
------------------------------------
Second way to write it:\n(x + {int(b/2)})(x + {int(b/2)})\n(x + {int(b/2)})²
""")
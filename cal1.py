import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry field to input numbers
        self.entry = tk.Entry(self.root, width=20, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=5, height=2, command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        current_text = self.entry.get()

        if button == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")

        else:
            current_text += button
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text)

def main():
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

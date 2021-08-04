import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("300x650")
        self.master.title("GUI Calculator")
        self.pack()

        # CREATE BUTTONS IN A FOR LOOP.
        btnclrs = ["Blue", "Red", "Green", "Red", "Green", "Blue", "Red", "Green", "Blue"]
        self.btns = []
        for i in range(9):
            def callback(self=self, var=i+1):
                self.text.insert(tk.END, var)
                self.text.pack()
            button = tk.Button(text=i+1, fg=btnclrs[i], bg="Black", command=callback)
            button.pack()
            self.btns.append(button)

        self.text = tk.Text(self.master)
        self.text.bind("<Key-Return>", self.calculation)  # DON'T CALL FUNCTION WHEN BINDING.
        self.text.pack()
        self.text.focus_set()  # ADDED SO BOUND EVENT-HANDLERS WILL BE CALLED.


        operations = ["+", "-", "*", "/"]
        self.ops = []

        for i in range(4):
            def callback1(self=self, var=operations[i]):
                self.text.insert(tk.END, var)
                self.text.pack()
            buttono = tk.Button(text=operations[i], fg="Black", bg="Black", command=callback1)
            buttono.pack()
            self.ops.append(buttono)

        self.output = tk.Text(self.master)
        self.output.insert(1.0, "Output: \n")
        self.output.pack()
        self.master.mainloop()

    def calculation(self, event = None):
        out = self.text.get('1.0', 'end')
        output1 = eval(out)
        self.output.delete(1.0, tk.END)
        self.output.insert(1.0, output1)

if __name__ == "__main__":
    Calculator()
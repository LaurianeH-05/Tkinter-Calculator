import tkinter as tk

class my_calculator:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title("Calculator")
        self.window.geometry("570x600+100+200") #+100+200 opens up the window at specific parts of the screen left n top
        self.window.resizable(False, False)
        self.window.configure(bg="#ffe6f2")

        self.label_result = tk.Label(self.window, width=25, height=2, text="", font=("arial", 30))
        self.label_result.pack()

        self.equation = ""

        self.buttonframe = tk.Frame(self.window)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)


        tk.Button(self.buttonframe, text='C', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.clear()).grid(row=0, column=0, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='/', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("/")).grid(row=0, column=1, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='%', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("%")).grid(row=0, column=2, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='*', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("*")).grid(row=0, column=3, sticky=tk.W+tk.E)

        tk.Button(self.buttonframe, text='7', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("7")).grid(row=1, column=0, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='8', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("8")).grid(row=1, column=1, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='9', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("9")).grid(row=1, column=2, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='-', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("-")).grid(row=1, column=3, sticky=tk.W+tk.E)

        tk.Button(self.buttonframe, text='4', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("4")).grid(row=2, column=0, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='5', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("5")).grid(row=2, column=1, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='6', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("6")).grid(row=2, column=2, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='+', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("+")).grid(row=2, column=3, sticky=tk.W+tk.E)

        tk.Button(self.buttonframe, text='1', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("1")).grid(row=3, column=0, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='2', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("2")).grid(row=3, column=1, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='3', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("3")).grid(row=3, column=2, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='=', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.calculate()).grid(row=3, column=3, rowspan=2, sticky=tk.N+tk.S+tk.W+tk.E)

        tk.Button(self.buttonframe, text='0', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show("0")).grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)
        tk.Button(self.buttonframe, text='.', font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#99004d", command=lambda: self.show(".")).grid(row=4, column=2, sticky=tk.W+tk.E)

        self.buttonframe.pack(fill="x")
        self.window.mainloop()

    

    def show(self, value):
        self.equation+=value
        self.label_result.config(text=self.equation)

    def clear(self):
        self.equation = ""
        self.label_result.config(text=self.equation)

    def calculate(self):
        result='No value'
        if self.equation != "":
            try:
                result = str(eval(self.equation))
            except:
                self.label_result.config(text="Error")
                self.equation = result
        self.label_result.config(text=result)
            


my_calculator()
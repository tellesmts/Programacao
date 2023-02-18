import tkinter as tk

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.label = tk.Label(frame, text="Meu primeiro Programa em Python!")
        self.label.pack()

        self.button = tk.Button(frame, text="Clique aqui", command=self.print_hello)
        self.button.pack()

        self.label = tk.Label(frame, text="")
        self.label.pack()
        
    def print_hello(self):
        self.label.config(text="Olá, mundo!")

root = tk.Tk()
root.geometry("500x500")
app = App(root)
root.mainloop()

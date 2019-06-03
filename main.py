from tkinter import *
from tkinter import ttk


LAYOUT = [
    ['7', '8', '9', '/'],        
    ['4', '5', '6', '*'],        
    ['1', '2', '3', '-'],        
    ['0', 'C', '=', '+'],        
]


class CalcApp(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.Template()

    def Template(self):
        self.display_var = StringVar()
        self.display_var.set('0')

        display_label = ttk.Label(self, textvariable = self.display_var)
        display_label.grid(
            column = 0, row = 0, columnspan = 4, sticky = (N, S, E, W)       
        )

        # レイアウト
        for y, row in enumerate(LAYOUT, 1):
            for x, char in enumerate(row):
                button = ttk.Button(self, text = char)
                button.grid(column = x , row = y, sticky = (N, S, E, W))
                button.bind('<Button-1>', self.calc)
        self.grid(column = 0, row = 0, sticky = (N, S, E, W))

        # 引き伸ばしの設定
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)

        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)

        self.master.columnconfigure(0, weight = 1)
        self.master.rowconfigure(0, weight = 1)

    def calc(self, event):
        char = event.widget['text']
        self.display_var.set(char)

def main():
    root = Tk()
    root.title('電卓')
    CalcApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()

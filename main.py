from tkinter import *
from tkinter import ttk


LAYOUT = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+'],
]

CALC_SYMBOLS = ('+', '-', '*', '/', '**', '//')

class CalcApp(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.exp_list = ['0']
        self.Style()
        self.Template()


    def Style(self):
        style = ttk.Style()

        #ラベルのスタイル
        style.configure(
            'TLabel', font = ('Helvetica', 20),
            foreground = 'black',
        )

        #ボタンのスタイル
        style.configure('TButton', font = ('Helvetica', 20))


    def Template(self):
        self.expression_var = StringVar()
        self.expression_var.set(0)

        display_label = ttk.Label(self, textvariable = self.expression_var)
        display_label.grid(
            column = 0, row = 0, columnspan = 4, sticky = (N, S, E, W)       
        )

        # レイアウト
        for y, row in enumerate(LAYOUT, 1):
            for x, char in enumerate(row):
                button = ttk.Button(self, text = char)
                button.grid(column = x , row = y, sticky = (N, S, E, W))
                button.bind('<Button-1>', self.calc)

        # 引き伸ばしの設定
        self.grid(column = 0, row = 0, sticky = (N, S, E, W))
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)

        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)

        self.master.columnconfigure(0, weight = 1)
        self.master.rowconfigure(0, weight = 1)


    def calc(self, event):
        char = event.widget['text']
        
        last = self.exp_list[-1]

        # = ボタン
        if char == '=':
            if last in CALC_SYMBOLS:
                self.exp_list.pop()
            exp = eval(''.join(self.exp_list))
            self.exp_list = [str(exp)]
        # C ボタン
        elif char == 'C':
            self.exp_list = ['0']
        # + - * / ボタン
        elif char in CALC_SYMBOLS:
            if last == char == '/':
                self.exp_list[-1] += '/'
            elif last == char == '*':
                self.exp_list[-1] += '*'
            elif last in CALC_SYMBOLS:
                self.exp_list[-1] = char
            else:
                self.exp_list.append(char)
        else:
            if last == '0':
                self.exp_list[-1] = char
            elif last in CALC_SYMBOLS:
                self.exp_list.append(char)
            else:
                self.exp_list[-1] += char


        # 画面に結果を出す
        self.expression_var.set(' '.join(self.exp_list))


def main():
    root = Tk()
    root.title('電卓')
    CalcApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()

""""
Calculator app
Author: Tigh Gallagher
Date: 07/03/2024
"""


from tkinter import *
import tkinter as TK


# Calculator

class Calc(Tk):
    def __init__(self):
        super(Calc ,self).__init__()
        self.configure(bg='black')
        self.title("Python Tkinter")
        self.minsize(475,600)
        self.input = []
        self.left = None
        self.right = None
        
    def num_click (self, num):
        if len(self.input) == 0:
            self.input.append(num)
        elif self.input[-1].isdigit():
            self.input[-1] += num
        else: self.input.append(num)
        self.update_screen()

    def symbol_click(self, symbol):
        self.input.append(symbol)
        self.update_screen()

    def update_screen(self):
        screen_text = ''.join(map(str, self.input))
        self.screen.config(text=screen_text)

    def display_result(self, result):
        screen_text = str(result)
        self.screen.config(text=screen_text)
        self.screen.config(fg='blue')
    
    def clear_screen(self):
        screen_text = ""
        self.screen.config(text=screen_text)
        self.screen.config(fg='black')
        self.input =[]
        
    def calculate(self):
        print("Your input:",self.input)
        left = None
        right= None
        solved = None
        while not solved:
            if '÷' in self.input and 'x' in self.input:
                    op = min(self.input.index('÷'), self.input.index('x'))
                    operation = self.input[op]
                    left = self.input.pop(op-1)
                    right = self.input.pop(op)
                    if operation == 'x':
                        self.input[op-1] = int(left) * int(right)
                    else:
                        self.input[op-1] = int(left) / int(right)
                    list(filter(None, self.input))

            elif 'x' in self.input:
                op = self.input.index('x')
                left = self.input.pop(op-1)
                right = self.input.pop(op)
                self.input[op-1] = int(left) * int(right)
                list(filter(None, self.input))

            elif '÷' in self.input:
                op = self.input.index('÷')
                left = self.input.pop(op-1)
                right = self.input.pop(op)
                self.input[op-1] = int(left) / int(right)
                list(filter(None, self.input))

            else:
                if '+' in self.input and '-' in self.input:
                    op = min(self.input.index('+'), self.input.index('-'))
                    operation = self.input[op]
                    left = self.input.pop(op-1)
                    right = self.input.pop(op)
                    if operation == '+':
                        self.input[op-1] = int(left) + int(right)
                    else:
                        self.input[op-1] = int(left) - int(right)
                    list(filter(None, self.input))
                    print(self.input)
                elif '+' in self.input:
                    op = self.input.index('+')
                    left = self.input.pop(op-1)
                    right = self.input.pop(op)
                    self.input[op-1] = int(left) + int(right)
                    list(filter(None, self.input))
                    print(self.input)
                elif '-' in self.input:
                    op = self.input.index('-')
                    left = self.input.pop(op-1)
                    right = self.input.pop(op)
                    self.input[op-1] = int(left) - int(right)
                    list(filter(None, self.input))
                    print(self.input)
            if len(self.input) == 1:
                solved = True
        self.display_result(self.input[0])              

# display calc
root = Calc()
root.title("Calculator")

# Screen
root.screen = TK.Label(root, text='', bg='white', fg='black', font=('Arial', 20), width=20)
root.screen.place(x=75, y=100)

# Framing
frame = TK.Frame(root)
frame.pack(expand=True, fill=TK.BOTH)

# Center of screen
x = (root.winfo_screenwidth()) // 2
y = (root.winfo_screenheight()) // 2

# Place the frame at center
frame.place(x=80, y=200)


# Number grid
for i in range(1,10):
    row = (i-1) // 3
    col = (i-1) % 3
    button = TK.Button(frame, text=str(i), command = lambda num = i: root.num_click(str(num)), width=10, height=5)
    button.grid(row = row, column=col)
button = TK.Button(frame, text='0', command = lambda:  root.num_click('0'), width=10, height=5)
button.grid(row = 3, column=1)

#Symbols
#Equals
button = TK.Button(frame, text='=', command=root.calculate, width=10, height=5)
button.grid(row =3, column=0)
#Addition
button = TK.Button(frame, text='+', command= lambda: root.symbol_click('+'), width=10, height=5)
button.grid(row =3, column=2)
#Subtraction
button = TK.Button(frame, text='-', command= lambda: root.symbol_click('-'), width=10, height=5)
button.grid(row =2, column=3)
#Multiplication
button = TK.Button(frame, text='x', command= lambda: root.symbol_click('x'), width=10, height=5)
button.grid(row =3, column=3)
#Division
button = TK.Button(frame, text='÷', command= lambda: root.symbol_click('÷'), width=10, height=5)
button.grid(row =1, column=3)
#Clear Screen
button = TK.Button(frame, text='C', command= lambda: root.clear_screen(), width=10, height=5)
button.grid(row =0, column=3)

root.mainloop()
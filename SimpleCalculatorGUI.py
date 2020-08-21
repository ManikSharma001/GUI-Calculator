#This program creates a GUI calculator. 

import tkinter as tk

class calculatorGUI():
    def __init__(self, parent):
        self.parent = parent
        parent.title("Calculator")
        parent.geometry("420x475")
        parent.resizable(0, 0)
        inputText = tk.StringVar()
        previousAnswer = tk.StringVar()

        inputFrame = tk.Frame(parent, width = 500, height = 50, bg = "white").pack(side = "top")
        inputField = tk.Entry(inputFrame, font = ('times new roman', 20, 'bold'), fg = "white", bg = "black", justify = tk.RIGHT, textvariable = inputText, width = 50).pack(side = "top", ipady = 15)

        buttonFrame = tk.Frame(parent, width = 500, height = 500, bg = "black").pack(side = 'bottom')

        def press(self,*args, **kwargs):
            global expression
            expression = ""
            expression = expression + str(self)
            inputText.set(inputText.get() + expression)                                          

        def clear(self, *args, **kwargs):
            global expression
            global previousAnswerLabel
            previousAnswer.set("Ans: " + inputText.get())
            previousAnswerLabel = tk.Label(inputFrame, bg = "black", fg = "white", textvariable = previousAnswer, font = ('lato', 8, 'bold'), justify = tk.LEFT).place(x = 5, y = 55)
            expression = ""
            inputText.set("")

        def equals(self, *args, **kwargs):
            try:
                inputText.set(eval(inputText.get()))
            except ZeroDivisionError:
                inputText.set("Math Error!")
            except TypeError:
                inputText.set("Invalid Syntax!")
            except SyntaxError:
                inputText.set("Invalid Syntax!")

        #Top Row
        clearExpression = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "C", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: clear(" ")).place(x = 5, y = 120)#Using .place() instead of .pack() for all because the buttons must be a certain way
        openBracket = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "(", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press(" ( ")).place(x = 110, y = 120)
        closeBracket = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = ")", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press(" ) ")).place(x = 215, y = 120)
        division = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "÷", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press(" / ")).place(x = 320, y = 120)

        #Second Row
        seven = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "7", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("7")).place(x = 5, y = 190)#Using .place() instead of .pack() for all because the buttons must be a certain way
        eight = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "8", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("8")).place(x = 110, y = 190)
        nine = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "9", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("9")).place(x = 215, y = 190)
        multiplication = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "x", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press(" * ")).place(x = 320, y = 190)

        #Third Row
        four = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "4", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("4")).place(x = 5, y = 260)#Using .place() instead of .pack() for all because the buttons must be a certain way
        five = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "5", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("5")).place(x = 110, y = 260)
        six = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "6", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("6")).place(x = 215, y = 260)
        minus = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "-", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press(" - ")).place(x = 320, y = 260)

        #4th Row
        three = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "1", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("1")).place(x = 5, y = 340)#Using .place() instead of .pack() for all because the buttons must be a certain way
        two = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "2", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("2")).place(x = 110, y = 340)
        one = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "3", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("3")).place(x = 215, y = 340)
        add = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "+", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press(" + ")).place(x = 320, y = 340)

        #5th Row
        zero = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "0", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press("0")).place(x = 5, y = 410)#Using .place() instead of .pack() for all because the buttons must be a certain way
        decimal = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = ".", fg = "white", bg = "gray35", width = 12, height = 3, command = lambda: press(".")).place(x = 110, y = 410)
        equalsSign = tk.Button(buttonFrame, font = ('lato', 9, 'bold'), text = "=", fg = "white", bg = "gray35", width = 27, height = 3, command = lambda: equals("= ")).place(x = 215, y = 410)
            
root = tk.Tk()
calc = calculatorGUI(root)
root.mainloop()

    
    

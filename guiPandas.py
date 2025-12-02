
import tkinter as tk
# import os  #if filedirectory wants current directory like:   initialdir=os.getcwd()
from tkinter import filedialog as fd
import pandas as pd
# may require pip pandas and openpyxl.
class MyWindow(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Test Template.")
      
        label.bind("<1>", self.quit)   
        t1button = tk.Button(self, text="test1", width=10, command=self.t1)
        t2button = tk.Button(self, text="file", width=10, command=self.t2)
        t3button = tk.Button(self, text="t3", width=10, command=self.t3)
        #vars for input text:
        self.my_string_var = tk.StringVar(self, root)
        self.my_string_var.set('Initial Text')
        path1 = tk.Entry(self, textvariable=self.my_string_var)   
        quitButton = tk.Button(self, text="Quit", width=10, command =self.closeWindow)

        label.grid(column = 0, row=0)
        t1button.grid(column=0,row=1)
        t2button.grid(column=0,row=2)
        path1.grid(column=1, row=2)
        t3button.grid(column=0, row=3)
        quitButton.grid(column=0, row=4)

    def quit(self, event=None):
        root.destroy()

    def t1(self):
        print("t1 test") 
       
    def t2(self):
        filepath = fd.askopenfilename(
        initialdir="/home/jim/Downloads/",  # Sets the initial directory (e.g., C:/)
        title="Select a File",
        filetypes=(("excel:", "*.xls *.xlsx *.csv"),("All files", "*.*")) # Filters file types
        )
        print(filepath)
        with open(filepath) as f:
            print(f.read())

    def t3(self):
        # path /home/jim/Documents/tk/pandas/dogs.xlsx
        #excelFile = pd.ExcelFile('/home/jim/Documents/tk/pandas/dogs.xlsx')
        #df1 = excelFile.parse('Sheet1')
        df = pd.read_excel('/home/jim/Documents/tk/pandas/dogs.xlsx')
        dfSorted = df.sort_values(by='name')
        dfInvertSort = df.sort_values(by='name', ascending=False)
        print(dfSorted)
        dfSorted.to_excel("dogsSorted.xlsx")
       
    #### syntax for t3 prev template for input:
    #   def t3(self):
    #       uinput = self.my_string_var.get() 
    #       print(uinput)
  
    def closeWindow(self):
        root.destroy()
        
root = tk.Tk()
root.geometry("400x400")

def linktest(event):
    linkpath = "/home/jim/Documents/tk/pandas/textfile.txt"
    with open(linkpath) as f:
        print(f.read())
    print("link tested")

label2 = tk.Label(root, text="Test 2")
label2.grid(column=4, row=5)
label3 = tk.Label(root, text ="test hyperlink", fg="blue", font="underline", cursor="hand2")
label3.bind("<Button-1>", linktest)
label3.grid(column=0, row=2)

MyWindow(root).grid(column=0,row=0)
root.mainloop()


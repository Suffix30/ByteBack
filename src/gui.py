import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import os
from backpack_analysis import analyze_file

class App:
    def __init__(self, root):
        # Setting title
        root.title("ByteBack: Decompiler Tool")
        # Setting window size
        width = 600
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        # Initialize GUI components
        self.setupUI(root)
    
    def setupUI(self, root):
        # Font for widgets
        font = tkFont.Font(family='Helvetica', size=12, weight='bold')
        
        # Instructions Label
        self.label = tk.Label(root, text="Drag and drop your .exe file here.", font=font)
        self.label.pack(pady=20)
        
        # Drag and Drop Area
        self.drop_area = tk.Label(root, text="Drop Area", width=40, height=10, bg='lightgrey')
        self.drop_area.pack(pady=10)
        self.drop_area.bind('<Button-1>', self.onDragStart)
        
        # Information Display Area
        self.info_area = tk.Text(root, height=10, width=60)
        self.info_area.pack(pady=10)
        
    def onDragStart(self, event):
        # Get the file path from file dialog
        file_path = filedialog.askopenfilename()
        if file_path:
            # Set the file path to the drop area
            self.drop_area['text'] = file_path
            # Call analysis function
            self.analyzeFile(file_path)
    
    def analyzeFile(self, file_path):
        # Call the analyze_file function from backpack_analysis.py
        analysis_results = analyze_file(file_path)
        # Display the analysis results in the info area
        self.displayInfo(analysis_results)
    
    def displayInfo(self, message):
        # Display the message in the info area
        self.info_area.delete('1.0', tk.END)  # Clear previous content
        self.info_area.insert(tk.END, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

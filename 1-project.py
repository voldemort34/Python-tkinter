import tkinter as tk
from tkinter import *

root = tk.Tk()

root.geometry("400x500")
root.title("tk gui project")

label = tk.Label(root, text=" hello world", font=("Arial ", 12))
label.pack(padx=20, pady=40)

textbox = tk.Text(root,height= 3 ,font=("times", 16))
textbox.pack(padx=10, pady=10)

buttonFrame = tk.Frame(root)        # çbuton için çerçeve oluşturuyoruz.
buttonFrame.columnconfigure(0, weight=1) # çerçevenin genişliğini ve kolon sırasını giriyoruz.
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font= ("arial 12 bold"))
btn1.grid(row= 0, column=0, sticky=tk.W + tk.E) #WEST AND EAST

btn2 = tk.Button(buttonFrame, text="2", font= ("arial 12 bold"))
btn2.grid(row= 0, column=1, sticky=tk.W + tk.E) #WEST AND EAST

btn3 = tk.Button(buttonFrame, text="3", font= ("arial 12 bold"))
btn3.grid(row= 0, column=2, sticky=tk.W + tk.E) #WEST AND EAST

btn4= tk.Button(buttonFrame, text="4", font= ("arial 12 bold"))
btn4.grid(row= 1, column=0, sticky=tk.W + tk.E) #WEST AND EAST

btn5 = tk.Button(buttonFrame, text="5", font= ("arial 12 bold"))
btn5.grid(row= 1, column=1, sticky=tk.W + tk.E) #WEST AND EAST

btn6 = tk.Button(buttonFrame, text="6", font= ("arial 12 bold"))
btn6.grid(row= 1, column=2, sticky=tk.W + tk.E) #WEST AND EAST

buttonFrame.pack(fill="x") # x düzleminde frame i  genişletecek


root.mainloop()
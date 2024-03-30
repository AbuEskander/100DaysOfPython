import tkinter as tk

window = tk.Tk()

window.title("First GUI program")
window.minsize(width=500,height=300)

MyLabel = tk.Label(text="I'm a Label")
MyLabel.grid(column=0,row=0)


MyLabel['text'] = 'NewText'



# 


inp = tk.Entry()
TextChange = inp.get()
def Button_Clicked():
    
    MyLabel.config(text=inp.get()) 

inp.grid(column=3,row=3)
Button = tk.Button(text="Click me",command=Button_Clicked)
Button.grid(column=1,row=1)
window.mainloop()
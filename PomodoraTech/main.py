import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    countDown(130)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    countMin = count // 60
    countSec = count % 60
    
    Canvas.itemconfig(TimerText,text=f"{countMin}:{countSec if countSec>=10 else f"0{countSec}"}")
    if count>0:
        Window.after(1000,countDown,count-1)

# ---------------------------- UI SETUP ------------------------------- #
Window = tk.Tk()
Window.title("Pomodoro")
Window.config(padx=100,pady=50,bg=YELLOW)


HeadTitle = tk.Label(text="Timer",font=(FONT_NAME,45,"bold"),bg=YELLOW,fg=GREEN)
HeadTitle.grid(column=1,row=0)
Canvas = tk.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
TomatoImg=tk.PhotoImage(file ="tomato.png")
Canvas.create_image(100,112,image=TomatoImg)
TimerText = Canvas.create_text(100,120,text="00:00",fill="White",font=(FONT_NAME,35,'bold'))


Canvas.grid(column=1,row=1)
startBTN = tk.Button(text="Start",command=startTimer)
startBTN.grid(column=0,row=2)
resetBTN =tk.Button(text="Reset")
resetBTN.grid(column=2,row=2)

CheckMark = tk.Label(text="✔️" ,fg=GREEN,bg=YELLOW,font=(FONT_NAME,14),highlightthickness=0)
CheckMark.grid(column=1,row=3)

Window.mainloop()
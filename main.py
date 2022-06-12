import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    root.after_cancel(timer)
    reps = 0
    name.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    tick.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        name.config(text="Break",fg=RED)
        count_down(long_break_secs)
    elif reps % 2 == 0:
        name.config(text="Break", fg=PINK)
        count_down(short_break_secs)
    else:
        name.config(text="Work", fg=GREEN)
        count_down(work_secs)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text,text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = root.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            root.deiconify()
            tick.config(text=reps//2 * CHECK_MARK)
# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Pomodoro")
root.config(bg=YELLOW, padx=100, pady=50)
name = tk.Label(text="Timer",font=(FONT_NAME,50),bg=YELLOW,fg=GREEN)
name.grid(row=0,column=1)
tomato = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1,column=1)

start = tk.Button(text="Start",relief="groove",highlightthickness=0,command=start_timer)
start.grid(row=3,column=0)
reset = tk.Button(text="Reset",relief="groove",highlightthickness=0,command=reset_timer)
reset.grid(row=3,column=2)
tick = tk.Label(bg=YELLOW,fg=GREEN)
tick.grid(row=4,column=1)
root.mainloop()

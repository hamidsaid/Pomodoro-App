from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    if count >= 0:
        minutes = math.floor(count/60)
        seconds = count%60
        #appending zero to the bigenning of the numb below 10 to match a real timer
        if seconds < 10:
            seconds = f"0{seconds}"
        if minutes < 10:
            minutes = f"0{minutes}"
        #updating the canvas item i.e timer
        canvas.itemconfig(timer_text , text=f"{minutes}:{seconds}")

        if count > 0:
            #put the window.timer ina variable so as we can stop it later
            #using the window.after_cancel method
            global timer
            timer = window.after(1000, count_down, count - 1)
        else:
            start_timer()
            marks = ""
            work_sessions = math.floor(reps / 2)
            for _ in range(work_sessions):
                marks += "✔"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", fg="#000", font=(FONT_NAME, 35), bg=YELLOW)
# label1.config(padx=12,pady=12)
title_label.grid(column=1, row=0)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)

btn_rst = Button(text="Reset" , command=reset_timer)
btn_rst.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(12))
check_marks.grid(column=1, row=3)

window.mainloop()

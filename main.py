from tkinter import *
from tkinter import messagebox, simpledialog

timer = None
countdown = 10
timing = None


def reset_timer(self):
    global timing
    window.after_cancel(timer)
    global countdown
    countdown = timing
    start_timer(countdown)


def start_timer(count):
    new_timer(count)


def new_timer(count):
    count_secs = count * 1
    minute = '00:'
    if count_secs < 10:
        minute = '00:0'
    timer_label.config(text=f'Timer: {minute}{count_secs}')
    if count > 0:
        global timer
        timer = window.after(1000, new_timer, count - 1)
    if count == 0:
        text.delete(1.0, 'end')


def game():
    global timing
    timing = simpledialog.askinteger(title='Session length', prompt='How many seconds?')
    if timing > 15:
        messagebox.showerror(title='Difficulty', message='Input should be a maximum of 15 Seconds')
        game()
    else:
        window.after(2000)
        text.bind("<KeyPress>", reset_timer)
        start_timer(timing)


window = Tk()
window.title("Disappearing Text")
window.config(padx=20, pady=20, bg='#5C5470')

heading_label = Label(text="The Most Dangerous Writing App", font=("courier", 30, "bold"))
heading_label.config(pady=10, padx=0, fg='#FAF0E6', bg='#5C5470')
heading_label.grid(column=0, row=1)

second_heading = Label(text="Don’t stop writing, or all progress will be lost.",
                       font=("Serif", 15, "bold"))
second_heading.config(pady=10, padx=0, fg='#FAF0E6', bg='#5C5470')
second_heading.grid(column=0, row=2)

timer_label = Label(text="Timer: 00:00", font=("Courier", 20, "bold"))
timer_label.config(pady=10, padx=0, fg='#FAF0E6', bg='#5C5470')
timer_label.grid(column=0, row=3)

text = Text(height=10, width=40, font=("Quicksand", 20), wrap="word", pady=80, padx=40)
text.config(pady=20, bg='#FAF0E6', fg='#5C5470')
text.grid(column=0, row=4)

window.wait_visibility()
ready = messagebox.askyesno(title="Welcome to the Speed Typing Test", message="Are you ready to start?")
if ready:
    game()
else:
    window.destroy()

window.mainloop()

from tkinter import *
from globals import *


def program_options():
    ##### WINDOW #######################################################################################################
    new_window = Toplevel()
    window_width = 700
    window_height = 680
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2) - 50)
    y = int((screen_height / 2) - (window_height / 2) - 50)

    new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    new_window.config(background=BACKGROUND)
    new_window.title("Program Options")

    ##### HEADER #######################################################################################################

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()
    header = Label(new_window,
                   text="Program Options", font=("Noto Sans", 30, "bold"), fg=fHEADER, bg=HEADER, padx=18)
    header.pack()
    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    ##### YEAR RANGE ###################################################################################################

    Label(new_window, font=("Noto Sans HK", 28, "bold"), text="Year Range", fg=fBACKGROUND, bg=BACKGROUND).pack()
    START_v = IntVar()
    END_v = IntVar()

    class ScrollScale(Scale):  # adds mouse wheel scroll functionality to spinbox
        def __init__(self, *args, **kwargs):
            Scale.__init__(self, *args, **kwargs)
            self.bind('<MouseWheel>', self.mousewheel)
            self.bind('<Button-4>', self.mousewheel)
            self.bind('<Button-5>', self.mousewheel)

        def mousewheel(self, event):
            if event.num == 5 or event.delta == -120:
                self.set(self.get() - 100)
            elif event.num == 4 or event.delta == 120:
                self.set(self.get() + 100)

    def set_end(*args):
        new_end_value = start_scale.get() + 1
        if end_scale.get() < start_scale.get():
            end_scale.set(new_end_value)

    def set_start(*args):
        new_start_value = end_scale.get() - 1
        if start_scale.get() > end_scale.get():
            start_scale.set(new_start_value)

    larger_range = BooleanVar()

    def range_edit(start, end):
        with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            lines = f.readlines()  # returns list with each line in the file as a list item
        start_year = lines[8]
        end_year = lines[9]
        is_large = False
        if start_year.strip() < "1800" or end_year.strip() > "2200" or start.get() < 1800 or end.get() > 2200:
            is_large = True
        if not is_large:
            start.config(from_=1800, to=2200, tickinterval=100)
            end.config(from_=1800, to=2200, tickinterval=100)
        if is_large or larger_range.get():
            if not larger_range.get():
                if start.get() < 1800 or start.get() > 2200:
                    start.set(1800)
                if end.get() > 2200 or end.get() < 1800:
                    end.set(2200)
                start.config(from_=1800, to=2200, tickinterval=100)
                end.config(from_=1800, to=2200, tickinterval=100)
            else:
                start.config(from_=1000, to=9999, tickinterval=2000)
                end.config(from_=1000, to=9999, tickinterval=2000)
        start.grid(row=0, column=1)
        end.grid(row=1, column=1)
        return start, end

    range_frame = Frame(new_window)
    start_scale = ScrollScale(range_frame, from_=1800, to=2200, length=500, orient=HORIZONTAL,
                              tickinterval=100,
                              font=("Noto Sans", 20), variable=START_v, command=set_end)
    end_scale = ScrollScale(range_frame, from_=1800, to=2200, length=500, orient=HORIZONTAL, tickinterval=100,
                            font=("Noto Sans", 20), variable=END_v, command=set_start)

    larger_range_box = Checkbutton(new_window, text="Extend Range", variable=larger_range, onvalue=True, offvalue=False,
                                   font=("Noto Sans", 14), command=lambda: range_edit(start_scale, end_scale),
                                   fg=fBACKGROUND, bg=BACKGROUND, activebackground=BACKGROUND)
    larger_range_box.pack()

    Label(range_frame, font=("Noto Sans", 20), text="Start: ").grid(row=0, column=0)

    start_scale.grid(row=0, column=1)
    end_scale.grid(row=1, column=1)

    start_scale, end_scale = range_edit(start_scale, end_scale)
    start_scale.grid(row=0, column=1)
    start_scale.set(START_YEAR)

    def left(scale):
        scale.set(scale.get() - 1)

    def right(scale):
        scale.set(scale.get() + 1)

    leftarrow = Button(range_frame, text="⯇", font=("Noto Sans", 16), command=lambda: left(start_scale))
    leftarrow.grid(row=0, column=2)
    rightarrow = Button(range_frame, text="⯈", font=("Noto Sans", 16), command=lambda: right(start_scale))
    rightarrow.grid(row=0, column=3)

    Label(range_frame, font=("Noto Sans", 20), text="End: ").grid(row=1, column=0)
    end_scale.grid(row=1, column=1)
    end_scale.set(END_YEAR)
    range_frame.pack()

    leftarrow2 = Button(range_frame, text="⯇", font=("Noto Sans", 16), command=lambda: left(end_scale))
    leftarrow2.grid(row=1, column=2)
    rightarrow2 = Button(range_frame, text="⯈", font=("Noto Sans", 16), command=lambda: right(end_scale))
    rightarrow2.grid(row=1, column=3)

    Label(new_window, bg=BACKGROUND, height=1).pack()

    ##### 24 HOUR TIME #################################################################################################

    hr_frame = Frame(new_window)
    HR24_var = StringVar()
    Label(hr_frame, font=("Noto Sans HK", 24), text="Hour Notation: ", fg=fBACKGROUND, bg=BACKGROUND, pady=5)\
        .grid(row=0, column=0)
    radiobutton_12 = Radiobutton(hr_frame, text="12-hour clock", font=("Noto Sans HK", 20), variable=HR24_var,
                                 value="12hr")
    radiobutton_24 = Radiobutton(hr_frame, text="24-hour clock", font=("Noto Sans HK", 20), variable=HR24_var,
                                 value="24hr")
    radiobutton_12.grid(row=0, column=1)
    Label(hr_frame, font=("Noto Sans HK", 28), text=" ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0, column=2)
    radiobutton_24.grid(row=0, column=3)
    hr_frame.pack()

    if HR24 == "12hr":
        radiobutton_12.select()
        radiobutton_24.deselect()
    elif HR24 == "24hr":
        radiobutton_12.deselect()
        radiobutton_24.select()

    ####### OTHER FUNCTIONS ############################################################################################

    Label(new_window, bg=BACKGROUND, height=1).pack()

    def reset():
        start_scale.set(1980)
        end_scale.set(2040)
        radiobutton_12.select()
        radiobutton_24.deselect()

    Button(new_window, text="Reset to Defaults", font=("Noto Sans", 25, "bold"), command=reset).pack()

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()
    Label(new_window, font=("Noto Sans HK", 18), text="Restart for changes to take effect.", fg=fBACKGROUND,
          bg=BACKGROUND).pack()
    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    def on_closing():
        with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            lines = f.readlines()  # returns list with each line in the file as a list item
        lines[8] = f"{START_v.get()}\n"
        lines[9] = f"{END_v.get()}\n"
        lines[10] = f"{HR24_var.get()}\n"
        with open(config_location, "w", encoding="utf8") as f:
            f.writelines(lines)
        new_window.destroy()

    new_window.protocol("WM_DELETE_WINDOW", on_closing)

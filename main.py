import sys
from tkinter import *
from number_converters import *
from language_options import language_options
from program_options import program_options
from display_options import display_options
from globals import *
from tts import tts, audio_options, init_volume_rate
import random
import datetime

year = ""
month = ""
day = ""
weekday = ""
hour = ""
minutes = ""
am_pm = ""


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


icon_path = resource_path("app_icon_dark.png")


def generate_date():
    global year
    global month
    global day
    global weekday

    year = str(random.randint(START_YEAR, END_YEAR))
    stryear = year_converter(year)

    month = str(random.randint(1, 12))
    strmonth = md_converter(month)
    month = english_month(month)

    day = str(random.randint(1, 31))
    strday = md_converter(day)

    global year_number
    year_number.config(text=stryear)
    global month_number
    month_number.config(text=strmonth)
    global day_number
    day_number.config(text=strday)

    chosen_weekday_sign = random.choice(("星期", "禮拜"))
    weekday = str(random.randint(1, 7))

    strweekday = number_converter(weekday)
    strweekday, weekday = english_weekday(strweekday, weekday)

    global weekday_label
    weekday_label.config(text=chosen_weekday_sign)
    global weekday_number
    weekday_number.config(text=strweekday)


def generate_time():
    global hour
    global minutes

    chosen_time_period = ""

    if HR24 == "12hr":
        hour = str(random.randint(1, 12))

        periods = ["上晝", "下晝", "晏晝"]
        chosen_time_period = str(random.choices(periods, weights=[8, 8, 1]))[2:-2]

        global am_pm
        if chosen_time_period == "上晝" or chosen_time_period == "晏晝":
            am_pm = "a.m."
        elif chosen_time_period == "下晝":
            am_pm = "p.m."

        global time_period
        time_period.config(text=chosen_time_period)

    elif HR24 == "24hr":
        hour = str(random.randint(0, 23))

    strhour = hour_converter(hour)

    minutes = str(random.randint(0, 59))
    if random.randint(1, 10) > 4:
        rounded = round(int(minutes) / 5)  # round to the nearest multiple of five
        if rounded == 12:
            rounded = 0
        minutes = str(rounded * 5)
        strminutes, minute_unit = five_minutes_converter(str(rounded))
    else:
        strminutes, minute_unit = minutes_converter(minutes)

    global hour_label
    global minute_label
    global hour_number
    global minute_number
    if chosen_time_period == "晏晝":
        hour = "12"
        minutes = "0"
        minute_unit = strhour = strminutes = ""
        hour_label.config(text="")
    else:
        hour_label.config(text="點")

    hour_number.config(text=strhour)
    minute_number.config(text=strminutes)
    minute_label.config(text=minute_unit)


def generate_new(*args):
    generate_date()
    generate_time()


###### WINDOW ##########################################################################################################

window = Tk()

window_width = 1120
window_height = 760
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2) - 50)
y = int((screen_height / 2) - (window_height / 2) - 50)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.config(background=BACKGROUND)
window.title("Date and Time Generator")

icon = PhotoImage(file=icon_path)
window.iconphoto(True, icon)

Label(window, bg=BACKGROUND, height=1).pack()

###### MENU BAR ########################################################################################################

menubar = Menu(window)
window.config(menu=menubar)

settings = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", menu=settings)
settings.add_command(label="Language Options", command=language_options)
settings.add_command(label="Program Options", command=program_options)
settings.add_command(label="Display Options", command=display_options)
settings.add_command(label="Audio Options", command=audio_options)
settings.add_separator()
settings.add_command(label="Reset All Settings to Default", command=reset_all)
settings.add_separator()
settings.add_command(label="Exit", command=window.destroy)

###### HEADER ##########################################################################################################

header = Label(window,
               text="DATE AND TIME — 日期和時間",
               font=("Noto Sans", 30, "bold"),
               fg=fHEADER,
               bg=HEADER,
               padx=18)
header.pack()
Label(window, bg=BACKGROUND, height=1).pack()

###### DATE ############################################################################################################

date = Frame(window)

year_number = Label(date, font=("Noto Sans HK", 60), width=7, fg=fDATE, bg=DATE)
year_label = Label(date, text="年", font=("Noto Sans HK", 60, "bold"), fg=fDATE_LABEL, bg=DATE_LABEL)
year_number.grid(row=0, column=0)
year_label.grid(row=0, column=1)

Label(date, font=("Noto Sans HK", 60), text=" ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0, column=2)

month_number = Label(date, font=("Noto Sans HK", 60), width=4, fg=fDATE, bg=DATE)
month_label = Label(date, text="月", font=("Noto Sans HK", 60, "bold"), fg=fDATE_LABEL, bg=DATE_LABEL)
month_number.grid(row=0, column=3)
month_label.grid(row=0, column=4)

Label(date, font=("Noto Sans HK", 60), text=" ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0, column=5)

SW_DAY = "號" if SW == "spoken" else "日"

day_number = Label(date, font=("Noto Sans HK", 60), width=5, fg=fDATE, bg=DATE)
day_label = Label(date, text=SW_DAY, font=("Noto Sans HK", 60, "bold"), fg=fDATE_LABEL, bg=DATE_LABEL)
day_number.grid(row=0, column=6)
day_label.grid(row=0, column=7)

date.pack()
Label(window, bg=BACKGROUND, height=1).pack()

###### WEEKDAY #########################################################################################################

weekday_frame = Frame(window)
weekday_label = Label(weekday_frame, font=("Noto Sans HK", 50, "bold"), width=4, fg=fWEEKDAY_LABEL, bg=WEEKDAY_LABEL)
weekday_number = Label(weekday_frame, font=("Noto Sans HK", 50), width=2, fg=fWEEKDAY, bg=WEEKDAY)
weekday_label.grid(row=0, column=0)
weekday_number.grid(row=0, column=1)

weekday_frame.pack()
Label(window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

###### TIME ############################################################################################################

time = Frame(window)

time_period = Label(time, font=("Noto Sans HK", 50, "bold"), width=4, fg=fTIME_LABEL, bg=TIME_LABEL)
Label(time, font=("Noto Sans HK", 50), text=" ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0, column=1)
if HR24 == "12hr":
    time_period.grid(row=0, column=0)

hour_number = Label(time, font=("Noto Sans HK", 50), width=4, fg=fTIME, bg=TIME)
if HR24 == "24hr":
    hour_number = Label(time, font=("Noto Sans HK", 50), width=6, fg=fTIME, bg=TIME)
hour_label = Label(time, font=("Noto Sans HK", 50, "bold"), width=2, fg=fTIME_LABEL, bg=TIME_LABEL)
hour_number.grid(row=0, column=2)
hour_label.grid(row=0, column=3)

Label(time, font=("Noto Sans HK", 50), text=" ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0, column=4)

minute_number = Label(time, font=("Noto Sans HK", 50), width=6, fg=fTIME, bg=TIME)
minute_label = Label(time, text="點", font=("Noto Sans HK", 50, "bold"), width=4, fg=fTIME_LABEL, bg=TIME_LABEL)
minute_number.grid(row=0, column=5)
minute_label.grid(row=0, column=6)

time.pack()

Label(window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

###### HEADER ##########################################################################################################

header2 = Label(window,
                text="Enter the date and time shown above:",
                font=("Noto Sans", 20),
                fg=fHEADER,
                bg=HEADER,
                padx=18)
header2.pack()
Label(window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

###### USER INPUTS #####################################################################################################
user_inputs = Frame(window)

user_weekday = StringVar()
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
weekday_selector = OptionMenu(user_inputs, user_weekday, *weekdays)
user_weekday.set("Thursday")
weekday_selector.config(font=("Noto Sans", 30))
weekday_selector.config(width=9)
weekday_selector.grid(row=0, column=0)


class ScrollSpinbox(Spinbox):  # adds mouse wheel scroll functionality to spinbox
    def __init__(self, *args, **kwargs):
        Spinbox.__init__(self, *args, **kwargs)
        self.bind('<MouseWheel>', self.mousewheel)
        self.bind('<Button-4>', self.mousewheel)
        self.bind('<Button-5>', self.mousewheel)

    def mousewheel(self, event):
        if event.num == 5 or event.delta == -120:
            self.invoke('buttondown')
        elif event.num == 4 or event.delta == 120:
            self.invoke('buttonup')


user_day = IntVar()


def test_char(self, a):  # check if input is digit
    if a == '1':  # insert
        if not self.isdigit():
            return False
    return True


day_selector = ScrollSpinbox(user_inputs, textvariable=user_day, font=("Noto Mono", 30), width=3, from_=1, to=31,
                             format="%2.0f")
day_selector.config(validate="key", validatecommand=(day_selector.register(test_char), '%P', '%d'))
# check if input is digit           ^^^
user_day.set(int(((day_selector["from"] - day_selector["to"]) / 2) + day_selector["to"]))  # set to midway value
day_selector.grid(row=0, column=1)

user_month = StringVar()
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December")
month_selector = OptionMenu(user_inputs, user_month, *months)
user_month.set("January")
month_selector.config(font=("Noto Sans", 30))
month_selector.config(width=9)
month_selector.grid(row=0, column=2)

user_year = IntVar()

year_selector = ScrollSpinbox(user_inputs, textvariable=user_year, font=("Noto Mono", 30), width=5, from_=START_YEAR,
                              to=END_YEAR)
year_selector.config(validate="key", validatecommand=(year_selector.register(test_char), '%P', '%d'))
user_year.set(int(((year_selector["from"] - year_selector["to"]) / 2) + year_selector["to"]))  # set to midway value
year_selector.grid(row=0, column=3)

user_inputs.pack()
Label(window, bg=BACKGROUND, height=1).pack()

###### TIME INPUTS #####################################################################################################

user_hour = StringVar()
user_minutes = StringVar()

time_inputs = Frame(window)

hour_selector = ScrollSpinbox(time_inputs, textvariable=user_hour, font=("Noto Mono", 30), width=3, from_=1, to=12)
if HR24 == "24hr":
    hour_selector = ScrollSpinbox(time_inputs, textvariable=user_hour, font=("Noto Mono", 30), width=3, from_=0, to=23)

user_hour.set(str(int(((hour_selector["from"] - hour_selector["to"]) / 2) + hour_selector["to"])))  # set to midway val
hour_selector.config(format="%2.0f", validate="key", validatecommand=(hour_selector.register(test_char), '%P', '%d'))
if HR24 == "24hr":
    hour_selector.config(format="%02.0f")
hour_selector.grid(row=0, column=0)

Label(time_inputs, font=("Noto Mono", 30), text=":").grid(row=0, column=1)
minute_selector = ScrollSpinbox(time_inputs, textvariable=user_minutes, font=("Noto Mono", 30), width=3, from_=00,
                                to=59)
user_minutes.set(str(int(((minute_selector["from"] - minute_selector["to"]) / 2) + minute_selector["to"])))
minute_selector.config(format="%02.0f", validate="key",
                       validatecommand=(minute_selector.register(test_char), '%P', '%d'))
minute_selector.grid(row=0, column=2)
time_inputs.pack()

if HR24 == "12hr":
    user_time_p = StringVar()
    time_p_selector = OptionMenu(time_inputs, user_time_p, "a.m.", "p.m.")
    user_time_p.set("a.m.")
    time_p_selector.config(font=("Noto Sans", 30))
    time_p_selector.config(width=4)
    time_p_selector.grid(row=0, column=3)
    Label(time_inputs, font=("Noto Sans", 40), text="  ", bg=BACKGROUND).grid(row=0, column=4)
elif HR24 == "24hr":
    Label(time_inputs, font=("Noto Sans", 40), text="  ", bg=BACKGROUND).grid(row=0, column=3)


def submit_user(*args):
    weekday_right = False
    day_right = False
    month_right = False
    year_right = False

    if user_weekday.get() == weekday:
        weekday_right = True
    if str(user_day.get()) == day:
        day_right = True
    if user_month.get() == month:
        month_right = True
    if str(user_year.get()) == year:
        year_right = True

    hour_right = False
    minutes_right = False
    time_p_right = False

    if str(int(user_hour.get())) == hour:
        hour_right = True
    if str(int(user_minutes.get())) == minutes:
        minutes_right = True
    if HR24 == "12hr":
        if user_time_p.get() == am_pm:
            time_p_right = True

    if HR24 == "12hr":
        if weekday_right and day_right and month_right and year_right and hour_right and minutes_right and time_p_right:
            messagebox.showinfo(title="Submit", message=f"Weekday : {weekday_right}\n"
                                                        f"Day : {day_right}\n"
                                                        f"Month : {month_right}\n"
                                                        f"Year : {year_right}\n"
                                                        f"Hour : {hour_right}\n"
                                                        f"Minutes : {minutes_right}\n"
                                                        f"Time Period : {time_p_right}\n\n"
                                                        f"Well done!")
            generate_new()
        else:
            messagebox.showinfo(title="Submit", message=f"Weekday : {weekday_right}\n"
                                                        f"Day : {day_right}\n"
                                                        f"Month : {month_right}\n"
                                                        f"Year : {year_right}\n"
                                                        f"Hour : {hour_right}\n"
                                                        f"Minutes : {minutes_right}\n"
                                                        f"Time Period : {time_p_right}\n\n"
                                                        f"Try again!")
    elif HR24 == "24hr":
        if weekday_right and day_right and month_right and year_right and hour_right and minutes_right:
            messagebox.showinfo(title="Submit", message=f"Weekday : {weekday_right}\n"
                                                        f"Day : {day_right}\n"
                                                        f"Month : {month_right}\n"
                                                        f"Year : {year_right}\n"
                                                        f"Hour : {hour_right}\n"
                                                        f"Minutes : {minutes_right}\n\n"
                                                        f"Well done!")
            generate_new()
        else:
            messagebox.showinfo(title="Submit", message=f"Weekday : {weekday_right}\n"
                                                        f"Day : {day_right}\n"
                                                        f"Month : {month_right}\n"
                                                        f"Year : {year_right}\n"
                                                        f"Hour : {hour_right}\n"
                                                        f"Minutes : {minutes_right}\n\n"
                                                        f"Try again!")


def show_answer(*args):
    global user_weekday
    global user_day
    global user_month
    global user_year
    global user_hour
    global user_minutes
    global user_time_p

    user_weekday.set(weekday)
    user_day.set(int(day))
    user_month.set(month)
    user_year.set(int(year))

    user_hour.set(hour)
    if HR24 == "12hr":
        user_hour.set(hour)
        hour_selector.config(format="%2.0f")
    else:
        user_hour.set(hour.zfill(2))
    user_minutes.set(minutes.zfill(2))
    if HR24 == "12hr":
        user_time_p.set(am_pm)


def current_date():
    global year
    global month
    global day
    global weekday

    x = datetime.datetime.now()
    year = str(x.strftime("%Y"))
    stryear = year_converter(year)

    month = str(int((x.strftime("%m"))))
    strmonth = md_converter(month)
    month = english_month(month)

    day = str(int(x.strftime("%d")))
    strday = md_converter(day)

    global year_number
    year_number.config(text=stryear)
    global month_number
    month_number.config(text=strmonth)
    global day_number
    day_number.config(text=strday)

    chosen_weekday_sign = random.choice(("星期", "禮拜"))
    weekday = str((x.strftime("%u")))

    strweekday = number_converter(weekday)
    strweekday, weekday = english_weekday(strweekday, weekday)

    global weekday_label
    weekday_label.config(text=chosen_weekday_sign)
    global weekday_number
    weekday_number.config(text=strweekday)


def current_time():
    global hour
    global minutes

    x = datetime.datetime.now()

    if HR24 == "12hr":
        hour = str(int(x.strftime("%I")))
        chosen_time_period = str(x.strftime("%p"))
        if chosen_time_period == "AM":
            chosen_time_period = "上晝"
        else:
            chosen_time_period = "下晝"

        global am_pm
        if chosen_time_period == "上晝" or chosen_time_period == "晏晝":
            am_pm = "a.m."
        elif chosen_time_period == "下晝":
            am_pm = "p.m."

        global time_period
        time_period.config(text=chosen_time_period)

    elif HR24 == "24hr":
        hour = str(x.strftime("%H"))

    strhour = hour_converter(hour)

    minutes = str(int(x.strftime("%M")))
    if (int(minutes) % 5) == 0:
        rounded = round(int(minutes) / 5)  # round to the nearest multiple of five
        if rounded == 12:
            rounded = 0
        strminutes, minute_unit = five_minutes_converter(str(rounded))
    else:
        strminutes, minute_unit = minutes_converter(minutes)

    global hour_label
    global minute_label
    global hour_number
    global minute_number
    hour_label.config(text="點")

    hour_number.config(text=strhour)
    minute_number.config(text=strminutes)
    minute_label.config(text=minute_unit)


def current_datetime(*args):
    current_date()
    current_time()
    show_answer()


submit = Button(time_inputs, text="Submit", font=("Noto Sans", 25, "bold"), command=submit_user)
submit.grid(row=0, column=5)
Label(time_inputs, font=("Noto Sans", 40), text="  ", bg=BACKGROUND).grid(row=0, column=6)
show_ans_button = Button(time_inputs, text="Show Answer", font=("Noto Sans", 18), command=show_answer)
show_ans_button.grid(row=0, column=7)

generate_new()

from PIL import Image, ImageTk

volume_icon_path = resource_path("audio_icon.png")

icon = ImageTk.PhotoImage(Image.open(volume_icon_path).resize((80, 80)))  # the one-liner I used in my app
vol_icon = Button(window, image=icon, command=lambda a=year_number.cget("text"), b=year_label.cget("text"),
                                                     c=month_number.cget("text"), d=month_label.cget("text"),
                                                     e=day_number.cget("text"), f=day_label.cget("text"),
                                                     g=weekday_label.cget("text"), h=weekday_number.cget("text"),
                                                     k=time_period.cget("text"), l=hour_number.cget("text"),
                                                     m=hour_label.cget("text"),
                                                     n=minute_number.cget("text"),
                                                     p=minute_label.cget("text"): tts(a, b, c, d, e, f, g, h, k, l, m,
                                                                                      n, p))
vol_icon.image = icon
vol_icon.place(relx=1, rely=0, anchor="ne")

init_volume_rate()

window.bind("<n>", generate_new)
window.bind("<b>", show_answer)
window.bind("<c>", current_datetime)
window.bind("<Return>", submit_user)
window.bind("<s>", lambda event, a=year_number.cget("text"), b=year_label.cget("text"),
                          c=month_number.cget("text"), d=month_label.cget("text"),
                          e=day_number.cget("text"), f=day_label.cget("text"),
                          g=weekday_label.cget("text"), h=weekday_number.cget("text"),
                          k=time_period.cget("text"), l=hour_number.cget("text"), m=hour_label.cget("text"),
                          n=minute_number.cget("text"),
                          p=minute_label.cget("text"): tts(a, b, c, d, e, f, g, h, k, l, m, n, p))
window.bind("<1>", lambda event: event.widget.focus_set())  # create a binding to move the focus to the window when
# you click on it

window.mainloop()

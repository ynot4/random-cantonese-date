import pyttsx3
from tkinter import *
from globals import *

engine = pyttsx3.init()  # initialize text-to-speech engine


def audio_options():
    new_window = Toplevel()
    window_width = 800
    window_height = 680
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2) - 50)
    y = int((screen_height / 2) - (window_height / 2) - 50)

    new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    new_window.config(background=BACKGROUND)
    new_window.title("Audio Options")

    ##### HEADER #######################################################################################################

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()
    header = Label(new_window,
                   text="Audio Options", font=("Noto Sans", 30, "bold"), fg=fHEADER, bg=HEADER, padx=18)
    header.pack()
    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

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

    ###### SPEAKING RATE ###############################################################################################
    def set_rate(*args):
        engine.setProperty("rate", TTSRATE_v.get())

    rframe = Frame(new_window)
    TTSRATE_v = IntVar()
    Label(rframe, font=("Noto Sans HK", 24), text="Speaking Rate:   ").grid(row=0, column=0)
    rate = ScrollScale(rframe, from_=10, to=400, length=500, orient=HORIZONTAL,
                       tickinterval=50, font=("Noto Sans", 20), variable=TTSRATE_v, command=set_rate)
    rate.set(TTSRATE)
    rate.grid(row=0, column=1)
    rframe.pack()

    ####### OTHER FUNCTIONS ############################################################################################

    Label(new_window, bg=BACKGROUND, height=1).pack()

    def reset():
        rate.set(100)

    Button(new_window, text="Reset to Defaults", font=("Noto Sans", 25, "bold"), command=reset).pack()

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()
    Label(new_window, font=("Noto Sans HK", 18), text="Restart for changes to take effect.", fg=fBACKGROUND,
          bg=BACKGROUND).pack()
    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    def on_closing():
        with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            lines = f.readlines()  # returns list with each line in the file as a list item
        lines[23] = f"{TTSRATE_v.get()}\n"
        with open(config_location, "w", encoding="utf8") as f:
            f.writelines(lines)
        new_window.destroy()

    new_window.protocol("WM_DELETE_WINDOW", on_closing)


###### TEXT TO SPEECH ##################################################################################################
def tts(year_number, year_label, month_number, month_label, day_number, day_label, weekday_label, weekday_number,
        time_period, hour_number, hour_label, minute_number, minute_label):
    text = year_number + year_label, month_number + month_label, day_number + day_label, weekday_label + \
           weekday_number, time_period, hour_number + hour_label, minute_number + minute_label

    engine.say(str(text))  # adds an utterance to speak to the event queue
    engine.runAndWait()  # runs the actual event loop until all commands queued up
    engine.stop()

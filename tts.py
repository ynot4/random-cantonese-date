import pyttsx3
from tkinter import *
from globals import *

engine = pyttsx3.init()  # initialize text-to-speech engine


def init_volume_rate():
    engine.setProperty("volume", int(TTSVOLUME) / 100)
    engine.setProperty("rate", TTSRATE)

    voices = engine.getProperty("voices")  # getting details of current voice
    if TTSGENDER == "male":
        engine.setProperty("voice", voices[4].id)  # changing index, changes voices
    elif TTSGENDER == "female":
        engine.setProperty("voice", voices[0].id)  # changing index, changes voices


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

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    ###### VOLUME ######################################################################################################

    def set_volume(*args):
        engine.setProperty("volume", TTSVOLUME_v.get() / 100)

    vframe = Frame(new_window)
    TTSVOLUME_v = IntVar()
    Label(vframe, font=("Noto Sans HK", 24), text="Volume:   ").grid(row=0, column=0)
    volume = ScrollScale(vframe, from_=0, to=100, length=500, orient=HORIZONTAL,
                         tickinterval=20, font=("Noto Sans", 20), variable=TTSVOLUME_v, command=set_volume)
    volume.set(TTSVOLUME)
    volume.grid(row=0, column=1)
    vframe.pack()

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    ###### GENDER ######################################################################################################

    def gender():
        voices = engine.getProperty("voices")  # getting details of current voice
        if TTSGENDER_v.get() == "male":
            engine.setProperty("voice", voices[4].id)  # changing index, changes voices
        elif TTSGENDER_v.get() == "female":
            engine.setProperty("voice", voices[0].id)  # changing index, changes voices

    gframe = Frame(new_window)
    TTSGENDER_v = StringVar()
    Label(gframe, font=("Noto Sans HK", 28), text="Voice: ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0,
                                                                                                 column=0)
    radiobutton_m = Radiobutton(gframe, text="Male", font=("Noto Sans HK", 20), variable=TTSGENDER_v,
                                value="male", command=gender)
    radiobutton_f = Radiobutton(gframe, text="Female", font=("Noto Sans HK", 20), variable=TTSGENDER_v,
                                value="female", command=gender)
    radiobutton_m.grid(row=0, column=1)
    Label(gframe, font=("Noto Sans HK", 28), text=" ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0, column=2)
    radiobutton_f.grid(row=0, column=3)
    gframe.pack()

    if TTSGENDER == "male":
        radiobutton_m.select()
        radiobutton_f.deselect()
    elif TTSGENDER == "female":
        radiobutton_m.deselect()
        radiobutton_f.select()

    ####### OTHER FUNCTIONS ############################################################################################

    Label(new_window, bg=BACKGROUND, height=1).pack()

    def reset():
        rate.set(200)
        volume.set(100)
        radiobutton_m.deselect()
        radiobutton_f.select()

    Button(new_window, text="Reset to Defaults", font=("Noto Sans", 25, "bold"), command=reset).pack()

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()
    Label(new_window, font=("Noto Sans HK", 18), text="Restart for changes to take effect.", fg=fBACKGROUND,
          bg=BACKGROUND).pack()
    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    def on_closing():
        with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            lines = f.readlines()  # returns list with each line in the file as a list item
        lines[23] = f"{TTSRATE_v.get()}\n"
        lines[24] = f"{TTSVOLUME_v.get()}\n"
        lines[25] = f"{TTSGENDER_v.get()}\n"
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

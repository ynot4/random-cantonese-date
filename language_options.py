from tkinter import *
from globals import *


def language_options():
    ##### WINDOW #######################################################################################################
    new_window = Toplevel()
    window_width = 700
    window_height = 420
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2) - 50)
    y = int((screen_height / 2) - (window_height / 2) - 50)

    new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    new_window.config(background=BACKGROUND)
    new_window.title("Language Options")

    ##### HEADER #######################################################################################################

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()
    header = Label(new_window,
                   text="Language Options", font=("Noto Sans", 30, "bold"), fg=fHEADER, bg=HEADER, padx=18)
    header.pack()
    Label(new_window, bg=BACKGROUND, height=1).pack()

    ##### ZERO OPTIONS #################################################################################################

    zero_frame = Frame(new_window)
    ZERO_v = StringVar()
    Label(zero_frame, font=("Noto Sans HK", 28), text="Zero Style: ", fg=fBACKGROUND, bg=BACKGROUND)\
        .grid(row=0, column=0)
    radiobutton_s = Radiobutton(zero_frame, text="Simplified (〇)", font=("Noto Sans SC", 20), variable=ZERO_v,
                                value="〇")
    radiobutton_t = Radiobutton(zero_frame, text="Traditional (零)", font=("Noto Sans HK", 20), variable=ZERO_v,
                                value="零")
    radiobutton_s.grid(row=0, column=1)
    Label(zero_frame, font=("Noto Sans HK", 28), text=" ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0, column=2)
    radiobutton_t.grid(row=0, column=3)
    zero_frame.pack()

    if ZERO == "〇":
        radiobutton_s.select()
        radiobutton_t.deselect()
    elif ZERO == "零":
        radiobutton_s.deselect()
        radiobutton_t.select()

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    ##### SPOKEN / WRITTEN CHINESE #####################################################################################

    sw_frame = Frame(new_window)
    SW_button_var = StringVar()
    Label(sw_frame, font=("Noto Sans HK", 28), text="Chinese: ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0, column=0)
    radiobutton_sp = Radiobutton(sw_frame, text="Spoken", font=("Noto Sans HK", 20), variable=SW_button_var,
                                 value="spoken")
    radiobutton_w = Radiobutton(sw_frame, text="Written", font=("Noto Sans HK", 20), variable=SW_button_var,
                                value="written")
    radiobutton_sp.grid(row=0, column=1)
    Label(sw_frame, font=("Noto Sans HK", 28), text=" ", fg=fBACKGROUND, bg=BACKGROUND).grid(row=0, column=2)
    radiobutton_w.grid(row=0, column=3)
    sw_frame.pack()

    if SW == "spoken":
        radiobutton_sp.select()
        radiobutton_w.deselect()
    elif SW == "written":
        radiobutton_sp.deselect()
        radiobutton_w.select()

    ##### OTHER FUNCTIONS ##############################################################################################

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    def reset():
        radiobutton_s.deselect()
        radiobutton_t.select()
        radiobutton_sp.deselect()
        radiobutton_w.select()

    Button(new_window, text="Reset to Defaults", font=("Noto Sans", 25, "bold"), command=reset).pack()

    Label(new_window, bg=BACKGROUND, height=1).pack()
    Label(new_window, font=("Noto Sans HK", 18), text="Restart for changes to take effect.", fg=fBACKGROUND,
          bg=BACKGROUND).pack()
    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    def on_closing():
        with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            lines = f.readlines()  # returns list with each line in the file as a list item
        lines[13] = f"{ZERO_v.get()}\n"
        lines[14] = f"{SW_button_var.get()}\n"
        with open(config_location, "w", encoding="utf8") as f:
            f.writelines(lines)
        new_window.destroy()

    new_window.protocol("WM_DELETE_WINDOW", on_closing)

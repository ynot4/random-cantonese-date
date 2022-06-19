from tkinter import *
from tkinter import colorchooser
from globals import *


def display_options():
    ##### WINDOW #######################################################################################################
    new_window = Toplevel()
    window_width = 700
    window_height = 750
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2) - 50)
    y = int((screen_height / 2) - (window_height / 2) - 50)

    new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    new_window.config(background=BACKGROUND)
    new_window.title("Display Options")

    ##### HEADER #######################################################################################################

    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()
    header = Label(new_window,
                   text="Display Options", font=("Noto Sans", 30, "bold"), fg=fHEADER, bg=HEADER, padx=18)
    header.pack()
    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    ##### COLOURCHOOSERS ###############################################################################################
    def get_font_colour(hex, line):
        black = "#000000"
        white = "#ffffff"
        h = hex.lstrip('#')
        rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # hex to rgb converter
        if (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]) <= 60:  # formula calculates luminance
            font_colour = white  # if dark bg colour set font to bright white
        else:
            font_colour = black
        with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            lines = f.readlines()  # returns list with each line in the file as a list item
        lines[line] = f"{font_colour}\n"
        with open(config_location, "w", encoding="utf8") as f:
            f.writelines(lines)
        return font_colour

    def select_colour(line_i, button):
        colour = colorchooser.askcolor(parent=new_window)
        colour_hex = colour[1]
        if colour_hex:
            with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
                lines = f.readlines()  # returns list with each line in the file as a list item
            lines[line_i] = f"{colour_hex}\n"
            font_colour = get_font_colour(str(colour_hex), line_i + 15)
            with open(config_location, "w", encoding="utf8") as f:
                f.writelines(lines)
            button.config(text=colour_hex, fg=font_colour, bg=colour_hex)

    cc_frame = Frame(new_window)
    Label(cc_frame, font=("Noto Sans", 20), text="Background colour:   ", fg=fBACKGROUND, bg=BACKGROUND, pady=10,
          anchor="w").grid(row=0, column=0, sticky="we")
    bg_button = Button(cc_frame, font=("Noto Mono", 20), text=BACKGROUND, fg=fBACKGROUND, bg=BACKGROUND)
    bg_button.config(command=lambda: select_colour(0, bg_button))
    bg_button.grid(row=0, column=1)

    Label(cc_frame, font=("Noto Sans", 20), text="Header colour:   ", fg=fBACKGROUND, bg=BACKGROUND, pady=10,
          anchor="w").grid(row=1, column=0, sticky="we")
    h_button = Button(cc_frame, font=("Noto Mono", 20), text=HEADER, fg=fHEADER, bg=HEADER)
    h_button.config(command=lambda: select_colour(1, h_button))
    h_button.grid(row=1, column=1)

    Label(cc_frame, font=("Noto Sans", 20), text="Date number colour:   ", fg=fBACKGROUND, bg=BACKGROUND, pady=10,
          anchor="w").grid(row=2, column=0, sticky="we")
    dn_button = Button(cc_frame, font=("Noto Mono", 20), text=DATE, fg=fDATE, bg=DATE)
    dn_button.config(command=lambda: select_colour(2, dn_button))
    dn_button.grid(row=2, column=1)
    Label(cc_frame, font=("Noto Sans", 20), text="Date label colour:   ", fg=fBACKGROUND, bg=BACKGROUND, pady=10,
          anchor="w").grid(row=3, column=0, sticky="we")
    dl_button = Button(cc_frame, font=("Noto Mono", 20), text=DATE_LABEL, fg=fDATE_LABEL, bg=DATE_LABEL)
    dl_button.config(command=lambda: select_colour(3, dl_button))
    dl_button.grid(row=3, column=1)

    Label(cc_frame, font=("Noto Sans", 20), text="Weekday label colour:   ", fg=fBACKGROUND, bg=BACKGROUND, pady=10,
          anchor="w").grid(row=4, column=0, sticky="we")
    wdl_button = Button(cc_frame, font=("Noto Mono", 20), text=WEEKDAY_LABEL, fg=fWEEKDAY_LABEL, bg=WEEKDAY_LABEL)
    wdl_button.config(command=lambda: select_colour(4, wdl_button))
    wdl_button.grid(row=4, column=1)
    Label(cc_frame, font=("Noto Sans", 20), text="Weekday number colour:   ", fg=fBACKGROUND, bg=BACKGROUND, pady=10,
          anchor="w").grid(row=5, column=0, sticky="we")
    wdn_button = Button(cc_frame, font=("Noto Mono", 20), text=WEEKDAY, fg=fWEEKDAY, bg=WEEKDAY)
    wdn_button.config(command=lambda: select_colour(5, wdn_button))
    wdn_button.grid(row=5, column=1)

    Label(cc_frame, font=("Noto Sans", 20), text="Time label colour:   ", fg=fBACKGROUND, bg=BACKGROUND, pady=10,
          anchor="w").grid(row=6, column=0, sticky="we")
    tl_button = Button(cc_frame, font=("Noto Mono", 20), text=TIME_LABEL, fg=fTIME_LABEL, bg=TIME_LABEL)
    tl_button.config(command=lambda: select_colour(6, tl_button))
    tl_button.grid(row=6, column=1)
    Label(cc_frame, font=("Noto Sans", 20), text="Time number colour:   ", fg=fBACKGROUND, bg=BACKGROUND, pady=10,
          anchor="w").grid(row=7, column=0, sticky="we")
    tn_button = Button(cc_frame, font=("Noto Mono", 20), text=TIME, fg=fTIME, bg=TIME)
    tn_button.config(command=lambda: select_colour(7, tn_button))
    tn_button.grid(row=7, column=1)

    cc_frame.pack()

    ##### OTHER ########################################################################################################
    def reset():
        with open(config_default_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            default_lines = f.readlines()  # returns list with each line in the file as a list item
        with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            lines = f.readlines()  # returns list with each line in the file as a list item
        font_colours = []
        for i in range(8):
            lines[i] = default_lines[i]
            font_colours.append(get_font_colour(default_lines[i], i + 15))
        for i in range(15, 23):
            lines[i] = font_colours[i-15] + "\n"
        with open(config_location, "w", encoding="utf8") as f:
            f.writelines(lines)
        bg_button.config(text=default_lines[0].strip(), fg=font_colours[0], bg=default_lines[0].strip())
        h_button.config(text=default_lines[1].strip(), fg=font_colours[1], bg=default_lines[1].strip())
        dn_button.config(text=default_lines[2].strip(), fg=font_colours[2], bg=default_lines[2].strip())
        dl_button.config(text=default_lines[3].strip(), fg=font_colours[3], bg=default_lines[3].strip())
        wdl_button.config(text=default_lines[4].strip(), fg=font_colours[4], bg=default_lines[4].strip())
        wdn_button.config(text=default_lines[5].strip(), fg=font_colours[5], bg=default_lines[5].strip())
        tn_button.config(text=default_lines[6].strip(), fg=font_colours[6], bg=default_lines[6].strip())
        tl_button.config(text=default_lines[7].strip(), fg=font_colours[7], bg=default_lines[7].strip())

    Label(new_window, bg=BACKGROUND, height=1).pack()

    def randomise_colours(*args):
        import random
        hexes = []
        font_colours = []
        for i in range(8):
            colour = ""
            for j in range(6):
                colour = "#" + "%06x" % random.randint(0, 0xFFFFFF) + "\n"
            hexes.insert(i, str(colour))
            font_colours.insert(i, get_font_colour(colour, i + 15))
        with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            lines = f.readlines()  # returns list with each line in the file as a list item
        for i in range(8):
            lines[i] = hexes[i]
        with open(config_location, "w", encoding="utf8") as f:
            f.writelines(lines)
        bg_button.config(text=hexes[0].strip(), fg=font_colours[0], bg=hexes[0].strip())
        h_button.config(text=hexes[1].strip(), fg=font_colours[1], bg=hexes[1].strip())
        dn_button.config(text=hexes[2].strip(), fg=font_colours[2], bg=hexes[2].strip())
        dl_button.config(text=hexes[3].strip(), fg=font_colours[3], bg=hexes[3].strip())
        wdl_button.config(text=hexes[4].strip(), fg=font_colours[4], bg=hexes[4].strip())
        wdn_button.config(text=hexes[5].strip(), fg=font_colours[5], bg=hexes[5].strip())
        tn_button.config(text=hexes[6].strip(), fg=font_colours[6], bg=hexes[6].strip())
        tl_button.config(text=hexes[7].strip(), fg=font_colours[7], bg=hexes[7].strip())

    button_frame = Frame(new_window)
    Button(button_frame, text="Randomise Colours", font=("Noto Sans", 22, "bold"), command=randomise_colours) \
        .grid(row=0, column=0)
    Label(button_frame, font=("Noto Sans", 22), text=" ", fg=fBACKGROUND, bg=BACKGROUND, pady=15).grid(row=0, column=1)
    Button(button_frame, text="Reset to Defaults", font=("Noto Sans", 22, "bold"), command=reset).grid(row=0, column=2)
    button_frame.pack()

    Label(new_window, font=("Noto Sans HK", 18), text="Restart for changes to take effect.", fg=fBACKGROUND,
          bg=BACKGROUND).pack()
    Label(new_window, fg=fBACKGROUND, bg=BACKGROUND, height=1).pack()

    new_window.bind("<r>", randomise_colours)

    def on_closing():
        with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
            lines = f.readlines()  # returns list with each line in the file as a list item
        font_colours = []
        for i in range(8):
            font_colours.append(get_font_colour(lines[i], i + 15))
        for i in range(15, 23):
            lines[i] = font_colours[i - 15] + "\n"
        with open(config_location, "w", encoding="utf8") as f:
            f.writelines(lines)
        new_window.destroy()

    new_window.protocol("WM_DELETE_WINDOW", on_closing)

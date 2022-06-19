from tkinter import messagebox

config_location = "C:\\Users\\tonys\\PycharmProjects\\randomdate\\config.buot"
config_default_location = "C:\\Users\\tonys\\PycharmProjects\\randomdate\\config_default.buot"

BACKGROUND = ""
HEADER = ""
DATE = ""
DATE_LABEL = ""
WEEKDAY_LABEL = ""
WEEKDAY = ""
TIME = ""
TIME_LABEL = ""

START_YEAR = int()
END_YEAR = int()
HR24 = ""

ZERO = ""
SW = ""  # spoken / written

fBACKGROUND = ""
fHEADER = ""
fDATE = ""
fDATE_LABEL = ""
fWEEKDAY_LABEL = ""
fWEEKDAY = ""
fTIME = ""
fTIME_LABEL = ""

TTSRATE = ""


def init_vars():
    with open(config_location, "r", encoding="utf8") as f:  # 'with' keyword automatically closes the file
        lines = f.readlines()  # returns list with each line in the file as a list item

    global BACKGROUND
    global HEADER
    global DATE
    global DATE_LABEL
    global WEEKDAY_LABEL
    global WEEKDAY
    global TIME
    global TIME_LABEL
    global START_YEAR
    global END_YEAR
    global HR24
    global ZERO
    global SW
    global fBACKGROUND
    global fHEADER
    global fDATE
    global fDATE_LABEL
    global fWEEKDAY_LABEL
    global fWEEKDAY
    global fTIME
    global fTIME_LABEL
    global TTSRATE

    BACKGROUND = lines[0].strip()
    HEADER = lines[1].strip()
    DATE = lines[2].strip()
    DATE_LABEL = lines[3].strip()
    WEEKDAY_LABEL = lines[4].strip()
    WEEKDAY = lines[5].strip()
    TIME = lines[6].strip()
    TIME_LABEL = lines[7].strip()

    START_YEAR = int(lines[8].strip())
    END_YEAR = int(lines[9].strip())
    HR24 = lines[10].strip()

    ZERO = lines[13].strip()
    SW = lines[14].strip()

    fBACKGROUND = lines[15].strip()
    fHEADER = lines[16].strip()
    fDATE = lines[17].strip()
    fDATE_LABEL = lines[18].strip()
    fWEEKDAY_LABEL = lines[19].strip()
    fWEEKDAY = lines[20].strip()
    fTIME = lines[21].strip()
    fTIME_LABEL = lines[22].strip()

    TTSRATE = lines[23].strip()


init_vars()


def reset_all():
    with open(config_default_location, "r", encoding="utf8") as f:
        lines = f.readlines()
    with open(config_location, "w", encoding="utf8") as f:
        f.writelines(lines)

    messagebox.showinfo(title="Date and Time Generator", message="Restart program for changes to take effect.")

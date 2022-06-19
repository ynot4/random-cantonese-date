from globals import *

SW_20, SW_30 = ("廿", "卅") if SW == "spoken" else ("二", "三")


def number_converter(digit):  # basic number conversion table, only converts single digits
    chinese_number = ""
    if digit == "1":
        chinese_number = "一"
    if digit == "2":
        chinese_number = "二"
    if digit == "3":
        chinese_number = "三"
    if digit == "4":
        chinese_number = "四"
    if digit == "5":
        chinese_number = "五"
    if digit == "6":
        chinese_number = "六"
    if digit == "7":
        chinese_number = "七"
    if digit == "8":
        chinese_number = "八"
    if digit == "9":
        chinese_number = "九"
    if digit == "0":
        chinese_number = ZERO
    return chinese_number


def year_converter(number):  # converts year number
    chinese_number = ""
    for digit in number:
        chinese_number += number_converter(digit)
    return chinese_number


def md_converter(number):  # converts month and day numbers, using tens
    ah = "呀" if SW == "spoken" else "十"
    chinese_number = ""
    if len(number) < 2:
        for digit in number:
            chinese_number += number_converter(digit)
    else:
        if number[1] == "0":
            if number[0] == "1":
                chinese_number = "十"
            elif number[0] == "2":
                chinese_number = "二十"
            elif number[0] == "3":
                chinese_number = "三十"
        elif number[0] == "1":
            chinese_number = "十"
            chinese_number += number_converter(number[1])
        elif number[0] == "2":
            if SW == "spoken":
                ah = ""
            chinese_number = SW_20 + ah
            chinese_number += number_converter(number[1])
        elif number[0] == "3":
            chinese_number = SW_30 + ah
            chinese_number += number_converter(number[1])
    return chinese_number


def hour_converter(number):  # converts hour numbers, using tens and changing word for 'two'
    ah = "呀" if SW == "spoken" else "十"
    chinese_number = ""
    if len(number) < 2:
        if number == "2":
            chinese_number = "兩"
        else:
            for digit in number:
                chinese_number += number_converter(digit)
    else:
        if number[1] == "0":
            if number[0] == "1":
                chinese_number = "十"
            elif number[0] == "2":
                chinese_number = "二十"
        elif number[0] == "1":
            chinese_number = "十"
            chinese_number += number_converter(number[1])
        elif number[0] == "2":
            if SW == "spoken":
                ah = ""
            chinese_number = SW_20 + ah
            chinese_number += number_converter(number[1])
    return chinese_number


def minutes_converter(number):  # converts minute numbers, using tens and zero
    minutes_number = ""
    minute_unit = ""
    if len(number) < 2:
        if number == "0":
            minutes_number = "鐘"
            return minutes_number, minute_unit
        else:
            minutes_number = ZERO
            for digit in number:
                minutes_number += number_converter(digit)
    else:
        ah = "呀" if SW == "spoken" else "十"
        if number[1] == "0":
            if number[0] == "1":
                minutes_number = "十"
            elif number[0] == "2":
                minutes_number = "二十"
            elif number[0] == "3":
                minute_unit = "半"  # half past
                return minutes_number, minute_unit
            elif number[0] == "4":
                minutes_number = "四十"
            elif number[0] == "5":
                minutes_number = "五十"
        elif number[0] == "1":
            minutes_number = "十"
            minutes_number += number_converter(number[1])
        elif number[0] == "2":
            if SW == "spoken":
                ah = ""
            minutes_number = SW_20 + ah
            minutes_number += number_converter(number[1])
        elif number[0] == "3":
            minutes_number = SW_30 + ah
            minutes_number += number_converter(number[1])
        elif number[0] == "4":
            minutes_number = "四" + ah
            minutes_number += number_converter(number[1])
        elif number[0] == "5":
            minutes_number = "五" + ah
            minutes_number += number_converter(number[1])
    minute_unit = "分"
    return minutes_number, minute_unit


def five_minutes_converter(number):  # minutes in five minute periods
    minutes_number = ""
    minute_unit = ""
    if len(number) < 2:
        if number == "0":
            minutes_number = "鐘"
            return minutes_number, minute_unit
        elif number == "3":  # quarter past
            minutes_number = "一"
            minute_unit = "個骨"
            return minutes_number, minute_unit
        elif number == "6":  # half past
            minutes_number = "半"
            return minutes_number, minute_unit
        elif number == "9":  # quarter to
            minutes_number = "三"
            minute_unit = "個骨"
            return minutes_number, minute_unit
        elif number == "2":
            minutes_number = "兩"
        else:
            for digit in number:
                minutes_number += number_converter(digit)
    else:
        if number[1] == "0":
            if number[0] == "1":
                minutes_number = "十"
        elif number[0] == "1":
            minutes_number = "十"
            minutes_number += number_converter(number[1])
    minute_unit = "個字"
    return minutes_number, minute_unit


def english_weekday(strweekday, weekday):
    if strweekday == "一":
        weekday = "Monday"
    if strweekday == "二":
        weekday = "Tuesday"
    if strweekday == "三":
        weekday = "Wednesday"
    if strweekday == "四":
        weekday = "Thursday"
    if strweekday == "五":
        weekday = "Friday"
    if strweekday == "六":
        weekday = "Saturday"
    if strweekday == "七":
        strweekday = "日"
        weekday = "Sunday"
    return strweekday, weekday


def english_month(month):
    eng_month = ""
    if month == "1":
        eng_month = "January"
    if month == "2":
        eng_month = "February"
    if month == "3":
        eng_month = "March"
    if month == "4":
        eng_month = "April"
    if month == "5":
        eng_month = "May"
    if month == "6":
        eng_month = "June"
    if month == "7":
        eng_month = "July"
    if month == "8":
        eng_month = "August"
    if month == "9":
        eng_month = "September"
    if month == "10":
        eng_month = "October"
    if month == "11":
        eng_month = "November"
    if month == "12":
        eng_month = "December"
    return eng_month
